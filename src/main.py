"""
Main entry point for the deckplant application.

This module uses Google's GenAI API to generate 3 words of the day with
rich, old-school dictionary-style definitions using structured output.
"""

import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import word_prompt, system_prompt
from models import ThreeWordsOfTheDay

# Load environment variables from .env file
load_dotenv()


def format_word_entry(word_data, index: int) -> str:
    """
    Format a single word entry for beautiful console display.

    Args:
        word_data: A WordOfTheDay model instance
        index: The word number (1-3)

    Returns:
        str: Beautifully formatted word entry
    """
    return f"""
{'=' * 80}
WORD {index}: {word_data.word.upper()}
{'=' * 80}

PRONUNCIATION
  IPA:       {word_data.ipa_pronunciation}
  Syllabic:  {word_data.syllabic_pronunciation}

ETYMOLOGY
  {word_data.etymology}

DEFINITION
  {word_data.definition}

EXAMPLE
  "{word_data.example_sentence}"
"""


def main():
    """
    Main function that generates and displays 3 words of the day.

    Uses structured output to ensure consistent, rich dictionary entries
    with pronunciations, etymologies, definitions, and example sentences.

    Requires GOOGLE_GENAI_API_KEY environment variable to be set.
    """
    # Get API key from environment
    api_key = os.environ.get('GOOGLE_GENAI_API_KEY')
    if not api_key:
        print("Error: GOOGLE_GENAI_API_KEY environment variable not set")
        return

    # Create client and generate content with structured output
    with genai.Client(api_key=api_key) as client:
        response = client.models.generate_content(
            model='gemini-2.0-flash-exp',
            contents=word_prompt(),
            config=types.GenerateContentConfig(
                system_instruction=system_prompt(),
                temperature=0.8,  # Higher for more creative/literary output
                response_mime_type='application/json',
                response_schema=ThreeWordsOfTheDay,
            )
        )

        # Parse the structured response
        words_data = response.parsed

        # Display the words in a beautiful format
        for i, word in enumerate(words_data.words, 1):
            print(format_word_entry(word, i))


if __name__ == "__main__":
    main()

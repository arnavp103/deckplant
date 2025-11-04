"""
Data models for structured output from the Google GenAI API.

This module defines Pydantic models that enforce type-safe structured responses
for word of the day entries with rich dictionary-style information.
"""

from pydantic import BaseModel, Field


class WordOfTheDay(BaseModel):
    """
    A single word of the day entry with comprehensive dictionary information.

    This model captures rich, old-school dictionary-style definitions with
    pronunciation guides and evocative example sentences.
    """

    word: str = Field(
        description="The word itself, in lowercase"
    )

    definition: str = Field(
        description=(
            "A rich, contextual definition in the style of Webster's 1913 dictionary. "
            "Should be elaborate, evocative, and capture nuances rather than being "
            "clinical or sterile. Include sensory details, philosophical context, "
            "and comparative usage notes where relevant."
        )
    )

    ipa_pronunciation: str = Field(
        description=(
            "The International Phonetic Alphabet (IPA) pronunciation. "
            "Example: /məˈlɪf.lu.əs/"
        )
    )

    syllabic_pronunciation: str = Field(
        description=(
            "A simplified syllabic pronunciation guide that anyone can read. "
            "Example: muh-LIF-loo-us (with stressed syllable in caps)"
        )
    )

    example_sentence: str = Field(
        description=(
            "An example sentence demonstrating the word's usage. Should be "
            "literary, evocative, and demonstrate the word's nuance—ideally "
            "in the style of classic literature or poetic prose, not mundane "
            "technical usage."
        )
    )

    etymology: str = Field(
        description=(
            "Brief etymology showing the word's origin and historical development. "
            "Example: 'From Latin mellifluus, from mel (honey) + fluere (to flow)'"
        )
    )


class ThreeWordsOfTheDay(BaseModel):
    """
    Collection of exactly three words of the day.

    Each word should be carefully chosen to be educational, thought-provoking,
    or uncommonly used, with rich dictionary-style entries.
    """

    words: list[WordOfTheDay] = Field(
        min_length=3,
        max_length=3,
        description="Exactly three word of the day entries"
    )

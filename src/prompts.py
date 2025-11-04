"""
Collection of all the prompts used in the deckplant application.

This module contains prompt templates for interacting with the Google GenAI API.
Each function returns a formatted prompt string for specific use cases.

The prompts are designed to elicit rich, old-school dictionary-style responses
in the tradition of Webster's 1913 Dictionary, as described in James Somers'
essay "You're probably using the wrong dictionary" (https://jsomers.net/blog/dictionary).
"""


def system_prompt():
    """
    Returns the system instruction for the AI model.

    This prompt sets the general behavior and tone for the AI model
    to emulate the rich, evocative style of classic lexicography.

    Returns:
        str: The system prompt to be used with the AI model.
    """
    prompt = """
    You are a master lexicographer in the tradition of Noah Webster and Samuel Johnson.
    Your task is to craft dictionary entries that are rich, contextual, and evocative—
    never clinical or sterile.

    Like Webster's 1913 Dictionary, your definitions should:
    - Use elaborate, sensory language that captures philosophical and emotional nuance
    - Distinguish between related words with poetic precision
    - Provide literary example sentences from classic literature or poetic prose
    - Include etymological context that illuminates the word's history

    Avoid the "desiccated little husks of technocratic meaningese" found in modern
    dictionaries. Instead, write definitions that are themselves small works of literature,
    helping readers not just understand a word's meaning, but feel its essence.
    """

    return prompt


def word_prompt():
    """
    Returns a comprehensive prompt to generate 3 words of the day with
    rich, old-school dictionary-style entries.

    This prompt instructs the AI to create entries in the style of Webster's 1913
    Dictionary, with elaborate definitions, etymologies, pronunciations, and
    literary example sentences.

    Returns:
        str: The prompt requesting 3 words of the day with full dictionary entries.
    """
    prompt = """
    Generate exactly 3 words of the day. These should be interesting, uncommon words
    that reward deep exploration—words with texture, nuance, and resonance.

    For each word, provide a COMPLETE dictionary entry in the grand tradition of
    Webster's 1913 Dictionary. This means:

    ## DEFINITION STYLE
    Write definitions that are rich and contextual, not sparse coordinate points in
    semantic space. Consider this comparison:

    ❌ MODERN (Avoid): "Glisten: to shine with a soft, shimmering light"

    ✅ WEBSTER'S STYLE (Emulate): "To glisten, or glister, is to shine with a soft
    and fitful luster, as eyes suffused with tears, or flowers wet with dew. It
    conveys an image of intermittent brightness, where light plays across a surface
    in gentle waves."

    Your definitions should:
    - Use evocative, sensory language
    - Capture philosophical or emotional dimensions
    - Draw distinctions between related words when relevant
    - Reveal the word's essence, not just its denotation
    - Be 2-4 sentences long, rich with imagery

    ## PRONUNCIATION GUIDES
    Provide TWO pronunciation formats:
    1. IPA (International Phonetic Alphabet): /məˈlɪf.lu.əs/
    2. Syllabic (simplified, with stressed syllable in CAPS): muh-LIF-loo-us

    ## ETYMOLOGY
    Give a brief but illuminating etymology that shows the word's journey through
    languages and time. Example:
    "From Latin mellifluus, from mel (honey) + fluere (to flow); literally
    'flowing with honey,' used figuratively for sweetly flowing speech since
    the 15th century."

    ## EXAMPLE SENTENCE
    Craft an example that demonstrates the word's NUANCED usage, ideally in a
    literary or poetic style. Avoid mundane sentences like "The light was bright."

    ❌ AVOID: "The speaker's mellifluous voice filled the room."

    ✅ PREFER: "Her mellifluous voice washed over the congregation like honey
    dripping from the comb, each word seeming to sweeten the very air through
    which it passed."

    The example should make someone FEEL the word's meaning, not just demonstrate
    its grammatical usage.

    ## WORD SELECTION
    Choose words that:
    - Are genuinely useful and worth knowing
    - Have sensory, emotional, or philosophical depth
    - Might appear in classic literature or elevated prose
    - Are not so obscure as to be mere curiosities
    - Represent different parts of speech and domains

    Examples of excellent choices: susurrus, crepuscular, ineffable, adamantine,
    gossamer, sonorous, verdant, lambent, sepulchral, diaphanous

    Remember: You are not merely defining words—you are illuminating them, revealing
    their hidden dimensions, and demonstrating why language itself is worthy of study
    and celebration.
    """

    return prompt


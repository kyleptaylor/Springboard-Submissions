"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


# story = Story(
#     ["place", "noun", "verb", "adjective", "plural_noun"],
#     """Once upon a time in a long-ago {place}, there lived a large {adjective} {noun}. It loved to {verb} {plural_noun}."""
# )

story = Story(
    ["celebrity", "noun", "verb", "adjective", "animal", "place", "plural_noun", "silly_word"],
    """In the mystical land of {place}, the famous {celebrity} stumbled upon a {adjective} {noun}. 
    To their surprise, the {noun} could {verb} and spoke in {silly_word}. 
    Together, they embarked on a quest to find the legendary {plural_noun} guarded by a giant {animal}. 
    Along the way, they encountered a talking tree that only communicated through interpretive dance and a village of gnomes who worshiped rubber ducks."""
)


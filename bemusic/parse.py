"""Parse texts from places like Project Gutenberg and probably from
nowhere else.
"""


import re


GUTENBERG_HEADER_RE = re.compile(
        r"\*\*\* START OF THIS PROJECT GUTENBERG EBOOK [^\r\n]* \*\*\*")
GUTENBERG_FOOTER_RE = re.compile(
        r"\*\*\* END OF THIS PROJECT GUTENBERG EBOOK [^\r\n]* \*\*\*")


def parse_guttenburg(text):
    """Remove starting and trailing guttenburg headers and footers if
    they are present.
    """
    header_match = GUTENBERG_HEADER_RE.search(text)
    if header_match is not None:
        text = text[header_match.end(0):]

    footer_match = GUTENBERG_FOOTER_RE.search(text)
    if footer_match is not None:
        text = text[:footer_match.start(0)]

    return text.strip()

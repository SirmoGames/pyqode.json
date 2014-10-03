
"""
This module contains a native python syntax highlighter.
"""
import logging
import re
from pyqode.core.api import SyntaxHighlighter as BaseSH


def any(name, alternates):
    """Return a named group pattern matching list of alternates."""
    return "(?P<%s>" % name + "|".join(alternates) + ")"


def make_json_patterns(fixed_format=True):
    keywords = r"\b" + any(
        "keyword", ["true", "false", "null"]) + r"\b"
    keys = any('tag', ['"[^"\n]*("|\n):', r"'[^'\n]*('|\n):"])
    string_vals = any('string', ['"[^"\n]*("|\n)', r"'[^'\n]*('|\n)"])
    numbers = any('number', [
        '\d+(\s*|\.$|$)',
        '[+-]?\d*\.\d+([eE][-+]?\d+)?',
        '[+-]?\d+\.\d*([eE][-+]?\d+)?'
    ])

    return "|".join(
        [
            keys,
            string_vals,
            numbers,
            keywords,
            # any("SYNC", [r"\n"])
        ]
    )


def _logger():
    return logging.getLogger(__name__)


class JSONSyntaxHighlighter(BaseSH):
    """
    Native cobol highlighter (fixed format).
    """
    PROG = re.compile(make_json_patterns(), re.S)

    def highlight_block(self, text, block):
        self.setFormat(0, len(text), self.formats["normal"])
        match = self.PROG.search(text)
        while match:
            for key, value in list(match.groupdict().items()):
                if value:
                    start, end = match.span(key)
                    try:
                        fmt = self.formats[key]
                    except KeyError:
                        _logger().debug('unsupported format: %s' % key)
                    else:
                        self.setFormat(start, end - start, fmt)
            match = self.PROG.search(text, match.end())

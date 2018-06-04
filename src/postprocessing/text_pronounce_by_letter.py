import re


def needs_process(text, language):
    """
    Tests if a word should be pronounced by letter
    """
    patterns = {
        'english': [
            'x',
            'ru',
            'bu',
            'au',
            'ce',
            'ei',
            'ou',
            'ow',
            'aw',
            'kn',
            'e$'
        ]
    }

    def test_func(pattern):
        return re.match(pattern, text)

    return any(map(test_func, patterns[language]))
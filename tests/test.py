import unittest
import json
from .context import WiktionaryParser
from deepdiff import DeepDiff

parser = WiktionaryParser()

class TestParser(unittest.TestCase):
    def test_multiple_languages(self):
        sample_output = {}
        with open('tests/testOutput.json', 'r') as f:
            sample_output = json.load(f)
        words_to_test = {
            'English': {'grapple': 50080840, 'test': 50342756, 'patronise': 49023308, 'abiologically': 43781266}

        }
        for lang, words in words_to_test.items():
            parser.set_default_language(lang)
            for word, old_id in words.items():
                parsed_word = parser.fetch(word, old_id=old_id)
                print("Testing \"{}\" in {}".format(word, lang))
                self.assertEqual(
                    DeepDiff(parsed_word, sample_output[lang][word], ignore_order=True), {})


if __name__ == '__main__':
    unittest.main()

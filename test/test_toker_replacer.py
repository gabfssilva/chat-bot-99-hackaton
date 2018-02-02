import unittest

from token_replacer import Link, Image, TokenReplacer

class TestTokenReplacer(unittest.TestCase):
    def test_change_link_in_test(self):
        entries = {
            'link:helpme': Link('helpme', 'Help Here', 'http://99app.com/helpme'),
            'img:go99': Image('go99', 'https://big.assets.huffingtonpost.com/ngWipN.gif')
        }

        replacer = TokenReplacer(entries)
        self.assertEquals(replacer.replace('I can help you in @link:helpme'), 'I can help you in <a class="follow_link" href="http://99app.com/helpme">Help Here<a/>')
        self.assertEquals(replacer.replace('I can help you in @link:helpme?'), 'I can help you in <a class="follow_link" href="http://99app.com/helpme">Help Here<a/>?')
        self.assertEquals(replacer.replace('I can help you in @link:helpme.'), 'I can help you in <a class="follow_link" href="http://99app.com/helpme">Help Here<a/>.')

        self.assertEquals(replacer.replace('Go 99 @img:go99'), 'Go 99 <img src="https://big.assets.huffingtonpost.com/ngWipN.gif"/>')

if __name__ == '__main__':
    unittest.main()    
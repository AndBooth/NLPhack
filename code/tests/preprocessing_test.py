import unittest
import preprocessing.text_preprocessing as txp
import re

class Test_TextPreprocessing(unittest.TestCase):
    
    def test_strip_html_tags(self):
        self.assertEqual(txp.strip_html_tags('<html><h2>Some import<br>ant text</h2></html>'), 'Some important text')

    def test_remove_accented_chars(self):
        self.assertEqual(txp.remove_accented_chars('Sómě Áccěntěd těxt ÀÁÂÃÄÇÈÉÊËÌÍÎÏÑÒÓÔÕÖŠÚÛÜÙÝŸŽàáâãäçèéêëìíîïñòóôõöšùúûüýÿž'), 'Some Accented text AAAAACEEEEIIIINOOOOOSUUUUYYZaaaaaceeeeiiiinooooosuuuuyyz')

    def test_expand_match(self):
        self.assertEqual(txp.expand_match(re.match("don't", "don't"), {"don't": "do not"}), "do not")
        self.assertEqual(txp.expand_match(re.match("Don't", "Don't"), {"don't": "do not"}), "Do not")
        self.assertEqual(txp.expand_match(re.match("DoN't", "DoN't"), {"don't": "do not"}), "Do not")

    def test_expand_contractions(self):
        self.assertEqual(txp.expand_contractions("Y'allcan't expand contractions I'd think i'd"), 'You allcannot expand contractions I would think i would')

    def test_remove_special_chars(self):
        self.assertEqual(txp.remove_special_characters('Well this was fun! What_do you think? 123#@!', remove_digits=True, remove_underscores=True), 'Well this was fun What do you think ')
        self.assertEqual(txp.remove_special_characters('Well this was fun! What_do you think? 123#@!'), 'Well this was fun What do you think 123')
        self.assertEqual(txp.remove_special_characters('Well this was fun! What_do you think? 123#@!', remove_underscores=False), 'Well this was fun What_do you think 123')
    
    def test_simple_stemmer(self):
      self.assertEqual(txp.simple_stemmer('My system keeps crashing his crashed yesterday, ours crashes daily'), 'My system keep crash hi crash yesterday, our crash daili')  

if __name__ == '__main__':
    unittest.main()

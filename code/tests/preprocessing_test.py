import unittest
import preprocessing.text_preprocessing as txp

class Test_TextPreprocessing(unittest.TestCase):
    
    def test_strip_html_tags(self):
        self.assertEquals(txp.strip_html_tags('<html><h2>Some import<br>ant text</h2></html>'), 'Some important text')

    def test_remove_accented_chars(self):
        self.assertEquals(txp.remove_accented_chars('Sómě Áccěntěd těxt ÀÁÂÃÄÇÈÉÊËÌÍÎÏÑÒÓÔÕÖŠÚÛÜÙÝŸŽàáâãäçèéêëìíîïñòóôõöšùúûüýÿž'), 'Some Accented text AAAAACEEEEIIIINOOOOOSUUUUYYZaaaaaceeeeiiiinooooosuuuuyyz')

    def test_expand_contractions(self):
        self.assertEquals(txp.expand_contractions("Y'all can't expand contractions I'd think"), 'You all cannot expand contractions I would think' )
if __name__ == '__main__':
    unittest.main()

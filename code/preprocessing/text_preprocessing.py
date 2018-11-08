from bs4 import BeautifulSoup
import unicodedata
import re
from preprocessing.contractions import CONTRACTION_MAP
import nltk
from nltk.corpus import wordnet

def strip_html_tags(text):
    soup = BeautifulSoup(text, "html.parser")
    stripped_text = soup.get_text()
    return stripped_text


def remove_accented_chars(text):
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    return text

def expand_match(contraction, contraction_mapping):
    '''Takes a match object that has matched with a key in the contraction_mapping and returns the equivelent value'''
    match = contraction.group(0)
    first_char = match[0]
    expanded_contraction = contraction_mapping.get(match)\
                            if contraction_mapping.get(match)\
                            else contraction_mapping.get(match.lower())                       
    expanded_contraction = first_char+expanded_contraction[1:]
    return expanded_contraction


def expand_contractions(text, contraction_mapping=CONTRACTION_MAP):
    
    contractions_pattern = re.compile('({})'.format('|'.join(contraction_mapping.keys())), 
                                      flags=re.IGNORECASE|re.DOTALL)

        
    expanded_text = contractions_pattern.sub(lambda x: expand_match(x, contraction_mapping), text)
    expanded_text = re.sub("'", "", expanded_text)
    return expanded_text

def remove_special_characters(text, remove_digits=False, remove_underscores=True):
    '''If remove_underscores is true, replace underscores with spaces'''
    pattern = r'[^a-zA-z0-9\s]' if not remove_digits else r'[^a-zA-z\s]'
    text = re.sub(pattern, '', text)
    
    if remove_underscores:
        text = re.sub('_', ' ', text)
        
    return text

def simple_stemmer(text):
    ps = nltk.PorterStemmer()
    text = ' '.join([ps.stem(word) for word in text.split()])
    return text

#def get_wordnet_pos(treebank_tag):
#    if treebank_tag.startswith('J'):
#        return wordnet.ADJ
#    elif treebank_tag.startswith('V'):
#        return wordnet.VERB
#    elif treebank_tag.startswith('N'):
#        return wordnet.NOUN
#    elif treebank_tag.startswith('R'):
#        return wordnet.ADV
#    else:
#        return wordnet.NOUN


#def normalize_text(text):
#    word_pos = nltk.pos_tag(nltk.word_tokenize(text))
#    lemm_words = [lmtzr(sw[0], get_wordnet_pos(sw[1])) for sw in word_pos]
#
#    return [x.lower() for x in lemm_words]


#if __name__ == '__main__':
    
    #my_string = expand_match("Y'all", CONTRACTION_MAP)
    #print(my_string)
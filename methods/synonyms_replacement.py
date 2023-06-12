import re
import random

from nltk import download
from nltk import word_tokenize
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer


download('stopwords')
stop_words=(stopwords.words('english'))

def get_synonyms(word):
    """
    Return a list of synonyms of the input word.
    """
    synonyms = set()
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synonym = re.sub(r'[^a-zA-Z\s+]', '', l.name().lower())
            if synonym != word:
                synonyms.add(synonym)
    return list(synonyms)

def synonym_replacement(sent, n):
    """
    Replace n words in the sent with their synonyms.
    """
    words = word_tokenize(sent)
    new_words = words.copy()
    random_word_list = list(
        set(
            [word for word in words if (
                word not in stop_words
                and re.sub(
                    r'[^a-zA-Z\s+]', '',
                    word.lower())==word.lower()
                )
            ]
        )
    )
    random.shuffle(random_word_list)
    num_replaced = 0
    for random_word in random_word_list:
        synonyms = get_synonyms(random_word)
        if len(synonyms) >= 1:
            synonym = random.choice(list(synonyms))
            new_words = [
                synonym if word == random_word else word
                for word in new_words
            ]
            num_replaced += 1
        if num_replaced >= n:
            # to limit replacements of only n words
            break
    sentence = TreebankWordDetokenizer().detokenize(new_words)
    return sentence

def replace_text(text, n):
    """
    Replace n words in each sentence in text with their synonyms.
    """
    sents = sent_tokenize(text)
    new_text = ""
    for sent in sents:
        new_text = " ".join(new_text, synonym_replacement(sent, n))
    return new_text

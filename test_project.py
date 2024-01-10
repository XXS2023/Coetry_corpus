from project import counting
from project import original
from project import noun
from project import adjective
from project import verb
from textblob import TextBlob

def main():

    test_counting()
    test_original()
    test_noun()
    test_adjective()
    test_verb()

file = "message.txt"
text = open(file).read().lower()
blob_object = TextBlob(text)
tokens = blob_object.words
tagged = blob_object.tags


def test_counting():
    assert counting(tokens) == 13

def test_original():
    assert original(tokens) == 10

def test_noun():
    assert noun(tagged) == ['example', 'sentence', 'tokenization', 'sentence']

def test_adjective():
    assert adjective(tagged) == ['beautiful']

def test_verb():
    assert verb(tagged) == ['be', 'be']

if __name__ == "__main__":
    main()



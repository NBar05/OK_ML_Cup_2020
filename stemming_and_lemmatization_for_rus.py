import pymorphy2
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

stopWords = stopwords.words('russian')

def stem_words(text, stemmer = SnowballStemmer("russian", ignore_stopwords = True)):
    clean_sents = [s.translate(str.maketrans('', '', string.punctuation)) for s in text.tolist()]
    list_of_sent_lists = [sent.split(' ') for sent in clean_sents]

    new_stemmed_sentences = []
    for sent_list in list_of_sent_lists:
        new_stemmed_sentences.append(' '.join([stemmer.stem(word) for word in sent_list]))

    return new_stemmed_sentences

def lemmatise_words(text):
    clean_sents = [s.translate(str.maketrans('', '', string.punctuation)) for s in text.tolist()]
    list_of_sent_lists = [sent.split(' ') for sent in clean_sents]

    morph = pymorphy2.MorphAnalyzer()
    new_lemmatised_sentences = []
    for sent_list in list_of_sent_lists:
        new_lemmatised_sentences.append(' '.join([morph.parse(word)[0].normal_form for word in sent_list]))

    return new_lemmatised_sentences

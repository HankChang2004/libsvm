from sklearn.feature_extraction.text import TfidfVectorizer
from pathlib import Path

DATA_PATH = Path('.') / 'Amazon-3M'
RAW_TEXT_FILE = 'Amazon-3M_raw_texts_{}.txt'
TFIDF_FILE = 'Amazon-3M_tfidf_{}_ver1.svm'
VOCABULARY_FILE = Path('.') / 'vocab.txt'

raw_text = {'test' : list(), 'train' : list()}
label = {'test' : list(), 'train' : list()}
vocabulary = list()

# get vocabulary
with open(VOCABULARY_FILE, 'r') as voc:
    vocabulary = [x[:-1] for x in voc.readlines()]

# get raw text
for partition in ['test','train']:
    RAW_TEXT_PATH = DATA_PATH / RAW_TEXT_FILE.format(partition)
    with open(str(RAW_TEXT_PATH.resolve()), 'r', encoding='utf-8') as file:
        label[partition],raw_text[partition] = zip(*map(lambda x:x.split('\t'), file.readlines()))

# set TfidfVectorizer
vectorize = TfidfVectorizer(vocabulary=vocabulary, stop_words = 'english', strip_accents = 'unicode')
vectorize.fit(raw_text['train'])

# compute tfidf
for partition in ['test','train']:
    TFIDF_PATH = DATA_PATH / TFIDF_FILE.format(partition)
    out_file = open(str(TFIDF_PATH.resolve()), 'w')
    X = vectorize.transform(raw_text[partition])
    for labels,feature,index in zip(label[partition], X.tolil().data, X.tolil().rows):
        label_str = labels.replace(' ', ',')
        feature_str = ' '.join([f'{x+1}:{y}' for x,y in zip(index,feature)])
        out_file.write(label_str + ' ' + feature_str + '\n')
    out_file.close()

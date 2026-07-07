import json,gzip
from pathlib import Path

DATA_PATH = Path('.') / 'Amazon-3M'
RAW_PATH = DATA_PATH / 'Amazon-3M.raw'
RAW_TEXT_FILE = 'Amazon-3M_raw_texts_{}.txt'

# extract raw text from json.gz
raw_text = {'test' : list(), 'train' : list()}
for file,partition in zip(['tst.json.gz','trn.json.gz'], ['test','train']):
    RAW_FILE = RAW_PATH / file
    RAW_TEXT_PATH = DATA_PATH / RAW_TEXT_FILE.format(partition)
    out_file = open(str(RAW_TEXT_PATH.resolve()), 'w', encoding='utf-8')
    with gzip.open(str(RAW_FILE.resolve()), 'rt') as f:
        for x in f:
            instance = json.loads(x)
            text = ' '.join([str(x) for x in instance['target_ind']]) + '\t' + ' '.join(instance['title'][:-1].split()) + ' ' + ' '.join(instance['content'].split()) + '\n'
            out_file.write(text)
    out_file.close()

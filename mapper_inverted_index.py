import sys

for line in sys.stdin:
    word, doc_ids = line.strip().split('\t')
    doc_ids = doc_ids.split(',')
    for doc_id in doc_ids:
        print(f"{word}:{doc_id}\t1")


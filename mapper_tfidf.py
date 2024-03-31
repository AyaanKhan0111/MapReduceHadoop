import sys
import math

for line in sys.stdin:
    word_doc_id, count = line.strip().split('\t')
    word, doc_id = word_doc_id.split(':')
    count = int(count)
    print(f"{word}\t{doc_id}:{count}")


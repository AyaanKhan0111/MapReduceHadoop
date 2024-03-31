import sys
import math

N = 1000  # Total number of documents (for example)

current_word = None
current_docs = {}

for line in sys.stdin:
    word, doc_count = line.strip().split('\t')
    doc_id, count = doc_count.split(':')
    count = int(count)
    
    if current_word == word:
        current_docs[doc_id] = count
    else:
        if current_word:
            idf = math.log(N / len(current_docs))
            for doc_id, tf in current_docs.items():
                tfidf = tf * idf
                print(f"{current_word}\t{doc_id}:{tfidf}")
        current_word = word
        current_docs = {doc_id: count}

# Output the last word
if current_word:
    idf = math.log(N / len(current_docs))
    for doc_id, tf in current_docs.items():
        tfidf = tf * idf
        print(f"{current_word}\t{doc_id}:{tfidf}")


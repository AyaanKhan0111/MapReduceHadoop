import sys
import math

# Cosine similarity function
def cosine_similarity(vec1, vec2):
    dot_product = sum(vec1.get(index, 0) * vec2.get(index, 0) for index in set(vec1.keys()) & set(vec2.keys()))
    magnitude1 = math.sqrt(sum(val ** 2 for val in vec1.values()))
    magnitude2 = math.sqrt(sum(val ** 2 for val in vec2.values()))
    return dot_product / (magnitude1 * magnitude2)

query_sparse = {}

for line in sys.stdin:
    index, tfidf = line.strip().split('\t')
    query_sparse[int(index)] = float(tfidf)

# Iterate over document vectors and calculate cosine similarity
for line in sys.stdin:
    doc_word_tfidf = line.strip().split('\t')
    doc_id, doc_tfidf = doc_word_tfidf[0], doc_word_tfidf[1:]
    doc_sparse = {int(word_tfidf.split(':')[0]): float(word_tfidf.split(':')[1]) for word_tfidf in doc_tfidf}
    similarity = cosine_similarity(query_sparse, doc_sparse)
    print(f"{doc_id}\t{similarity}")


import sys
import math

# IDF values obtained from the indexing step
idf_values = {
    'word1': idf1,
    'word2': idf2,
    # Add IDF values for all words in the vocabulary
}

# Total number of documents (for example)
N = 1000

# Tokenize and preprocess the query
query = sys.argv[1].lower().split()  # Assuming query is passed as command-line argument

# Calculate TF for the query
query_tf = {}
for word in query:
    if word in query_tf:
        query_tf[word] += 1
    else:
        query_tf[word] = 1

# Calculate TF-IDF for the query and construct sparse vector representation
query_sparse = {}
for word, tf in query_tf.items():
    if word in idf_values:
        idf = idf_values[word]
        tfidf = (1 + math.log(tf)) * idf
        query_sparse[word] = tfidf

# Emit (word_index, TF-IDF) pairs for the sparse query vector
for index, (word, tfidf) in enumerate(query_sparse.items()):
    print(f"{index}\t{tfidf}")


import sys

current_word = None
current_doc_ids = []

for line in sys.stdin:
    word, doc_id = line.strip().split('\t')
    
    if current_word == word:
        current_doc_ids.append(doc_id)
    else:
        if current_word:
            print(f"{current_word}\t{','.join(current_doc_ids)}")
        current_word = word
        current_doc_ids = [doc_id]

# Output the last word
if current_word:
    print(f"{current_word}\t{','.join(current_doc_ids)}")


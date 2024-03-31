import sys

for line in sys.stdin:
    article_id, text = line.strip().split('\t')
    words = text.split()
    for word in words:
        print(f"{word}\t{article_id}")


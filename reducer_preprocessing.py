#!/usr/bin/env python

import sys

def reducer():
    current_article_id = None
    current_article_text = []

    # Read input from standard input
    for line in sys.stdin:
        # Parse the input
        article_id, section_text = line.strip().split('\t', 1)
        
        # If it's the same article as before, append the section text
        if article_id == current_article_id:
            current_article_text.append(section_text)
        else:
            # If it's a new article, emit the previous article's concatenated text
            if current_article_id:
                print(f"{current_article_id}\t{' '.join(current_article_text)}")
            
            # Reset for the new article
            current_article_id = article_id
            current_article_text = [section_text]

    # Emit the last article's concatenated text
    if current_article_id:
        print(f"{current_article_id}\t{' '.join(current_article_text)}")

if __name__ == "__main__":
    reducer()


#!/usr/bin/env python

import sys
import csv

def clean_text(text):
    # Remove special characters and lowercase the text
    cleaned_text = ''.join(e for e in text if e.isalnum() or e.isspace()).lower()
    return cleaned_text

def mapper():
    # Read input from standard input
    for line in sys.stdin:
        # Parse the CSV line
        article_id, section_text = line.strip().split(',', 1)
        
        # Clean the text
        cleaned_section_text = clean_text(section_text)
        
        # Emit article_id and cleaned_section_text as key-value pair
        print(f"{article_id}\t{cleaned_section_text}")

if __name__ == "__main__":
    mapper()


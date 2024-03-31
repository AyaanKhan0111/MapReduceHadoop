import sys

current_key = None
current_count = 0

for line in sys.stdin:
    key, count = line.strip().split('\t')
    
    if current_key == key:
        current_count += int(count)
    else:
        if current_key:
            print(f"{current_key}\t{current_count}")
        current_key = key
        current_count = int(count)

# Output the last key
if current_key:
    print(f"{current_key}\t{current_count}")


import sys
from functools import cmp_to_key

word = sys.stdin.readline().rstrip('\n')

def fitness(word):
    num = ord(word)
    if num >= 97 and num <= 122: # a -> z
        return num + 100
    elif num >= 65 and num <= 90: # A -> Z
        return num + 200
    else: # numbers
        if num % 2 == 1:
            return num + 300
        else:
            return num + 400

print(
    "".join(sorted(list(word), key=cmp_to_key(lambda item1,
                                              item2: fitness(item1) - fitness(item2))))
)

# ❯ echo "Sorting1234" | python ginorts.py
# ginortS1324

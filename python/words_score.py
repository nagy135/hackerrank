import sys
from functools import reduce

sys.stdin.readline() # skip unneeded number
words = sys.stdin.readline().rstrip('\n').split()

vowels = ('a', 'e', 'i', 'o', 'u', 'y')

def word_score(word):
    if reduce(
        lambda carry, x: carry + 1 if x in vowels else carry,
        list(word),
        0
    ) % 2 == 0:
        return 2
    else:
        return 1

print(
    reduce(
        lambda carry, x: carry + word_score(x),
        words,
        0
    )
)

# ❯ python words_score.py <<EOF
# 3
# programming is awesome
# EOF
# 4 <-- this is result

import sys
import re
from functools import reduce

sys.stdin.readline() # skip unneeded number
words = list(map(lambda x: x.rstrip('\n'), sys.stdin.readlines()))

def is_credit_card(word):
    parts = word.split('-')
    word = word.replace('-', '')
    if int(word[0]) not in (4,5,6):
        return False
    elif len(word) != 16:
        return False
    elif re.match(r'^([0-9]{4}){4}$', word) is None:
        return False
    elif has_4_repeating_digits(word):
        return False
    return reduce(
        lambda carry, x: len(x) in [4,16] and carry,
        parts,
        True
    )

def has_4_repeating_digits(word):
    target = None
    count = 0
    for letter in word:
        if letter == target:
            count += 1
            if count == 4:
                return True
        else:
            target = letter
            count = 1
    return False

for word in words:
    if is_credit_card(word):
        print("Valid")
    else:
        print("Invalid")

# ❯ python credit_card.py <<EOF
# 6
# 4123456789123456
# 5123-4567-8912-3456
# 61234-567-8912-3456
# 4123356789123456
# 5133-3367-8912-3456
# 5123 - 3567 - 8912 - 3456
# EOF
# Valid
# Valid
# Invalid
# Valid
# Invalid
# Invalid

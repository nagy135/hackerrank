import sys

letters = sys.stdin.readline().rstrip('\n')
hits = dict()
for letter in letters:
    if letter in hits:
        hits[letter] += 1
    else:
        hits[letter] = 1

pairs = []
for key in hits:
    pairs.append((key, hits[key]))

pairs.sort(key=lambda x: (-x[1], x[0]))

for item in pairs[:3]:
    print(f"{item[0]} {item[1]}")


# print 3 most occuring letters 
# if there are multiple, order alphabetically

# ❯ echo "cclllaade" | python company_logo.py
# l 3
# a 2
# c 2

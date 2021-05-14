import sys

sys.stdin.readline()  # skip meaningsless number

heatmap = dict()
for line in sys.stdin.readlines():
    word = line.rstrip('\n')
    if word in heatmap:
        heatmap[word] += 1
    else:
        heatmap[word] = 1

print(len(heatmap))
print(" ".join(map(lambda x: str(x), heatmap.values())))

# ❯ python word_order.py <<EOF
# 4
# bcdef
# abcdefg
# bcde
# bcdef
# EOF
# 3
# 2 1 1

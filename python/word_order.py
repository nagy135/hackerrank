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

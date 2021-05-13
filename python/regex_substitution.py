import sys
import re

sys.stdin.readline() # we dont need first line

lines = list(map(lambda x: x.rstrip('\n'), sys.stdin.readlines()))
lines = list(map(lambda x: re.sub(r' ', '  ', x), lines))
lines = list(map(lambda x: re.sub(r' && ', ' and ', x), lines))
lines = list(map(lambda x: re.sub(r' \|\| ', ' or ', x), lines))
lines = list(map(lambda x: re.sub(r'  ', ' ', x), lines))

print("\n".join(lines))

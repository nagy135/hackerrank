import re
import sys

lines = re.sub(r'\n', '\t', sys.stdin.read())
print(lines)

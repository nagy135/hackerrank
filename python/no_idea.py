import sys
from functools import reduce

sys.stdin.readline()  # skip unneeded first line

numbers = list(map(int, sys.stdin.readline().rstrip('\n').split()))
A       =  set(map(int, sys.stdin.readline().rstrip('\n').split()))
B       =  set(map(int, sys.stdin.readline().rstrip('\n').split()))

print(
    reduce(
        lambda y, x: y + 1 if x in A else (y - 1 if x in B else y),
        numbers,
        0
    )
)

# ❯ python no_idea.py <<EOF
# 3 2         <- not needed
# 1 5 3       <- input numbers
# 3 1         <- if its one of these, result + 1
# 5 7         <- if its one of these, result - 1
# EOF
# 1           <- this is result

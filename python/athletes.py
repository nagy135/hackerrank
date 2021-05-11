import sys

input_lines = list(map(lambda x: x.rstrip('\n'), sys.stdin.readlines()[1:]))
sort_index = int(input_lines[-1])
attrs = list(
    map(lambda x: list(map(lambda y: int(y), x.split())), input_lines[:-1]))
for i, line in enumerate(attrs):
    line.append(i)

attrs.sort(key=lambda x: (x[sort_index], x[-1]))
for line in attrs:
    print(" ".join(list(map(lambda x: str(x), line[:-1]))))

# ❯ python athletes.py <<EOF
# 5 3       <-- skip this line
# 10 2 5    <-- athlete attributes start
# 7 1 0
# 9 9 9
# 1 23 12
# 6 5 9    <-- athlete attributes end
# 1        <-- sort index (order is other index)
# EOF
# 7 1 0
# 10 2 5
# 6 5 9
# 9 9 9
# 1 23 12

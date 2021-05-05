import sys

string = sys.stdin.readline().rstrip('\n')

result = ""
symbol = string[0]
count = 1
for letter in string[1:]:
    if letter == symbol:
        count +=1
    else:
        result += f"({count}, {symbol}) "
        symbol = letter
        count = 1
result += f"({count}, {symbol}) "
print(result.rstrip())

# ❯ echo "1222311" | python compress_string.py
# (1, 1) (3, 2) (1, 3) (2, 1)               <- this is result

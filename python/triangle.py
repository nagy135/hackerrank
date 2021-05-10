import sys

size = int(sys.stdin.readline().rstrip('\n'))

answer = ""

for middle in range(1, size+1):
    i = 1
    while i < middle:
        answer += "{}".format(i)
        i += 1
    while i > 0:
        answer += "{}".format(i)
        i -= 1
    answer += "\n"
print(answer, end="")

# only one print statement is allowed !
# str() is not allowed

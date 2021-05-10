import sys

size = int(sys.stdin.readline().rstrip('\n'))

# iterative answer (dummy)
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

# onliner answer
print("\n".join(["".join([str(y) for y in range(1, x+1)] + [str(y) for y in range(x-1, 0, -1)]) for x in range(1, size+1)]))

# only one print statement is allowed !
# str() is not allowed

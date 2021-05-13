import sys
import re

sys.stdin.readline() # we dont need first line

lines = list(map(lambda x: x.rstrip('\n'), sys.stdin.readlines()))
lines = list(map(lambda x: re.sub(r' ', '  ', x), lines))
lines = list(map(lambda x: re.sub(r' && ', ' and ', x), lines))
lines = list(map(lambda x: re.sub(r' \|\| ', ' or ', x), lines))
lines = list(map(lambda x: re.sub(r'  ', ' ', x), lines))

print("\n".join(lines))

# ❯ python regex_substitution.py <<EOF
# 11
# a = 1;
# b = input();
# 
# if a + b > 0 && a - b < 0:
#     start()
# elif a*b > 10 || a/b < 1:
#     stop()
# print set(list(a)) | set(list(b))
# #Note do not change &&& or ||| or & or |
# #Only change those '&&' which have space on both sides.
# #Only change those '|| which have space on both sides.
# EOF              <---- answer is after this
# a = 1;
# b = input();
# 
# if a + b > 0 and a - b < 0:
#     start()
# elif a*b > 10 or a/b < 1:
#     stop()
# print set(list(a)) | set(list(b))
# #Note do not change &&& or ||| or & or |
# #Only change those '&&' which have space on both sides.
# #Only change those '|| which have space on both sides.


# ❯ python regex_substitution.py <<EOF
# 1
# x&& &&& && && x || | ||\|| x
# EOF               <---- answer after this
# x&& &&& and and x or | ||\|| x

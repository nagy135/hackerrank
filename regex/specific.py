import re
import sys

inp = sys.stdin.readline().rstrip('\n')

print(
    str(
        bool(re.search(r'[123][120][xs0][30Aa][xsu][.,]', inp)
             )
    ).lower()
)

# ❯ echo "21xAx." | python specific.py
# true
# ❯ echo "zffxO." | python specific.py
# false

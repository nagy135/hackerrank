import re
import sys

lines = re.sub(r'\n', '\t', sys.stdin.read())
print(lines)


# ❯ python paste3.py <<EOF
# Albany, N.Y.
# Albuquerque, N.M.
# Anchorage, Alaska
# Asheville, N.C.
# Atlanta, Ga.
# Atlantic City, N.J.
# Austin, Texas
# Baltimore, Md.
# Baton Rouge, La.
# Billings, Mont.
# Birmingham, Ala.
# Bismarck, N.D.
# Boise, Idaho
# Boston, Mass.
# Bridgeport, Conn.
# EOF
# Albany, N.Y.    Albuquerque, N.M.       Anchorage, Alaska       Asheville, N.C. Atlanta, Ga. A
# tlantic City, N.J.      Austin, Texas   Baltimore, Md.  Baton Rouge, La.        Billings, Mont
# .       Birmingham, Ala.        Bismarck, N.D.  Boise, Idaho    Boston, Mass.   Bridgeport, Co
# nn.

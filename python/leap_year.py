def is_leap(year):
    if not year % 4:
        if year % 100:
            return True
        else:
            return year % 400 == 0
    return False

# This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years
# print(is_leap(2000))
# print(is_leap(2400))
# print(is_leap(1800))
# print(is_leap(1900))
# print(is_leap(2100))
# print(is_leap(2200))
# print(is_leap(2300))
# print(is_leap(2500))

year = int(input())
print(is_leap(year))


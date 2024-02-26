# Given your birthday, in the format "DD-MM-YYYY",
# write a function that calculates how many days have passed since your birthday
# (without counting the days in your birth year and the current year, so just whole years).
#
# The function takes your birthday as a parameter in string format.
#
# Do not import anything, use only what we learned in class


# My birthday is 10-12-2003.
# Thus, not counting days in my birthyear, makes it as if I was born on 1-1-2004.
# So the question is, how many days are between 1-1-2004, and 31-12-2023

yeardiff = 2023 - 2004
daydiff = yeardiff * 365 + 365
leapdays = ((2020 - 2004) / 4) + 1
print(daydiff + leapdays)
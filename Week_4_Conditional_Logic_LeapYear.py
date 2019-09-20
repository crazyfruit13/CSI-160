def is_hebrew_leap_year():
  year=int(input("Please enter the year "))
  year=year%19

  if year == 0 or year == 3 or year == 6 or year == 8 or year == 11 or year == 14 or year == 17:
    print("True")
  else:
    print("False")
is_hebrew_leap_year()
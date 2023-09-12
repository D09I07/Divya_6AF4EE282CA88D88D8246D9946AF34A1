def isLeapYear(Year):
  if (Year % 4) == 0 and (Year % 100) != 0 or (Year % 400) == 0:
    return True
  else:
    return False


year= (int(input()))
if isLeapYear(year):
    print ("{} is a leap year". format (year))
else: 
  print ("{} is not a leap year". formaot (year))
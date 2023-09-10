def isLeapYear(year):
  if (year % 4 ==0 and year % 100!= 0) or year % 400 == 0:
     return True
  else:
     return flase
year = int(input("enter a value"))
if isLeapYear(year):
  print('{}is a Leapyear.'.format(year))
else:
print('{}is not a leapyear.'.format(year))
  
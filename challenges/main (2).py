#program to check a leap year using if elif
year=int(input("please enter the year number:"))
if(year%400==0):
  print("%d is a leap year"%year)
elif(year%100==0):
  print("%d is not a leap year"%year)
elif(year%4==0):
  print("%d is a leap year"%year)
else:
  print("%d is not the leap year"%year)
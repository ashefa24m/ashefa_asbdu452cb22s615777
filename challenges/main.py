#recursive function
def factorial(x):
  if x==0 or x==1:
    return 1
  else:
    return(x*factorial (x-1))

#main
x=int(input("enter n:"))
print("factorial of a given number is:",factorial(x))
    
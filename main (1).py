#creating a program for find the factorial of the given number
#formula=n×(n-1)!

def fact_rec(n):
  if n==0 or n==1:
    return 1
  else:
    return n*fact_rec(n-1)
    
number=int(input("enter the number :"))
res = fact_rec(number)
  
print("The factorial of",number,"is",res)
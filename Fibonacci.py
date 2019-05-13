a = 1
b = 1
fib=12
fib_numbers =[]
print ("The first 12 even Fibonacci numbers is ",end=" ")

while(fib):
    c=a+b
    a=b
    b=c
    if c%2==0:
        print (c,end=" ")
        fib=fib-1


   

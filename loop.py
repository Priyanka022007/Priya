#04-06-2025(Wendeday)

#Program to print 1 to 10 number
"""i=1
while i<=10:
    print(i)
    i+=1"""

#Program to find 10 to 1 numbers
"""i=10
while i>=1:
    print(i)
    i-=1"""

#Program to print 77 to 100 numbers
"""i=77
while i<=100:
    print(i)
    i+=1"""

#Program to print 150 to 100 numbers
"""i=150
while i>=100:
    print(i)
    i-=1"""

#Program to print even numbers from 1 to 100
"""i=1
while i<=100:
    if i%2==0:
        print(i)
    i+=1"""

#Program to create table of given number
"""num=int(input("Enter any number:"))
i=1
while i<=10:
    print(num*i)
    i+=1"""

#for loop

#Program to print 1 to 10 numbers
"""for i in range(1,11):
    print(i) """   

#Program to print 10 to 0 numbers
"""for i in range(10,0,-1):
    print(i)"""

#Program to print 77 to 100 numbers
"""for i in range(77,101):
    print(i)"""

#Program to print 150 to 100 numbers
"""for i in range(150,99,-1):
    print(i)"""

#Program to print even numbers in 1 to 100
"""for i in range(1,101):
    if i%2==0:
        print(i)"""

#Program to print odd numbers in 1 to 100
"""for i in range(1,100):
    if i%2==1:
        print(i)"""

#Program to create table of given number
"""num=int(input("Enter number:"))
for i in range(1,11):
    print(num*i)"""

#Program to print numbers from  which number given by user to the 10 numbers 
"""num=int(input("Enter number:"))
for i in range(num,num+11):
    print(i)"""

#Program to add 1 to 10 numbers
"""sum=0
for i in range(1,11):
    sum+=i
print(sum)"""

#Program to check the given number is prime or not
"""num=int(input("Enter number:"))
cnt=2
while cnt<=num:
    if num%cnt==0:
        break
    cnt+=1
print("Count is:",cnt) 
if cnt==num:
    print("Number is Prime")
else:
    print("Number is not Prime")   """     

#Progra  to calculate factorial which number given by user
"""num=int(input("Enter number:"))
f=1
if num < 0:
    print("No factorial to negative number")
else:
    for i in range(1,num+1):
        f*=i   
    print("Factorial of",num,"is :",f)    """

#Program to find prime number from 1 to 1000
for n in range(2,1001):
    for i in range(2,n):
        if n % i ==0:
            break
        else :
            print(n)
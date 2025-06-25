#05-06-2025,06-06-2025 (Thursday,Friday)

#Without Parameter without return

#program to add 2 numbers
"""def add():
    num1=int (input("Enter first number:"))
    num2=int (input("Enter second number:"))
    result=num1+num2
    print("Result is:",result)
add()  """  

#Program to seperate digits in number
"""def digits():
    num=int(input("Enter number:"))
    rem=0
    while num>0:
        rem=num%10
        print(rem)
        num=int(num/10)
digits()   """     

#Program to reverse the given number
"""def reverse():
    num=int(input("Enter Number:"))
    rem=0
    rev=0
    while num>0:
        rem=num%10
        rev=(rev*10)+rem
        num=int(num/10)
    print(rev)  
reverse()      """

#Program to find the given number is palindrome or not
"""def palindrome():
    num=int(input("Enetr number:"))
    rem=0
    rev=0
    temp=num
    while num>0:
        rem=num%10
        rev=(rev*10)+rem
        num=int(num/10)
    print(rev) 

    if temp==rev :
        print(" Number is Palindrome") 
    else:
        print(" Number is not palindrome")
palindrome()       """

#Program to check the given number is  Armstrong number or not
"""def armno():
    num=int(input("Enter number:"))
    rem=0
    sum=0
    temp=sum
    while num>0:
        rem=num%10
        sum+=(rem*rem*rem)
        num=int(num/10)
    print(sum)
    if temp==sum:
        print("Number is armstrong number") 
    else:
        print("Number is not Armstrong number")

armno()  """

#Program to calculate power of number
"""def power():
    num=int(input("Enter number:"))
    pow=int(input("Enter power:"))
    sum=1
    while pow>0:
        sum*=num
        pow-=1
    print(sum)
power()        """

#Without parameter with return

#Program to add 2 numbers
"""def add():
    n1=int(input("Enter  1st number:"))
    n2=int(input("Enter 2nd number:"))
    res=n1+n2
    return res
res=add()
print("Result is:",res)"""

#Program to check no is even or odd
"""def evenodd():
    num=int(input("Enter number:"))
    if num%2==0:
        return "no is even"
    else:
        return "no is not even"
res=evenodd()
print("Result is=",res)
print(type(res))    """

#Program to check given number is prime or not
"""def prime():
    num=int(input("Enetr number:"))
    cnt=2
    while cnt<=num:
        if num%cnt==0:
            break
        cnt+=1
    if cnt==num:
        return "prime number"
    else:
        return "not prime number"
    
no=prime()
print("Result :",no)    """

#With parameter without return

#Program to add two numbers
'''def add(num1,num2):
    res=num1+num2
    print("Result:",res)
add(23,10)  ''' 

#Program to calculate net salary
'''def net_salary(bs,da,hra,pf):
    ns=bs+da+hra-pf
    print("Net Salary:",ns)
net_salary(2000,500,400,200)    '''

#With Parameter with return

#Program to calculate net salary
'''def net_salary(bs,da,hra,pf):
    ns=bs+da+hra-pf
    return ns
ns=net_salary(2000,500,400,200) 
print("Net salary:",ns)'''

#program to calculate percentage and total of 3 subjects
'''def total(m1,m2,m3):
    t=m1+m2+m3
    return t

def percentage(total):
    p=t/3 
    return p
t= total(50,50,40)
print("Total=",t)
p= percentage(t)
print("Percentage:",p)'''

#Default Parameter
'''def add(n1,n2=20):
    n3=n1+n2
    return n3
s=add(10)
print("Addition:",s)'''

'''def add(n1=10,n2=20):
    n3=n1+n2
    return n3
s=add(30,40)                       # on Default parameter passsed parameter override and it cosider passed parameter
print("Addition:",s)'''


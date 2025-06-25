#09-06-2025(Monday)

#Program to display string

str="anjali"
print(str)

for i in str:
    print(i)

#len()
print(len(str))    

#Display both index and value 
for i in range(0,len(str)):
    print(i,"-",str[i])

#in ,not in 
print("h" in str)
print("e" not in str)

#Slicing
print(str[2:6])
print(str[:6])
print(str[2:])

#lower(),upper()
print(str.lower())
print(str.upper())

#strip()
print(str.strip())             #this method remove white spaces

#split()
str1="a,b,c,d"
str1=str.split()
print(str1)
for j in str1:
    print(j)

#Concatenation of string use + operator    
a="Hello"
b="piyu"
c="jadhav"
d=a+" "+b+" "+c
print(d)

#Program to count a in given string
cnt=0
for i in str:
    if i=='a':
        cnt+=1
print("Count:",cnt)        
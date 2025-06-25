#13-06-2025

#1)File handling

#read mode
'''f=open("first.txt")
print(f.read())'''

#Append mode
'''f=open("first.txt","a")
f.write("I am priyanka")
f.close()
f=open("first.txt","r")
print(f.read())'''

#Write mode     #Only that data will be print original data will remove
'''f=open("first.txt","w")
f.write("I am priyanka")
f.close()
f=open("first.txt","r")
print(f.read())'''

#Create mode
'''f=open("second.txt","x")'''

#Delete file
'''import os
os.remove("second.txt")'''

#2)Exception handling

#try-except block
'''x=56
try:
    print(x)           #When get error here then print the statements in except blk
except:
    print("try again") ''' 

#try-except-else block
'''x=56
try:
    print(x)           #When get error here then print the statements in except blk
except:
    print("try again") 
else:
    print("In Working")    #it will execute when not error in try blk'''

#try-except-finally block
'''x=56
try:
    print(x)           #When get error here then print the statements in except blk
except:
    print("try again") 
finally:
    print("Finally execute") '''

#x=56
'''try:
    f=open("second.txt")         #When get error here then print the statements in except blk
except FileNotFoundError:
    print("file not found") 
except NameError:
    print("Name Error")'''

'''try:
    f=open("second.txt")
except Exception as e:
    print(e)    '''
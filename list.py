#10-06-2025(Tuesday)

#Program to create list display it and check it's type
mylist = [1,2,"Hello","piyu",1.4,2.4]
print(mylist)
print(type(mylist))

#Access element using index
print(mylist[2])

#len()
print(len(mylist))

#Slicing
print(mylist[3:])
print(mylist[:2])
print(mylist[3:6])

#update
mylist[1]="jadhav"
print(mylist)

#Functions of List

#insert()
mylist.insert(2,5)
print(mylist)

#append()
mylist.append(9)
print(mylist)

#extend()
mylist1=[6.8,"piya"]
mylist.extend(mylist1)
print(mylist)

#remove()
mylist.remove("piya")
print(mylist)

#pop()
mylist.pop(3)
print(mylist)

#del
'''del mylist
print(mylist)'''

#clear()
'''mylist.clear()
print(mylist)'''

#sort()
mylist2=["abc","pqr","xyz"]
mylist2.sort()
print(mylist2)

#reverse()
mylist.reverse()
print(mylist)

#Using loop display elements of list
for i in mylist:
    print(i)

#Concatenate two lists
mylist3=mylist1+mylist2
print(mylist3)

#Display elements of list with its index
for i in range(0,len(mylist)):
    print(i,"-",mylist[i])
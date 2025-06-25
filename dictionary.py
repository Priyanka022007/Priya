# 11-06-2025 (Wednseday)

#Program to create a dictionary and display it also check it's type.
thisdist ={
    "Brand":"Ford",
    "Model":"Mustung",
    "Year": 1964,
    "Year": 2020
}
print(thisdist)
print(type(thisdist))

#Access specific element from dictionary
print(thisdist["Brand"])

#Keys are unique and last key will be considerd
print(thisdist["Year"])

#Functions of Dictionary:-

#len()
print(len(thisdist))  #this function will return the length of dictionary

#get()
print(thisdist.get("Model"))  #this function will return only value of keys

#keys()
print(thisdist.keys())  #this function will return the keys of the dictionary

#values()
print(thisdist.values()) #this function will return the values of dictionary

#in and not in
print("Year" in thisdist)   #year is present in dictionary therefore it return true
print("Name"  not in thisdist)   #name is not present in dictionary therefore it return true

#insert element to the dictionry
thisdist["Name"]="swift"
print(thisdist)

#update record in dictionary
thisdist["Name"]="Thar"
print(thisdist)
print(thisdist.update({"Year":2025}))
print(thisdist)

#pop()
thisdist.pop("Year")
print(thisdist)

#popitem()
thisdist.popitem()
print(thisdist)

#delete dictionary
'''del thisdist
print(thisdist)'''

#clear()
'''thisdist.clear()
print(thisdist)'''

#Using loop display dictionary elements
for i in thisdist:
    print(i)           #it return only keys

#Display both keys and values
for i in  thisdist:
    print(i,"-",thisdist[i])

#Display only keys
for i in thisdist.keys():
    print(i)   

#Display only values
for i in thisdist.values():
    print(i)   

#items()-display both keys and values     
for x,y in thisdist.items():
    print(x,"-",y)

#copy()
thisdist1=thisdist.copy()    
print(thisdist1)

#dict()
thisdist2=dict(thisdist)    
print(thisdist2)

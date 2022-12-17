print("hello world")

#integer
type(3)

#float
type(73.81)

#string
type("Hello")

#boolean
type(True)

mylist = ["Arapahoe" , "Denver" , "Alabama"]
#returns Denver, starts at 0.....
mylist[1]
#returns Arapahoe and Denver, if i say [0:1] i only get Arapahoe
mylist[0:2]
#returns denver
print(mylist[1])
mylist[-1]
#returns 3
len(mylist)
#returns Denver and Alabama, saying everything after index position 1 here 
mylist[1:]
#appending to a list 
mylist.append("Ottawa")
mylist

#choosing Boston to be inserted at index 0, super helpful 
mylist.insert(0, "Boston")

#removes a value
mylist.remove("Boston")
#can also use .pop() to remove an item from a specific index location, it will return what was removed too
mylist.pop(0)
mylist

mylist.index("whatever you want to find")
#returns the index of the first object with a matching value 


mylist[0] = "New Denver"
mylist


mytuple = ("This" , "Is" , "A" , "Test")
#returns tuple
type(mytuple)
len(mytuple)
mytuple[:-2]
mytuple[:-1]

#Dictionaries!! 
myDictionary = {"Fruit" : "Apple"}
myotherdictionary = {1 : 2}

testDictionary = {}
testDictionary["Denver"] = 42
testDictionary["Chicago"] = 52
testDictionary["Boston"] = 62
#says that the length is 3! 
len(testDictionary)
#to return back a tuple where the first element in each tuple is the key and the second is the value!! 
testDictionary.items()
testDictionary.keys()
#to return the keys 
testDictionary.values()
#to return the values 

#this will return the value for a specific key 
testDictionary.get("Chicago")
#this also works 
testDictionary["Chicago"]

#this is a list of dictionaries 
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
voting_data


if 2 < 3:
    print("Two is less than three")

mylist
if mylist[2] == "Ottawa":
    print(mylist[2])

temperature = int(input("What is the temperature outside "))

if temperature >80:
    print("Turn on the AC!")

else:
    print("open windows please")

grade = int(input("What did u get "))

if grade >= 90:
    print("An A")
else:
    if grade >= 80:
        print("B")
    else:
        if grade >= 70:
            print("C")


grade = int(input("What did u get "))

if grade >= 90:
    print("AN A!!")
elif grade <90:
    print("You got less than a 90")

mylist = [2,3]

if 1 in mylist:
    print("1 is in ur list")
else:
    print("1 is not in ur list")


x = 0

while x <= 5:
    print(x)

    x = x + 1

mylist = [1,2,3]
for item in mylist:
    print(item)

#prints
#0
#1
#2 
for num in range(3):
    print(num)

#this will print 1, 2, 3 also 
for i in range(len(mylist)):
    print(mylist[i])


counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#to get the keys in a dictionary 
for i in counties_dict.keys():
    print(i)
#to get the values in a dictionary 
for i in counties_dict.values():
    print(i)
#to return both the keys and the values 
for i in counties_dict.items():
    print(i)

#have to convert the int to a str because you can't concatenate a str to an int.... 
for i in counties_dict:
    print(i + " county has " + str(counties_dict.get(i)) + " registered voters")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for i in voting_data:
    for value in i.values():
        print(value)
#to print each county only         
for i in voting_data:
    print(i['county'])


#f-string literals 

value1 = 10
value2 = 20
print(f"when i divide value1 by value 2 the answer is {value1/value2}")
#returns this string + 0.5!! 


counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters")
#this is good, but can also say: 
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters"
    f" this is a multiline f-string"
    f" with three lines")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters")
#the above :, after voters adds a comma to make it 432,438 with a comma 




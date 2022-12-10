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








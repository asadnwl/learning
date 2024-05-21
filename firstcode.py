# write first code Hello world!
print("Hello World!")

# Declaring variables
myNumber = 10       # Int
print(myNumber)
myNumber = 10.5    # float
print(myNumber)
myNumber = 10j      # complex
print(myNumber)
myNumber = "Asad"   # string
print(myNumber)
x = True            # boolen
print(x)
x = b"Asad"         # binary
print(x)
x = ["Muhammad", "Asad", "Muhammad", "Iqran"]       # list
print(x)
x = ("Muhammad", "Asad", "Muhammad", "Iqran")       # tuple
print(x)
x = {"Muhammad", "Asad", "Muhammad", "Iqran"}       # set
print(x)
x = {"name": "Asad", "age" : 25}                    # dictionary
print(x)

# list in python
# list is mutable data structure.
# create an empty list & append diff types of data

nums = []               # empty list
print(nums)
nums.append(20)         # add int value
print(nums)
nums.append(20.50)      # add float value
print(nums)
nums.append("ASAD")     # add string value
print(nums)

# Input & output
nums.append(input("Enter item into list: "))
print(nums)
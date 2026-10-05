import sys

print(sys.version)
print(sys.executable)

# Day 2 — Step 1: Variable কী?

name = "Mahfuza"

print(name)
print(name)
print("Hello", name)

# Day 2 — Step 2: = মানে কী?

name2 = "Rifa"

# এখানে (=) কে assignment operator বলা হয়।
print(name2)

# Vary + able

name = "Mobarak"

print(name)

president = "BaraK"
print (president)
president = "Donald"
print (president)

president = "joe"
print (president)

president = "Donald"
print (president)


#  Day 2 — Step 3: একসাথে একাধিক Variable

name = "Mahfuza"
age = 30
country = "USA"

print(name)
print(type(name))

print(age)
print(type(age))

print(country)
print(type(country))

print('-----')


# Day 2 — Step 4: প্রধান Data Types
name = "Mahfuza"     # str
age = 30             # int
height = 5.4         # float
is_learning = True   # bool


print(type(name))
print(type(age))
print(type(height))
print(type(is_learning))

print('-----')
is_learning = True
is_admin = False

print(is_learning)
print(type(is_learning))

print(is_admin)
print(type(is_admin))

# এবার ছোট্ট Challenge
a = "100" # str
b = 100     # int
c = 100.5   # float
d = False   # bool

print (type(a), type(b), type(c), type(d))

# Day 2 — Step 5: input() — User-এর কাছ থেকে তথ্য নেওয়া

print ("++++++ input () +++++++")

name = input("What is your name? ")

print(name)

# Step 6: input() সবসময় String দেয়
age = input("How old are you? ")

print("Before conversion: ",age)
print(type(age))

age = int(age)
print("After conversion: ",age)

print(type(age))
next_age = age + 1

print(next_age)

# print()
# type() // Show Data type
# int()  // coverts string to integer
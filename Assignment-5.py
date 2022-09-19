# 1 Write a python script to remove the last digit from a given number. 
# (for example, if user enters 2534 then your output should be 253)
"""Solution
userInput = int(input("Enter a Number : "))
userInput = userInput/10

print(int(userInput))
"""

# 2 Write a python script to get the last digit from a given number. (for example, if user
# enters 2089 then your output should be 9)
"""Solution
userInput = int(input("Enter a Number : "))
userInput = int(userInput%10)
print(userInput)
"""

# 3 Write a python script to swap data of two variables
"""Solution 
a = int(input("Enter A value :"))
b = int(input("Enter B value :"))
a = a+b
b = a-b
a = a-b

print("A is ",a)
print("B is ",b)
"""

# 4. Write a python script to find x power y, where values of x and y are given by user
"""Solution
base_Val = int(input("Enter Base Value : "))
exponent_Val = int(input("Enter Exponent Value : "))
print("Power is",base_Val**exponent_Val)
"""

# 5. Write a python script which takes a three digit number from the user and displays
# only its first digit.
"""Solution
userInput = int(input("Enter Three Digit Value : "))
userInput = int(userInput/100)
print(userInput)
"""

# 6. Write a python script which takes a three digit number from the user and displays
# only its middle digit.
"""Solution
userInput = int(input("Enter Three Digit Value : "))
userInput = int(userInput/10%10)
print(userInput)
"""

# 7. Write a python script which takes a three digit number from the user and displays
# only its last digit.
"""Solution
userInput = int(input("Enter Three Digit Value : "))
userInput = int(userInput%10)
print(userInput)
"""

#8. Write a python script to use IN operator to display the data present in the list
"""Solution
mylist = ["ineuron"]
result = 'i' in mylist[0]
print(result)
"""

#9. Write a python script to use NOT IN operator to display the data not present in list
"""Solution
mylist = ["ineuron"]
result = 'Z' not in mylist[0]
print(result)
"""

#10. Write a python script to use IS operator to display if both variables are the same
# object or not?
"""Solution
a = b = 100
print(a is b)
print(b is a)
"""
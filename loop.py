# Age = int(input("Enter your age: "))

# while Age < 0 :
#     print("Age can't be negative")
#     age = int(input("Enter your age : "))

#     print(f"You are {age} years old ")

# food =input("What's your fav food?(q to quit):")

# while not  food == "q":
#         print(f"you like {food}")
#         food = input("Enter another food you like (q to quit) :")

#         print("see ya")

num =int(input("Enter a # between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a # between 1 -10: "))
    print(f"Your number is {num}")
    

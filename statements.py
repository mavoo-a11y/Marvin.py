age = int(input("Enter your age: "))

if age >= 100:
  print("you are too old ")
if age >= 18:
    print("You are a grown up!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You must be 18+ to be a grown up")
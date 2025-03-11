# If statement
temperature: int = 30
if temperature >= 30 :
    print("Its a hot weather")
elif temperature >= 20 and temperature <= 30:
    print("Its a pleasant weather")
elif temperature < 20 :
    print("Its a cold weather")
else:
    print("Invalid temperature")

# While loop
table = 0
while table < 10:
    table += 1
    print(f"2 * {table} = {2 * table}")

# For loop
    cars = ["BMW", "Audi", "Mercedes", "Toyota", "Ford"]
    for i in cars:
        print(i)

# Nested loop
for x in range(4):
    for y in range(3):
        print(f"{x}, {y}")
    

# Nested If else statement
submission_ontime = True

if submission_ontime:
    print("You have submitted your assignment on time")
    user = input("Are All answers is completed ? (yes or no)")
    if user == "yes":
        print("You have completed all the answers")
    else:
        print("You have not completed all the answers")
else:
    print("You have not submitted your assignment on time")





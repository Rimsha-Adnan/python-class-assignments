# 01 ARITHMETIC OPERATORS
# These operators perform basic mathematical operations
print("--- Arithmetic Operators ---")
number1 = 10
number2 = 3

addition = number1 + number2        # Addition
subtraction = number1 - number2     # Subtraction
multiplication = number1 * number2  # Multiplication
division = number1 / number2        # Division
remainder = number1 % number2       # Remainder (modulus)
power = number1 ** 2               # Power (exponential)
floor_division = number1 // number2 # Floor division (removes decimal)

print(f"Addition: {number1} + {number2} = {addition}")
print(f"Subtraction: {number1} - {number2} = {subtraction}")
print(f"Multiplication: {number1} * {number2} = {multiplication}")
print(f"Division: {number1} / {number2} = {division}")
print(f"Remainder: {number1} % {number2} = {remainder}")
print(f"Power: {number1} ** 2 = {power}")
print(f"Floor Division: {number1} // {number2} = {floor_division}")

# 02 ASSIGNMENT OPERATORS
print("\n--- Assignment Operators ---")
score = 10                  # Basic assignment
print(f"Initial score: {score}")

score += 5                  # Add and assign
print(f"After += 5: {score}")

score -= 2                  # Subtract and assign
print(f"After -= 2: {score}")

score *= 2                  # Multiply and assign
print(f"After *= 2: {score}")

score /= 2                  # Divide and assign
print(f"After /= 2: {score}")

# 03 COMPARISON OPERATORS
print("\n--- Comparison Operators ---")
age1 = 25
age2 = 30

print(f"age1 = {age1}, age2 = {age2}")
print(f"Equal to: {age1} == {age2} is {age1 == age2}")
print(f"Not equal to: {age1} != {age2} is {age1 != age2}")
print(f"Greater than: {age1} > {age2} is {age1 > age2}")
print(f"Less than: {age1} < {age2} is {age1 < age2}")
print(f"Greater than or equal to: {age1} >= {age2} is {age1 >= age2}")
print(f"Less than or equal to: {age1} <= {age2} is {age1 <= age2}")

# 04 LOGICAL OPERATORS
print("\n--- Logical Operators ---")
is_sunny = True
is_warm = True

print(f"is_sunny: {is_sunny}, is_warm: {is_warm}")
print(f"is_sunny AND is_warm: {is_sunny and is_warm}")  # True if both are True
print(f"is_sunny OR is_warm: {is_sunny or is_warm}")    # True if at least one is True
print(f"NOT is_sunny: {not is_sunny}")                  # Inverts the boolean value

# 05 MEMBERSHIP OPERATORS
print("\n--- Membership Operators ---")
fruits = ['apple', 'banana', 'orange']
fruit_to_find = 'banana'

print(f"Fruits list: {fruits}")
print(f"Is '{fruit_to_find}' in fruits? {fruit_to_find in fruits}")
print(f"Is 'grape' not in fruits? {'grape' not in fruits}")

# 06 IDENTITY OPERATORS
print("\n--- Identity Operators ---")
original_list = [1, 2, 3]
same_list = original_list      # Points to the same object
different_list = [1, 2, 3]     # Creates a new object with same values

print(f"original_list is same_list: {original_list is same_list}")
print(f"original_list is different_list: {original_list is different_list}")

# 07 BITWISE OPERATORS
print("\n--- Bitwise Operators ---")
num1 = 10  # 1010 in binary
num2 = 12  # 1100 in binary

print(f"num1 = {num1} (binary: {bin(num1)[2:]})")
print(f"num2 = {num2} (binary: {bin(num2)[2:]})")
print(f"AND (&): {num1 & num2} (binary: {bin(num1 & num2)[2:]})")
print(f"OR (|): {num1 | num2} (binary: {bin(num1 | num2)[2:]})")
print(f"XOR (^): {num1 ^ num2} (binary: {bin(num1 ^ num2)[2:]})")
print(f"Left shift num1 << 1: {num1 << 1} (binary: {bin(num1 << 1)[2:]})")
print(f"Right shift num1 >> 1: {num1 >> 1} (binary: {bin(num1 >> 1)[2:]})")



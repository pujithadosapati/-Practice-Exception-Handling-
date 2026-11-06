# Practice Exception Handling
print("===== EXCEPTION HANDLING DEMONSTRATION =====")
# CASE 1: Handling invalid numeric input
print("\n1. Invalid Numeric Input")
try:
    number = int(input("Enter an integer: "))
    print("You entered:", number)
except ValueError:
    print("Error: Please enter a valid integer.")
else:
    print("Numeric input accepted.")
finally:
    print("Input operation completed.")
# CASE 2: Handling division by zero
print("\n2. Division by Zero")
try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    result = a / b
except ValueError:
    print("Error: Please enter valid numbers.")
except ZeroDivisionError:
    print("Error: Cannot divide a number by zero.")
else:
    print("Division result:", result)
finally:
    print("Division operation completed.")
# CASE 3: Handling missing values
print("\n3. Handling Missing Values")
try:
    name = input("Enter your name: ").strip()

    if not name:
        raise ValueError("Name cannot be empty.")
    print("Welcome,", name)
except ValueError as e:
    print("Error:", e)
finally:
    print("Name validation completed.")
# CASE 4: Handling invalid list index

print("\n4. Handling Invalid List Index")

try:
    numbers = [10, 20, 30, 40]

    index = int(input("Enter list index (0-3): "))

    print("Selected value:", numbers[index])

except ValueError:
    print("Error: Please enter a valid integer index.")

except IndexError:
    print("Error: Index is outside the list range.")

else:
    print("List access successful.")

finally:
    print("List operation completed.")


# CASE 5: Handling file not found

print("\n5. Handling Missing File")

try:
    file = open("sample.txt", "r")
    content = file.read()
    print("File content:", content)
    file.close()

except FileNotFoundError:
    print("Error: The requested file does not exist.")

finally:
    print("File operation completed.")
print("\n===== PROGRAM EXECUTION FINISHED =====")

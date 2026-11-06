## Practice Exception Handling
## Project Description
This project demonstrates how to handle common runtime errors in Python using exception handling techniques.
The program safely handles invalid numeric input, division by zero, missing values, invalid list indexes, and missing files without crashing unexpectedly.
## Objective
To learn and implement Python exception handling using:
try
except
else
finally
raise
## Tools and Technologies
Programming Language: Python 3
## Exception Cases Handled
Exception	Description
ValueError	Handles invalid numeric input
ZeroDivisionError	Handles division by zero
Missing Value	Handles empty user input
IndexError	Handles invalid list indexes
FileNotFoundError	Handles missing files
## How to Run the Project
Step 1: Install Python 3 on your computer.
Step 2: Open the project folder in Code.
Step 3: Open the terminal.
Step 4: Run the following command:bash
python exception_handling.py
## Sample Test Cases
Test Case	Input	Expected Output
Invalid number	abc	Please enter a valid integer
Division by zero	10 / 0	Cannot divide by zero
Missing name	Empty input	Name cannot be empty
Invalid index	10	Index is outside the list range
Missing file	sample.txt unavailable	Requested file does not exist
## Key Concepts Learned
Understanding Python exceptions.
Handling runtime errors safely.
Using specific exception classes.
Providing meaningful error messages.
Using finally for cleanup operations.
Raising custom exceptions using raise.
## Conclusion
This project provides practical experience with Python exception handling. It demonstrates how to identify and handle common runtime errors and make programs more reliable and user-friendly.

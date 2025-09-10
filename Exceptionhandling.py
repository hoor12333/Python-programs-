try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter a valid integer.")
else:
    print("Division successful! Result =", result)
finally:
    print("Program finished (finally block executed).")

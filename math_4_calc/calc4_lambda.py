num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))


def calc(num_1, num_2):
    print("Select operation:\n"
          "1. Addition\n"
          "2. Subtraction\n"
          "3. Multiplication\n"
          "4. Division\n")

    calc = input().strip().lower()
    
    operations = {
        '1': lambda num_1 , num_2: num_1 + num_2,
        '2': lambda num_1 , num_2: num_1 - num_2,
        '3': lambda num_1 , num_2: num_1 * num_2,
        '4': lambda num_1 , num_2: num_1 / num_2 if num_2 != 0 else "Error! Division by zero."
    }
    
    if calc in operations:
        result = operations[calc](num_1, num_2)
        if isinstance(result, str):
            print(result)
        else:
            print(f"The result is: {result}")
            
calc(num_1, num_2)
def input_numbers():
    try:
        num_1 = float(input("Enter the first number: "))
        num_2 = float(input("Enter the second number: "))
        return num_1, num_2
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None, None

def calculator(num_1, num_2):  
    print("Select operation:\n"
          "1. Addition\n"
          "2. Subtraction\n"
          "3. Multiplication\n"
          "4. Division\n")

    calc = input().strip().lower()
    
    match calc:

        case '1':
            result = num_1 + num_2
        case '2':
            result = num_1 - num_2
        case '3':
            result = num_1 * num_2
        case '4':
            if num_2 == 0:
                print("Error! Division by zero.")
                result = None
            else:
                result = num_1 / num_2
        case _:
            print("Invalid operation selected.")
            result = None
    if result is not None:
            print(f"The result is: {result}")
            
num_1, num_2 = input_numbers()
calculator(num_1, num_2)
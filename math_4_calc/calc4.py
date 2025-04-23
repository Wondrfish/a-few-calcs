try:
    num_1 = float(input("Enter the first number: "))
    num_2 = float(input("Enter the second number: "))
   
   
    
    print("Select operation:\n"
          "1. Addition\n"
          "2. Subtraction\n"
          "3. Multiplication\n"
          "4. Division\n")
    
    calc = input().strip().lower()
    
    if calc == '1':
        result = num_1 + num_2
    elif calc == '2':
        result = num_1 - num_2
    elif calc == '3':
        result = num_1 * num_2
    elif calc == '4':
        if num_2 == 0:
            print("Error! Division by zero.")
            result = None
        else:
            result = num_1 / num_2
    else:
        print("Invalid operation selected.")
        result = None
    if result is not None:
        print(f"The result is: {result}")
        
        
    
except ValueError:
    print("Invalid input. Please enter a number.")
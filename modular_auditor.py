inventory = 0
number_of_invalid_inputs = 0

while True:
    user_input = input("\nEnter the stock quantity (or type 'quit' to quit): ").strip().lower()
    
    if user_input == 'quit':
        print(f"Total Units Processed: {inventory}")
        print(f"Number of Rejected entries: {number_of_invalid_inputs}")
        break
    try:
        quantity = int(user_input)
        if quantity < 0:
            print("Invalid input. Please enter a non-negative integer.")
            number_of_invalid_inputs += 1
        else:
            inventory += quantity
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        number_of_invalid_inputs += 1
    if inventory > 500:
        print("Warning: Inventory exceeds 500 units.")
        break
    print ("\nCurrent inventory:", inventory)
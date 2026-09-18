def get_valid_input():
    user_input = input("\nEnter the stock quantity (or type 'quit' to quit): ").strip().lower()

    if user_input == 'quit':
        return "quit"
    
    try:
        quantity = int(user_input)
        if quantity < 0:
            print("Invalid input. Please enter a non-negative integer.")
            return None
        return quantity
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return None


def process_delivery(current_total, new_value):
    return current_total + new_value


def calculate_tax(amount):
    return amount * 0.10


def generate_report(total_units, failed_attempts):
    print(f"\nTotal Units Processed: {total_units}")
    print(f"Number of Rejected entries: {failed_attempts}")


def main():
    inventory = 0
    number_of_invalid_inputs = 0

    while True:
        quantity = get_valid_input()
        
        if quantity == "quit":
            generate_report(inventory, number_of_invalid_inputs)
            break
        
        if quantity is None:
            number_of_invalid_inputs += 1
        else:
            inventory = process_delivery(inventory, quantity)
            tax = calculate_tax(quantity)
            print(f"Tax for this delivery (10%): ${tax:.2f}")
            
            if inventory > 500:
                print("Warning: Inventory exceeds 500 units.")
                generate_report(inventory, number_of_invalid_inputs)
                break
                
            print("\nCurrent inventory:", inventory)


if __name__ == "__main__":
    main()
# Digital Detective — Mission 5: Number Converter
# A beginner-friendly program to convert a decimal integer to binary and hexadecimal.

def main():
    print("=== Decimal to Binary & Hexadecimal Converter ===")
    user_input = input("Enter a positive decimal integer: ")
    
    # Convert string input to integer
    decimal_number = int(user_input)
    
    # Perform conversions
    binary_representation = bin(decimal_number)
    hexadecimal_representation = hex(decimal_number)
    
    # Display the results
    print(f"Decimal Value:     {decimal_number}")
    print(f"Binary Value:      {binary_representation}")
    print(f"Hexadecimal Value: {hexadecimal_representation}")

if __name__ == "__main__":
    main()

def main():
    # Get user input
    food_charge = float(input("Enter food charge: $"))
    
    # Calculate amounts
    tip = food_charge * 0.18
    tax = food_charge * 0.07
    total = food_charge + tip + tax
    
    # Display results
    print("\n--- Receipt ---")
    print(f"Food: ${food_charge:.2f}")
    print(f"Tip (18%): ${tip:.2f}")
    print(f"Tax (7%): ${tax:.2f}")
    print("---------------")
    print(f"TOTAL: ${total:.2f}")

if __name__ == "__main__":
    main()
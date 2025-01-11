'''#6) In this activity, you will create the code that a candy store will use in their state-of-the-art candy vending machine.

        # Instructions
        # Create a loop that prints all of the candies in the store to the terminal, with their index stored in brackets beside them.

        # For example: "[0] Snickers"
        # Create a second loop that runs for a set number of times determined by the variable allowance.

        # For example: If allowance is equal to five, the loop should run five times.

        # Each time this second loop runs, take in a user's input, preferably a number, and then add the candy with the matching index to the variable candy_cart.

        # For example: If the user enters "0" as their input, "Snickers" should be added into the candy_cart list.

        # Use another loop to print all of the candies selected to the terminal.
# List of candies available in the store'''

candies = ["Snickers", "Kit Kat", "Twix", "M&M's", "Skittles", "Reese's", "Hershey's", "Milky Way", "Twizzlers", "Starburst"]

# Empty list to store selected candies
candy_cart = []

# Print all available candies with their indices
print("Available candies:")
for index, candy in enumerate(candies):
    print(f"[{index}] {candy}")

# Set the allowance (number of candies the user can select)
allowance = 5

# Loop for selecting candies based on allowance
print(f"\nYou can select {allowance} candies.")
for i in range(allowance):
    while True:
        try:
            choice = int(input(f"Enter the number for candy {i+1}: "))
            if 0 <= choice < len(candies):
                candy_cart.append(candies[choice])
                print(f"Added {candies[choice]} to your cart.")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

# Print selected candies
print("\nYou have selected the following candies:")
for candy in candy_cart:
    print(candy)
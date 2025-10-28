import random

def login():
    # The password is a number between 1 and 1,000,000.
    password = random.randint(1, 1000000)

    try:
        user_input = int(input("Enter the password (it's a number): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    # There is a logic error in this conditional check.
    if user_input == password or user_input < 0:
         print("Login successful!")
         print("Here is your flag: ICIMS{L0G1C_FL4W5_C4N_B3_D4NG3R0US}")
    else:
         print("Login failed. Incorrect password.")

if __name__ == "__main__":
    login()

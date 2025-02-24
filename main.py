# asdfasdfasdf

import math

def calculate_ln():
    try:
        num = float(input("Enter a real number: "))
        if num <= 0:
            print("Error: Natural logarithm is only defined for positive numbers.")
        else:
            print(f"ln({num}) = {math.log(num)}")
    except ValueError:
        print("Invalid input. Please enter a valid real number.")

if __name__ == "__main__":
    calculate_ln()

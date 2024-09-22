import random

def generate_random_numbers(count, lower_bound, upper_bound):
    return [random.randint(lower_bound, upper_bound) for _ in range(count)]

if __name__ == "__main__":
    try:
        count = int(input("Enter the number of random numbers to generate: "))
        lower_bound = int(input("Enter the lower bound: "))
        upper_bound = int(input("Enter the upper bound: "))
        
        random_numbers = generate_random_numbers(count, lower_bound, upper_bound)
        print("Generated random numbers:", random_numbers)
        
    except ValueError:
        print("Please enter valid integers.")

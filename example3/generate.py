# generate.py
import random

def generate_data(filename="data.txt"):
    with open(filename, "w") as file:
        for _ in range(10):  # Generate 10 random numbers
            file.write(f"{random.randint(1, 100)}\n")
    print(f"Generated {filename}")

#if __name__ == "__main__"
generate_data()

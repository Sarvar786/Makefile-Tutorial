# process.py
def process_data(input_file, output_file):
    try:
        with open(input_file, "r") as infile, open(output_file, "w") as outfile:
            numbers = [int(line.strip()) for line in infile]
            sorted_numbers = sorted(numbers)  # Sort numbers
            for num in sorted_numbers:
                outfile.write(f"{num}\n")
        print(f"Processed {input_file} → {output_file}")
    except FileNotFoundError:
        print(f"Error: {input_file} not found. Run 'make generate' first.")

if __name__ == "__main__":
    process_data("data.txt","Processed.txt" )


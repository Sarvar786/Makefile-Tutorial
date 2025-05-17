# summary.py
def summarize_data(input_file="Processed.txt", output_file="summary.txt"):
    try:
        with open(input_file, "r") as infile, open(output_file, "w") as outfile:
            numbers = [int(line.strip()) for line in infile]
            total = sum(numbers)
            avg = total / len(numbers) if numbers else 0
            min_val, max_val = (min(numbers), max(numbers)) if numbers else (None, None)

            summary = f"Total: {total}\nAverage: {avg:.2f}\nMin: {min_val}\nMax: {max_val}"
            outfile.write(summary)
            print(f"Summary written to {output_file}\n{summary}")
    except FileNotFoundError:
        print(f"Error: {input_file} not found. Run 'make process' first.")

if __name__ == "__main__":
    summarize_data()


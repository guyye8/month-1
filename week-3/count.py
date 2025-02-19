# Task 1: Write a program to calculate word and line counts in a text file.


def count_words_and_lines(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()  # Read all lines
            line_count = len(lines)  # Count lines
            word_count = sum(len(line.split()) for line in lines)  # Count words

        print(f"Total Lines: {line_count}")
        print(f"Total Words: {word_count}")

    except FileNotFoundError:
        print("Error: File not found. Please check the filename.")

# Example usage
filename = "sample.txt"  # Replace with your file name
count_words_and_lines(filename)

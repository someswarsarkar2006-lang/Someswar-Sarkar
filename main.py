"""
DNA Sequence Matcher
A beginner-friendly Python mini project for exact DNA pattern matching.

Features:
- Validates DNA sequences (A, T, G, C only)
- Finds all exact matches, including overlapping matches
- Counts A, T, G, and C bases
- Reads a sequence from a text file
- Saves search results to a text file

Educational project only; not a medical diagnostic tool.
"""

from pathlib import Path

VALID_BASES = set("ATGC")


def normalize_sequence(sequence):
    """Remove whitespace and convert a sequence to uppercase."""
    return "".join(sequence.split()).upper()


def is_valid_dna(sequence):
    """Return True when sequence is non-empty and contains only A/T/G/C."""
    return bool(sequence) and all(base in VALID_BASES for base in sequence)


def find_all_matches(dna, pattern):
    """Return zero-based positions of all exact matches, including overlaps."""
    positions = []
    start = 0
    while True:
        position = dna.find(pattern, start)
        if position == -1:
            break
        positions.append(position)
        start = position + 1  # +1 allows overlapping matches
    return positions


def count_bases(dna):
    """Return the count of each DNA base."""
    return {base: dna.count(base) for base in "ATGC"}


def read_sequence_file(filename):
    """Read a DNA sequence from a text file and normalize it."""
    return normalize_sequence(Path(filename).read_text(encoding="utf-8"))


def save_results(filename, dna, pattern, positions):
    """Write search results to a text file."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write("DNA SEQUENCE MATCHER - SEARCH REPORT\n")
        file.write("=" * 40 + "\n")
        file.write(f"DNA sequence length: {len(dna)}\n")
        file.write(f"Pattern searched: {pattern}\n")
        file.write(f"Number of matches: {len(positions)}\n")
        if positions:
            file.write("Zero-based positions: " + ", ".join(map(str, positions)) + "\n")
            file.write("One-based positions: " + ", ".join(str(p + 1) for p in positions) + "\n")
        else:
            file.write("Pattern was not found.\n")
        file.write("\nBase counts:\n")
        for base, count in count_bases(dna).items():
            file.write(f"{base}: {count}\n")


def ask_for_dna(prompt):
    """Keep asking until the user enters a valid DNA sequence."""
    while True:
        sequence = normalize_sequence(input(prompt))
        if is_valid_dna(sequence):
            return sequence
        print("Invalid input. Use only A, T, G, and C, and do not leave it empty.")


def search_dna(dna):
    """Ask for a pattern, search it, display the result, and save a report."""
    pattern = ask_for_dna("Enter the DNA pattern to search for: ")
    positions = find_all_matches(dna, pattern)

    print("\n--- Search Result ---")
    print(f"DNA length: {len(dna)}")
    print(f"Pattern: {pattern}")
    print(f"Number of matches: {len(positions)}")
    if positions:
        print("Zero-based positions:", positions)
        print("One-based positions:", [p + 1 for p in positions])
    else:
        print("Pattern not found.")

    print("\nBase counts:")
    for base, count in count_bases(dna).items():
        print(f"{base}: {count}")

    filename = "results.txt"
    save_results(filename, dna, pattern, positions)
    print(f"\nResults saved to {filename}")


def main():
    print("=" * 42)
    print("         DNA SEQUENCE MATCHER")
    print("=" * 42)

    while True:
        print("\nMAIN MENU")
        print("1. Enter DNA sequence manually")
        print("2. Load DNA sequence from a text file")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            dna = ask_for_dna("Enter DNA sequence (A/T/G/C): ")
            search_dna(dna)
        elif choice == "2":
            filename = input("Enter file name (example: sample_dna.txt): ").strip()
            try:
                dna = read_sequence_file(filename)
                if not is_valid_dna(dna):
                    print("The file is empty or contains invalid DNA characters.")
                    continue
                print(f"Loaded DNA sequence with {len(dna)} bases.")
                search_dna(dna)
            except OSError:
                print("Could not read that file. Check the file name and try again.")
        elif choice == "3":
            print("Thank you for using DNA Sequence Matcher!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Extract current CV entries from LaTeX document."""

import argparse

from TexSoup import TexSoup


def extract_current_positions(filename):
    """Extract current cv entries from LaTeX file."""
    with open(filename, "r", encoding="utf-8") as f:
        latex_content = f.read()

    soup = TexSoup(latex_content)
    current_positions = []

    # Find all cventry commands
    cventries = soup.find_all("cventry")

    for entry in cventries:
        args = entry.args
        if len(args) >= 5:
            period = str(args[0]).strip().strip("{}")
            position = str(args[1]).strip().strip("{}")
            company = str(args[4]).strip().strip("{}")  # Company is the 5th argument

            # Check if it's a current position (no end date)
            if "seit" in period.lower() or period.endswith("--"):
                # Format as simple markdown
                output = f"**{position}** bei {company} ({period})"
                current_positions.append(output)

    return current_positions


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Extract current CV entries")
    parser.add_argument("filename", help="LaTeX file to process")

    args = parser.parse_args()

    positions = extract_current_positions(args.filename)

    if positions:
        for position in positions:
            print(position)
    else:
        print("Keine aktuellen Positionen gefunden.")


if __name__ == "__main__":
    main()

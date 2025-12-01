# Hi! This is a Python script that converts exported Weglot translations to the format
# expected by Linguana. Simply run the following command in your terminal to complete
# the conversion process:

### python convert_from_weglot_to_linguana.py /path/to/input/file.csv /path/to/output/file.csv

# NOTE: Remember to replace /path/to/input/file.csv and /path/to/output/file.csv with the
# correct path to your exported Weglot translations CSV and the desired path and file name
# for the output CSV.

import csv
import sys


def convert_row(row):
    """
    Mapping function to convert original fields to target format
    """
    # Skip malformed rows where type field contains translation text
    if row["type"] not in ["Text", "Meta (SEO)"]:
        return None
    
    text = row["word_from"]
    ai_translation = row["word_to"] if row["quality"] == "Automatic" else ""
    manual_translation = row["word_to"] if row["quality"] != "Automatic" else ""
    
    # Map Weglot types to Linguana format
    if row["type"] == "Meta (SEO)":
        # Return both ATTRIBUTE and TEXT entries for Meta (SEO)
        attribute_row = [
            text,
            ai_translation,
            manual_translation,
            "ATTRIBUTE",
            "content",
            "meta",
        ]
        text_row = [
            text,
            ai_translation,
            manual_translation,
            "TEXT",
            "",
            "",
        ]
        return [attribute_row, text_row]
    else:  # row["type"] == "Text"
        return [[
            text,
            ai_translation,
            manual_translation,
            "TEXT",
            "",
            "",
        ]]


def main():
    if len(sys.argv) != 3:
        print(
            "Usage: python convert_from_weglot_to_linguana.py <input_file.csv> <output_file.csv>"
        )
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(input_file, mode="r", encoding="utf-8") as infile, open(
            output_file, mode="w", encoding="utf-8", newline=""
        ) as outfile:
            reader = csv.DictReader(infile, delimiter=";")
            writer = csv.writer(outfile, delimiter="|", quoting=csv.QUOTE_ALL)

            writer.writerow(
                [
                    "text",
                    "ai_translation",
                    "manual_translation",
                    "text_type",
                    "attribute_name",
                    "parsed_element_type",
                ]
            )

            for row in reader:
                converted_rows = convert_row(row)
                if converted_rows is not None:
                    for converted_row in converted_rows:
                        writer.writerow(converted_row)

        print("Conversion complete! Check the output file.")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

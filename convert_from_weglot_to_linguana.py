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
    text = row["word_from"]
    ai_translation = row["word_to"] if row["quality"] == "Automatic" else ""
    manual_translation = row["word_to"] if row["quality"] != "Automatic" else ""
    text_type = row["type"].upper() if row["type"] else "TEXT"
    attribute_name = "content" if text_type == "ATTRIBUTE" else ""
    parsed_element_type = (
        "meta" if row["type"] == "Meta (SEO)" else row["url"].strip("/")
    )

    return [
        text,
        ai_translation,
        manual_translation,
        text_type,
        attribute_name,
        parsed_element_type,
    ]


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
                writer.writerow(convert_row(row))

        print("Conversion complete! Check the output file.")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

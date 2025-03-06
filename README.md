# Convert Weglot Translations to Linguana Format

This Python script converts exported Weglot translation files into the format expected by Linguana.

## Usage

Run the following command in your terminal:

```sh
python convert_from_weglot_to_linguana.py /path/to/input/file.csv /path/to/output/file.csv
```

### Parameters
- `/path/to/input/file.csv`: The path to your exported Weglot translations CSV.
- `/path/to/output/file.csv`: The desired path and file name for the output CSV.

Make sure to replace these placeholders with actual file paths.

## Conversion Details
The script reads the Weglot CSV file and transforms its fields into the following format for Linguana:

| Field               | Description |
|--------------------|-------------|
| `text`            | Original text from Weglot |
| `ai_translation`  | Translation if marked as "Automatic" |
| `manual_translation` | Translation if not marked as "Automatic" |
| `text_type`       | Type of text (uppercase, defaults to "TEXT") |
| `attribute_name`  | Set to "content" if the type is "ATTRIBUTE", otherwise empty |
| `parsed_element_type` | Extracted element type from the `url` field, or "meta" if "Meta (SEO)" |

## Example Input
A sample Weglot CSV row:
```csv
word_from;word_to;quality;type;url
Hello;Bonjour;Automatic;Text;/home
```

## Example Output
After conversion, the corresponding row in the output CSV would look like:
```csv
Hello|Bonjour||TEXT||home
```

## Error Handling
If an error occurs during conversion, the script will print an error message and exit.

## Requirements
- Python 3
- CSV files must be semicolon (`;`) delimited

## Notes
- The script assumes that the Weglot CSV file uses a semicolon (`;`) as the delimiter.
- The output file will use a pipe (`|`) delimiter.

## License
This script is provided as-is, without any warranty or guarantee. Use at your own risk.

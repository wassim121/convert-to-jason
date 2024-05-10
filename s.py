import json

def transform_to_json(input_file, output_file):
    # List of keys to extract from each line
    keys_to_extract = ["id", "type", "year", "title", "authors", "pages", "booktitle", "journal", "url", "cites"]

    # List to store transformed data
    transformed_data = []

    # Read the input file
    with open(input_file, 'r') as infile:
        for line in infile:
            # Split the line into values (assuming it's CSV)
            values = line.strip().split(',')

            # Create a dictionary with specified keys and values
            data = {key: value for key, value in zip(keys_to_extract, values)}

            # Add the dictionary to the list
            transformed_data.append(data)

    # Write the transformed data to a JSON file
    with open(output_file, 'w') as outfile:
        json.dump(transformed_data, outfile, indent=2)

# Example usage with an input text file (replace "DBLP.txt" with your actual file)
transform_to_json("DBLP.txt", "output_json.json")

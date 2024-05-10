import json

def transform_to_json(input_file, output_file):
 
    keys_to_extract = ["id", "type", "year", "title", "authors", "pages", "booktitle", "journal", "url", "cites"]

    
    transformed_data = []

   
    with open(input_file, 'r') as infile:
        for line in infile:
            # Split the line into values (assuming it's CSV)
            values = line.strip().split(',')

           
            data = {key: value for key, value in zip(keys_to_extract, values)}

            transformed_data.append(data)


    with open(output_file, 'w') as outfile:
        json.dump(transformed_data, outfile, indent=2)

transform_to_json("DBLP.txt", "output_json.json")

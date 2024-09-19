import csv
import json
import os

def csv_to_dynamodb_json(csv_file):
    """
    Convert a CSV file to a JSON format that can be imported into DynamoDB.
    """
    items = []
    with open(csv_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            item = {}
            for key, value in row.items():
                if value:  # Only include non-empty values
                    item[key] = {'S': value}
            items.append(item)

    return json.dumps(items, indent=2)

# Get the current working directory
current_dir = os.getcwd()

# Construct the absolute path to the CSV file
csv_file = os.path.join(current_dir, 'Final_Expanded_Data_Latest_v2.csv')

# Convert CSV to JSON
json_data = csv_to_dynamodb_json(csv_file)

# Write the JSON data to a file
output_file = 'dynamodb_import.json'
with open(output_file, 'w') as f:
    f.write(json_data)

print(f"JSON data has been written to {output_file}")
import csv
import json
import os

def csv_to_dynamodb_json(csv_file):
    """
    Convert a CSV file to a JSON format that can be imported into DynamoDB.
    """
    # Construct the absolute path to the CSV file
    csv_file = os.path.join(current_dir, 'Final_Expanded_Data_Latest_v2.csv')

    items = []
    with open(csv_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            item = {}
            for key, value in row.items():
                if value:  # Only include non-empty values
                    item[key] = {'S': value}
            items.append(item)

    return json.dumps(items, indent=2)

# Get the current working directory
current_dir = os.getcwd()


# Convert CSV to JSON
json_data = csv_to_dynamodb_json(csv_file)

# Write the JSON data to a file
output_file = 'dynamodb_import.json'
with open(output_file, 'w') as f:
    f.write(json_data)

print(f"JSON data has been written to {output_file}")

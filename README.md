# CSV-JSON-Converter
 
The following Python script allows CSV files to be instantly converted into JSON files.  JSON formatted files are often necessary in data-related projects.

Our use case for converting to JSON was to import batch records into a DynamoDb table.

We did not include error handling, as this was only used for test data, however feel free to modify.

To use this simple script, you only need the following modules installed in your Python environment:
1. [JSON Module](https://docs.python.org/3/library/json.html) (import JSON)
2. [OS Module](https://docs.python.org/3/library/os.html) (import OS)
3. [CSV Module](https://docs.python.org/3/library/csv.html) (import CSV)

Its benefit is that it lets users quickly convert and build CSV files for any project use case.

## Adjustments

- The output file in our script is named 'dynamodb_import.json', which will be downloaded to your computer.  

```bash
output_file = 'dynamodb_import.json'
```

We stored the source file for conversion in the same directory as the script, if not you will have to point it to the [absolute path](https://www.delftstack.com/howto/python/set-file-path-python) and 
be sure to rename the <FILENEME> to your source file.

You will also need to rename the file of your source file to your source file. replace <FILENAME.CSV> with yours.

```bash
csv_file = os.path.join(current_dir, '<FILENAME.CSV>')
```

## Contributing

### Setting up the development environment

You'll need to have Python 3.8+ installed.  We used 3.12.4 

Create a [virtual environment](https://docs.python.org/3/library/venv.html):

```bash
python3 -m venv .venv
source .venv/bin/activate
```


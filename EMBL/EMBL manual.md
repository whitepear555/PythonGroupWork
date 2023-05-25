# EMBLParser Manual

## Introduction
The `EMBLParser` class is designed to parse EMBL (European Molecular Biology Laboratory) files and extract relevant information and sequences from them. It provides methods to parse the EMBL file, retrieve parsed records, list information, and obtain the sequence.

## Class Definition
```python
class EMBLParser:
    def __init__(self, embl_file):
        ...
    
    def parse_embl_file(self):
        ...
    
    def parse_sequence(self):
        ...
    
    def parse(self):
        ...
    
    def get_records(self):
        ...
    
    def list_information(self):
        ...
    
    def get_sequence(self):
        ...
```

## Class Methods

### \_\_init__(self, embl_file)
The constructor method initializes an instance of the `EMBLParser` class.

**Parameters:**
- `embl_file`: The path or filename of the EMBL file to be parsed.

**Usage:**

```python
embl_file = "path/to/your_embl_file"
parser = EMBLParser(embl_file)
```

### parse_embl_file(self)
This method parses the EMBL file and extracts relevant information into a dictionary.

**Usage:**
```python
parser.parse_embl_file()
```

### parse_sequence(self)
This method parses the EMBL file and extracts the DNA/RNA sequence.

**Usage:**
```python
parser.parse_sequence()
```

### parse(self)
This method combines the `parse_embl_file` and `parse_sequence` methods to parse both the file and the sequence.

**Usage:**
```python
parser.parse()
```

### get_records(self)
This method returns the parsed records as a dictionary.

**Returns:**
- `record` : A dictionary containing the parsed records.

**Usage:**
```python
records = parser.get_records()
```

### list_information(self)
This method prints the parsed information in a formatted manner.

**Usage:**
```python
parser.list_information()
```

### get_sequence(self)
This method returns the parsed DNA/RNA sequence.

**Returns:**
- `sequence` : The DNA/RNA sequence.

**Usage:**
```python
sequence = parser.get_sequence()
```

## Example Usage
Here is an example of how to use the `EMBLParser` class:

```python
embl_file = "path/to/your_embl_file"
parser = EMBLParser(embl_file)
parser.parse()
records = parser.get_records()

print("Record Information:")
parser.list_information()
for i in range(1, parser.num_records + 1):
    record = records[f'Record {i}']
    print(f"Record {i}:")
    print("RN:",record.get('RN'))
    print("RP:",record.get('RP'))
    print("RA:",record.get('RA'))
    print("RT:",record.get('RT'))
    print("RL:",record.get('RL'))
    print()

print("\nSequence:")
print(parser.get_sequence())
```

This example demonstrates how to instantiate an `EMBLParser` object, parse the EMBL file, retrieve parsed records, list the information, and obtain the sequence.
# VCFParser Manual

## Introduction
The `VCFParser` class is designed to parse Variant Call Format (VCF) files and extract variant information from them. It provides methods to parse the VCF file and retrieve the parsed variants.

The `Variant` class is used to represent a single variant and store its attributes.

## Class Definitions

### Variant Class
```python
class Variant:
    def __init__(self, CHROM, POS, REF, ALT, QUAL, FILTER, INFO, FORMAT):
        self.CHROM = CHROM
        self.POS = POS
        self.REF = REF
        self.ALT = ALT
        self.QUAL = QUAL
        self.FILTER = FILTER
        self.INFO = INFO
        self.FORMAT = FORMAT
```

### VCFParser Class
```python
class VCFParser:
    def __init__(self, filename):
        ...

    def parse_vcf(self):
        ...

    def get_variants(self):
        ...
```

## Class Methods

### \_\_init__(self, filename)
The constructor method initializes an instance of the `VCFParser` class.

**Parameters:**
- `filename` : The path or filename of the VCF file to be parsed.

**Usage:**
```python
filename = "path/to/your_vcf_file"
vcf_parser = VCFParser(filename)
```

### parse_vcf(self)
This method parses the VCF file and extracts variant information into a list of `Variant` objects.

**Usage:**
```python
vcf_parser.parse_vcf()
```

### get_variants(self)
This method returns the parsed variants as a list of `Variant` objects.

**Returns:**
- `variants` : A list of `Variant` objects representing the parsed variants.

**Usage:**
```python
variants = vcf_parser.get_variants()
```

## Example Usage
Here is an example of how to use the `VCFParser` class:

```python
filename = "path/to/your_vcf_file"
vcf_parser = VCFParser(filename)
vcf_parser.parse_vcf()
variants = vcf_parser.get_variants()

for variant in variants:
    print('Chromosome:', variant.CHROM)
    print('Position:', variant.POS)
    print('Reference:', variant.REF)
    print('Alternate:', variant.ALT)
    print('Quality:', variant.QUAL)
    print('Filter:', variant.FILTER)
    print('Info:', variant.INFO)
    print('Format:', variant.FORMAT)
    print()
```

This example demonstrates how to instantiate a `VCFParser` object, parse the VCF file, retrieve parsed variants, and access the variant attributes. The variant attributes printed in this example include Chromosome, Position, Reference allele, Alternate allele, Quality score, Filter information, and INFO field.
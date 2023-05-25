class Variant:
    def __init__(self, CHROM, POS, REF, ALT, QUAL, FILTER, INFO, FORMAT):
    #def __init__(self, CHROM, POS, REF, ALT, QUAL, FILTER, INFO, info, FORMAT_extra):
        self.CHROM = CHROM
        self.POS = POS
        self.REF = REF
        self.ALT = ALT
        self.QUAL = QUAL
        self.FILTER = FILTER
        self.INFO = INFO
        self.FORMAT = FORMAT
        #self.FORMAT_extra = FORMAT_extra

class VCFParser:
    def __init__(self, filename):
        self.filename = filename
        self.variants = []

    def parse_vcf(self):
        with open(self.filename, 'r') as file:
            for line in file:
                line = line.strip()

                if line.startswith('#'):
                    continue  # Skip header lines

                fields = line.split('\t')

                CHROM = fields[0]
                POS = int(fields[1])
                REF = fields[3]
                ALT = fields[4]
                QUAL = float(fields[5])
                FILTER = fields[6]
                INFO = fields[7]

                FORMAT = {}
                FORMAT_extra = {}
                format_fields = fields[8].split(':')
                format_fields_extra = fields[8].split(':')
                sample_data = fields[9].split(':')
                #sample_data_extra = fields[10].split(':') #if it contains A and B,then sample_data represents A,sample_data_extra represents B

                for i, field in enumerate(format_fields):
                    FORMAT[field] = sample_data[i]
                #for i, field in enumerate(format_fields_extra):
                    #FORMAT_extra[field] = sample_data_extra[i]


                variant = Variant(CHROM, POS, REF, ALT, QUAL, FILTER, INFO, FORMAT)
                #variant = Variant(CHROM, POS, REF, ALT, QUAL, FILTER, INFO, info, FORMAT_extra)

                self.variants.append(variant)

    def get_variants(self):
        return self.variants


# Usage example
filename = 'D:\edgedownload\\concat-a.vcf'
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
    #print('Format_extra:', variant.FORMAT_extra)
    print()

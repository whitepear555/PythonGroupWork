class EMBLParser:
    def __init__(self, embl_file):
        self.embl_file = embl_file
        self.record = {}
        self.sequence = ""

    def parse_embl_file(self):
        with open(self.embl_file, 'r') as file:
            record_number = 0
            record = {}
            for line in file:
                line = line.strip()

                if line.startswith('ID'):
                    self.record['ID_number'] = line.split()[1]
                    self.record['Topology'] = line.split()[4]
                    self.record['Mol_type'] = line.split()[5] + " " + line.split()[6]
                    self.record['Dataclass'] = line.split()[7]
                    self.record['Tax_division'] = line.split()[8]
                    self.record['Base_count'] = line.split()[9] + " " + line.split()[10]
                elif line.startswith('AC'):
                    self.record['Accession'] = line.split()[1]
                elif line.startswith('PR'):
                    self.record['PR'] = "   " + line.split()[1]
                elif line.startswith('DT'):
                    if 'DT' in self.record:
                        self.record['DT'] += line[2:]+ "."
                    else:
                        self.record['DT'] = line[2:]
                elif line.startswith('DE'):
                    if 'DE' in self.record:
                        self.record['DE'] += " " + line[2:]
                    else:
                        self.record['DE'] = line[2:]
                elif line.startswith('KW'):
                    self.record['KW'] = line[2:]
                elif line.startswith('OS'):
                    self.record['Organism'] = line.split()[1] + " " + line.split()[2] + ";"
                elif line.startswith('OC'):
                    if 'OC' in self.record:
                        self.record['OC'] += " " + line[2:]
                    else:
                        self.record['OC'] = line[2:]
                elif line.startswith('OG'):
                    self.record['Organelle'] = line.split()[1] + ";"
                elif line.startswith('RN'):
                    record_number += 1
                    record = {}
                    record['RN'] = "   " + line.split()[1]
                elif line.startswith('RP'):
                    record['RP'] = "   " + line.split()[1] + ";"
                elif line.startswith('RA'):
                    if 'RA' in record:
                        record['RA'] += " " + line[2:]
                    else:
                        record['RA'] = line[2:]
                elif line.startswith('RT'):
                    if 'RT' in record:
                        record['RT'] += " " + line[2:]
                    else:
                        record['RT'] = line[2:]
                elif line.startswith('RL'):
                    if 'RL' in record:
                        record['RL'] += " " + line[2:] + "."
                    else:
                        record['RL'] = line[2:]
                elif line.startswith('XX'):
                    self.record[f'Record {record_number}'] = record
                elif line.startswith('DR'):
                    if 'DR' in self.record:
                        self.record['DR'] += " " + line[2:]
                    else:
                        self.record['DR'] = line[2:]
                elif line.startswith('CC'):
                    if 'CC' in self.record:
                        self.record['CC'] += " " + line[2:]
                    else:
                        self.record['CC'] = line[2:]
                elif line.startswith('FT'):
                    if 'FT' in self.record:
                        self.record['FT'] += "\n" + line[2:]
                    else:
                        self.record['FT'] = line[2:]
                elif line.startswith('SQ'):
                    self.record['SQ'] = line[2:]
                    break
        self.num_records = record_number

    def parse_sequence(self):
        with open(self.embl_file, 'r') as file:
            start_sequence = False

            for line in file:
                line = line.strip()

                if line.startswith('SQ'):
                    start_sequence = True
                elif line.startswith('//'):
                    break
                elif start_sequence and line and not line.startswith('SQ'):
                    line_without_numbers = ''.join(char for char in line if not char.isdigit())
                    self.sequence += line_without_numbers.replace(' ', '')

    def parse(self):
        self.parse_embl_file()
        self.parse_sequence()

    def get_records(self):
        return self.record

    def list_information(self):
        print("ID_number:",self.record.get('ID_number'))
        print("Accession:",self.record.get('Accession'))
        print("Organism:",self.record.get('Organism'))
        print("Organelle:",self.record.get('Organelle'))
        print("Topology:",self.record.get('Topology'))
        print("Mol_type:",self.record.get('Mol_type'))
        print("Dataclass:",self.record.get('Dataclass'))
        print("Tax_division:",self.record.get('Tax_division'))
        print("Base_count:",self.record.get('Base_count'))
        print("PR:",self.record.get('PR'))
        print("DT:",self.record.get('DT'))
        print("DE:",self.record.get('DE'))
        print("KW:",self.record.get('KW'))
        print("OC:",self.record.get('OC'))
        print("DR:",self.record.get('DR'))
        print("CC:",self.record.get('CC'))
        print("FT:")
        if 'FT' in self.record:
            ft_lines = self.record['FT'].split('\n')
            merged_lines = []
            for line in ft_lines:
                line = line.strip()
                if line.startswith('/'):
                    line = line[1:]
                if merged_lines and not merged_lines[-1].endswith("\""):
                    merged_lines[-1] += " " + line
                else:
                    merged_lines.append(line)
            for line in merged_lines:
                print("   " + line)
        print("SQ:",self.record.get('SQ'))
    def get_sequence(self):
        return self.sequence


# Example usage
embl_file = "D:\edgedownload\KT266646.1.txt"
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


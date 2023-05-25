import EMBL

# 使用示例

EMBL_parser = EMBL.EMBLParser("your_file_path")

#输出基本解析信息

EMBL_parser.parse()

#输出序列顺序外的其他解析信息

EMBL_parser.get_records()

EMBL_parser.list_information()

for i in range(1, EMBL_parser.num_records + 1):

    record = EMBL_parser.get_records()[f'Record {i}']

    record.get() #RN RP RA RT RL

#输出序列排列顺序的解析信息

EMBL_parser.get_sequence()

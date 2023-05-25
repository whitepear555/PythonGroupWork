import blast

# 使用示例
blast_parser = blast.BlastParser("your_file_path")
#输出基本解析信息
blast_parser.parse()

#输出所用的数据库
blast_parser.db

#输出所用的参数
blast_parser.parse_para()

#输出所用blast工具的版本
blast_parser.version

#输出对比上的序列的信息
blast_parser.parse_hit()

#输出具体序列信息
blast_parser.parse_seq()

#输出比对上的具体序列
blast_parser.hit_seq

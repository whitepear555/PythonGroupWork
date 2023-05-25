import vcf

# 使用示例

vcf_parser = vcf.VCFParser("your_file_path")

#输出基本解析信息

vcf_parser.parse_vcf()

#分别输出不同位点的信息

vcf_parser.get_variants()

for variant in vcf_parser.get_variants():
    
    variant.CHROM #POS REF ALT QUAL FILTER INFO FORMAT
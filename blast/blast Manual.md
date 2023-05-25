# Manual

这是一个用于解析blast后得到的xml格式文件的工具，经过解析后可以得到输出文件的一系列基本信息。

## 运行环境

python 3

## 基本功能

### 1.得到基本解析信息

```python
import blast
blast_parser = blast.BlastParser("your_file_path")
blast_parser.parse()
```

输出以`>`开头，用`;`分为八列。

第一列为目标序列的名称；第二列为比对上的序列的序号；第三列为比对序列的长度；第四列为比对序列的框架；第五列为目标序列的起始位置；第六列为目标序列的结束位置；第七列为比对序列的id；第八列为比对序列的具体信息。

### 2.得到所用数据库

```python
import blast
blast_parser = blast.BlastParser("your_file_path")
blast_parser.db
```

输出即为所使用的数据库。

### 3.得到blast参数

```python
import blast
blast_parser = blast.BlastParser("your_file_path")
blast_parser.parse_para()
```

输出用`;`分为四列。

第一列为E值；第二列为match的分数；第三列为mismatch的分数；第四列为过滤方法。

### 4.得到blast版本

```python
import blast
blast_parser = blast.BlastParser("your_file_path")
blast_parser.version
```

输出为blast版本。

### 5.得到比对序列信息

```python
import blast
blast_parser = blast.BlastParser("your_file_path")
blast_parser.parse_hit()
```

输出两行为一组。

第一行以`>`开头，用`;`分为四列。

第一列为比对序列的序号；第二列为比对序列的id；第三列为比对序列的详细信息；第四列为比对序列的accession。

第二行以`>>`开头，用`;`分为四列。

第一列为对比序列中对比上的片段序号；第二列为该片段的bitscore；第三列为该片段的score；第四列为该片段的E值。

### 6.得到具体序列信息

```python
import blast
blast_parser = blast.BlastParser("your_file_path")
blast_parser.parse_seq()
```

输出六行为一组。

第一行以`>`开头，用`;`分为两列。

第一列为比对序列的序号；第二列为比对片段的序号。

第二行 用`;`分为两列。

第一列为目标序列起始位置；第二列为目标序列终止位置。

第三行为目标序列比对上的片段的具体序列，第四行为midline，第五行为比对序列片段的具体序列。

第六行用`;`分为两列。

第一列为比对序列的起始位置；第二列为比对序列的终止位置。

### 7.得到比对序列的具体序列

```python
import blast
blast_parser = blast.BlastParser("your_file_path")
blast_parser.hit_seq
```

输出两行为一组。

第一行以`>`开头，用`;`分为两列。

第一列为比对序列的序号；第二列为比对序列中片段的序列。

第二行为比对序列。
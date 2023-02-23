# this script is coming form this link https://www.pythontutorial.net/python-basics/python-write-csv-file/
import csv

# open the file in the write mode
f = open('./csv_file1', 'w')

# create the csv writer
writer = csv.writer(f)

# write a row to the csv file
for r in range(255):
    for g in range(255):
        for b in range(255):
            row = [str(r), str(g), str(b), '255']
            writer.writerow(row)
# close the file
f.close()

# dataframe读取中文列名，gbk编码
df = pandas.read_csv(i, skiprows=0,encoding='gbk',sep="\s+")

# dataframe 替换列名
for c in df1.columns:
    if c=="深度":
        df1 = df1.rename(columns={c: "DEPT"})

# 删除列
df1 = df1.drop(columns=[c])

# dataframe转浮点
df1 = df1.astype(float)

# 检查dataframe各个列的数据类型
df1.dtypes

# 获取文件的文件夹名
i=r"I:\aaa\bbb\cc\测井曲线.txt"
os.path.basename(os.path.dirname(i))

# 获取所有文件的目录列表
path1=r"I:\aaa\bbb"
all = []
for fpathe, dirs, fs in os.walk(path1):
    for f in fs:
        filename = os.path.join(fpathe, f)
        print(os.path.basename(os.path.dirname(filename)))
        all.append(filename)
        
# CSV文件整块读取
with open(i) as fp:
    data = fp.read()
    
# CSV文件单行读取
with open(i) as fp:
    first_line = fp.readline()
    
    
    

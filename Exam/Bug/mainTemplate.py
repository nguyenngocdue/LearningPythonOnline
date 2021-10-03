import csv
import pandas as pd

case_num = 5

schema = {}

with open(f'./sample_data/case_{case_num}/schema.csv') as f:
    reader = csv.reader(f)

    for idx, line in enumerate(reader):
        if idx: 
            schema[line[0]] = line[1]

num_fields = len(schema)

columns = []
data = []  

with open(f'./sample_data/case_{case_num}/data.csv') as f:
    reader = csv.reader(f)
    for idx, line in enumerate(reader):
        if idx:
            data.append(line[:num_fields])
        else:
            columns.extend(line[:num_fields]) 



df = pd.DataFrame(data, columns=schema.keys())

# """
# Code convert kiểu dữ liệu ở đoạn này
# Trong demo này không đưa vào vì phức tạp
# """
print(df.head())
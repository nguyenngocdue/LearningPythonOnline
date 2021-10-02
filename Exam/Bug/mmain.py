import csv
import pandas as pd

case_num = 4

schema = {}

with open(f'./sample_data/case_{case_num}/schema.csv') as f:
    reader = csv.reader(f)

    for idx, line in enumerate(reader):
        if idx: # có nghĩa idx >= 1, kết quả If True có value = 1, bỏ đi hàng thứ 0
            schema[line[0]] = line[1] # ép cột trái (key) gtri field_name , cột phải (value) gt field_dtype
            print(schema[line[0]], line[1], idx)

print("shema",schema)
print("***************")

num_fields = len(schema)
print(num_fields)


# Excel Data
# add gía trị field_name
#data 2: bị thiếu 1 cột salary

columns = []

# add giá trị field_type
#data 2: bị thiếu 1 cột salary
data = []  

with open(f'./sample_data/case_{case_num}/data.csv') as f:
    reader = csv.reader(f)
    for idx, line in enumerate(reader):
        if idx:# nếu idx =! 0 thì append các hàng từ thứ 1 trở đi vào data
            data.append(line[:num_fields])
        else:
            #field_name
            # nếu idx = 0 thì extend hàng thứ 0 vào columns
            #data2: sai, thiếu chiều dài lấy value khi dùng extend
            columns.extend(line[:num_fields]) 
print(columns)
print(data)
print("***********")


df = pd.DataFrame(data, columns=schema.keys())
print(schema)
print("**********")
print(df)
# """
# Code convert kiểu dữ liệu ở đoạn này
# Trong demo này không đưa vào vì phức tạp
# """
# print(df.head())
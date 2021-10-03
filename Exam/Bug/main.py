import csv
import pandas as pd

case_num = 5
schema = {}

with open(f'./Exam/Bug/sample_data/case_{case_num}/schema.csv') as f:
    reader = csv.reader(f) #Read CSV
    
    #Create a dict which was retrived Value from (field_name & field_dtype)
    for idx, line in enumerate(reader):
        if idx: # index >= 1, skip index == 0 and the first line
            schema[line[0]] = line[1] # add value of field_dtype into value of dictionary
            print("Index: ",idx," ,dict Key: ",line[0]," ,dict value: ",line[1])

print("My shema",schema)

num_fields = len(schema)
print("Length of Schema: ",num_fields)

print("**********************************")
# Excel Data
# add value form data.csv
columns = []
data = []  
with open(f'./Exam/Bug/sample_data/case_{case_num}/data.csv') as f:
    reader = csv.reader(f)
    for idx, line in enumerate(reader):
        if idx:# index >= 1, skip index == 0 and the first line
            data.append(line[:num_fields])
            print("data: ", data)
        else:
            #get value the first line of data.csv
            columns.extend(line[:num_fields])
            print("Columns: ", columns)
print("Columns value: ",columns)
print("Data value: ",data)
print("My Schema: ",schema)

df = pd.DataFrame(data, columns=schema.keys())

print("******************************")
# """
# Code convert kiểu dữ liệu ở đoạn này
# Trong demo này không đưa vào vì phức tạp
# """
print(df.head())
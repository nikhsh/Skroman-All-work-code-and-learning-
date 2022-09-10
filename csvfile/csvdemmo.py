'''
import json
import csv  
f = open('aa11234.json')
  
data = json.load(f)

column = list(map(lambda i: i, data[0]))
row = list(map(lambda i: i , data))

f.close()

with open("NikhilShinde1234.csv", 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=column)
    writer.writeheader()
    writer.writerows(row) 
    f.close()
'''

import json

my_dict = open('one.json')

cs = my_dict.readlines()
print("we are here...", cs)

my_list = []

dict_copy = my_dict.copy() # 👈️ create copy

my_list.append(dict_copy)

print(my_list)  # 👉️ [{'name': 'Alice', 'age': 30}]

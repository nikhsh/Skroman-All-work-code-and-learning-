'''
import json
import csv  
f = open('Shinde.json')
  
data = json.load(f)

column = list(map(lambda i: i, data[0]))
row = list(map(lambda i: i , data))

f.close()

with open("Aniket1233.csv", 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=column)
    writer.writeheader()
    writer.writerows(row) 
    f.close()


'''


import json
import csv

with open("aa2.json","r") as a:
    cd = a.readlines()
    print("welcome tijff..", cd)
   # f.close()
#dc = json.load(cd)
#print("we are here..", dc)

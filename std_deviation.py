import math
import csv

with open('pro105.csv',newline='') as f:
  reader = csv.reader(f)
  files_data = list(reader)

data= files_data[0]

def mean(data):
    n= len(data)
    total= 0
    for x in data:
        total+= int(x)
    mean= total/n
    return mean

s_list= []
for number in data:
    a= int(number)-mean(data)
    a= a**2
    s_list.append(a)

sum= 0
for i in s_list:
    sum= sum+i
result= sum/(len(data)-1)
std_deviation= math.sqrt(result)
print(std_deviation)
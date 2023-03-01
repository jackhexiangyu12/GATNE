import numpy as np
#f = open(r"D:\data.txt")
f = open("train.txt", encoding='gbk',mode='r+')
line = f.readline()
data_list = []
while line:
    num = list(map(float,line.split( )))
    f.write(str(num[1])+","+str(num[2])+"\n")
    line = f.readline()
f.close()
data_array = np.array(data_list)
#print(data_array[0])
print(len(data_array))
print(len(data_array[0]))

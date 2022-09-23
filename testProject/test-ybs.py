#两个哈希表dict1，dict2分别存入1000和2000，key为单词，value为出现次数
#ict1的最大值的键值对后将key存在maxlist中
#maxlist为为key的dict2中的值

import os
filename = r'D:\python_venv_test\pyVenvTest\test\tt.txt'
dict1 = {}
dict2 = {}
maxlist = []

with open(filename,'r') as file:
    
    for num1 in range(1,1001):
        #将1000行存入哈希表中
        line1 = file.readline().strip()
        if line1 not in  dict1:
            dict1[line1] = 1
        else:
            dict1[line1] = dict1[line1]+ 1
           
with open(filename,'r') as file:
    #将2000行存入哈希表2中
    for num2 in range(1,2001):
        line2 = file.readline().strip()
        if line2 not in  dict2:
            dict2[line2] = 1
        else:
            dict2[line2] = dict2[line2]+ 1
#获取1000行哈希表中的最大值
maxcount = max(dict1.values())
#获取1000中出现次数最多的key，并存入列表中
for key,value in dict1.items():
    if (value == maxcount):
        maxlist.append(key)
#1-1000行出现次数最多的key在整个文件中出现的次数
for i in maxlist:
        print('word : {} and count : {}' .format(i,dict2[i]))                                                                      
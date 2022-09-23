#数组中三个元素组成最小数字，若数组小于3，则所有元素组成最小
#  输入： 21,30,62,5,31
# 输出：21305
l1 = list(map(int,input().strip().split(',')))
sum = 0
if len(l1) == 0 :
    sum = 0
if len(l1) == 1:
    sum = l1[0]
if len(l1) == 2:
    sum = l1[0] + l1[1]
if len[l1] >= 3:
    l2 = ll.sort()
    sum = l2[0] + l2[1] + l2[2]
print(sum)




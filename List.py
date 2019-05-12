# list1=[1,'name']

# print(type(list1))
# print(id(list1))
# list1[0]=2
# print(list1)
# print(id(list1))

# list1=[1,'name',0.454,'myname',45]
#
# print(list1[2:])
# print(list1[:2])
# print(list1[-1:])
# print(list1[2:5])
#



# list1=[2,3,4]
# list2=[2,4,5]

# print(list1+list2)
# print(list1*3)

# print(len(list1))

# list3=list1[2:]
# print(list3)
#
# list4=[[1,2],[3,4],(3,4)]
# print(list4)
#
#


# Methods :

# list1=[2,3,5,6,7,8,9,0,0,3]

# list1.append(0)
# print(list1)

# print(list1.count(0))

# print(list1.index(3,2,9))

# list1.clear()
# print(list1)

# list2=list1.copy()
# print(id(list2))
# print(id(list1))

# list2=list1
# list1.append(3)
# print(id(list2))
# print(id(list1))
#
# print(list2)
# print(list1)


# list1=[2,3,5,6,7,8,9,0,0,3,'try']
# list2=[2,3,5,6,7,8,9,0,0,3,45,6,45,6,4756,7,65756,7]


# list1.extend(list2)
# print(list1)

# list1.insert(2,344334)
# print(list1)

# list1.remove(3)
# del list1[3]
# print(list1)

# list1.pop()
# print(list1)

# list1.reverse()
# print(list1)

# list1.sort()
# print(list1)

# list1=['s','c','d']
# list2=[x*2 for x in list1 if x=='s']
# print(list2)
#





# Conditional satatements:

# if False:
#     if False:
#         print('passsed')
#     else:
#         print('failed')
# else:
#     print("Failed")
#
# a=True
# b=0
# while b<5:
#     b+=1
#     print("a")
#
#
# for i in range(100,0,-1):
#     print(i)
#
#


# list_sum=[45,34545,6457,567,5688,678,69]
# sum=0
# for item in list_sum:
#     sum+=item
# print(sum)


# list_mulitple=[3,4,6,7]
# multiple=1
#
# for i in list_mulitple:
#     multiple*=i
# print(multiple)

# list_gr=[9,5,11,8,6]
# max1=0
# for i in range(0,len(list_gr)-1):
#     value=list_gr[i]
#     if max1>value:
#         max1=value
#     else:
#         pass
# print(max1)

# list_gr=[9,5,11,8,6]
# max1=list_gr[0]
# for i in range(0,len(list_gr)-1):
#     value=list_gr[i]
#     if max1<value:
#         max1=value
#     else:
#         pass
# print(max1)
'''
Write a Python program to count the number of strings where
 the string length is 2 or more and the first and last character are
  same from a given list of strings. Go to the editor 
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
'''
# sample_list=['abc', 'xyz', 'aba','c', '1221']
# res=0
# for sample_list_item in sample_list:
#  if len(sample_list_item)>=2 and sample_list_item[0]==sample_list_item[len(sample_list_item) - 1]:
#     res+= 1
# print(res)
#
#
# def sec(tunple_value):
#     return tunple_value[1]
#
# Sample_List = [(2, 5,3), (1, 2,4), (4, 4,4), (2, 3,2), (2, 1,3)]
#
# Sample_List.sort(key=sec,reverse=True)
# print(Sample_List)



a=[
    [1,2,3],
    [4,5,6],
    [3,4,5]

]

b = [
    [3, 2, 3],
    [5, 5, 6],
    [3, 6, 5]

]

import numpy as np

matrix_a=np.matrix(a)
matrix_b=np.matrix(b)

print(matrix_a+matrix_b)


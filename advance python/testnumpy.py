import numpy as np

# s=np.array([[1,2,4],[2,3,4.7]],dtype=np.int64)
# print(type(s))
# print(np.shape(s))
# print(s.itemsize)
#
#
# d=np.array([[2,3,4],[2,3,4]],ndmin=3)
# print(d)
# print(np.shape(d))
# print(d.shape)
# print(d.itemsize)
#
# # d=d.reshape(2,3,1)
# # print(d)


# x = np.empty([1,2,3], dtype = float)
# x = np.zeros([1,2,3], dtype = float)
# x = np.ones([1,2,3])

# print(x.dtype)
#
# print(x)


# arr = np.array(
#     [
#         [
#             [2, 3],
#             [4, 5],
#             [3,4]
#         ],
#         [
#             [5, 6],
#             [7, 8],
#             [3,7]
#         ]
#     ]
# )
#
# print(arr[:,:,:1])

# a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
#
#
# b=np.array([2,1,0,2])
#
# print(a[np.arange(4),b])
#
#

#
# a=np.array([[2,3,4]])
# print(a.shape)
# b=np.array([[6.0],[8],[4]])
# print(b.shape)
# c=a*b
# print(c.shape)
# print(c)



# x = np.array(
#     [
#         [1,2],
#         [3,4]
#     ]
# )
#
#
# print(np.sum(x))
# print(np.sum(x,axis=0))
# print(np.sum(x,axis=1))
#
# print(x.T)


# x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
# v = np.array([1, 0, 1])
# print(x+v)
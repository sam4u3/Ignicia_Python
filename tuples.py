#
#
# tup=('sayar','anand','ignicia',20)
# tuplist=['sayar','anand','ignicia',20]
# #
# # print(tup[3])
# # print(tup[1:3])
# # print(tup[-1:])
#
# tuplist[3]=40
# print(tuplist)
# tup[3]=40
# print(tup)
# x = ("Guru99", 20, "Education")    # tuple packing
# (name, id, profession) = ("Guru99", 20, "Education")    # tuple unpacking
# print(name)
# print(id)
# print(profession)
#
#
# a=(0,2)
# b=(0,2)
#
# if a==b:
#     print("yes")
# else:
#     print("no")
#
#
#
# s=(1,4,3,5,6,4,3)
#
# print(max(s))
# print(min(s))
#
# print(sorted(s))
# print(len(s))


a=9
print(id(a))
a=7
print(id(a))
a=9
print(id(a))

tup=(1,2,3,3,4,5)
# print(tup[3])
# (a,b,c,d,e,f)=tup
# print(a)
print(id(tup))

tup=tup+(8,9)
print(id(tup))
print(tup)
print(type(str(tup)))


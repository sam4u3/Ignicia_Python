# s1=r'helloworld\ns'
#
# print('h' not in s1)
#
#
name = 'guru'
number = 99

print('%s %d' % (name,number))

# print("{} {}".format(name,number))


# s1="hello,"

# print(s1.index("o"))
# print(s1*3)


# -----------------------------------------------------------

# 1) replace

# a="i am groot"
# a=a.replace("groot","root")
# print(a)

# 2) lowe and uper

# a="I am Groot I am"
#
# print(a.lower())
# print(a.upper())
# print(a.capitalize())

# 3)join

# print(":".join("iaa"))
# print(":".join("Python"))

# 4) reversed

# a="hello"
#
# print(' '.join(reversed(a)))


# 5) split scrren

# a="i :> am : groot"
#
# sp=a.split("p")
# print(sp)


#
# a="sadaAfad"
# print(a.casefold())
# print(a.count('s'))
# # print(a.center(3,'d'))
# print("1a".isalnum())
# print("4".isdigit())
# print(hex(45).isdecimal())


# -----------------------------------------------Pratice


'''
get input from user as a full name and 

a) split into firstname and lastname
b) replace "sam" to "RAM"
c) Set format to Upper case
d) repeat # after each characters
e) Reversed the full name


'''

#
# a=input("please enter full name")
# print(a.split(' '))
# print(a.replace("sam","RAM"))
# print(a.upper())
# print('#'.join(a))
# print(' '.join(reversed(a)))

'''
3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string. Go to the editor 
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Expected Result : Empty String'''
#
# s1='w3resource'
# print(s1[0:2]+s1[-2:])
# s2='w3'
# print(s2*2)
# s3='w'
# print(s3[0:0])

s="restartr"
print("".join((s[0], s[1:].replace(s[0],"$"))))

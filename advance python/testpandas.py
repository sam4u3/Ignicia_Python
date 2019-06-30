import pandas as pd

# dataheader=["name","age","std"]
# datavalues=["sayar","24","tyit"]
#
# header=pd.Series(dataheader)
# data=pd.Series(datavalues)
#
# print(type(header))
# print(type(data))
#
# df=pd.DataFrame(dataheader)
#
# print(type(df))

# data=[]
#
#
# student1={
#     "name":"ajay",
#     "age":20,
#     "std":"fyit"
#
# }
#
# student2 = {
#               "name": "sunil",
#               "age":22,
#           "std":"syit"
#
# }
#
# student3 = {
#               "name": "ramesh",
#               "age":23,
#           "std":"tyit"
#
# }
#
#
# data.append(student1)
# data.append(student2)
# data.append(student3)
#
# dataframe_student=pd.DataFrame(data)
# dataframe_student.to_csv("test.csv",index=False)
# dataframe_student.to_excel("test.xlsx",index=False)


#
# data=pd.read_excel("test.xlsx")
# print(data.fillna("N/A"))
#
# sum=0
# for ages in data['age']:
#     sum+=ages
# print(sum)
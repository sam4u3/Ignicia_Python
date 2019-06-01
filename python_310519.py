


class student():
    count=0
    def __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age
        self.class_name="TYIT"
        student.count+=1

    def student_print(self):
        print("ID : {}\nNAME : {}\nAGE: {}\nCLASS :{}\n".format(self.id,self.name,self.age,self.class_name))

    @classmethod
    def student_print_class(cls):
        print("Count :{}".format(cls.count))

stud1=student(1,"anand",21)
stud2=student(2,"sayar",23)
stud1.attr=34
stud1.asdsd=342




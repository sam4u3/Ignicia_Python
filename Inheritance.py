class programming():
    count=0
    def __init__(self,interpreter):
        self.interpreter=interpreter
        programming.count+=1

    def print_progarm(self):
        print(self.interpreter)

class python(programming):
    count=0
    def __init__(self,name,interpreter):
        self.name=name
        super().__init__(interpreter)
        python.count+=1

    def print_lang(self):
        print(self.name)


    def print_progarm(self):
        print('from python',self.interpreter)

class java(programming):
    count=0
    def __init__(self,name,interpreter):
        self.name=name
        super().__init__(interpreter)
        java.count+=1

    def print_lang(self, greeting):
        print(greeting, self.name)


# if __name__ == '__main__':
#         py1=python("python1","c#")
#         jv1=java("java","c")


import datetime

a=datetime.datetime(2014,12,23)+datetime.timedelta(days=2)



class Programmer(object):
    def __init__(self):
        self.plang=self.plang

    def p_print(self):
        print(self.plang)

class Tester(object):
    def __init__(self):
        self.tlang=self.tlang

class Employee(Programmer,Tester):
    def __init__(self,name,plang,tlang):
        self.name=name
        self.plang=plang
        self.tlang = tlang
        super(Programmer,self).__init__()
        super(Tester,self).__init__()


    def p_print(self):
        print(self.name)
        super().p_print()

emp=Employee("employe","java","selenium")

print(Employee.__mro__)


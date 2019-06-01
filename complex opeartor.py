class complex():
    def __init__(self,i=0,j=0):
        self.real=i
        self.img=j

    def __add__(self, other):
        self.real=self.real+other.real
        self.img = self.img + other.img
        return str(self.real)+'i+'+str(self.img)+'j'

    def __repr__(self):
       str_i="REAL part :"+str(self.real)+"\nIMAG part :"+ str(self.img)
       return str_i

c1=complex(1,1)
c2=complex(2,2)
print(c1)
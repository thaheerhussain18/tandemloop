#created an calculator class and taking parameters 
class calculator:
    def __init__(self,a,b,type_of_operation):
        self.a=a;
        self.b=b;
        self.type_of_operation=type_of_operation;
    def calculate(self):
        if(self.type_of_operation=="Addition"):
            return self.a+self.b;
        elif(self.type_of_operation=="Subtraction"):
            return self.a-self.b;
        elif(self.type_of_operation=="Multiplication"):
            return self.a*self.b;
        elif(self.type_of_operation=="Division"):
            return self.a/self.b;
        else:
            return "Invalid Operation Type"

#taking inputs from user and creating constructer of calculator to perform calculation
a=int(input("enter the a variable: "))
b=int(input("enter the b variable: "))
type_of_operation=input("enter the Operation to perform: ")
var1=calculator(a,b,type_of_operation)
print(var1.calculate())

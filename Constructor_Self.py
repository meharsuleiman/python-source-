#start of the class
class employee:
    #start of class method
    def printline(self):
        return f"the emplyee name is {self.name} and salary is {self.salary}"
    #end of class method

    #start of cunstroctor
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    #end of cunstroctor
#end of class

#create an object of class 
rohan = employee("sulaiman",234)
print(rohan.printline())



        



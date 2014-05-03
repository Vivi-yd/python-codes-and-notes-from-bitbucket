#header of the class definition
class Robot:
    
    #object has an attribute "name" which is set here in this method
    def __init__(self,name,buildYear):
        ##we will make the class attributes private by 
        ##appending their name with __
        self.__name = name
        self.__buildYear = buildYear

    def sayHello(self):
        print("Hello, I am " + self.__name + 
              ". I became a robot in the year " + 
              str(self.__buildYear) + ".")

    #set the name of the robot
    def setName(self, name):
        self.__name = name

    #get name of the robot 
    def getName(self):
        return self.__name
    
    #set the year when the robot was build
    def setBuildYear(self, buildYear):
        self.__buildYear = buildYear

    def getBuildYear(self):
        return str(self.__buildYear)
        
if __name__ == "__main__":
    x = Robot("Ashutosh", 2000)
    y = Robot("Veronica", 2010)
    for rob in [x, y]:
        rob.sayHello()
        print("I was built in the year " + rob.getBuildYear() + "!")    

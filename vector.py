##trying to define a vector class. it should have its three components as 
##its attributes

from math import sqrt

class Vector:
    
    ##in the init method we will set its components as privates
    def __init__(self, x, y, z):
        self.__x = x   ### the double underscore "__" that preceed the name is to make that particular
        self.__y = y   ### attribute inaccessible from the outside (users), making it unalterable.
        self.__z = z
    
    ##string reprsentation of the vector class
    def __str__(self):
        return "<%s, %s, %s>" %(self.__x, self.__y, self.__z)

    ##trying to define internal representation of the vector. the eval equality
    ##however won't work here
    def __repr__(self):
        return "<%s, %s, %s>" %(self.__x, self.__y, self.__z)
        
    
    ##get its components
    def getX(self):
        return self.__x
                                                
    def getY(self):
        return self.__y

    def getZ(self):
        return self.__z 

    #get the length of vector
    def length(self):
        return sqrt(self.__x ** 2 + self.__y ** 2 + self.__z ** 2)

    #add to another vector
    def add(self, other):
        return Vector(self.__x + other.__x, self.__y + other.__y, self.__z + other.__z)

    #dot product with another vector
    def dot(self, other):
        return self.__x * other.__x  + self.__y * other.__y + self.__z * other.__z
                                                                                                                                                                        
if __name__ == "__main__":
    a = Vector(2, 3, 4)
    b = Vector(3, 2, 1)
    c = a.add(b)
    print c #should print <5, 5, 5>
    print str(a.dot(b)) #should print 16
    
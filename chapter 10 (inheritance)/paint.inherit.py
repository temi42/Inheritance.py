from math import pi,sqrt
class PaintCircle:
    PAINT_COVERAGE=11
    PAINTCOST= 15
    NoOfObjectsPainted = 0
    def __init__(self,radius = 1):
        self.__rad = radius
        PaintCircle.NoOfObjectsPainted += 1

    def getRadius(self):
        return self.__rad
    
    def setRadius(self,radius):
        self.__rad = radius

    def getSArea(self):
        SA= (pi * self.getRadius()**2)
        return SA
    
    def getReqPaintCans(self):
        if PaintCircle.PAINT_COVERAGE > self.getRadius() :
            return self.getSArea() // PaintCircle.PAINT_COVERAGE
        else:
            return PaintCircle.PAINT_COVERAGE
        
    def getPaintCost(self):
        return PaintCircle.PAINTCOST * self.getReqPaintCans()

    def __str__(self):
        return " Radius: %.2f ft," %float(self.getRadius()) +\
                "Surface area: %.2f sqft," % float(self.getSArea())+\
                " Required paint: %d litres," %int(self.getReqPaintCans())+\
                " Paint cost: $%.2f\n" % float(self.getPaintCost())
#def main():
#    c1 = PaintCircle(5)
#    c2 = PaintCircle(10)
#    c3 = PaintCircle(15)
#    print("CIRCLE1:")
#    print(c1)
#    print("CIRCLE2:")
#    print(c2)
#    print("CIRCLE3:")
#    print(c3)
#    print("Number of Objects Painted: ", PaintCircle.NoOfObjectsPainted)
#main()

class PaintCone(PaintCircle):
    def __init__(self, radius, height = 1):
        super().__init__(radius)
        self.__radius = radius
        self.__height = height

    def getHeight(self):
        return self.__height

    def setHeight(self,height):
        self.__height = height

    def getSArea(self):
        area = (pi * self.__radius)*(self.__radius + sqrt(self.getHeight() **2 + self.__radius**2))
        return float(area)
    
    def __str__(self):
        return " Height: %.2f" %float(self.getHeight()) +\
               super().__str__()

class PaintCylinder(PaintCone):
    def __init__(self, radius, height):
        super().__init__(radius, height)
        self.__radius = radius
        self.__height = height

    def getCylinder(self):
        return self.__cylinder

    def setCylinder(self,cylinder):
        self.__cylinder = cylinder

    def getSArea(self):
        super().getSArea()
        area = (2 * pi * self.__radius * self.__height) + (2 * pi * self.__radius**2)
        return float(area)

    def __str__(self):
        return super().__str__()
    

def main():
    #question 1(a)
    c1 = PaintCircle(5)
    c2 = PaintCircle(10)
    c3 = PaintCircle(15)
    print("CIRCLE1:")
    print(c1)
    print("CIRCLE2:")
    print(c2)
    print("CIRCLE3:")
    print(c3)
    #question1(b)
    cone1 = PaintCone(10,10)
    cone2 = PaintCone(4,12)
    print("CONE1: ")
    print (cone1)
    print("CONE2: ")
    print(cone2)
    #question1(c)
    cylinder1 = PaintCylinder(5,12)
    cylinder2 = PaintCylinder(4,10)
    print("CYLINDER1: ")
    print(cylinder1)
    print("CYLINDER2: ")
    print(cylinder2)
    
    print("Number of Objects Painted: ", PaintCircle.NoOfObjectsPainted)
main()
    
        
                                                                                                             
                                                                                    
            
    

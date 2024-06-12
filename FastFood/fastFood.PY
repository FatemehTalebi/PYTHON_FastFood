import enum
from abc import ABC,abstractmethod


class Delivery(enum.Enum):
    
    PICKUP=0
    BIKE=5
    MOTOR=10
    CAR=15

class Size(enum.Enum):
    MINI=1
    MEDIUM=2
    LARGE=3
    
class DrinkType(enum.Enum):
    WATER=4
    PEPSI=6
    COKE=7
# ----------------------------------------------------

class Order():
    def __init__(self, deliveryMethod):
        self.deliveryMethod=deliveryMethod
        self.contents=[]
        
        
    def addItem(self,item):
        self.contents.append(item)
        
    def invoice(self):
        
        factor=0
        for item in self.contents:
            factor += item 
        factor +=self.deliveryMethod.value
        return f"delivery Method: {self.deliveryMethod.name}\nTotal: {factor} $ "
# ----------------------------------------------

class Pizza():
    def __init__(self,size):
        self.size=size
        self.contents=[]
        self.basePrice=10
        
    def addContent(self,content):
        self.contents.append(content)
        
    def factor(self):
        factor=0
        for content in self.contents:
            factor +=content.calculateContents()
        factor *= self.size  
        factor += self.basePrice
        return factor
# ---------------------------------------------
class Content(ABC):
    def __init__(self):
        super().__init__()
        
    @abstractmethod
    def calculateContents(self):
        pass
# ----------------------------------------------
class Chiken(Content):
    def __init__(self,weight):
        super().__init__()
        self.weight=weight
        
   
    def calculateContents(self):
        factor=self.weight*10
        return factor

# ----------------------------------------------
class Cheese(Content):
    def __init__(self,weight):
        super().__init__()
        self.weight=weight
        
   
    def calculateContents(self):
        factor=self.weight*5
        return factor
# ----------------------------------------------
class Mushroom(Content):
    def __init__(self,weight):
        super().__init__()
        self.weight=weight
        
   
    def calculateContents(self):
        factor=self.weight*4
        return factor
# ------------------------------------------------
class Drink():
    def __init__(self,drink):
        self.price=drink
        
# main app--------------------------------------
p1=Pizza(Size.LARGE.value)
p1.addContent(Chiken(0.3))
p1.addContent(Mushroom(0.1))
p1.addContent(Cheese(.01))
d1=Drink(DrinkType.COKE.value)
order1=Order(Delivery.BIKE)
order1.addItem(p1.factor())
order1.addItem(d1.price)
order1.invoice()
print(order1.invoice())


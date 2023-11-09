class thing():
    def __init__(self):
        pass
print(thing())
example = thing()
print(example)
print('they\'re the same')

class thing2():
    def __init__(self):
        self.letters = 'abc'
print(thing2().letters)
print('printed letters')

class thing3():
    def __init__(self,letters):
        self.letters = letters
ye = thing3('xyz')
print(ye.letters)
print(thing3('xyz').letters)
print('no I do not need to make an instance of this object to do this, but it is within the scope of reason')

class Element():
    def __init__(self,name,symbol,number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def dump(self):
        print(self.name,self.symbol,self.number)

e = Element('Hydrogen','H',1)

d = {'name' : 'Hydrogen', 'symbol' : 'H', 'number' : 1}
hydrogen = Element(**d)
hydrogen.dump()
print(hydrogen)

class Element():
    def __init__(self,name,symbol,number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def __str__(self):
        return (str(self.name)+' '+str(self.symbol)+' '+str(self.number))
    def __print__(self):
        print(__str__(self))
d = {'name' : 'Hydrogen', 'symbol' : 'H', 'number' : 1}
hydrogen = Element(**d)
print(hydrogen)

class Element():
    def __init__(self,name,symbol,number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number
    @property
    def name(self):
        return self.__name
    @property
    def symbol(self):
        return self.__symbol
    @property
    def number(self):
        return self.__number
    @name.setter
    def set_name(self,name):
        self.__name = name
    @symbol.setter
    def set_symbol(self,symbol):
        self.__symbol = symbol
    @number.setter
    def set_number(self,number):
        self.__number = number

class Bear():
    def eats(self):
        return 'berries (Bear)'
class Rabbit():
    def eats(self):
        return 'clovers (Rabbit)'
class Octothorpe():
    def eats(self):
        return 'campers (Octothorpe)'
b,r,o = Bear(),Rabbit(),Octothorpe()
print(b.eats(),r.eats(),o.eats())

class Laser():
    def does(self):
        return 'disintegrate (Laser)'
class Claw():
    def does(self):
        return 'crush (Claw)'
class SmartPhone():
    def does(self):
        return 'ring (Smartphone)'

class Robot(Laser,Claw,SmartPhone):
    def does(self):
        print(Laser().does(),Claw().does(),SmartPhone().does())
Robot().does()
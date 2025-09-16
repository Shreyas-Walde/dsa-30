class Human: 
# convention to always use first letter as Capital
    def __init__(self,age,name):
        self._age = age
        self._name = name
    
    def __str__(self):
        return "A human with name " + self._name + " age " + str(self._age)  
    
    def older_younger_than(self,age):
        if self._age> age:
            print("our age is bigger")
        elif self._age == age:
            print("onaji")
        else:
            print("our age is lesser")
    
h = Human(age=32,name="yamaguchi") # object
# object or instance of the human class
print(h)

print(h.__str__())

oldya= h.older_younger_than(32)
print(oldya)
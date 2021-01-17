class Node:
    def __init__(self, nodeVal=None, nextVal=None): 
        self.nodeVal = nodeVal
        self.nextVal = nextVal


# Create a class called AnimalShelter which holds only dogs and cats.
# The shelter operates using a first-in, first-out approach.
class AnimalShelter: 
    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear

# enqueue(animal): adds animal to the shelter. animal can be either a dog or a cat object.
    def enqueue(self, animal):
        new_node = Node(animal)
        if self.isempty() is True:
            self.front, self.rear = new_node
            return

        self.rear.next = new_node
        self.rear = new_node

# dequeue(pref): returns either a dog or a cat. If pref is not "dog" or "cat" then return null.
    def dequeue(self, pref):
        lower_pref = pref.lower()
        current_node = self.front
        prev_node = None

        if lower_pref != 'dog' and lower_pref != 'cat':
            return "Null"
        while current_node:
            animal = current_node.nodeVal
            if animal.species == lower_pref:
                if prev_node is None:
                    self.front = current_node.nextVal
                    current_node.nextVal = None
                    return current_node
                prev_node.nextVal = current_node.next
                if current_node.nextVal == None:
                    self.rear = prev_node
                current_node.nextVal = None
                return current_node
            prev_node = current_node
            current_node = current_node.nextVal

        return "Null" 


    def isempty(self):
        if self.front is None and self.rear is None: 
            print("True")
            return True
        else: 
            print("False")
            return False


    def print_helper(self):
        current_node = self.front
        new_str = ''
        while (current_node) :
            new_str += '[ name: ' + current_node.nodeVal.name + ', species: ' + current_node.nodeVal.species + '] -> '
        current_node = current_node.nextVal
        new_str += 'null'
        return new_str


class Animal:
    def __init__(self, name="", species=None): 
        self.name = name
        self.species = species

class Dog(Animal): 
    def __init__(self, species):
        self.species = 'dog'

class Cat(Animal): 
    def __init__(self, name=None):
        self.name = name
        self.species = 'cat'

littleton = Animal.Dog('Littleton')
print("------------")
print(littleton)




# class Animal:
#     def __init__(self, Name=", Age=0, Type="):
#         self.Name = Name
#         self.Age = Age
#         self.Type = Type
#     def GetName(self):
#         return self.Name
#     def SetName(self, Name):
#         self.Name = Name
#     def GetAge(self):
#         return self.Age
#     def SetAge(self, Age):
#         self.Age = Age
#     def GetType(self):
#         return self.Type
#     def SetType(self, Type):
#         self.Type = Type
#     def __str__(self):
#         return "{0} is a {1} aged {2}".format(self.Name,
#                 self.Type,
#                 self.Age)

# class Chicken(Animal):
#     def __init__(self, Name="", Age=0):
#         self.Name = Name
#         self.Age = Age
#         self.Type = "Chicken"
#     def SetType(self, Type):
#         print("Sorry, {0} will always be a {1}"
#         .format(self.Name, self.Type))
#     def MakeSound(self):
#         print("{0} says Cluck, Cluck, Cluck!".format(self.Name))

# MyChicken = Animal.Chicken("Sally", 2)
# print("--------")
# print(MyChicken)
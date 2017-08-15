## animal is-a object
class Animal(object):
	pass

##?? dog is annoying
class Dog(animal):

	def __init))(self, name):
		## bow bow, dog has a name
		self.name = name

## ?? cat is an animal
class Cat(Animal):

	def __init__(self, name):
		# cats have names
		self.name = name

## really animal, but fine, i'll take object
class Person(object):

	def __init__(self, name):
		## just call a human an object with name?
		self.name = name

		# and we own pets!
		self.pet = None # only animals I own are edible.

## employee is object of class person?
class Employee(Person):

	def __init__(self, name, salary):
		## ?? what is this magic?
		super(Employee,self).__init__(name)
		##??
		self.salary = salary

## Fish is a class of object
class Fish(object):
	pass

## salmon is a class of fish
class Salmon(Fish):
	pass

##?? Halibut is a class of fish
class Halibut(Fish):
	pass


## rover isa dog
rover = Dog("Rover")

## satan is a cat
satan = Cat("Satan")

##mary is a person
mary = Person("Mary")

## mary has a pet, satan
mary.pet = satan

## frank is an employee and has a salary of 12000
frank = Employee("Frank",120000)

## frank has a pet rover
frank.pet = rover

## flipper is a fish
flipper = Fish()

## crouse is a salmon
crouse = Salmon()

## harry is a halibut()
harry = Halibut()

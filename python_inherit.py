class Student:
	def __init__(self, name, school):
		self.name = name
		self.school = school
		self.marks = []

	def average(self):
		return sum(self.marks) /len(self.marks)
#	@classmethod
#        def friend(cls, friend_name):
#                return cls(friend_name, self.school)

	@classmethod
	def friend(cls,origin, friend_name, salary):
		return cls(friend_name, origin.school, salary)

class Wat(Student):
	def __init__(self, name, school, salary):
		super().__init__(name, school)
		self.salary = salary

sunil = Wat("sunil", "JNV", 20)
sunil.marks = [76, 85, 90, 39]
print(sunil.average())
#print(sunil.average())
bozo = sunil.friend(sunil, "vishal", 20)
print(bozo.name)
print(bozo.school)
bozo.marks = [10, 5, 6]
print(bozo.average())
print(bozo.salary)

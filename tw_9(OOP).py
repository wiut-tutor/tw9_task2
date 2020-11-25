class Student:
	def __init__(self, id, marks):
		self.id = id
		self.marks = marks

	def calculateAverage(self):
		total = 0
		for key in self.marks:
			total = total + self.marks[key]
		average = total / len(self.marks)
		return average

	def display_average(self):
		print(self.calculateAverage())

if __name__=='__main__':
	Student1 = Student(1234, {'CSF': 75, 'FunPro': 80, 'WT': 85})
	Student1.display_average()

	Student2 = Student(4321, {'CSF': 65, 'FunPro': 70, 'WT': 75})
	Student2.display_average()

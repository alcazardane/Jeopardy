class gameClass:
	def __init__(self, categ, q_value):
		self.categ = categ
		self.q_value = q_value

	def categ_value(self):
		print("Your category is " + self.categ)
		print("The value is " + self.q_value)
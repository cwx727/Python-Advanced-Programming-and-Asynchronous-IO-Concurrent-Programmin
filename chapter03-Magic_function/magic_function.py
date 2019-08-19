class Company:
	def __init__(self, employee_list):
		self.employee_list = employee_list

	def __str__(self):
		return ','.join(self.employee_list)

	def __repr__(self):
		return ','.join(self.employee_list)

	def __len__(self):
		return len(self.employee_list)

	def __getitem__(self, item):
		return self.employee_list[item]

company = Company(['tom','bob','jame'])
for em in company:
	print(em)
 
class Date:
	def __init__(self, year, month, day):
		self.year = year
		self.month = month
		self.day = day

	def tomorrow(self):
		self.day = int(self.day) + 1

	@staticmethod
	def parse_from_string(date_str):
		year,month,day =  tuple(date_str.split('-'))
		return Date(int(year), int(month), int(day))

	@staticmethod
	def valid_str(date_str):
		year,month,day =  tuple(date_str.split('-'))
		if int(year)>0 and int(month)<=12 and int(day)<=31:
			return True
		else:
			return False

	@classmethod
	def from_string(cls, date_str):
		year,month,day =  tuple(date_str.split('-'))
		return cls(int(year), int(month), int(day))



	def __str__(self):
		return str(self.year) + '/' + str(self.month) + '/'+ str(self.day)


if __name__ == '__main__':
	new_day = Date(2019,1,1)
	new_day.tomorrow()
	print(new_day)
	print(new_day.year)

	new_day = Date.parse_from_string('2019-1-1')
	print(new_day)

	new_day = Date.from_string('2019-1-1')
	print(new_day)

	new_day = Date.valid_str('2019-1-1')
	print(new_day)
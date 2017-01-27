from terminaltables import AsciiTable

class Todo(object):

	def __init__(self):
		self.skill_dict={}
		self.course =''
		self.status =''

	def helper(self):
		Green= '\033[32m' #Green Text Color

		self.choice = eval(input(
			Green + 
				'''

			Welcome to my Console App
		This app checks progress on various courses

			Please select appropriately
			1. Add a skill
			2. View All SKills
			3. View Completed SKills
			4. View Pending Skills

			''' + B))

		if type(self.choice) ==int:

			if self.choice == 1:
				self.add_skill()

			elif self.choice == 2:
				self.view_all()

			elif self.choice == 3:
				self.view_completed()

			elif self.choice == 4:
				self.view_pending()

			elif self.choice == 5:
				self.delete_skill()

		else:
			raise TypeError('Invalid input {}'.format(type(self.choice)))

	def add_skill(self):
		self.skill_len = eval(input("How many skills to add: "))

		count = 0

		while count < self.skill_len:
			self.course = input("Add a Skill: ")
			self.status = input("Is {} completed? [y/n]: ".format(self.course))

			if self.status == "y":
				self.skill_dict[self.course] = "Completed"
			elif self.status == "n":
				self.skill_dict[self.course] = "Pending"

			count +=1

		print('''You have successfully added  the following Courses''')

		self.add_dict = [['Course', 'Status']]

		for key, value in self.skill_dict.items():
			temp_add_dict = [key, value]

			self.add_dict.append(temp_add_dict)

		self.add_table = AsciiTable(self.add_dict)
		print(self.add_table.table)

		self.add_more_skill()

	def add_more_skill(self):

		self.add_more = input("Do you want to add more skills?")

		if self.add_more == "y":
			self.add_skill()

		elif self.add_more == "n":
			self.helper()

	def view_all(self):
		self.new_skill_dict = [['Course', 'Status']]

		for key, value in self.skill_dict.items():

			temp = [key, value]

			self.new_skill_dict.append(temp)
		
		#print(list(self.new_skill_dict))


		self.view_table = AsciiTable(self.new_skill_dict)
		print('\x1b[6;30;43m'+self.view_table.table)

		self.add_more_skill()


	def view_pending(self):

		self.pending_dict = {key: value for key, value in self.skill_dict.items() if value == "Pending"}
		self.key_list = [['Pending Courses']]
		for key, value in self.pending_dict.items():
			temp_key_list = [key]

			self.key_list.append(temp_key_list)
		self.view_pending_table = AsciiTable(self.key_list)
		print(self.view_pending_table.table)

		self.add_more_skill()


	def view_completed(self):
		self.completed_dict = {key: value for key, value in self.skill_dict.items() if value == "Completed"}
		self.total_completed = str(len(self.completed_dict))
		self.key_list = [['{} Completed Courses'.format(self.total_completed)]]
		for key, value in self.completed_dict.items():
			temp_key_list = [key]

			self.key_list.append(temp_key_list)

		self.view_completed_table = AsciiTable(self.key_list)
		print(self.view_completed_table.table)

		self.add_more_skill()


s = Todo()
s.helper()

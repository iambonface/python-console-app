from terminaltable import AsciiTable

class Todo(object):

	def __init__(self):
		self.skill_dict={}
		self.course =''
		self.status =''

	def helper(self):
		self.choice = eval(input('''
		\x1b[6;30;46m +  

			Welcome to my Console App
		This app checks progress on various courses

			Please select appropriately
			1. Add a skill
			2. View All SKills
			3. View Completed SKills
			4. View Pending Skills
			5. Delete a Skill

			\x1b[0m

			 '''))

		if type(self.choice) ==int:

			if self.choice == 1:
				self.add_skill()

			elif self.choice == 2:
				self.view_all()

			elif self.choice == 3:
				self.view_completed

			elif self.choice == 4:
				self.view_pending

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

		print("Successfully added {}".format(self.skill_dict))

		self.add_more = input("Do you want to add more skills?")

		if self.add_more == "y":
			self.add_skill()

		elif self.add_more == "n":
			self.helper()



	def view_all(self):
		pass

	def view_pending(self):
		pass

	def view_completed(self):
		pass

	def delete_skill(self):
		pass

s = Todo()
s.helper()
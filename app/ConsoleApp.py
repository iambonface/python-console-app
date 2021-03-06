"""
Console App

It's useful to track personal learning progress when going through any learning program (like bootcamp). 
This command line program, helps bootcamp participants to track their progress using the learning map. 
As a user you can 
    1. Add skills
    2. View a list of all the skills added
    3. View the list of skills that you have studied(completed)
    4. View the list of skills that you haven't studied yet (Pending) and see the learning progress.

"""
import sys

from terminaltables import AsciiTable

class LearningMap(object):

	def __init__(self):
		self.skill_dict={}
		self.course =''
		self.status =''


	def get_input(self,text):
		return input(text)


	def get_prompt(self):
		#Green= '\033[32m' #Green Text Color
		print('''
			Welcome to my Console App
		This app checks progress on various courses

			1. Add a skill
			2. View All SKills
			3. View Completed SKills
			4. View Pending Skills
			5. View Statistics
			6. Exit
			''')

		while True:
			try:
				self.choice = self.get_input("Select 1, 2, 3, 4, 5, 6:")
				self.choice = int(self.choice)
				self.get_method()
				break
			except ValueError:
				print("INVALID INPUT. TRY AGAIN")

	def get_method(self):

		if self.choice == 1:
			self.add_skill()

		elif self.choice == 2:
			self.view_all()

		elif self.choice == 3:
			self.view_completed()

		elif self.choice == 4:
			self.view_pending()

		elif self.choice == 5:
			self.view_statistics()

		elif self.choice ==6:
			sys.exit()
		else:
			print("Invalid selection. You must select [1, 2, 3 or 4]")


	def add_skill(self):
		while True:
			try:
				self.skill_len = input("How many skills do you want to add? ")
				self.skill_len = int(self.skill_len)
				if self.skill_len < 1:
					print("You cannot add {}".format(self.skill_len))
					self.add_skill()
				else:
					break

			except ValueError:
				print("Invalid input. This must be an Integer")

		count = 0

		while count < self.skill_len:
			self.course = input("Add a Skill: ")

			while True:
				try:
					self.status = input("Is {} completed? [y/n]: ".format(self.course))
					self.status = str(self.status)
					break
				except ValueError:
					print("Choose [y/n]")
			if self.status == "y":
				self.skill_dict[self.course] = "Completed"
			elif self.status == "n":
				self.skill_dict[self.course] = "Pending"
			else:
				print("\nInvalid selection. You must select [y/n]")
	
			count +=1

		print("\nThe following following Courses were added correctly\n")

		self.add_dict = [['Course', 'Status']]

		for key, value in self.skill_dict.items():
			temp_add_dict = [key, value]

			self.add_dict.append(temp_add_dict)

		self.add_table = AsciiTable(self.add_dict)
		print(self.add_table.table)

		self.add_more_skill()

	def add_more_skill(self):

		while True:
			try:
				self.add_more = input("Do you want to add more skills? [y/n]: ")
				self.add_more = str(self.add_more)
				break

			except ValueError:
				print("Choose [y/n]")

		if self.add_more == "y":
			self.add_skill()

		elif self.add_more == "n":
			self.get_prompt()
		else:
			print("Invalid selection. You must select [y/n]")
			self.add_more_skill()


	def view_all(self):
		self.new_skill_dict = [['Course', 'Status']]

		for key, value in self.skill_dict.items():

			temp = [key, value]

			self.new_skill_dict.append(temp)
		
		#print(list(self.new_skill_dict))


		self.view_table = AsciiTable(self.new_skill_dict)
		print(self.view_table.table)

		self.add_more_skill()


	def view_pending(self):

		self.pending_dict = {key: value for key, value in self.skill_dict.items() if value == "Pending"}

		self.total_length = len(self.skill_dict.items())

		self.pending_length = len(self.pending_dict)


		self.total_pending = str(self.pending_length)
		self.key_list = [['{} Pending Courses'.format(self.total_pending)]]
		for key, value in self.pending_dict.items():
			temp_key_list = [key]

			self.key_list.append(temp_key_list)

		self.view_pending_table = AsciiTable(self.key_list)
		print(self.view_pending_table.table)


		self.add_more_skill()


	def view_completed(self):
		self.completed_dict = {key: value for key, value in self.skill_dict.items() if value == "Completed"}

		self.total_length = len(self.skill_dict.items())
		

		self.completed_length = len(self.completed_dict)

		self.total_completed = str(self.completed_length)
		self.key_list = [['{} Completed Courses'.format(self.total_completed)]]

		for key, value in self.completed_dict.items():
			temp_key_list = [key]

			self.key_list.append(temp_key_list)

		self.view_completed_table = AsciiTable(self.key_list)
		print(self.view_completed_table.table)


		self.add_more_skill()

	def view_statistics(self):
		self.completed_dict = {key: value for key, value in self.skill_dict.items() if value == "Completed"}

		self.pending_dict = {key: value for key, value in self.skill_dict.items() if value == "Pending"}

		self.pending_length = len(self.pending_dict)

		self.completed_length = len(self.completed_dict)

		self.total_length = len(self.skill_dict.items())

		if self.total_length < 1:
			print("No courses were added. We cannot figure out statistics with 0 courses")
			self.add_more_skill()

		elif self.completed_length == 0:
			print("You currently only have {} pending course".format(self.pending_length))
			self.add_more_skill()


		elif self.pending_length == 0:
			print("You currently only have {} completed sourse".format(self.completed_length))
			self.add_more_skill()


		else:
			self.percentage_pending =  ((self.pending_length/self.total_length) * 100)
			self.percentage_completed =  ((self.completed_length/self.total_length) * 100)

			print("\n{} Total Courses \n".format(self.total_length))

			
			print('%.0f' % (self.percentage_completed) + '% Completed')

			print('%.0f' % (self.percentage_pending)  + '% Pending\n')





lm = LearningMap()


lm.get_prompt()



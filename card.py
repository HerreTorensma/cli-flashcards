# import the Foreskin class from colorama 
from colorama import Fore

import platform
import os

def clear():
	if platform.system() == "Windows":
		os.system("CLS")
	else:
		os.system("clear")

class Card:
	def __init__(self, name, desc, known):
		self.name = name
		self.desc = desc
		self.known = known

		self.width = 60
		# Use odd numbers only
		self.height = 11

	def display_name(self):
		clear()

		print(Fore.MAGENTA + "Front")
		self.print_card(self.name, Fore.YELLOW)

		self.show_prompts()

	def print_top_row(self):
		print(Fore.WHITE + "┌", end="")
		for i in range(self.width):
			print("─", end="")
		print("┐")

	def print_bottom_row(self):
		print("└", end="")
		for i in range(self.width):
			print("─", end="")
		print("┘")

	def print_middle_rows(self):
		space = int(self.height / 2) - 1
		for i in range(space):
			print("│", end="")
			for j in range(self.width):
				print(" ", end="")
			print("│")

	def print_card(self, text, color):
		self.print_top_row()
		self.print_middle_rows()

		left_space = int((self.width / 2) - (0.5 * len(text)))
		print("│", end="")
		for i in range(left_space):
			print(" ", end="")
		print(color + text, end="")
		right_space = self.width - (left_space + len(text))
		for i in range(right_space):
			print(" ", end="")
		print(Fore.WHITE + "│")

		self.print_middle_rows()
		self.print_bottom_row()

	def print_desc_card(self):
		self.print_top_row()

		split_desc = self.desc.split()
		words = []
		for word in split_desc:
			words.append(word + " ")

		print("│", end="")
		
		space_left = self.width
		lines_used = 1
		for i in range(0, len(words)):
			space_left -= len(words[i])
			if len(words[i]) <= space_left:
				print(words[i], end="")
			else:
				print(words[i], end="")

				for j in range(space_left):
					print(" ", end="")

				print("│")
				print("│", end="")
				space_left = self.width
				lines_used += 1
			
		for i in range(space_left):
			print(" ", end="")
		
		print("│")

		for i in range(self.height - lines_used - 2):
			print("│", end="")
			for j in range(self.width):
				print(" ", end="")
			print("│")

		self.print_bottom_row()

	def display_desc(self):
		print()

		print(Fore.MAGENTA + "Back" + Fore.WHITE)
		self.print_desc_card()

		input()

	def show_prompts(self):
		knew = " Know (y)"
		print(Fore.GREEN + knew, end="")
		
		didntknow = "Don't know (n)"
		for i in range(self.width - len(knew) - len(didntknow) + 1):
			print(" ", end="")

		print(Fore.RED + didntknow)

		print()

		inputted = False
		while inputted == False:
			card_input = input(Fore.WHITE + ">>> ")
			if card_input == "y" or card_input == "Y":
				inputted = True
				self.known = True
				self.display_desc()
			elif card_input == "n" or card_input == "N":
				inputted = True
				self.known = False
				self.display_desc()
			else:
				print("Invalid input. Type y for yes or n for no.")
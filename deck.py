import yaml
from card import Card
from colorama import Fore
from random import shuffle

class Deck:
	def __init__(self, deck_name):
		self.deck_name = deck_name

		self.read_file()
		self.fill_cards()

	def read_file(self):
		with open(f"decks/{self.deck_name}.yml", "r") as file:
			self.data = yaml.safe_load(file)

	def fill_cards(self):
		self.cards = []
		for card in self.data["cards"]:
			known = False

			if "known" in card:
				known = card["known"]

			self.cards.append(Card(card["name"], card["desc"], known))

	def update_data(self):
		for i in range(len(self.cards)):
			self.data["cards"][i]["name"] = self.cards[i].name
			self.data["cards"][i]["desc"] = self.cards[i].desc
			self.data["cards"][i]["known"] = self.cards[i].known

	def write_file(self):
		with open(f"decks/{self.deck_name}.yml", "w") as file:
			yaml.dump(self.data, file, default_flow_style=False, sort_keys=False)

	def set_all_cards_false(self):
		for card in self.cards:
			card.known = False

		self.update_data()
		self.write_file()

	def loop_cards(self):
		shuffle(self.cards)

		for card in self.cards:
			if card.known == False:
				card.display_name()
				self.update_data()
				self.write_file()

		inputted = False
		while inputted == False:
			unknown_cards = 0
			for card in self.cards:
				if card.known == False:
					unknown_cards += 1
			
			print(f"There are {unknown_cards} cards you don't know.")

			if unknown_cards == 0:
				print("Congratulations! You know everything.")
				return
			
			again = input("Go again? (y/n) ")
			if again == "y" or again == "Y":
				inputted = True
				self.loop_cards()
			elif again == "n" or again == "N":
				inputted = True
			else:
				print("Invalid input. Type y for yes or n for no.")

	def add_cards(self):
		while True:
			name = input("Name: ")
			desc = input("Desc: ")
			continue_adding = input("Stop? (y) ")
			
			self.data["cards"].append({"name": name, "desc": desc, "known": False})
			
			if continue_adding == "y" or continue_adding == "Y":
				break

		self.write_file()

	def list_cards(self):
		for i in range(0, len(self.data["cards"])):
			print(Fore.MAGENTA + f"{i}: ", end="")
			print(Fore.YELLOW + self.data["cards"][i]["name"])
			print(Fore.WHITE + self.data["cards"][i]["desc"])
			print()

	def remove_card(self):
		self.list_cards()
		inputted = False
		while inputted == False:
			card_to_remove = int(input("Card number to remove: "))
			if card_to_remove < len(self.data["cards"]):
				inputted = True
			else:
				print("Number too big. Try again.")
		
		self.data["cards"].pop(card_to_remove)
		self.write_file()
		print("Removed card.")
import yaml
import sys

from deck import Deck

def start():
	if len(sys.argv) > 3:
		print("Too many arguments.")
		return

	if len(sys.argv) > 1:
		if sys.argv[1] == "create":
			with open(f"decks/{sys.argv[2]}.yml", "w") as file:
				yaml.dump({"cards": []}, file)
			return

		deck = Deck(sys.argv[1])

		if len(sys.argv) == 3:
			if sys.argv[2] == "clear":
				deck.set_all_cards_false()
				return
			
			if sys.argv[2] == "add":
				deck.add_cards()
				return

			if sys.argv[2] == "list":
				deck.list_cards()
				return

			if sys.argv[2] == "remove":
				deck.remove_card()
				return

		deck.loop_cards()

	else:
		print("Too few arguments.")

if __name__ == "__main__":
	start()
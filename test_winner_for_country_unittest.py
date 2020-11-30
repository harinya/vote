from winner_declaration import get_winner_for_country
import unittest

class TestWinnerForCountry(unittest.TestCase):
	def test_winner_for_country_valid(self):
		winner = get_winner_for_country()
		self.assertEqual(winner,"Draw")

	def test_winner_for_country_valid_negative(self):
		winner = get_winner_for_country()
		self.assertFalse(winner == "Bunty")

	def test_winner_for_country_valid_negative2(self):
		winner = get_winner_for_country()
		self.assertFalse(winner == "Babli")

	def test_winner_for_country_invalid_integer(self):
		with self.assertRaises(TypeError):
			get_winner_for_country(10)

	def test_winner_for_country_invalid_string(self):
		with self.assertRaises(TypeError):
			get_winner_for_country("abv")

if __name__ == "__main__":
   	unittest.main()
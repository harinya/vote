from winner_declaration import get_winner_of_state
import unittest

class TestWinnerOfState(unittest.TestCase):
	def test_winner_of_state_california(self):
		winner = get_winner_of_state('California')
		self.assertEqual(winner,"Babli")

	def test_winner_of_state_false_california(self):
		winner = get_winner_of_state('California')
		self.assertFalse(winner =="Draw")

	def test_winner_of_state_arizona(self):
		winner = get_winner_of_state('Arizona')
		self.assertTrue(winner =="Bunty")

	def test_winner_of_state_ohio(self):
		winner = get_winner_of_state("Ohio")
		self.assertEqual(winner, "Draw")

	def test_winner_of_invalid_state(self):
		winner = get_winner_of_state("random")
		self.assertEqual(winner, "Invalid")

	def test_winner_of_integer_state(self):
		winner = get_winner_of_state(10)
		self.assertTrue(winner == "Invalid")

	def test_winner_of_empty_state(self):
		winner = get_winner_of_state("")
		self.assertTrue(winner == "Invalid")

	def test_winner_of_null_state(self):
		with self.assertRaises(NameError):
			get_winner_of_state(null)

	def test_winner_of_multiple_states(self):
		with self.assertRaises(TypeError):
			get_winner_of_state("Arizona", "Ohio")

if __name__ == "__main__":
   	unittest.main()
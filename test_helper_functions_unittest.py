from output import *
import unittest
from winner_declaration import select_query
from winner_declaration import get_max_voted

class TestHelperFunctions(unittest.TestCase):
	def test_select_valid_query_bunty(self):
		sql_fetch_query = "SELECT * FROM vote WHERE state='Illinois' and voted_for='Bunty'"
		record = select_query(sql_fetch_query)
		self.assertNotEqual(len(record),0)
		self.assertEqual(record[0],output_bunty)

	def test_select_valid_query_babli(self):
		sql_fetch_query = "SELECT * FROM vote WHERE state='Ohio' and voted_for='Babli'"
		record = select_query(sql_fetch_query)
		self.assertNotEqual(len(record),0)
		self.assertEqual(record[0],output_babli)

	def test_select_invalid_state(self):
		sql_fetch_query = "SELECT * FROM vote WHERE state='Massachusetts' and voted_for='Babli'"
		record = select_query(sql_fetch_query)
		self.assertEqual(len(record),0)
		self.assertEqual(record, [])

	def test_select_invalid_name(self):
		sql_fetch_query = "SELECT * FROM vote WHERE state='Ohio' and voted_for='BabliBunty'"
		record = select_query(sql_fetch_query)
		self.assertEqual(len(record),0)
		self.assertEqual(record, [])

	def test_select_empty_query(self):
		sql_fetch_query = ""
		record = select_query(sql_fetch_query)
		self.assertEqual(len(record),0)
		self.assertEqual(record, [])

	def test_select_null_query(self):
		with self.assertRaises(NameError):
			select_query(null)

	#tests for get_max_voted

	def test_get_max_voted_babli(self):
		max_value = get_max_voted(45,55)
		self.assertEqual(max_value,"Babli")

	def test_get_max_voted_bunty(self):
		max_value = get_max_voted(65,55)
		self.assertEqual(max_value,"Bunty")

	def test_get_max_voted_equal(self):
		max_value = get_max_voted(55,55)
		self.assertEqual(max_value,"Draw")

	def test_get_max_empty_values(self):
		with self.assertRaises(TypeError):
			get_max_voted(45,)

if __name__ == "__main__":
   	unittest.main()
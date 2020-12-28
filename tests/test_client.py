import unittest
from client import NamedEntity

class TestClient(unittest.TestCase):
	
	def test_get_ents_return_dict_given_empty_str(self):
		ner=NamedEntity()
		ents=ner.get_ents("")
		self.assertIsInstance(ents, dict)
	
	def test_get_ents_return_list_given_nonempty_str(self):
		ner=NamedEntity()
		ents=ner.get_ents("Cleanliness is half of faith")
		self.assertIsInstance(ents, dict)
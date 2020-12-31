import unittest
from client import NamedEntity
from test_doubles import NerModelTestDouble

class TestClient(unittest.TestCase):
	
	def test_get_ents_return_dict_given_empty_str_causes_empty_spacy_doc_ents(self):
		model = NerModelTestDouble('eng')
		model.return_doc_ents([])
		ner=NamedEntity(model)
		ents=ner.get_ents("")
		self.assertIsInstance(ents, dict)
	
	def test_get_ents_return_dict_given_nonempty_str(self):
		model = NerModelTestDouble('eng')
		model.return_doc_ents([])
		ner=NamedEntity(model)
		ents=ner.get_ents("Cleanliness is half of faith")
		self.assertIsInstance(ents, dict)
import unittest


class TestClient(unittest.TestCase):

	 def test_get_ents_return_dict_given_empty_str(self):
		 ner=NamedEntity()
		 ents=ner.get_ents("")
		 self.assertIsInstance(ents, dict)

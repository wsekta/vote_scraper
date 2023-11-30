from unittest import TestCase, mock
from src.datatypes.results import Results
from src.datatypes.party import Party

class TestResults(TestCase):
    def setUp(self):
        self.results = Results()

    def test_add_party(self):
        party = Party("Party A", 100)
        self.results.add_party(party)

        self.assertEqual(len(self.results.parties), 1)
        self.assertEqual(self.results.parties[0], party)

    def test_get_parties(self):
        party1 = Party("Party A", 100)
        party2 = Party("Party B", 200)
        self.results.add_party(party1)
        self.results.add_party(party2)

        parties = list(self.results.get_parties())

        self.assertEqual(len(parties), 2)
        self.assertIn(party1, parties)
        self.assertIn(party2, parties)

    def test_str(self):
        self.results.district_name = "District A"
        party1 = Party("Party A", 100)
        party2 = Party("Party B", 200)
        self.results.add_party(party1)
        self.results.add_party(party2)

        expected_output = "District A\nWyniki:\n\tParty A\t100\n\tParty B\t200"
        self.assertEqual(str(self.results), expected_output)
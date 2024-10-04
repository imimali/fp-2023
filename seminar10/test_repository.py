from unittest import TestCase
from seminar10.repository import Repository, RepositoryError
from seminar10.flight import Flight


class RepositoryTest(TestCase):

    def __init__(self,methodName):
        super().__init__(methodName=methodName)
        self.repo = Repository("../test_flights.txt")

    def setUp(self) -> None:
        self.repo.add(Flight("0123", 456, "Cluj-Napoca", "Dubai"))

    def tearDown(self) -> None:
        self.repo.clear()

    def testRepositoryAdd(self):
        self.repo.add(Flight("0124", 456, "Cluj-Napoca", "Dubai"))
        self.assertEqual(len(self.repo), 2)

    def testRepositoryFind(self):
        self.repo.add(Flight("0123", 456, "Cluj-Napoca", "Dubai"))

        self.assertIsNotNone(self.repo.find_by_code("0123"))

        self.assertEqual(self.repo.find_by_code("0123").get_destination() ,"Dubai")

        with self.assertRaises(RepositoryError):
            self.repo.find_by_code("012123")

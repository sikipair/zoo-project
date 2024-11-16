import unittest
from zoo import Zoo  

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_invalid_age(self):
        self.assertEqual(self.zoo.get_ticket_price(-10), "Invalid age") 

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)  

    def test_teen_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(13), 100)  

    def test_adult_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)  

    def test_senior_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)  

if __name__ == "__main__":
    unittest.main()
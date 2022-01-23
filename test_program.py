import unittest
from program import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_is_adult(self):
        # Stworzyć instancję klienta niepełnoletniego 17
        customer17 = Customer("John", "Smith", 17)
        self.assertEqual(False, customer17.is_adult())
        # Stworzyć instancję klienta pełnoletniego 18
        customer18 = Customer("Anna", "Black", 18)
        self.assertEqual(True, customer18.is_adult())
        # Stworzyć instancję klienta pełnoletniego 19
        customer19 = Customer("Barbara", "Streisland", 19)
        self.assertEqual(True, customer19)

if __name__ == "__main__":
    unittest.main()

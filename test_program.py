import unittest
from program import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_is_adult(self):
        # Stworzyć instancję klienta niepełnoletniego 17
        # Stworzyć instancję klienta pełnoletniego 18
        # Stworzyć instancję klienta pełnoletniego 19
        # sprawdzic is_adult() na kazdej instancji

if __name__ == "__main__":
    unittest.main()

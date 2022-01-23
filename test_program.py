import unittest

class TestHelloWorld(unittest.TestCase):
    # Metody testowe
    # Zaczynają się od słowa "test"
    def test001(self):
        print('Prawdziwy test: kroki, asercje')

    def test002(self):
        print("Prawdziwy test2")

    def tearDown(self):
        print("Sprzątanie po teście")

    def setUp(self):
        print("Przygotowuję test (warunki wstępne)")

# Jeśli uruchamiam z tego pliku
if __name__ == '__main__':
    # Uruchamiam metodę main(), która
    # zajmie się resztą
    unittest.main()




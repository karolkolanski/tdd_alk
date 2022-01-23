import unittest
import program

class TestHelloWorld(unittest.TestCase):
    def setUp(self):
        # Przygotowanie testu
        # Stworzenie obiektu klasy Hello()
        self.prog = program.Hello()

    # Metody testowe
    # Zaczynają się od słowa "test"
    def test_welcome(self):
        # Sprawdzamy, czy metoda welcome()
        # zwraca napis "hello, world"
        expected = "hello, world"
        actual = self.prog.welcome()
        # Porównuję expected z actual

        # "Czysty" Python
        # assert expected == actual
        # Bardziej unittestowa metoda
        self.assertEqual(expected, actual)

    def tearDown(self):
        del self.prog

# Jeśli uruchamiam z tego pliku
if __name__ == '__main__':
    # Uruchamiam metodę main(), która
    # zajmie się resztą
    unittest.main()




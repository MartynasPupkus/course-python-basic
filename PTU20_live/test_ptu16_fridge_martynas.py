from fridge import Fridge
import unittest


class TestFridge(unittest.TestCase):
    def setUp(self):
        self.fridge = Fridge ()
        self.fridge.add('something', 4.2)
    def test_add(self):
        self.fridge.add('something', )

    def test_remove(self):
        pass

    def test_check(self):
        pass


    if __name__ == '__main__':
        unittest.main()
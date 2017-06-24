import unittest
from sorting import DictionarySorting

class TestSorting(unittest.TestCase):

    instance = None

    def setUp(self):
        self.instance = DictionarySorting()

    def test_convertToList(self):
        x = {"aman": 23, "Tom": 35}
        self.assertEqual(id(self.instance.convertToList(x)), id(zip(x.keys(), x.values())), {"There is some problem with the convert method"})

    def test_convertToDictionary(self):
        x = self.instance.convertToList({"aman": 23, "Tom": 35})
        self.assertEqual(self.instance.convertToDictionary(x), {"aman": 23, "Tom": 35}, {"There is something wrong with the convertDictonary method"})

    def test_sorting(self):
        self.assertEqual(self.instance.sorting({"Tom": 35, "aman": 23}), {"aman": 23, "Tom": 35}, {"There is something wrong with the sorting method"})

    def test_max(self):
        self.assertEqual(self.instance.max({"aman": 23, "Tom": 35}, "value"), {"Tom": 35}, {"There was something wrong with the max method"})
        self.assertEqual(self.instance.max({"aman": 23, "Tom": 35}, "key"), {"aman": 23}, {"There was something wrong with the max method when using orderBy"})

    def test_min(self):
        self.assertEqual(self.instance.min({"aman": 23, "Tom": 35}, "value"), {"aman": 23},{"There was something wrong with the min method"})
        self.assertEqual(self.instance.min({"aman": 23, "Tom": 35}, "key"), {"Tom": 35},{"There was something wrong with the min method when using orderBy"})

if __name__ == '__main__':
    unittest.main()
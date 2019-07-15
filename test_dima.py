"""Dima's testing with unittest"""
import unittest
import taskdima

class MyTest(unittest.TestCase):
    """Class for unittest"""

    def test_4(self):
        """test for task4"""
        self.assertEqual(taskdima.task4('1,2,3'), (['1', '2', '3'], ('1', '2', '3')))

    def test_10(self):
        """test for task10"""
        self.assertEqual(taskdima.task10('hello world and hello earth and sun'),\
        'and earth hello sun world')

    def test_16(self):
        """test for task16"""
        self.assertEqual(taskdima.task16('1,2,3'), [1, 9])

    def test_22(self):
        """test for task22"""
        self.assertEqual(taskdima.task22('new to Python 2 or to 3'), {'2': 1, '3': 1,\
        'Python': 1, 'new': 1, 'or': 1, 'to': 2})

    def test_28(self):
        """test for task28"""
        self.assertEqual(taskdima.task28('maxim', 'nova'), 'maxim')

    def setUp(self):
        self.temp1 = taskdima.task34(1)
        self.temp2 = self.temp1[0]**0.5
        self.temp3 = int(self.temp2) - self.temp2

    def test_34(self):
        """test for task34"""
        self.assertEqual(self.temp3, 0)
        self.assertGreaterEqual(self.temp2, 1)
        self.assertLessEqual(self.temp2, 20)

    def test_40(self):
        """test for task40"""
        self.assertEqual(taskdima.task40((2, 7, 8, 10, 7, 11)), (2, 8, 10))

    def test_46(self):
        """test for task46"""
        self.temp1 = taskdima.task46()
        self.temp2 = next(self.temp1)
        for _ in range(4):
            next(self.temp1)
        self.temp3 = next(self.temp1)
        self.assertEqual(self.temp2, 1)
        self.assertEqual(self.temp3, 36)

    def test_52(self):
        """test for task52"""
        self.assertEqual(taskdima.task52(5), 500)

    def test_58(self):
        """test for task58"""
        self.temp1 = taskdima.task58()
        self.temp2 = self.temp1 % 5
        self.temp3 = self.temp1 % 7
        self.assertEqual(self.temp2 + self.temp3, 0)

if __name__ == '__main__':
    unittest.main()

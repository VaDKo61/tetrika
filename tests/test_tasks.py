import unittest

import task1.solution as task1


class TestTasks(unittest.TestCase):

    def test_task_1(self):
        self.assertEqual(task1.sum_two(1, 2), 3)
        self.assertRaises(TypeError, lambda: task1.sum_two(1, 2.4))

        self.assertEqual(task1.sum_two_1(1.1, 2.3), 3.4)
        self.assertRaises(TypeError, lambda: task1.sum_two_1(1, 2.4))

        self.assertEqual(task1.sum_two_2(True, False), 1)
        self.assertRaises(TypeError, lambda: task1.sum_two_2(True, 2.4))

        self.assertEqual(task1.sum_two_3('1', '2'), '12')
        self.assertRaises(TypeError, lambda: task1.sum_two_3('1', 2.4))

    def test_test_task_2(self):
        """Не тестирую, так как парсит много страниц, занимает определенное время, и результат не статичен.
         Результаты уже находятся в файле result.csv
         P.S. Можно запустить solution.py из task2, для парсинга"""
        pass


if __name__ == '__main__':
    unittest.main()

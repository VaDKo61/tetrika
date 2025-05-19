import unittest

import task1.solution as task1
import task3.solution as task3


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

    def test_test_task_3(self):
        tests = [
            {'intervals': {'lesson': [1594663200, 1594666800],
                           'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
                           'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
             'answer': 3117
             },
            {'intervals': {'lesson': [1594702800, 1594706400],
                           'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564,
                                     1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096,
                                     1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500,
                                     1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
                           'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
             'answer': 3577
             },
            {'intervals': {'lesson': [1594692000, 1594695600],
                           'pupil': [1594692033, 1594696347],
                           'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
             'answer': 3565
             },
        ]

        for i, test in enumerate(tests):
            test_answer = task3.appearance(test['intervals'])
            self.assertEqual(test_answer, test['answer'])


if __name__ == '__main__':
    unittest.main()

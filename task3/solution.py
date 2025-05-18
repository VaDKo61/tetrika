def edit_list_by_time(interval: list[int], start_lesson: int, end_lesson: int) -> list[int]:
    cut: int = 0
    for index in range(0, len(interval), 2):
        if interval[index] <= start_lesson:
            interval[index] = start_lesson
            cut = index
        else:
            interval = interval[cut:]
            break
    cut = -1
    for index in range(-1, -len(interval), -2):
        if interval[index] >= end_lesson:
            interval[index] = end_lesson
            cut = index
        else:
            interval = interval[:] if cut == -1 else interval[:cut + 1]
            break
    return interval


def edit_time_by_lesson(intervals: dict[str, list[int]]) -> None:
    time_lesson: list[int] = intervals.pop('lesson')
    start_lesson: int = time_lesson[0]
    end_lesson: int = time_lesson[1]
    for key in intervals:
        intervals[key] = edit_list_by_time(intervals[key], start_lesson, end_lesson)


def get_intersection(time_pupil: list[int], time_tutor: list[int]) -> int:
    intersection: list[int] = []
    cut_tutor: int = 0
    for index_pupil in range(0, len(time_pupil), 2):
        for index_tutor in range(cut_tutor, len(time_tutor), 2):
            if time_tutor[index_tutor] > time_pupil[index_pupil + 1]:
                break
            if time_tutor[index_tutor + 1] < time_pupil[index_pupil]:
                cut_tutor += 2
                continue
            intersection.append(
                min(time_tutor[index_tutor + 1], time_pupil[index_pupil + 1]) -
                max(time_tutor[index_tutor], time_pupil[index_pupil]))
    print(intersection)
    print(sum(intersection))
    return sum(intersection)


def appearance(intervals: dict[str, list[int]]) -> int:
    edit_time_by_lesson(intervals)
    return get_intersection(intervals['pupil'], intervals['tutor'])


tests = [
    # {'intervals': {'lesson': [1594663200, 1594666800],
    #                'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
    #                'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
    #  'answer': 3117
    #  },
    # {'intervals': {'lesson': [1594702800, 1594706400],
    #                'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564,
    #                          1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096,
    #                          1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500,
    #                          1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
    #                'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    #  'answer': 3577
    #  },
    {'intervals': {'lesson': [1594692000, 1594695600],
                   'pupil': [1594692033, 1594696347],
                   'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
     },
]

if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['intervals'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'

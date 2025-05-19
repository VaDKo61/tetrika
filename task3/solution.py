def edit_time_by_start_lesson(interval: list[int], start_lesson: int) -> list[int]:
    cut: int = 0
    for index in range(0, len(interval), 2):
        if interval[index] <= start_lesson:
            interval[index] = start_lesson
            cut = index
        else:
            interval = interval[cut:]
            break
    return interval


def edit_time_by_end_lesson(interval: list[int], end_lesson: int) -> list[int]:
    cut: int = -1
    for index in range(-1, -len(interval), -2):
        if interval[index] >= end_lesson:
            interval[index] = end_lesson
            cut = index
        else:
            interval = interval[:] if cut == -1 else interval[:cut + 1]
            break
    return interval


def edit_time_by_intersection_session(intervals: dict[str, list[int]]) -> None:
    for interval in intervals.values():
        for index in range(1, len(interval) - 1, 2):
            if interval[index] > interval[index + 1]:
                interval[index] = interval[index + 1] - 1


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
    return sum(intersection)


def appearance(intervals: dict[str, list[int]]) -> int | None:
    for interval in intervals.values():
        if len(interval) == 0:
            return None
    time_lesson: list[int] = intervals.pop('lesson')
    start_lesson: int = time_lesson[0]
    end_lesson: int = time_lesson[1]
    for key in intervals:
        intervals[key] = edit_time_by_start_lesson(intervals[key], start_lesson)
        intervals[key] = edit_time_by_end_lesson(intervals[key], end_lesson)
    edit_time_by_intersection_session(intervals)
    return get_intersection(intervals['pupil'], intervals['tutor'])

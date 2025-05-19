def edit_intervals_by_lesson(intervals: list[int], start_lesson: int, end_lesson: int) -> list[int]:
    edit_intervals: list[int] = []
    for index in range(0, len(intervals), 2):
        start_session: int = intervals[index]
        end_session: int = intervals[index + 1]
        if start_session >= start_lesson and end_session <= end_lesson:
            edit_intervals.extend(intervals[index:index + 2])
        elif start_session < start_lesson and end_session <= end_lesson:
            edit_intervals.append(start_lesson)
            edit_intervals.append(end_session)
        elif start_session >= start_lesson and end_session > end_lesson:
            edit_intervals.append(start_session)
            edit_intervals.append(end_lesson)
            break
    return edit_intervals


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
    for interval in intervals:
        intervals[interval] = edit_intervals_by_lesson(intervals[interval], start_lesson, end_lesson)
        intervals[interval] = edit_intervals_by_intersection_session(intervals[interval])
        if len(intervals[interval]) == 0:
            return None
    return get_intersection(intervals['pupil'], intervals['tutor'])

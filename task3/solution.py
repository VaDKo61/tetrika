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


def edit_intervals_by_intersection_session(intervals: list[int]) -> list[int]:
    edit_intervals: list[int] = intervals[0:2]
    for index in range(2, len(intervals), 2):
        start_session: int = intervals[index]
        end_session: int = intervals[index + 1]
        end_long_session: int = edit_intervals[-1]
        if start_session > end_long_session:
            edit_intervals.extend(intervals[index:index + 2])
        elif start_session < end_long_session > end_session:
            continue
        else:
            edit_intervals.append(end_long_session)
            edit_intervals.append(end_session)
    return edit_intervals


def get_intersection(intervals_pupil: list[int], intervals_tutor: list[int]) -> int:
    intersection: list[int] = []
    cut_tutor: int = 0
    for index_pupil in range(0, len(intervals_pupil), 2):
        start_session_pupil: int = intervals_pupil[index_pupil]
        end_session_pupil: int = intervals_pupil[index_pupil + 1]
        for index_tutor in range(cut_tutor, len(intervals_tutor), 2):
            start_session_tutor: int = intervals_tutor[index_tutor]
            end_session_tutor: int = intervals_tutor[index_tutor + 1]
            if start_session_tutor > end_session_pupil:
                break
            if end_session_tutor < start_session_pupil:
                cut_tutor += 2
                continue
            intersection.append(
                min(end_session_tutor, end_session_pupil) -
                max(start_session_tutor, start_session_pupil))
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

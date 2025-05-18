from functools import wraps


def strict(func):
    @wraps(func)
    def wrapper(*args):
        for i in zip(args, func.__annotations__.items()):
            if not isinstance(i[0], i[1][1]):
                raise TypeError(f'Несоответсвие переданных типов данных аннтотациям ({i[0]} not {i[1][1]})')
        return func(*args)

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


@strict
def sum_two_1(a: float, b: float) -> float:
    return a + b


@strict
def sum_two_2(a: bool, b: bool) -> bool:
    return a + b


@strict
def sum_two_3(a: str, b: str) -> str:
    return a + b

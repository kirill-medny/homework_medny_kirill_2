import os
from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор, который будет логировать вызов функции
    и ее результат в файл или в консоль."""

    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args: tuple, **kwargs: dict) -> Any:

            try:
                result = func(*args, **kwargs)
                log_str = f"{func.__name__} ok. Result: {result}"
                return result

            except Exception as e:
                log_str = f"{func.__name__} {type(e).__name__}: {e}. Inputs: {args}, {kwargs}"
                raise e

            finally:
                if filename:  # Запись лога в файл.
                    if not os.path.exists(r"logs"):
                        os.mkdir(r"logs")  # Создать папку «logs», если ее нет.
                    with open(os.path.join(r"logs", filename), "at") as file:
                        file.write(log_str + "\n")

                else:  # Вывод лога в консоль.
                    print(log_str)

        return inner

    return wrapper

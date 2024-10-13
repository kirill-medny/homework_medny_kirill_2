import os

import pytest

from src.decorators import log


def test_log_console(capsys: pytest.CaptureFixture) -> None:
    """Тест проверяет декоратор log, который будет логировать вызов функции
    и ее результат в консоль."""

    @log()
    def example_function(x: int, y: int) -> float:
        """Функция умножения"""
        return x * y

    result = example_function(5, 100)
    captured = capsys.readouterr()

    assert captured.out == "example_function ok. Result: 500\n"
    assert result == 500


def test_log_file_raise() -> None:
    """Тест проверяет декоратор log, логировать вызов функции в файл."""

    @log(filename="mylog.txt")
    def example_function(x: int, y: int) -> str:
        """Функция с ошибкой"""
        raise TypeError("Что-то пошло не так")

    with pytest.raises(TypeError, match="Что-то пошло не так"):
        example_function(5, 100)

    with open(os.path.join(r"logs", "mylog.txt"), "rt") as file:
        for line in file:
            log_string = line

    assert log_string == "example_function TypeError: Что-то пошло не так. Inputs: (5, 100), {}\n"


def test_log_console_raise(capsys: pytest.CaptureFixture) -> None:
    """Тест проверяет декоратор log, который будет логировать вызов функции
    и ее результат в консоль."""

    @log()
    def example_function(x: int, y: int) -> str:
        """Функция с ошибкой"""
        raise ValueError("Что-то пошло не так")

    with pytest.raises(ValueError, match="Что-то пошло не так"):
        example_function(5, 100)
    captured = capsys.readouterr()
    assert captured.out == "example_function ValueError: Что-то пошло не так. Inputs: (5, 100), {}\n"


def test_log_console_raise_1(capsys: pytest.CaptureFixture) -> None:
    """Тест проверяет декоратор log, который будет логировать вызов функции
    и ее результат в консоль."""

    @log()
    def example_function(x: int, y: int) -> str:
        """Функция с ошибкой"""
        raise ValueError("Что-то пошло не так")

    with pytest.raises(ValueError, match="Что-то пошло не так"):
        example_function(5, 100)

    captured = capsys.readouterr()

    assert captured.out == "example_function ValueError: Что-то пошло не так. Inputs: (5, 100), {}\n"

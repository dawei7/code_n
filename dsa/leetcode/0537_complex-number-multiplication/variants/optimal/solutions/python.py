"""Direct component arithmetic for LeetCode 537."""


def _components(value: str) -> tuple[int, int]:
    real, imaginary = value[:-1].split("+")
    return int(real), int(imaginary)


def solve(num1: str, num2: str) -> str:
    first_real, first_imaginary = _components(num1)
    second_real, second_imaginary = _components(num2)
    real = first_real * second_real - first_imaginary * second_imaginary
    imaginary = first_real * second_imaginary + first_imaginary * second_real
    return f"{real}+{imaginary}i"

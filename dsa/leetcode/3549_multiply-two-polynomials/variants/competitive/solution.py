from cmath import exp, pi


def _fft(values: list[complex], sign: int) -> None:
    length = len(values)
    if length < 2:
        return
    even = values[::2]
    odd = values[1::2]
    _fft(even, sign)
    _fft(odd, sign)
    factor = 1
    root = exp(sign * 2j * pi / length)
    half = length // 2
    for i in range(half):
        contribution = factor * odd[i]
        values[i] = even[i] + contribution
        values[i + half] = even[i] - contribution
        factor *= root


class Solution:
    def multiply(self, poly1: list[int], poly2: list[int]) -> list[int]:
        result_length = len(poly1) + len(poly2) - 1
        transform_length = 1
        while transform_length < result_length:
            transform_length *= 2
        first = [complex(value) for value in poly1] + [0j] * (transform_length - len(poly1))
        second = [complex(value) for value in poly2] + [0j] * (transform_length - len(poly2))
        _fft(first, -1)
        _fft(second, -1)
        for i in range(transform_length):
            first[i] *= second[i]
        _fft(first, 1)
        return [round(first[i].real / transform_length) for i in range(result_length)]

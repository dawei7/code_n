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
    for index in range(half):
        contribution = factor * odd[index]
        values[index] = even[index] + contribution
        values[index + half] = even[index] - contribution
        factor *= root


def solve(poly1: list[int], poly2: list[int]) -> list[int]:
    result_length = len(poly1) + len(poly2) - 1
    transform_length = 1
    while transform_length < result_length:
        transform_length *= 2

    packed = [
        complex(
            poly1[index] if index < len(poly1) else 0,
            poly2[index] if index < len(poly2) else 0,
        )
        for index in range(transform_length)
    ]
    _fft(packed, -1)

    spectrum = packed[:]
    for index in range(transform_length):
        mirrored = spectrum[-index % transform_length].conjugate()
        first = (spectrum[index] + mirrored) * 0.5
        second = (spectrum[index] - mirrored) * -0.5j
        packed[index] = first * second

    _fft(packed, 1)
    return [
        round(packed[index].real / transform_length)
        for index in range(result_length)
    ]

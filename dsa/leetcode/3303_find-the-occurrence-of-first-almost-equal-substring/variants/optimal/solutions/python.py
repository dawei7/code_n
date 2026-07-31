def solve(s: str, pattern: str) -> int:
    def z_values(text: str) -> list[int]:
        values = [0] * len(text)
        left = 0
        right = 0

        for index in range(1, len(text)):
            if index <= right:
                values[index] = min(right - index + 1, values[index - left])
            while (
                index + values[index] < len(text)
                and text[values[index]] == text[index + values[index]]
            ):
                values[index] += 1
            if index + values[index] - 1 > right:
                left = index
                right = index + values[index] - 1

        return values

    source_length = len(s)
    pattern_length = len(pattern)
    forward = z_values(pattern + "#" + s)
    backward = z_values(pattern[::-1] + "#" + s[::-1])
    offset = pattern_length + 1

    for start in range(source_length - pattern_length + 1):
        prefix = min(pattern_length, forward[offset + start])
        reversed_start = source_length - start - pattern_length
        suffix = min(pattern_length, backward[offset + reversed_start])
        if prefix + suffix >= pattern_length - 1:
            return start

    return -1

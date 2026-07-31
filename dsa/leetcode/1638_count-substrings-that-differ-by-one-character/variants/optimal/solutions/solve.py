def solve(s: str, t: str) -> int:
    width = len(t)
    previous_equal = [0] * (width + 1)
    previous_one_difference = [0] * (width + 1)
    total = 0

    for char_s in s:
        current_equal = [0] * (width + 1)
        current_one_difference = [0] * (width + 1)
        for j, char_t in enumerate(t, 1):
            if char_s == char_t:
                current_equal[j] = previous_equal[j - 1] + 1
                current_one_difference[j] = previous_one_difference[j - 1]
            else:
                current_one_difference[j] = previous_equal[j - 1] + 1
            total += current_one_difference[j]
        previous_equal = current_equal
        previous_one_difference = current_one_difference

    return total

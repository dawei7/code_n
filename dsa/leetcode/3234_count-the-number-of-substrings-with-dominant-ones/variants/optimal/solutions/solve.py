from math import isqrt


def solve(s: str) -> int:
    n = len(s)
    zeros = [-1]
    zeros.extend(index for index, bit in enumerate(s) if bit == "0")
    zeros.append(n)

    answer = 0
    for index in range(len(zeros) - 1):
        ones = zeros[index + 1] - zeros[index] - 1
        answer += ones * (ones + 1) // 2

    zero_count = len(zeros) - 2
    for count in range(1, isqrt(n) + 1):
        if count * count + count > n:
            break
        for first_index in range(1, zero_count - count + 2):
            last_index = first_index + count - 1
            first_zero = zeros[first_index]
            last_zero = zeros[last_index]
            left_choices = first_zero - zeros[first_index - 1]
            right_choices = zeros[last_index + 1] - last_zero
            core_length = last_zero - first_zero + 1
            required_extension = count * count + count - core_length

            if required_extension <= 0:
                answer += left_choices * right_choices
                continue

            full_rows = min(
                left_choices,
                max(0, required_extension - right_choices + 1),
            )
            partial_end = min(left_choices, required_extension)
            partial_rows = partial_end - full_rows
            invalid = full_rows * right_choices
            invalid += partial_rows * required_extension
            invalid -= (full_rows + partial_end - 1) * partial_rows // 2
            answer += left_choices * right_choices - invalid

    return answer

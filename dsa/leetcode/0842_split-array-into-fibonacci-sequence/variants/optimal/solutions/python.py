"""Optimal app-local solution for LeetCode 842."""


def solve(num):
    limit = 2**31 - 1
    length = len(num)

    for first_end in range(1, min(10, length - 2) + 1):
        if num[0] == "0" and first_end > 1:
            break
        first = int(num[:first_end])
        if first > limit:
            break

        max_second_end = min(first_end + 10, length - 1)
        for second_end in range(first_end + 1, max_second_end + 1):
            if num[first_end] == "0" and second_end > first_end + 1:
                break
            second = int(num[first_end:second_end])
            if second > limit:
                break

            sequence = [first, second]
            position = second_end
            while position < length:
                next_value = sequence[-2] + sequence[-1]
                if next_value > limit:
                    break
                token = str(next_value)
                if not num.startswith(token, position):
                    break
                sequence.append(next_value)
                position += len(token)

            if position == length and len(sequence) >= 3:
                return sequence

    return []

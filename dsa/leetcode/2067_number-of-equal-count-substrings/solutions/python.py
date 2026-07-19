def solve(s: str, count: int) -> int:
    answer = 0
    length = len(s)

    for distinct in range(1, 27):
        window_size = distinct * count
        if window_size > length:
            break

        frequencies = [0] * 26
        exact_count = 0

        for right, character in enumerate(s):
            index = ord(character) - ord("a")
            if frequencies[index] == count:
                exact_count -= 1
            frequencies[index] += 1
            if frequencies[index] == count:
                exact_count += 1

            if right >= window_size:
                left_index = ord(s[right - window_size]) - ord("a")
                if frequencies[left_index] == count:
                    exact_count -= 1
                frequencies[left_index] -= 1
                if frequencies[left_index] == count:
                    exact_count += 1

            if right + 1 >= window_size and exact_count == distinct:
                answer += 1

    return answer

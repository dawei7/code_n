def solve(s: str) -> bool:
    n = len(s)

    for first_end in range(1, n):
        previous = int(s[:first_end])
        position = first_end

        while position < n and previous > 0:
            target = previous - 1
            if target == 0:
                if all(char == "0" for char in s[position:]):
                    return True
                break

            cursor = position
            value = 0
            while cursor < n and value < target:
                value = value * 10 + int(s[cursor])
                cursor += 1

            if value != target:
                break

            position = cursor
            previous = target
            if position == n:
                return True

    return False

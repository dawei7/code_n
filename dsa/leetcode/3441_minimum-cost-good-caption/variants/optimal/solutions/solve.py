from array import array


def solve(caption: str) -> str:
    n = len(caption)
    if n < 3:
        return ""

    values = [ord(char) - ord("a") for char in caption]
    inf = 2_000_000
    dp = [array("I", [0]) * (n + 1) for _ in range(26)]

    for i in range(n - 1, -1, -1):
        best_value = inf
        second_value = inf
        best_char = -1
        if i + 3 <= n:
            for char in range(26):
                value = abs(values[i] - char) + abs(values[i + 1] - char) + abs(values[i + 2] - char) + dp[char][i + 3]
                if value < best_value:
                    second_value = best_value
                    best_value = value
                    best_char = char
                elif value < second_value:
                    second_value = value

        for last in range(26):
            extend = abs(values[i] - last) + dp[last][i + 1]
            switch = second_value if best_char == last else best_value
            dp[last][i] = min(extend, switch)

    best_cost = inf
    first_char = 0
    for char in range(26):
        cost = abs(values[0] - char) + abs(values[1] - char) + abs(values[2] - char) + dp[char][3]
        if cost < best_cost:
            best_cost = cost
            first_char = char

    answer = [chr(first_char + ord("a"))] * 3
    i = 3
    last = first_char
    while i < n:
        target = dp[last][i]
        chosen = 26
        if abs(values[i] - last) + dp[last][i + 1] == target:
            chosen = last

        if i + 3 <= n:
            for char in range(26):
                if char == last:
                    continue
                cost = abs(values[i] - char) + abs(values[i + 1] - char) + abs(values[i + 2] - char) + dp[char][i + 3]
                if cost == target:
                    chosen = min(chosen, char)

        if chosen == last:
            answer.append(chr(last + ord("a")))
            i += 1
        else:
            last = chosen
            answer.extend([chr(last + ord("a"))] * 3)
            i += 3

    return "".join(answer)

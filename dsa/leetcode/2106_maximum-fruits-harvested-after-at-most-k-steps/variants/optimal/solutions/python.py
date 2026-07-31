def solve(fruits: list[list[int]], startPos: int, k: int) -> int:
    left = 0
    window_total = 0
    answer = 0

    for right, (right_position, amount) in enumerate(fruits):
        window_total += amount

        while left <= right:
            left_distance = max(0, startPos - fruits[left][0])
            right_distance = max(0, right_position - startPos)
            steps = min(
                2 * left_distance + right_distance,
                left_distance + 2 * right_distance,
            )
            if steps <= k:
                break
            window_total -= fruits[left][1]
            left += 1

        answer = max(answer, window_total)

    return answer

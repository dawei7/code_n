def solve(points: list[int], m: int) -> int:
    n = len(points)

    def feasible(target: int) -> bool:
        if target == 0:
            return True

        required = [(target + value - 1) // value for value in points]
        moves = 1
        incoming = 1

        for index in range(n - 1):
            if index == n - 2:
                need_current = max(0, required[index] - incoming)
                continue_moves = moves + 2 * need_current + 1
                last_incoming = need_current + 1
                continue_moves += 2 * max(0, required[index + 1] - last_incoming)

                stop_bounces = max(need_current, required[index + 1])
                stop_moves = moves + 2 * stop_bounces
                return min(continue_moves, stop_moves) <= m

            bounces = max(0, required[index] - incoming)
            moves += 2 * bounces + 1
            if moves > m:
                return False
            incoming = bounces + 1

        return moves + 2 * max(0, required[0] - incoming) <= m

    low, high = 0, min(points) * m
    answer = 0
    while low <= high:
        mid = (low + high) // 2
        if feasible(mid):
            answer = mid
            low = mid + 1
        else:
            high = mid - 1
    return answer

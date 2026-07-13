def solve(nums: list[int]) -> int:
    values = {(number // 100, (number // 10) % 10): number % 10 for number in nums}
    total = 0
    stack = [(1, 1, 0)]
    while stack:
        depth, position, path_sum = stack.pop()
        path_sum += values[(depth, position)]
        left = (depth + 1, position * 2 - 1)
        right = (depth + 1, position * 2)
        if left not in values and right not in values:
            total += path_sum
        else:
            if left in values:
                stack.append((*left, path_sum))
            if right in values:
                stack.append((*right, path_sum))
    return total

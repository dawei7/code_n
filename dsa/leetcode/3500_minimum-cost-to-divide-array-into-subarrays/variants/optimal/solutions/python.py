def solve(nums: list[int], cost: list[int], k: int) -> int:
    n = len(nums)
    prefix_nums = [0] * (n + 1)
    prefix_cost = [0] * (n + 1)
    for index, (num, cst) in enumerate(zip(nums, cost), start=1):
        prefix_nums[index] = prefix_nums[index - 1] + num
        prefix_cost[index] = prefix_cost[index - 1] + cst

    inf = 10**30
    previous = [inf] * (n + 1)
    previous[0] = 0
    answer = inf

    def value(line: tuple[int, int], x: int) -> int:
        return line[0] * x + line[1]

    def intersection(first: tuple[int, int], second: tuple[int, int]) -> float:
        return (first[1] - second[1]) / (second[0] - first[0])

    for part in range(1, n + 1):
        current = [inf] * (n + 1)
        lines: list[tuple[int, int]] = []
        starts: list[float] = []
        pointer = 0

        for end in range(part, n + 1):
            start = end - 1
            if previous[start] < inf:
                line = (-prefix_cost[start], previous[start])
                begin = float("-inf")
                while lines:
                    begin = intersection(lines[-1], line)
                    if begin <= starts[-1]:
                        lines.pop()
                        starts.pop()
                        if pointer > len(lines) - 1:
                            pointer = max(0, len(lines) - 1)
                    else:
                        break
                if not lines:
                    begin = float("-inf")
                lines.append(line)
                starts.append(begin)

            x = prefix_nums[end] + k * part
            while pointer + 1 < len(lines) and starts[pointer + 1] <= x:
                pointer += 1
            current[end] = x * prefix_cost[end] + value(lines[pointer], x)

        if current[n] < answer:
            answer = current[n]
        previous = current

    return answer

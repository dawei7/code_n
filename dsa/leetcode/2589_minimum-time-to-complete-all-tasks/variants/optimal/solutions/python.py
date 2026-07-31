def solve(tasks: list[list[int]]) -> int:
    tasks.sort(key=lambda task: task[1])
    limit = max(end for _, end, _ in tasks)
    bit = [0] * (limit + 2)
    parent = list(range(limit + 1))

    def prefix(time: int) -> int:
        total = 0
        while time > 0:
            total += bit[time]
            time -= time & -time
        return total

    def activate(time: int) -> None:
        while time <= limit:
            bit[time] += 1
            time += time & -time

    def find(time: int) -> int:
        root = time
        while parent[root] != root:
            root = parent[root]
        while parent[time] != time:
            next_time = parent[time]
            parent[time] = root
            time = next_time
        return root

    active = 0
    for start, end, duration in tasks:
        needed = duration - (prefix(end) - prefix(start - 1))
        time = find(end)
        while needed > 0:
            activate(time)
            active += 1
            needed -= 1
            parent[time] = find(time - 1)
            time = find(time)

    return active

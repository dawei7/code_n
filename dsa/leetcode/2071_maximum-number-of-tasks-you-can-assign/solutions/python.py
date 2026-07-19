from collections import deque


def solve(
    tasks: list[int],
    workers: list[int],
    pills: int,
    strength: int,
) -> int:
    tasks.sort()
    workers.sort()

    def feasible(task_count: int) -> bool:
        available = deque()
        task_index = 0
        pills_left = pills

        for worker in workers[len(workers) - task_count :]:
            while (
                task_index < task_count
                and tasks[task_index] <= worker + strength
            ):
                available.append(tasks[task_index])
                task_index += 1

            if not available:
                return False
            if available[0] <= worker:
                available.popleft()
            else:
                if pills_left == 0:
                    return False
                pills_left -= 1
                available.pop()

        return True

    low = 0
    high = min(len(tasks), len(workers))
    while low < high:
        middle = (low + high + 1) // 2
        if feasible(middle):
            low = middle
        else:
            high = middle - 1
    return low

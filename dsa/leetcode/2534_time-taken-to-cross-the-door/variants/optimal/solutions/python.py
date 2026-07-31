from collections import deque


def solve(arrival: list[int], state: list[int]) -> list[int]:
    n = len(arrival)
    queues = [deque(), deque()]
    answer = [0] * n
    next_person = 0
    current = 0
    previous_direction = 1

    while next_person < n or queues[0] or queues[1]:
        if not queues[0] and not queues[1] and current < arrival[next_person]:
            current = arrival[next_person]
            previous_direction = 1

        while next_person < n and arrival[next_person] <= current:
            queues[state[next_person]].append(next_person)
            next_person += 1

        direction = previous_direction
        if not queues[direction]:
            direction ^= 1

        person = queues[direction].popleft()
        answer[person] = current
        previous_direction = direction
        current += 1

    return answer

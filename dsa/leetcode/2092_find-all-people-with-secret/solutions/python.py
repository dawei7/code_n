from collections import defaultdict, deque


def solve(n: int, meetings: list[list[int]], firstPerson: int) -> list[int]:
    meetings.sort(key=lambda meeting: meeting[2])
    informed = {0, firstPerson}
    index = 0

    while index < len(meetings):
        end = index
        time = meetings[index][2]
        graph: dict[int, list[int]] = defaultdict(list)
        participants: set[int] = set()

        while end < len(meetings) and meetings[end][2] == time:
            person1, person2, _ = meetings[end]
            graph[person1].append(person2)
            graph[person2].append(person1)
            participants.add(person1)
            participants.add(person2)
            end += 1

        reached = participants & informed
        queue = deque(reached)
        while queue:
            person = queue.popleft()
            for neighbor in graph[person]:
                if neighbor not in reached:
                    reached.add(neighbor)
                    queue.append(neighbor)

        informed.update(reached)
        index = end

    return list(informed)

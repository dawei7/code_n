import heapq


def solve(words: list[str]) -> str:
    graph = {character: set() for word in words for character in word}
    indegree = {character: 0 for character in graph}
    for first, second in zip(words, words[1:]):
        if len(first) > len(second) and first.startswith(second):
            return ""
        for left, right in zip(first, second):
            if left == right:
                continue
            if right not in graph[left]:
                graph[left].add(right)
                indegree[right] += 1
            break
    available = [character for character, degree in indegree.items() if degree == 0]
    heapq.heapify(available)
    order: list[str] = []
    while available:
        character = heapq.heappop(available)
        order.append(character)
        for neighbor in sorted(graph[character]):
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                heapq.heappush(available, neighbor)
    return "".join(order) if len(order) == len(graph) else ""

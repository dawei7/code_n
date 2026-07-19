from collections import defaultdict


def solve(pairs: list[list[int]]) -> list[list[int]]:
    adjacency: dict[int, list[int]] = defaultdict(list)
    balance: dict[int, int] = defaultdict(int)

    for start, end in pairs:
        adjacency[start].append(end)
        balance[start] += 1
        balance[end] -= 1

    trail_start = pairs[0][0]
    for vertex, difference in balance.items():
        if difference == 1:
            trail_start = vertex
            break

    stack = [trail_start]
    reversed_vertices = []
    while stack:
        vertex = stack[-1]
        if adjacency[vertex]:
            stack.append(adjacency[vertex].pop())
        else:
            reversed_vertices.append(stack.pop())

    vertices = reversed_vertices[::-1]
    return [[vertices[index], vertices[index + 1]] for index in range(len(pairs))]

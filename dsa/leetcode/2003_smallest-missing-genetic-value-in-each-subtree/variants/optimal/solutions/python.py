def solve(parents: list[int], nums: list[int]) -> list[int]:
    length = len(parents)
    answer = [1] * length

    try:
        current = nums.index(1)
    except ValueError:
        return answer

    children = [[] for _ in range(length)]
    for node in range(1, length):
        children[parents[node]].append(node)

    visited = [False] * length
    present = set()
    missing = 1

    while current != -1:
        stack = [current]
        while stack:
            node = stack.pop()
            if visited[node]:
                continue
            visited[node] = True
            present.add(nums[node])
            stack.extend(children[node])

        while missing in present:
            missing += 1
        answer[current] = missing
        current = parents[current]

    return answer

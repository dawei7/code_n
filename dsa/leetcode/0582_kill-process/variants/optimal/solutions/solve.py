from collections import defaultdict


def solve(pid: list[int], ppid: list[int], kill: int) -> list[int]:
    children = defaultdict(list)
    for process, parent in zip(pid, ppid):
        children[parent].append(process)

    killed = []
    stack = [kill]
    while stack:
        process = stack.pop()
        killed.append(process)
        stack.extend(children[process])

    return killed

from collections import defaultdict


def solve(pid: list[int], ppid: list[int], kill: int) -> list[int]:
    """Return the killed process and all descendants."""
    children: dict[int, list[int]] = defaultdict(list)
    for process, parent in zip(pid, ppid):
        children[parent].append(process)

    killed: list[int] = []
    stack = [kill]
    while stack:
        process = stack.pop()
        killed.append(process)
        stack.extend(children[process])

    return killed


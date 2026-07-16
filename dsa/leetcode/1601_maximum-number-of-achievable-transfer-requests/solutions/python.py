def solve(n: int, requests: list[list[int]]) -> int:
    balance = [0] * n
    best = 0

    def search(index: int, chosen: int) -> None:
        nonlocal best
        if chosen + len(requests) - index <= best:
            return
        if index == len(requests):
            if all(change == 0 for change in balance):
                best = chosen
            return

        source, destination = requests[index]
        balance[source] -= 1
        balance[destination] += 1
        search(index + 1, chosen + 1)
        balance[source] += 1
        balance[destination] -= 1
        search(index + 1, chosen)

    search(0, 0)
    return best

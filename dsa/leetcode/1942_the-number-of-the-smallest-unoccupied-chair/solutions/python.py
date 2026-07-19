from heapq import heappop, heappush


def solve(times: list[list[int]], targetFriend: int) -> int:
    arrivals = sorted(
        (arrival, leaving, friend)
        for friend, (arrival, leaving) in enumerate(times)
    )
    available: list[int] = []
    occupied: list[tuple[int, int]] = []
    next_chair = 0

    for arrival, leaving, friend in arrivals:
        while occupied and occupied[0][0] <= arrival:
            _, chair = heappop(occupied)
            heappush(available, chair)

        if available:
            chair = heappop(available)
        else:
            chair = next_chair
            next_chair += 1

        if friend == targetFriend:
            return chair

        heappush(occupied, (leaving, chair))

    raise RuntimeError("target friend must arrive")

from collections import defaultdict


def _find_itinerary(tickets: list[list[str]]) -> list[str]:
    destinations: dict[str, list[str]] = defaultdict(list)
    for departure, arrival in tickets:
        destinations[departure].append(arrival)
    for arrivals in destinations.values():
        arrivals.sort(reverse=True)

    stack = ["JFK"]
    reversed_route: list[str] = []
    while stack:
        current = stack[-1]
        if destinations[current]:
            stack.append(destinations[current].pop())
        else:
            reversed_route.append(stack.pop())
    return reversed_route[::-1]


def solve(tickets: list[list[str]]) -> list[str]:
    return _find_itinerary(tickets)

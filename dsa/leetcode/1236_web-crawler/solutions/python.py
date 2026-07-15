def _hostname(url: str) -> str:
    return url.split("/", 3)[2]


def solve(urls: list[str], edges: list[list[int]], start_url: str) -> list[str]:
    outgoing: dict[str, list[str]] = {url: [] for url in urls}
    for source, destination in edges:
        outgoing[urls[source]].append(urls[destination])

    allowed_hostname = _hostname(start_url)
    visited = {start_url}
    stack = [start_url]
    while stack:
        current = stack.pop()
        for neighbor in outgoing[current]:
            if _hostname(neighbor) == allowed_hostname and neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
    return list(visited)

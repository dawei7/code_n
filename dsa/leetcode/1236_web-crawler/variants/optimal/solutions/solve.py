class HtmlParser:
    """Local equivalent of LeetCode's URL-adjacency interface."""

    def __init__(self, urls: list[str], edges: list[list[int]]):
        self.outgoing = {url: [] for url in urls}
        for source, destination in edges:
            self.outgoing[urls[source]].append(urls[destination])

    def getUrls(self, url: str) -> list[str]:
        return list(self.outgoing.get(url, ()))


def solve(startUrl: str, htmlParser: HtmlParser) -> list[str]:
    hostname = startUrl.split("/", 3)[2]
    visited = {startUrl}
    stack = [startUrl]

    while stack:
        current = stack.pop()
        for neighbor in htmlParser.getUrls(current):
            if neighbor.split("/", 3)[2] == hostname and neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

    return list(visited)

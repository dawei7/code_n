"""Source-native concurrency reference for LeetCode 1242."""

from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
from typing import List


class HtmlParser:
    """Local equivalent of LeetCode's URL-adjacency interface."""

    def __init__(self, urls: list[str], edges: list[list[int]]):
        self.outgoing = {url: [] for url in urls}
        for source, destination in edges:
            self.outgoing[urls[source]].append(urls[destination])

    def getUrls(self, url: str) -> list[str]:
        return list(self.outgoing.get(url, ()))


class Solution:
    def crawl(self, startUrl: str, htmlParser: "HtmlParser") -> List[str]:
        hostname = startUrl.split("/", 3)[2]
        visited = {startUrl}

        with ThreadPoolExecutor(max_workers=8) as executor:
            pending = {executor.submit(htmlParser.getUrls, startUrl)}
            while pending:
                completed, pending = wait(pending, return_when=FIRST_COMPLETED)
                for future in completed:
                    for neighbor in future.result():
                        if neighbor.split("/", 3)[2] == hostname and neighbor not in visited:
                            visited.add(neighbor)
                            pending.add(executor.submit(htmlParser.getUrls, neighbor))

        return list(visited)

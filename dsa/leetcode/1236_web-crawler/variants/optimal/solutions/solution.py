from typing import List


class Solution:
    def crawl(self, startUrl: str, htmlParser: "HtmlParser") -> List[str]:
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

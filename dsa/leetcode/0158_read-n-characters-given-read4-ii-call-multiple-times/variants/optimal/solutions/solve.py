from typing import List


class Solution:
    def __init__(self):
        self.temporary = [""] * 4
        self.available = 0
        self.position = 0

    def read(self, buf: List[str], n: int) -> int:
        copied = 0
        while copied < n:
            if self.position == self.available:
                self.available = read4(self.temporary)  # noqa: F821
                self.position = 0
                if self.available == 0:
                    break
            while self.position < self.available and copied < n:
                buf[copied] = self.temporary[self.position]
                copied += 1
                self.position += 1
        return copied


def solve(content: str, requests: list[int]) -> list[str]:
    source_position = 0

    def read_four(buffer: list[str]) -> int:
        nonlocal source_position
        chunk = content[source_position : source_position + 4]
        source_position += len(chunk)
        buffer[: len(chunk)] = chunk
        return len(chunk)

    Solution.read.__globals__["read4"] = read_four
    reader = Solution()
    output: list[str] = []
    for request in requests:
        buffer = [""] * request
        copied = reader.read(buffer, request)
        output.append("".join(buffer[:copied]))
    return output

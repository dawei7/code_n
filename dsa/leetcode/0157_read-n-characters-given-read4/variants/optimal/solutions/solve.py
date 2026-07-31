from typing import List


class Solution:
    def read(self, buf: List[str], n: int) -> int:
        temporary = [""] * 4
        copied = 0
        while copied < n:
            available = read4(temporary)  # noqa: F821
            if available == 0:
                break
            take = min(available, n - copied)
            for index in range(take):
                buf[copied + index] = temporary[index]
            copied += take
            if available < 4:
                break
        return copied


def solve(content: str, n: int) -> str:
    source_position = 0

    def read_four(buffer: list[str]) -> int:
        nonlocal source_position
        chunk = content[source_position : source_position + 4]
        source_position += len(chunk)
        buffer[: len(chunk)] = chunk
        return len(chunk)

    Solution.read.__globals__["read4"] = read_four
    output = [""] * n
    copied = Solution().read(output, n)
    return "".join(output[:copied])

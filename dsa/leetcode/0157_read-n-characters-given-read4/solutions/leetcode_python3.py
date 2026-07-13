from typing import List


class Solution:
    def read(self, buf: List[str], n: int) -> int:
        temporary = [""] * 4
        copied = 0
        while copied < n:
            available = read4(temporary)
            if available == 0:
                break
            take = min(available, n - copied)
            for index in range(take):
                buf[copied + index] = temporary[index]
            copied += take
            if available < 4:
                break
        return copied

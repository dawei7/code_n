class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        used: set[str] = set()
        best = 0

        def search(start: int) -> None:
            nonlocal best

            if len(used) + len(s) - start <= best:
                return
            if start == len(s):
                best = len(used)
                return

            for end in range(start + 1, len(s) + 1):
                part = s[start:end]
                if part in used:
                    continue
                used.add(part)
                search(end)
                used.remove(part)

        search(0)
        return best

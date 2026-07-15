class TimeMap:
    def __init__(self):
        self.history = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.history.setdefault(key, []).append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        entries = self.history.get(key, [])
        left = 0
        right = len(entries)
        while left < right:
            middle = (left + right) // 2
            if entries[middle][0] <= timestamp:
                left = middle + 1
            else:
                right = middle
        return entries[left - 1][1] if left else ""

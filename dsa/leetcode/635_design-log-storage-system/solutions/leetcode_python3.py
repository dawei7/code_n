from typing import List


class LogSystem:
    def __init__(self):
        self.logs = []
        self.prefix_length = {
            "Year": 4,
            "Month": 7,
            "Day": 10,
            "Hour": 13,
            "Minute": 16,
            "Second": 19,
        }

    def put(self, id: int, timestamp: str) -> None:
        self.logs.append((id, timestamp))

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        length = self.prefix_length[granularity]
        lower = start[:length]
        upper = end[:length]
        return [
            identifier
            for identifier, timestamp in self.logs
            if lower <= timestamp[:length] <= upper
        ]

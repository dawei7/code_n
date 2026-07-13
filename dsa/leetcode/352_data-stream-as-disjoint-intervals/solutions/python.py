class SummaryRanges:
    def __init__(self) -> None:
        self.present: set[int] = set()
        self.start_to_end: dict[int, int] = {}
        self.end_to_start: dict[int, int] = {}

    def addNum(self, value: int) -> None:
        if value in self.present:
            return
        self.present.add(value)

        has_left = value - 1 in self.present
        has_right = value + 1 in self.present

        if has_left and has_right:
            start = self.end_to_start.pop(value - 1)
            end = self.start_to_end.pop(value + 1)
            self.start_to_end[start] = end
            self.end_to_start[end] = start
        elif has_left:
            start = self.end_to_start.pop(value - 1)
            self.start_to_end[start] = value
            self.end_to_start[value] = start
        elif has_right:
            end = self.start_to_end.pop(value + 1)
            self.start_to_end[value] = end
            self.end_to_start[end] = value
        else:
            self.start_to_end[value] = value
            self.end_to_start[value] = value

    def getIntervals(self) -> list[list[int]]:
        return [[start, self.start_to_end[start]] for start in sorted(self.start_to_end)]


def solve(values: list[int]) -> list[list[list[int]]]:
    summary = SummaryRanges()
    snapshots: list[list[list[int]]] = []
    for value in values:
        summary.addNum(value)
        snapshots.append(summary.getIntervals())
    return snapshots

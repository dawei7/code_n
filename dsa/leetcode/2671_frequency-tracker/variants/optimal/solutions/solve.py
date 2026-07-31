from collections import defaultdict


class FrequencyTracker:
    def __init__(self):
        self.number_frequency = defaultdict(int)
        self.frequency_count = defaultdict(int)

    def add(self, number: int) -> None:
        old_frequency = self.number_frequency[number]
        if old_frequency > 0:
            self.frequency_count[old_frequency] -= 1
        new_frequency = old_frequency + 1
        self.number_frequency[number] = new_frequency
        self.frequency_count[new_frequency] += 1

    def deleteOne(self, number: int) -> None:
        old_frequency = self.number_frequency[number]
        if old_frequency == 0:
            return
        self.frequency_count[old_frequency] -= 1
        new_frequency = old_frequency - 1
        self.number_frequency[number] = new_frequency
        if new_frequency > 0:
            self.frequency_count[new_frequency] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.frequency_count[frequency] > 0


def solve(operations: list[str], arguments: list[list[int]]) -> list[bool | None]:
    tracker = None
    output: list[bool | None] = []
    for operation, args in zip(operations, arguments):
        if operation == "FrequencyTracker":
            tracker = FrequencyTracker()
            output.append(None)
        elif operation == "add":
            assert tracker is not None
            tracker.add(args[0])
            output.append(None)
        elif operation == "deleteOne":
            assert tracker is not None
            tracker.deleteOne(args[0])
            output.append(None)
        elif operation == "hasFrequency":
            assert tracker is not None
            output.append(tracker.hasFrequency(args[0]))
        else:
            raise ValueError(f"unknown operation: {operation}")
    return output

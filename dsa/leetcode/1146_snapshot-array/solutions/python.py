from bisect import bisect_right


class SnapshotArray:
    def __init__(self, length: int):
        self.histories = [[[-1, 0]] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        history = self.histories[index]
        if history[-1][0] == self.snap_id:
            history[-1][1] = val
        else:
            history.append([self.snap_id, val])

    def snap(self) -> int:
        current = self.snap_id
        self.snap_id += 1
        return current

    def get(self, index: int, snap_id: int) -> int:
        history = self.histories[index]
        pos = bisect_right(history, [snap_id, 10**18]) - 1
        return history[pos][1]


def solve(length, operations):
    snapshot = SnapshotArray(length)
    output = []
    for operation, args in operations:
        if operation == "set":
            output.append(snapshot.set(args[0], args[1]))
        elif operation == "snap":
            output.append(snapshot.snap())
        elif operation == "get":
            output.append(snapshot.get(args[0], args[1]))
        else:
            raise ValueError(f"unknown operation: {operation}")
    return output

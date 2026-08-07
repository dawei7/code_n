from bisect import bisect_right


class SnapshotArray:
    def __init__(self, length: int):
        self.histories = [[[0, 0]] for _ in range(length)]
        self.next_snap_id = 0

    def set(self, index: int, val: int) -> None:
        history = self.histories[index]
        if history[-1][0] == self.next_snap_id:
            history[-1][1] = val
        else:
            history.append([self.next_snap_id, val])

    def snap(self) -> int:
        snap_id = self.next_snap_id
        self.next_snap_id += 1
        return snap_id

    def get(self, index: int, snap_id: int) -> int:
        history = self.histories[index]
        position = bisect_right(history, [snap_id, float("inf")]) - 1
        return history[position][1]

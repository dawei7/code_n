from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        waiting_left = [(-(row[0] + row[2]), -worker, worker) for worker, row in enumerate(time)]
        heapify(waiting_left)
        waiting_right = []
        working_left = []
        working_right = []
        current = 0
        boxes = n

        while boxes > 0 or waiting_right or working_right:
            while working_left and working_left[0][0] <= current:
                _, worker = heappop(working_left)
                row = time[worker]
                heappush(waiting_left, (-(row[0] + row[2]), -worker, worker))
            while working_right and working_right[0][0] <= current:
                _, worker = heappop(working_right)
                row = time[worker]
                heappush(waiting_right, (-(row[0] + row[2]), -worker, worker))

            if waiting_right:
                _, _, worker = heappop(waiting_right)
                current += time[worker][2]
                heappush(working_left, (current + time[worker][3], worker))
            elif boxes > 0 and waiting_left:
                _, _, worker = heappop(waiting_left)
                current += time[worker][0]
                boxes -= 1
                heappush(working_right, (current + time[worker][1], worker))
            else:
                next_time = working_right[0][0] if working_right else float("inf")
                if boxes > 0 and working_left:
                    next_time = min(next_time, working_left[0][0])
                current = next_time

        return current

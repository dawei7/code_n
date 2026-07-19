import heapq
from typing import List


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ordered_tasks = sorted(
            (enqueue_time, processing_time, index)
            for index, (enqueue_time, processing_time) in enumerate(tasks)
        )
        available = []
        answer = []
        time = 0
        next_task = 0

        while next_task < len(ordered_tasks) or available:
            if not available and time < ordered_tasks[next_task][0]:
                time = ordered_tasks[next_task][0]

            while (
                next_task < len(ordered_tasks)
                and ordered_tasks[next_task][0] <= time
            ):
                _, processing_time, index = ordered_tasks[next_task]
                heapq.heappush(available, (processing_time, index))
                next_task += 1

            processing_time, index = heapq.heappop(available)
            answer.append(index)
            time += processing_time

        return answer

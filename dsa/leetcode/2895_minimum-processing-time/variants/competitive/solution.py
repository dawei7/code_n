from typing import List


class Solution:
    def minProcessingTime(
        self,
        processorTime: List[int],
        tasks: List[int],
    ) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        return max(start_time + tasks[4 * index] for index, start_time in enumerate(processorTime))

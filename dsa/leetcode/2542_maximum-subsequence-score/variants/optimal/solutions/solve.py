import heapq


def solve(nums1: list[int], nums2: list[int], k: int) -> int:
    selected: list[int] = []
    selected_sum = 0
    answer = 0

    for second, first in sorted(zip(nums2, nums1), reverse=True):
        heapq.heappush(selected, first)
        selected_sum += first

        if len(selected) > k:
            selected_sum -= heapq.heappop(selected)

        if len(selected) == k:
            answer = max(answer, selected_sum * second)

    return answer

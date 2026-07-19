import heapq


def solve(nums: list[int], changeIndices: list[int]) -> int:
    total = sum(nums)
    second_to_index = {}
    first_seen = set()

    for second, one_indexed in enumerate(changeIndices):
        idx = one_indexed - 1
        if nums[idx] > 0 and idx not in first_seen:
            first_seen.add(idx)
            second_to_index[second] = idx

    def can_mark(seconds: int) -> bool:
        heap = []
        heap_sum = 0
        free_marks = 0

        for second in range(seconds - 1, -1, -1):
            idx = second_to_index.get(second)
            if idx is None:
                free_marks += 1
                continue

            value = nums[idx]
            heapq.heappush(heap, value)
            heap_sum += value
            if free_marks == 0:
                removed = heapq.heappop(heap)
                heap_sum -= removed
                free_marks += 1
            else:
                free_marks -= 1

        zeroed = len(heap)
        normal_cost = total - heap_sum + (len(nums) - zeroed)
        zero_cost = 2 * zeroed
        return normal_cost + zero_cost <= seconds

    lo, hi = 0, len(changeIndices) + 1
    while lo < hi:
        mid = (lo + hi) // 2
        if can_mark(mid):
            hi = mid
        else:
            lo = mid + 1

    return lo if lo <= len(changeIndices) else -1

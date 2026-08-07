class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        starts = []
        ends = []
        bits = []
        run_at = [0] * n
        start = 0

        while start < n:
            end = start + 1
            while end < n and s[end] == s[start]:
                end += 1
            run_id = len(starts)
            starts.append(start)
            ends.append(end - 1)
            bits.append(s[start])
            for position in range(start, end):
                run_at[position] = run_id
            start = end

        run_count = len(starts)
        size = 1
        while size < run_count:
            size *= 2
        tree = [0] * (2 * size)

        for run_id in range(1, run_count - 1):
            if bits[run_id] == "1":
                left_zeros = ends[run_id - 1] - starts[run_id - 1] + 1
                right_zeros = ends[run_id + 1] - starts[run_id + 1] + 1
                tree[size + run_id] = left_zeros + right_zeros

        for node in range(size - 1, 0, -1):
            tree[node] = max(tree[2 * node], tree[2 * node + 1])

        def range_max(left: int, right: int) -> int:
            if left > right:
                return 0
            left += size
            right += size
            best = 0
            while left <= right:
                if left % 2 == 1:
                    best = max(best, tree[left])
                    left += 1
                if right % 2 == 0:
                    best = max(best, tree[right])
                    right -= 1
                left //= 2
                right //= 2
            return best

        active = s.count("1")
        answer = []

        for left, right in queries:
            left_run = run_at[left]
            right_run = run_at[right]
            first = left_run + 1 if bits[left_run] == "0" else left_run + 2
            last = right_run - 1 if bits[right_run] == "0" else right_run - 2
            best_gain = 0

            if first <= last:
                first_gain = starts[first] - max(left, starts[first - 1]) + min(right, ends[first + 1]) - ends[first]
                last_gain = starts[last] - max(left, starts[last - 1]) + min(right, ends[last + 1]) - ends[last]
                best_gain = max(
                    first_gain,
                    last_gain,
                    range_max(first + 1, last - 1),
                )

            answer.append(active + best_gain)

        return answer

from collections import Counter


def solve(nums: list[int]) -> int:
    mod = 10**9 + 7

    def choose2(count: int) -> int:
        return count * (count - 1) // 2 if count >= 2 else 0

    left = Counter()
    right = Counter(nums)
    left_pair_total = 0
    right_pair_total = sum(choose2(count) for count in right.values())
    answer = 0

    for index, middle in enumerate(nums):
        old_right = right[middle]
        right_pair_total -= old_right - 1
        right[middle] -= 1
        if right[middle] == 0:
            del right[middle]

        left_size = index
        right_size = len(nums) - index - 1
        left_middle = left[middle]
        right_middle = right.get(middle, 0)
        left_other = left_size - left_middle
        right_other = right_size - right_middle

        left_distinct_other_pairs = choose2(left_other) - (
            left_pair_total - choose2(left_middle)
        )
        right_distinct_other_pairs = choose2(right_other) - (
            right_pair_total - choose2(right_middle)
        )

        current = 0

        current += choose2(left_middle) * choose2(right_middle)
        current += choose2(left_middle) * right_middle * right_other
        current += left_middle * choose2(right_middle) * left_other
        current += choose2(left_middle) * choose2(right_other)
        current += choose2(right_middle) * choose2(left_other)
        current += left_middle * left_other * right_middle * right_other

        if left_middle:
            ways = 0
            for value, left_count in left.items():
                if value == middle:
                    continue
                right_count = right.get(value, 0)
                ways += left_count * (
                    right_distinct_other_pairs
                    - right_count * (right_other - right_count)
                )
            current += left_middle * ways

        if right_middle:
            ways = 0
            for value, right_count in right.items():
                if value == middle:
                    continue
                left_count = left.get(value, 0)
                ways += right_count * (
                    left_distinct_other_pairs
                    - left_count * (left_other - left_count)
                )
            current += right_middle * ways

        answer = (answer + current) % mod

        old_left = left[middle]
        left_pair_total += old_left
        left[middle] += 1

    return answer

"""Merge-sort cross-pair counting for LeetCode 493."""


def solve(nums: list[int]) -> int:
    values = nums.copy()
    buffer = [0] * len(values)

    def sort_and_count(left: int, right: int) -> int:
        if right - left <= 1:
            return 0
        middle = (left + right) // 2
        count = sort_and_count(left, middle) + sort_and_count(middle, right)

        partner = middle
        for index in range(left, middle):
            while partner < right and values[index] > 2 * values[partner]:
                partner += 1
            count += partner - middle

        first = left
        second = middle
        write = left
        while first < middle and second < right:
            if values[first] <= values[second]:
                buffer[write] = values[first]
                first += 1
            else:
                buffer[write] = values[second]
                second += 1
            write += 1
        while first < middle:
            buffer[write] = values[first]
            first += 1
            write += 1
        while second < right:
            buffer[write] = values[second]
            second += 1
            write += 1
        values[left:right] = buffer[left:right]
        return count

    return sort_and_count(0, len(values))

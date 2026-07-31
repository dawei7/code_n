from collections import Counter


def solve(nums: list[int]) -> int:
    modulus = 1_000_000_007

    def choose_two(count: int) -> int:
        return count * (count - 1) // 2

    left = Counter()
    right = Counter(nums)
    left_pairs = 0
    right_pairs = sum(choose_two(count) for count in right.values())
    sum_left_right = 0
    sum_left_right_squared = 0
    sum_left_squared_right = 0
    answer = 0
    length = len(nums)

    for index, middle in enumerate(nums):
        left_middle = left[middle]
        old_right_middle = right[middle]
        right_middle = old_right_middle - 1

        right_pairs -= right_middle
        sum_left_right -= left_middle
        sum_left_right_squared += left_middle * (right_middle * right_middle - old_right_middle * old_right_middle)
        sum_left_squared_right -= left_middle * left_middle
        right[middle] = right_middle

        left_size = index
        right_size = length - index - 1
        left_other = left_size - left_middle
        right_other = right_size - right_middle

        other_left_pairs = left_pairs - choose_two(left_middle)
        other_right_pairs = right_pairs - choose_two(right_middle)
        other_cross = sum_left_right - left_middle * right_middle
        other_left_right_squared = sum_left_right_squared - left_middle * right_middle * right_middle
        other_left_squared_right = sum_left_squared_right - left_middle * left_middle * right_middle

        total = choose_two(left_size) * choose_two(right_size)
        invalid = choose_two(left_other) * choose_two(right_other)
        invalid += left_middle * (left_other * other_right_pairs + right_other * other_cross - other_left_right_squared)
        invalid += right_middle * (right_other * other_left_pairs + left_other * other_cross - other_left_squared_right)
        answer = (answer + total - invalid) % modulus

        left_pairs += left_middle
        sum_left_right += right_middle
        sum_left_right_squared += right_middle * right_middle
        sum_left_squared_right += (2 * left_middle + 1) * right_middle
        left[middle] = left_middle + 1

    return answer

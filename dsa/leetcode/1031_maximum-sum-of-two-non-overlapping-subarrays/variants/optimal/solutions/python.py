"""Optimal app-local solution for LeetCode 1031."""


def solve(nums, first_len, second_len):
    prefix = [0]
    for value in nums:
        prefix.append(prefix[-1] + value)

    def window_sum(left, length):
        return prefix[left + length] - prefix[left]

    def best_order(left_len, right_len):
        best_left = window_sum(0, left_len)
        answer = 0
        for right_start in range(left_len, len(nums) - right_len + 1):
            best_left = max(
                best_left, window_sum(right_start - left_len, left_len)
            )
            answer = max(answer, best_left + window_sum(right_start, right_len))
        return answer

    return max(best_order(first_len, second_len), best_order(second_len, first_len))

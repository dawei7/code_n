def solve(nums: list[int]) -> int:
    best_by_digit = [-1] * 10
    answer = -1
    for number in nums:
        largest_digit = max(map(int, str(number)))
        if best_by_digit[largest_digit] != -1:
            answer = max(answer, best_by_digit[largest_digit] + number)
        best_by_digit[largest_digit] = max(best_by_digit[largest_digit], number)
    return answer

def solve(arr: list[int]) -> int:
    length = len(arr)

    prefix_end = 0
    while prefix_end + 1 < length and arr[prefix_end] <= arr[prefix_end + 1]:
        prefix_end += 1

    if prefix_end == length - 1:
        return 0

    suffix_start = length - 1
    while suffix_start > 0 and arr[suffix_start - 1] <= arr[suffix_start]:
        suffix_start -= 1

    answer = min(length - prefix_end - 1, suffix_start)
    left = 0
    right = suffix_start

    while left <= prefix_end and right < length:
        if arr[left] <= arr[right]:
            answer = min(answer, right - left - 1)
            left += 1
        else:
            right += 1

    return answer

def solve(nums1: list[int], nums2: list[int]) -> int:
    ending_with_first = 1
    ending_with_second = 1
    answer = 1

    for index in range(1, len(nums1)):
        next_first = 1
        next_second = 1

        if nums1[index] >= nums1[index - 1]:
            next_first = max(next_first, ending_with_first + 1)
        if nums1[index] >= nums2[index - 1]:
            next_first = max(next_first, ending_with_second + 1)
        if nums2[index] >= nums1[index - 1]:
            next_second = max(next_second, ending_with_first + 1)
        if nums2[index] >= nums2[index - 1]:
            next_second = max(next_second, ending_with_second + 1)

        ending_with_first = next_first
        ending_with_second = next_second
        answer = max(answer, ending_with_first, ending_with_second)

    return answer

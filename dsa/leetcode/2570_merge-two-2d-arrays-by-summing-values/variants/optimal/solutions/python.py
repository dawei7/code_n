def solve(nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
    first = 0
    second = 0
    merged: list[list[int]] = []

    while first < len(nums1) and second < len(nums2):
        first_id, first_value = nums1[first]
        second_id, second_value = nums2[second]

        if first_id == second_id:
            merged.append([first_id, first_value + second_value])
            first += 1
            second += 1
        elif first_id < second_id:
            merged.append([first_id, first_value])
            first += 1
        else:
            merged.append([second_id, second_value])
            second += 1

    while first < len(nums1):
        merged.append(nums1[first][:])
        first += 1

    while second < len(nums2):
        merged.append(nums2[second][:])
        second += 1

    return merged

from collections import Counter


def solve(nums1, nums2):
    frequencies = Counter()
    cost = 0
    selected = 0
    dominant_value = 0
    dominant_count = 0

    for index, (left, right) in enumerate(zip(nums1, nums2)):
        if left == right:
            cost += index
            selected += 1
            frequencies[left] += 1
            if frequencies[left] > dominant_count:
                dominant_value = left
                dominant_count = frequencies[left]

    for index, (left, right) in enumerate(zip(nums1, nums2)):
        if dominant_count * 2 <= selected:
            break
        if left != right and left != dominant_value and right != dominant_value:
            cost += index
            selected += 1

    return cost if dominant_count * 2 <= selected else -1

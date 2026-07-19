from collections import Counter


class FindSumPairs:
    def __init__(self, nums1: list[int], nums2: list[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.nums2_frequency = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        old_value = self.nums2[index]
        self.nums2_frequency[old_value] -= 1
        self.nums2[index] += val
        self.nums2_frequency[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        return sum(
            self.nums2_frequency[tot - value] for value in self.nums1
        )


def solve(
    operations: list[str], arguments: list[list[object]]
) -> list[int | None]:
    pairs = None
    output: list[int | None] = []

    for operation, values in zip(operations, arguments, strict=True):
        if operation == "FindSumPairs":
            pairs = FindSumPairs(values[0], values[1])
            output.append(None)
            continue
        if pairs is None:
            raise ValueError("FindSumPairs must be constructed first")
        if operation == "add":
            pairs.add(values[0], values[1])
            output.append(None)
        elif operation == "count":
            output.append(pairs.count(values[0]))
        else:
            raise ValueError(f"unsupported operation: {operation}")

    return output

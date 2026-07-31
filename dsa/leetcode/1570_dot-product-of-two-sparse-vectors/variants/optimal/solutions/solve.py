class SparseVector:
    def __init__(self, nums):
        self.values = {index: value for index, value in enumerate(nums) if value != 0}

    def dotProduct(self, vec):
        smaller = self.values
        larger = vec.values
        if len(smaller) > len(larger):
            smaller, larger = larger, smaller

        return sum(value * larger.get(index, 0) for index, value in smaller.items())


def solve(nums1, nums2):
    return SparseVector(nums1).dotProduct(SparseVector(nums2))

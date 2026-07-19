from collections import Counter


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def pair_products(values: List[int]) -> Counter[int]:
            products: Counter[int] = Counter()
            for left in range(len(values)):
                for right in range(left + 1, len(values)):
                    products[values[left] * values[right]] += 1
            return products

        products1 = pair_products(nums1)
        products2 = pair_products(nums2)

        total = sum(products2[value * value] for value in nums1)
        total += sum(products1[value * value] for value in nums2)
        return total

from collections import Counter


def solve(nums1, nums2):
    def pair_products(values):
        products = Counter()
        for i, first in enumerate(values):
            for second in values[i + 1 :]:
                products[first * second] += 1
        return products

    products1 = pair_products(nums1)
    products2 = pair_products(nums2)

    return sum(products2[value * value] for value in nums1) + sum(
        products1[value * value] for value in nums2
    )

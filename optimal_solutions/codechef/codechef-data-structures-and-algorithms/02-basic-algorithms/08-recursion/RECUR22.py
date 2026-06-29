


def solve():
    class Solution:
        def getAllSubsets(self, arr):
            all_subsets = []

            # Generate subsets of all sizes
            for r in range(len(arr) + 1):
                for combo in combinations(arr, r):
                    all_subsets.append(list(combo))

            # Sort elements in each subset
            for subset in all_subsets:
                subset.sort()

            # Sort all subsets
            all_subsets.sort()
            return all_subsets


if __name__ == "__main__":
    solve()

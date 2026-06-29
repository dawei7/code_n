


def solve():
    def backtrack(multiset: List[int], start: int, path: List[int], subsets: List[List[int]]):
        subsets.append(path.copy())

        for i in range(start, len(multiset)):
            if i > start and multiset[i] == multiset[i - 1]:
                continue

            path.append(multiset[i])
            backtrack(multiset, i + 1, path, subsets)
            path.pop()

    def unique_subsets(multiset: List[int]) -> List[List[int]]:
        multiset.sort()
        subsets = []
        path = []
        backtrack(multiset, 0, path, subsets)
        return subsets


if __name__ == "__main__":
    solve()

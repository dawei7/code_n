


def solve():
    def backtrack(multiset, used, path, permutations):
        # If the current path length equals the multiset length, add it to permutations
        if len(path) == len(multiset):
            permutations.append(path[:])
            return

        for i in range(len(multiset)):
            # Skip used elements or skip duplicates to avoid duplicate permutations
            if used[i] or (i > 0 and multiset[i] == multiset[i - 1] and not used[i - 1]):
                continue

            # Include current element in path
            path.append(multiset[i])
            used[i] = True

            # Recurse
            backtrack(multiset, used, path, permutations)

            # Backtrack
            used[i] = False
            path.pop()

    def uniquePermutations(multiset):
        # Sort the multiset to handle duplicates easily
        multiset.sort()

        # Resultant list of permutations
        permutations = []

        # Temporary list to store the current permutation
        path = []

        # Boolean array to keep track of used elements
        used = [False] * len(multiset)

        # Start backtracking from index 0
        backtrack(multiset, used, path, permutations)

        # Return the list of unique permutations
        return permutations

    def printPermutations(permutations):
        for permutation in permutations:
            print("[", end="")
            for i in range(len(permutation)):
                print(permutation[i], end="")
                if i < len(permutation) - 1:
                    print(" ", end="")
            print("]")

    if __name__ == "__main__":
        n = int(input())

        multiset = list(map(int, input().split()))

        # Get the unique permutations
        result = uniquePermutations(multiset)

        # Print the unique permutations
        printPermutations(result)


if __name__ == "__main__":
    solve()

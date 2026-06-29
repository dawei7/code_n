


def solve():
    def findSubsetsWithDuplicates(inputNumbers):
        inputNumbers.sort()  # sort to handle duplicates
        result = []

        def backtrack(start, current):
            result.append(current[:])  # add a copy of current subset
            for i in range(start, len(inputNumbers)):
                if i > start and inputNumbers[i] == inputNumbers[i - 1]:
                    continue  # skip duplicates
                current.append(inputNumbers[i])
                backtrack(i + 1, current)
                current.pop()

        backtrack(0, [])
        return result


if __name__ == "__main__":
    solve()

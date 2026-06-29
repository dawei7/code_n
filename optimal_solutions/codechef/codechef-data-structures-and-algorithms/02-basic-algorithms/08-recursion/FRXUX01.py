


def solve():
    class Solution:
        def findCombinationSum2(self, candidateNumbers, targetSum):
            candidateNumbers.sort()
            result = []
            current = []

            def backtrack(start, target):
                if target == 0:
                    result.append(list(current))
                    return

                for i in range(start, len(candidateNumbers)):
                    # avoid duplicates
                    if i > start and candidateNumbers[i] == candidateNumbers[i - 1]:
                        continue

                    if candidateNumbers[i] > target:
                        break

                    current.append(candidateNumbers[i])
                    backtrack(i + 1, target - candidateNumbers[i])
                    current.pop()

            backtrack(0, targetSum)
            return result


if __name__ == "__main__":
    solve()

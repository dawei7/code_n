


def solve():
    class Solution:
        def backtrack(self, start, combinationCount, targetSum, current, result):
            # If current combination has the required size
            if len(current) == combinationCount:
                if targetSum == 0:
                    result.append(current[:])  # Valid combination found
                return

            for i in range(start, 10):  # Numbers from 1 to 9
                if i > targetSum:
                    break  # No need to continue if i exceeds remaining sum
                current.append(i)
                self.backtrack(i + 1, combinationCount, targetSum - i, current, result)
                current.pop()  # Backtrack

        def findCombinations(self, combinationCount, targetSum):
            result = []
            self.backtrack(1, combinationCount, targetSum, [], result)
            return result


if __name__ == "__main__":
    solve()

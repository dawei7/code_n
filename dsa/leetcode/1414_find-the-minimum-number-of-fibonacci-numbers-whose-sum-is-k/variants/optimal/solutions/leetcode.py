class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fibonacci = [1]
        previous, current = 1, 1
        while current <= k:
            if current != fibonacci[-1]:
                fibonacci.append(current)
            previous, current = current, previous + current

        terms = 0
        for value in reversed(fibonacci):
            if value <= k:
                k -= value
                terms += 1
            if k == 0:
                break
        return terms

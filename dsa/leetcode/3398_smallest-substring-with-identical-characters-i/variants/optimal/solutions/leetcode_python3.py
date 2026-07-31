class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        runs = []
        run_length = 1

        for index in range(1, len(s)):
            if s[index] == s[index - 1]:
                run_length += 1
            else:
                runs.append(run_length)
                run_length = 1
        runs.append(run_length)

        def can_limit(longest: int) -> bool:
            if longest == 1:
                mismatches = sum(
                    character != ("0" if index % 2 == 0 else "1")
                    for index, character in enumerate(s)
                )
                return min(mismatches, len(s) - mismatches) <= numOps

            required = sum(length // (longest + 1) for length in runs)
            return required <= numOps

        low, high = 1, len(s)
        while low < high:
            middle = (low + high) // 2
            if can_limit(middle):
                high = middle
            else:
                low = middle + 1

        return low

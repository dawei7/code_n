class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)

        suffix_minimum = [0] * n
        suffix_minimum[-1] = nums[-1]
        for index in range(n - 2, -1, -1):
            suffix_minimum[index] = min(nums[index], suffix_minimum[index + 1])

        good_cut = [True] * (n + 1)
        prefix_maximum = nums[0]
        for cut in range(1, n):
            good_cut[cut] = prefix_maximum <= suffix_minimum[cut]
            prefix_maximum = max(prefix_maximum, nums[cut])

        divisors = []
        candidate = 1
        while candidate * candidate <= n:
            if n % candidate == 0:
                divisors.append(candidate)
                paired = n // candidate
                if paired != candidate:
                    divisors.append(paired)
            candidate += 1

        answer = 0
        for block_length in divisors:
            if any(not good_cut[cut] for cut in range(block_length, n, block_length)):
                continue

            sortable = True
            for start in range(0, n, block_length):
                descents = 0
                previous = nums[start + block_length - 1]

                for index in range(start, start + block_length):
                    current = nums[index]
                    if previous > current:
                        descents += 1
                        if descents > 1:
                            sortable = False
                            break
                    previous = current

                if not sortable:
                    break

            if sortable:
                answer += block_length

        return answer

from collections import Counter, defaultdict


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        groups = defaultdict(list)
        for value, frequency in Counter(nums).items():
            groups[value % k].append((value, frequency))

        answer = 1
        for group in groups.values():
            group.sort()
            not_taken = 1
            taken = 0
            previous_value = -k

            for value, frequency in group:
                choices = (1 << frequency) - 1
                total = not_taken + taken

                if value - previous_value == k:
                    next_taken = not_taken * choices
                else:
                    next_taken = total * choices

                not_taken = total
                taken = next_taken
                previous_value = value

            answer *= not_taken + taken

        return answer - 1

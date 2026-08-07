from collections import Counter, defaultdict


class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        groups = defaultdict(list)
        for character, frequency in Counter(s).items():
            groups[frequency].append(character)
        return "".join(
            max(
                groups.items(),
                key=lambda item: (len(item[1]), item[0]),
            )[1]
        )

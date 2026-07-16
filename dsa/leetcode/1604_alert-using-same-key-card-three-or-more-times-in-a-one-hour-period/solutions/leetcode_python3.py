from collections import defaultdict
from typing import List


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        uses_by_name = defaultdict(list)
        for name, timestamp in zip(keyName, keyTime):
            hour, minute = map(int, timestamp.split(":"))
            uses_by_name[name].append(hour * 60 + minute)

        alerted = []
        for name, uses in uses_by_name.items():
            uses.sort()
            if any(uses[i] - uses[i - 2] <= 60 for i in range(2, len(uses))):
                alerted.append(name)

        return sorted(alerted)

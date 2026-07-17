from typing import List


class Solution:
    def countMatches(
        self,
        items: List[List[str]],
        ruleKey: str,
        ruleValue: str,
    ) -> int:
        field_index = {"type": 0, "color": 1, "name": 2}[ruleKey]
        return sum(item[field_index] == ruleValue for item in items)

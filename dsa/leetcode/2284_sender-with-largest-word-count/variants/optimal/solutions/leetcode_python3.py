from collections import defaultdict
from typing import List


class Solution:
    def largestWordCount(
        self, messages: List[str], senders: List[str]
    ) -> str:
        totals = defaultdict(int)
        for message, sender in zip(messages, senders):
            totals[sender] += message.count(" ") + 1

        return max(totals, key=lambda sender: (totals[sender], sender))

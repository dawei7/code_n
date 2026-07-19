from collections import defaultdict
from typing import List


class Solution:
    def findingUsersActiveMinutes(
        self, logs: List[List[int]], k: int
    ) -> List[int]:
        minutes_by_user = defaultdict(set)
        for user_id, minute in logs:
            minutes_by_user[user_id].add(minute)

        answer = [0] * k
        for minutes in minutes_by_user.values():
            answer[len(minutes) - 1] += 1
        return answer

from typing import List


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        max_age = 120
        counts = [0] * (max_age + 1)
        for age in ages:
            counts[age] += 1

        prefix = counts[:]
        for age in range(1, max_age + 1):
            prefix[age] += prefix[age - 1]

        requests = 0
        for sender_age in range(15, max_age + 1):
            senders = counts[sender_age]
            if senders == 0:
                continue

            lower_cutoff = sender_age // 2 + 7
            eligible_people = prefix[sender_age] - prefix[lower_cutoff]
            requests += senders * (eligible_people - 1)

        return requests

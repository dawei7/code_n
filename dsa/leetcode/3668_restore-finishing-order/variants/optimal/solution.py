from typing import List


class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        friend_ids = set(friends)
        return [participant for participant in order if participant in friend_ids]

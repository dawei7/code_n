from random import choice
from typing import Optional


class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.values = []
        current = head
        while current is not None:
            self.values.append(current.val)
            current = current.next

    def getRandom(self) -> int:
        return choice(self.values)

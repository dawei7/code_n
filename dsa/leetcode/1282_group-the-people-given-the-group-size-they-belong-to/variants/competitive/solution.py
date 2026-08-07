from collections import defaultdict
from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        buckets = defaultdict(list)
        groups = []

        for person, size in enumerate(groupSizes):
            bucket = buckets[size]
            bucket.append(person)
            if len(bucket) == size:
                groups.append(bucket)
                buckets[size] = []

        return groups

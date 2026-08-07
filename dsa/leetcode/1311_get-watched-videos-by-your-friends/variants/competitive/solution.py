from collections import Counter, deque
from typing import List


class Solution:
    def watchedVideosByFriends(
        self,
        watchedVideos: List[List[str]],
        friends: List[List[int]],
        id: int,
        level: int,
    ) -> List[str]:
        queue = deque([id])
        seen = {id}

        for _ in range(level):
            for _ in range(len(queue)):
                person = queue.popleft()
                for friend in friends[person]:
                    if friend not in seen:
                        seen.add(friend)
                        queue.append(friend)

        counts = Counter()
        for person in queue:
            counts.update(watchedVideos[person])

        return sorted(counts, key=lambda video: (counts[video], video))

from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class FileSharing:

    def __init__(self, m: int):
        self.next_id = 1
        self.available_ids = []
        self.user_chunks = {}
        self.chunk_users = defaultdict(set)

    def join(self, ownedChunks: List[int]) -> int:
        if self.available_ids:
            user_id = heappop(self.available_ids)
        else:
            user_id = self.next_id
            self.next_id += 1

        chunks = set(ownedChunks)
        self.user_chunks[user_id] = chunks
        for chunk_id in chunks:
            self.chunk_users[chunk_id].add(user_id)
        return user_id

    def leave(self, userID: int) -> None:
        for chunk_id in self.user_chunks.pop(userID):
            owners = self.chunk_users[chunk_id]
            owners.remove(userID)
            if not owners:
                del self.chunk_users[chunk_id]
        heappush(self.available_ids, userID)

    def request(self, userID: int, chunkID: int) -> List[int]:
        owners = self.chunk_users.get(chunkID)
        if not owners:
            return []

        result = sorted(owners)
        owners.add(userID)
        self.user_chunks[userID].add(chunkID)
        return result

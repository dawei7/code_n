from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        available_rooms = list(range(n))
        heapify(available_rooms)
        occupied_rooms = []
        meeting_counts = [0] * n

        for start, end in sorted(meetings):
            while occupied_rooms and occupied_rooms[0][0] <= start:
                _, room = heappop(occupied_rooms)
                heappush(available_rooms, room)

            duration = end - start
            if available_rooms:
                room = heappop(available_rooms)
                finish = end
            else:
                finish, room = heappop(occupied_rooms)
                finish += duration

            heappush(occupied_rooms, (finish, room))
            meeting_counts[room] += 1

        return meeting_counts.index(max(meeting_counts))

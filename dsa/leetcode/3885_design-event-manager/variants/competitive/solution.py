import heapq


class EventManager:
    def __init__(self, events: list[list[int]]):
        self.priorities = {}
        self.heap = []

        for event_id, priority in events:
            self.priorities[event_id] = priority
            heapq.heappush(self.heap, (-priority, event_id))

    def updatePriority(self, eventId: int, newPriority: int) -> None:
        self.priorities[eventId] = newPriority
        heapq.heappush(self.heap, (-newPriority, eventId))

    def pollHighest(self) -> int:
        while self.heap:
            negative_priority, event_id = heapq.heappop(self.heap)
            priority = -negative_priority

            if self.priorities.get(event_id) == priority:
                del self.priorities[event_id]
                return event_id

        return -1

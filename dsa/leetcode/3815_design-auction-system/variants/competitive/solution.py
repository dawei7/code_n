from collections import defaultdict
from heapq import heappop, heappush


class AuctionSystem:
    def __init__(self):
        self.bids = {}
        self.heaps = defaultdict(list)

    def addBid(self, userId: int, itemId: int, bidAmount: int) -> None:
        self.bids[(itemId, userId)] = bidAmount
        heappush(self.heaps[itemId], (-bidAmount, -userId))

    def updateBid(self, userId: int, itemId: int, newAmount: int) -> None:
        self.addBid(userId, itemId, newAmount)

    def removeBid(self, userId: int, itemId: int) -> None:
        del self.bids[(itemId, userId)]

    def getHighestBidder(self, itemId: int) -> int:
        heap = self.heaps[itemId]
        while heap:
            negative_amount, negative_user = heap[0]
            amount = -negative_amount
            user_id = -negative_user
            if self.bids.get((itemId, user_id)) == amount:
                return user_id
            heappop(heap)
        return -1

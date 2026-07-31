from collections import defaultdict
from heapq import heappop, heappush


class AuctionSystem:
    def __init__(self) -> None:
        self.bids: dict[tuple[int, int], int] = {}
        self.heaps: defaultdict[int, list[tuple[int, int]]] = defaultdict(list)

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


def solve(operations: list[str], arguments: list[list[int]]) -> list[int | None]:
    auction: AuctionSystem | None = None
    output: list[int | None] = []

    for operation, values in zip(operations, arguments):
        if operation == "AuctionSystem":
            auction = AuctionSystem()
            output.append(None)
        elif operation == "addBid":
            assert auction is not None
            auction.addBid(values[0], values[1], values[2])
            output.append(None)
        elif operation == "updateBid":
            assert auction is not None
            auction.updateBid(values[0], values[1], values[2])
            output.append(None)
        elif operation == "removeBid":
            assert auction is not None
            auction.removeBid(values[0], values[1])
            output.append(None)
        elif operation == "getHighestBidder":
            assert auction is not None
            output.append(auction.getHighestBidder(values[0]))
        else:
            raise ValueError(f"unknown operation: {operation}")

    return output

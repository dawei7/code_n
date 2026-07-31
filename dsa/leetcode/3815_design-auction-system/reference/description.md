## Description

Design an auction system that manages bids from multiple users in real time.

Every bid belongs to one `userId` and one `itemId` and stores a `bidAmount`.

Implement the `AuctionSystem` class with these operations:

- `AuctionSystem()` creates an empty auction system.
- `addBid(userId, itemId, bidAmount)` adds the user's bid for the item. If that user already has a bid for the same item, replace the old amount with `bidAmount`.
- `updateBid(userId, itemId, newAmount)` changes an existing bid to `newAmount`. The specified bid is guaranteed to exist.
- `removeBid(userId, itemId)` removes an existing bid. The specified bid is guaranteed to exist.
- `getHighestBidder(itemId)` returns the user with the greatest bid amount for that item. If several users share the greatest amount, return the greatest `userId`. Return `-1` when the item has no bids.

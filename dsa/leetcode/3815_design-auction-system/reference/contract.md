## Function Contract

**Inputs**

- `operations`: A list beginning with `"AuctionSystem"`, followed by method names from `"addBid"`, `"updateBid"`, `"removeBid"`, and `"getHighestBidder"`.
- `arguments`: A parallel list containing the arguments for each construction or method call.

The canonical interface constructs one stateful `AuctionSystem` and applies the calls in order. A bid is uniquely identified by the pair `(itemId, userId)`. `addBid` and `updateBid` both replace the current amount for that pair rather than creating a second active bid.

Let $Q$ be the number of method calls after construction.

**Return value**

Return one result for every operation: `null` for construction, addition, update, and removal; the selected `userId` for a nonempty `getHighestBidder` query; and `-1` for a queried item with no current bids.

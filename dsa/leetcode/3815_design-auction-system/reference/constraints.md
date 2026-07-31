## Constraints

- `1 <= userId, itemId <= 5 * 10^4`
- `1 <= bidAmount, newAmount <= 10^9`
- At most `5 * 10^4` total calls are made to `addBid`, `updateBid`, `removeBid`, and `getHighestBidder`.
- Every `updateBid` and `removeBid` call refers to a valid existing bid for the specified `userId` and `itemId`.

## Examples

**Example 1**

- Input: `operations = ["AuctionSystem", "addBid", "addBid", "getHighestBidder", "updateBid", "getHighestBidder", "removeBid", "getHighestBidder", "getHighestBidder"]; arguments = [[], [1,7,5], [2,7,6], [7], [1,7,8], [7], [2,7], [7], [3]]`
- Output: `[null, null, null, 2, null, 1, null, 1, -1]`
- Explanation:
  - `AuctionSystem auctionSystem = new AuctionSystem();` initializes an empty auction system.
  - `auctionSystem.addBid(1, 7, 5);` records User `1`'s bid of `5` for item `7`.
  - `auctionSystem.addBid(2, 7, 6);` records User `2`'s bid of `6` for item `7`.
  - `auctionSystem.getHighestBidder(7);` returns `2` because User `2` has the greater bid.
  - `auctionSystem.updateBid(1, 7, 8);` changes User `1`'s bid for item `7` to `8`.
  - `auctionSystem.getHighestBidder(7);` returns `1` because User `1` now has the greater bid.
  - `auctionSystem.removeBid(2, 7);` removes User `2`'s bid for item `7`.
  - `auctionSystem.getHighestBidder(7);` returns `1`, the remaining highest bidder for item `7`.
  - `auctionSystem.getHighestBidder(3);` returns `-1` because item `3` has no bids.

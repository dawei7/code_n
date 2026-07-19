## General
**Viewing unresolved items as next-smaller-or-equal queries**

Scanning from left to right, an item cannot be finalized until the first later price less than or equal to it appears. Keep the indices of such unresolved items in a stack. When the current price is `price`, it resolves every consecutive index on top of the stack whose original price is at least `price`.

For each resolved index, subtract `price` from its copy in the result. Then push the current index because its own discount, if any, must occur farther right.

**Why the stack is monotonic**

After all resolvable indices are popped, either the stack is empty or its top price is strictly smaller than the current price. Pushing the current index therefore leaves stack prices in strictly increasing order from bottom to top.

Equal prices do not remain adjacent on the stack: the later equal value immediately resolves the earlier one, as required by the less-than-or-equal condition. Indices on the stack also remain in increasing order because they are pushed during a left-to-right scan.

**Why a pop uses the first legal discount**

Consider an index `i` popped when processing index `j`. The pop condition proves `prices[j] <= prices[i]`. If any earlier position `k` with $i<k<j$ had also satisfied `prices[k] <= prices[i]`, then `i` would have been on the stack when `k` was processed and would have been popped then. Because it survived until `j`, no earlier qualifying discount exists, so `j` is exactly the required minimum index.

One current price may pop several larger unresolved prices. That is correct: for each of them, all intervening prices were too large, making the same current position its first qualifying discount.

**Handling items that never leave the stack**

Initialize `result` as a copy of `prices`. Popping changes an entry to its discounted value. Any index still on the stack after the scan has no qualifying item to its right, so leaving its copied price unchanged implements the no-discount rule without a cleanup traversal.

## Complexity detail
Every index is pushed once and popped at most once. Although the inner `while` loop may remove many indices in one iteration, it performs at most $N$ pops across the entire scan. The total time is $O(N)$.

The result array contains $N$ values, and the monotonic stack can contain up to $N$ indices for strictly increasing prices. Total space is $O(N)$; excluding the required result, auxiliary stack space is also $O(N)$.

## Alternatives and edge cases
- **Scan rightward for every item:** Stop at the first later price not exceeding the current price. This directly follows the definition but takes $O(N^2)$ time for strictly increasing prices.
- **Scan from right with a value stack:** A carefully maintained monotonic stack can also find the first qualifying value, but preserving the nearest index while discarding dominated entries is less direct than resolving indices left to right.
- **In-place output:** The input array itself can hold final prices, but comparisons must continue using original unresolved prices. Storing indices and reading already modified entries can corrupt the pop condition unless handled carefully.
- **One item:** No later item exists, so its price is unchanged.
- **Strictly increasing prices:** No index is popped; the answer equals the input and the stack reaches its maximum size.
- **Strictly decreasing prices:** Every item except the last uses the immediately following price as its discount.
- **Equal prices:** Equality qualifies, so the first later equal price produces a final price of zero.
- **Multiple possible discounts:** Only the nearest qualifying index matters, even when a smaller price appears later.
- **Repeated values:** Each occurrence is processed independently according to its own later suffix.

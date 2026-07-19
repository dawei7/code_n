## General
**Identify the state needed to extend a sequence:** Its final index alone is insufficient because arithmetic subsequences ending at the same value may have different common differences. Let `dp[i][difference]` be the longest arithmetic subsequence ending at index `i` with that difference.

**Use every earlier element as a predecessor:** For each pair `j < i`, compute `difference = nums[i] - nums[j]`. If an arithmetic subsequence with this difference already ends at `j`, appending `nums[i]` increases its length by one. Otherwise, the pair `nums[j], nums[i]` starts a length-two subsequence.

Several predecessors can produce the same state. Updating with the larger of its existing and candidate lengths is necessary: a later predecessor is not guaranteed to represent the longest chain. Track the largest state value as the answer.

Every stored length describes a valid subsequence because it is created by appending a later element with the required difference. Conversely, remove the last element from any arithmetic subsequence of length at least two; the remaining prefix is exactly a predecessor state considered by this transition. Thus the DP constructs an optimal state for every possible ending pair.

## Complexity detail
There are $\binom{N}{2}$ ordered index pairs with `j < i`, and each hash-map lookup and update takes expected $O(1)$ time, giving $O(N^2)$ time. In the worst case, each of the $N$ ending indices stores $O(N)$ differences, so the maps use $O(N^2)$ space.

## Alternatives and edge cases
- **Bounded-difference table:** Because values lie between $0$ and $500$, differences lie between $-500$ and $500$; fixed-width rows can replace hash maps while retaining $O(N^2)$ time and $O(N)$ space under these fixed source bounds.
- **Choose a starting pair and scan forward:** Greedily extend every pair by its required next value. This is correct but repeats suffix scans and takes $O(N^3)$ time.
- **Duplicate values:** Equal elements form arithmetic subsequences with common difference zero.
- **Negative difference:** A valid subsequence may decrease; differences must not be restricted to nonnegative values.
- **Minimum length:** Any two input elements form an arithmetic subsequence of length two.

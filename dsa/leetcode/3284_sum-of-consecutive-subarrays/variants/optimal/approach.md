## General

**Aggregate valid subarrays by their ending index**

Track increasing-consecutive subarrays ending at the previous index. Their count includes the singleton, and their aggregate value is the sum of all their element sums. If the new adjacent difference is `1`, every tracked subarray can be extended by the new value, and a new singleton is added. The new count grows by one, while the aggregate increases by `new_count * value`.

If the difference is not `1`, no earlier increasing subarray can extend across that edge, so reset both quantities to the new singleton. Maintain an identical count and aggregate for difference `-1`.

At an index, the increasing aggregate plus the decreasing aggregate contains every qualifying subarray ending there. The singleton appears in both directions, so subtract the current value once before adding the contribution to the answer. Any subarray of length at least two has a unique direction and is counted exactly once.

The recurrence extends precisely those subarrays whose prior differences were uniform and whose new difference matches. Resetting at the first mismatch is necessary because every longer extension would still contain that mismatch. Processing all ending indices therefore covers every consecutive subarray exactly as described.

## Complexity detail

The algorithm performs constant work per element, giving $O(n)$ time. It retains two counts, two aggregate sums, and the answer, using $O(1)$ auxiliary space. Intermediate sums are reduced modulo $10^9+7$.

## Alternatives and edge cases

- **Enumerate every subarray:** Extending from every left endpoint and stopping at the first invalid difference is correct but takes $O(n^2)$ on a long consecutive run.
- **Count valid subarrays only:** The required result is the sum of their element sums, so lengths alone are insufficient.
- **Treat absolute differences as enough:** A pattern of `+1, -1` has absolute differences of one but changes direction and is not consecutive.
- Every singleton is valid and must be counted once rather than once per direction.
- Equal adjacent values break both increasing and decreasing runs.
- A direction change ends both longer candidates at that boundary, even when both differences have magnitude one.
- Multiple separated runs contribute independently.
- Long runs and large values require modular reduction during accumulation.

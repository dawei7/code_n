## General
**Classify subarrays by the sign of their final element**

For each index $i$, let $A_i$ be the greatest alternating sum of a subarray
ending at $i$ in which `nums[i]` has a positive sign. Such a subarray has odd
length. Let $S_i$ describe an ending subarray in which `nums[i]` is
subtracted, so its length is even.

These two states retain exactly the information needed to append the next
contiguous element. Keeping only one generic best sum would lose the next sign.

**Either restart with addition or extend the opposite state**

An added state can start a new one-element subarray or extend the previous
subtracted state. A subtracted state must extend the previous added state:

$$
A_i = \max\left(\texttt{nums[i]}, S_{i-1}+\texttt{nums[i]}\right),
$$

$$
S_i = A_{i-1}-\texttt{nums[i]}.
$$

There is no restart option for $S_i$ because the first element of every
subarray is added. Compute both new values from the previous pair before
overwriting either state.

**Take the best endpoint and parity**

Every nonempty subarray ends at some index and has either odd length or even
length, so it belongs to exactly one of these states. The transitions consider
all valid ways to produce each state: restart when allowed, or extend the only
opposite-sign predecessor. Induction on the endpoint therefore makes each
state optimal for its class. The maximum state seen across all endpoints is
the required answer.

## Complexity detail
Each of the $N$ elements performs a constant number of arithmetic operations
and comparisons, for $O(N)$ time. Only the two previous states and the running
answer are retained, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Enumerate all starts and ends:** Maintaining an alternating sum while
  extending every start is correct but takes $O(N^2)$ time.
- **Recompute every subarray sum:** A third loop that sums each selected segment
  raises the cost to $O(N^3)$ and is unnecessary.
- A single element is a valid subarray and is always treated as positive.
- With all negative values, an even-length segment may still be positive
  because subtracting a negative value increases the sum.
- The problem asks for a subarray, not a subsequence; no interior element may
  be skipped.
- A new subarray resets the sign to positive regardless of the absolute index's
  parity.
- The result can exceed the individual value bounds, so fixed-width
  implementations need a sufficiently wide integer type.

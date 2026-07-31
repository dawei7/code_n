## General

Fix one allowed length $k$. Every candidate of that length can be evaluated in one left-to-right pass. Compute the first window sum once, then move the window by adding the entering element and subtracting the leaving element. Each shift therefore costs constant time.

Repeat this pass for every $k$ from $l$ through $r$. Whenever a window sum is strictly positive, compare it with the best value seen so far. Initialize the answer with a sentinel larger than every legal sum; if the sentinel remains unchanged, no qualifying subarray exists and the result is `-1`.

Every allowed subarray has one unique length and starting index, so it appears in exactly one sliding-window pass. Its sum is calculated exactly, and the algorithm retains precisely the minimum among the positive candidates. This covers all and only the subarrays named by the contract.

## Complexity detail

Let $n$ be the array length and let $w=r-l+1$ be the number of allowed lengths. Each length performs at most $n$ constant-time window operations, giving $O(nw)=O(n(r-l+1))$ time. In the worst case $w=\Theta(n)$, so this is $O(n^2)$.

The running sum, answer, and loop indices use $O(1)$ auxiliary space.

The benchmark defines `size` as $n$, sets $l=1$ and $r=n$, and therefore exercises every subarray length. The reference updates adjacent windows in $O(n^2)$ total time. A correct baseline that recomputes every candidate by looping over all of its elements requires $\Theta(n^3)$ work.

## Alternatives and edge cases

- **Prefix sums:** They also evaluate each candidate in constant time after $O(n)$ preprocessing, giving the same $O(n(r-l+1))$ time with $O(n)$ extra space.
- **Resum every candidate:** Directly looping through the elements of each subarray is correct but takes $O(n^3)$ time when all lengths are allowed.
- **Check only lengths `l` and `r`:** The optimum may have any intermediate allowed length.
- **Zero sum:** The condition is strictly greater than zero, so zero never qualifies.
- **No positive candidate:** Leave the sentinel unchanged and return `-1`.
- **Fixed length:** When $l=r$, exactly one sliding-window pass is needed.
- **Length one:** Individual positive elements are valid candidates.
- **Negative values:** Window sums are not monotonic as the window moves or grows, so a two-pointer shrinking rule does not apply.

## General
**Take the largest available reduction**

Operating on a pile of size $p$ removes $\lfloor p/2\rfloor$ stones. This
quantity is nondecreasing with $p$, so a currently largest pile offers a
largest immediate reduction. Store all pile sizes in a max-priority queue,
extract the largest, replace it with
`largest - largest // 2`, and repeat exactly $K$ times.

**Why the greedy choices remain optimal**

Each pile exposes a sequence of possible removal gains as it is repeatedly
chosen. That sequence never increases because the pile only becomes smaller.
At any step, the first unclaimed gain from each pile is available, while later
gains from that pile cannot be taken before it.

The priority queue always takes the largest available gain. If an optimal
schedule instead takes a smaller available gain first, exchanging that
operation with the greedy choice cannot reduce the stones removed, and the
remaining gain sequences are still feasible afterward. Repeating the exchange
aligns an optimum with every greedy operation. Maximizing removed stones
minimizes the remaining total.

## Complexity detail
Building the heap from $N$ piles takes $O(N)$ time. Each of the $K$ operations
performs one removal and insertion in $O(\log N)$ time, giving
$O(N+K\log N)$ total time. The heap stores $N$ integers and uses $O(N)$ space.

## Alternatives and edge cases
- **Scan for the largest pile each time:** This makes the same greedy choices
  but spends $O(N)$ per operation, for $O(KN)$ time.
- **Sort after every operation:** Reordering the complete array repeatedly is
  correct but costs $O(KN\log N)$ time.
- An odd pile keeps the extra stone because the operation removes the floor of
  half; for example, `9` becomes `5`.
- A pile of size one remains one when selected, but the operation still counts
  toward the required total.
- Tied largest piles are interchangeable because they offer equal reductions.

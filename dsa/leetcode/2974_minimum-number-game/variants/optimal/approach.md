## General

The sequence of removed values is simply `nums` in non-decreasing order:
Alice takes the first remaining value, Bob takes the next, and the process
repeats. Sort a copy of the array once to expose that complete removal order.

For every adjacent sorted pair `(alice, bob)`, the game appends Bob's value
before Alice's. Swap positions `0` and `1`, then `2` and `3`, and so on. The
input length is even, so every sorted value belongs to exactly one complete
round.

Sorting preserves duplicates as separate game elements. Within an equal pair,
swapping has no visible effect, which is consistent with either equal minimum
being removed first.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$. Sorting takes $O(N\log N)$ time and the
pairwise swaps take $O(N)$ time. The sorted copy uses $O(N)$ space.

## Alternatives and edge cases

- **Min-heap simulation:** Heapifying and performing two removals per round also takes $O(N\log N)$ time but performs more operations than sorting once.
- **Repeated linear minimum search:** Directly simulating each removal without a heap takes $O(N^2)$ time.
- **Counting frequencies:** Because values are bounded by `100`, a frequency table can produce the removal order in $O(N+100)$ time and $O(100)$ space, but sorting is the general comparison-based approach represented by this branch.
- **Duplicate minima:** Equal values are still removed as distinct elements; their relative identity does not affect the result.
- **Two elements:** One round returns the larger value first and the smaller value second.
- **Even length:** The guarantee ensures there is always a value available for Bob after Alice's removal.

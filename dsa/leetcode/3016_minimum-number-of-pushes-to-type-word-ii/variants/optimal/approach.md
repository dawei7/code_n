## General

**Frequency determines placement value.** The order in which characters appear does not constrain the remapping. Count how often each of the at most 26 letters occurs. Placing a frequency $f$ in a position costing $p$ pushes contributes $fp$ to the total.

**Match high frequencies with cheap positions.** The keypad offers eight positions of cost one, eight of cost two, eight of cost three, and then two relevant positions of cost four. Sort the nonzero frequencies from largest to smallest and assign them to those positions in increasing cost order.

This greedy pairing is optimal by exchange. Suppose frequencies $a\ge b$ were assigned to costs $x>y$. Their contribution would be $ax+by$. Swapping them produces $ay+bx$, smaller by $(a-b)(x-y)\ge0$. Repeating this exchange removes every inversion, leaving the sorted-frequency assignment used by the algorithm.

For zero-based sorted position `index`, the push cost is `index // 8 + 1`. Summing each frequency times that cost gives the minimum.

## Complexity detail

Let $N=\lvert\texttt{word}\rvert$ and let $A\le26$ be the number of distinct lowercase letters. Counting costs $O(N)$ and sorting costs $O(A\log A)$, which is bounded by a constant alphabet. The total time is $O(N)$ and the auxiliary space is $O(1)$ with respect to $N$.

## Alternatives and edge cases

- **Fixed frequency array:** Count into an array of 26 integers and sort it. This has the same asymptotic bounds and avoids hash-table overhead.
- **Frequency buckets:** Because every frequency is between $1$ and $N$, frequencies can be bucketed, but an $O(N)$ bucket array uses more space without improving the overall bound.
- **Recount each occurrence:** Calling a full-string count for every position can still produce the right frequencies after deduplication, but it wastes $O(N^2)$ time.
- **At most eight distinct letters:** Every used letter receives a one-push position, so the answer is exactly $N$.
- **Equal frequencies:** Their relative placement is irrelevant because exchanging equal contributions does not change the total.
- **Highly skewed input:** The most frequent letter must receive a one-push position; assigning it deeper can only increase the answer.

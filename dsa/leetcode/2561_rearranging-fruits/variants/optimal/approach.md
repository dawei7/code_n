## General

The final baskets must contain half of the combined copies of every fruit cost. Therefore, if any value appears an odd number of times across both baskets, equalization is impossible. Subtract the second basket's frequencies from the first. Every difference must be even; half of its absolute value is the number of copies of that fruit that are misplaced on one side.

Collect those required outgoing copies from both baskets in one list. Its length is twice the number of swaps that must ultimately occur. For a direct exchange of values $x$ and $y$, the cost is $\min(x,y)$. Consequently, an optimal opposing pairing makes the smaller endpoint of every pair one of the smallest half of all misplaced values; pairing details among the larger endpoints cannot lower those direct costs further.

There is also an indirect option. Let $g$ be the smallest fruit cost anywhere in either basket. The intended exchange of $x$ and $y$ can be routed through $g$ in two swaps, restoring the minimum fruit afterward, for cost $2g$. Thus a pair whose smaller endpoint is $x$ costs $\min(x,2g)$.

Sort the complete misplaced list, take its first half, and sum $\min(x,2g)$ for those values. This simultaneously chooses the cheapest direct endpoints and applies the global-minimum detour exactly where it helps. If the baskets already have equal frequencies, the misplaced list is empty and the cost is zero.

## Complexity detail

Let $n$ be the number of fruits in each basket. Building the frequency difference and the misplaced list takes $O(n)$ time. At most $n$ misplaced entries are sorted, which costs $O(n\log n)$ time, and the final sum is linear. The counter and misplaced list use $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Sort both complete baskets:** Coordinating sorted frequency runs can identify surpluses, but it sorts $2n$ inputs and still needs the same greedy cost reasoning.
- **Repeatedly choose the cheapest remaining pair:** Searching an unsorted surplus list for each swap is correct with careful pairing but can take $O(n^2)$ time.
- **Direct swaps only:** Pairing surpluses without considering the global minimum overpays whenever both exchanged values exceed $2g$.
- **Odd combined frequency:** A fruit cost with an odd total count can never be split equally, so the result is immediately `-1`.
- **Already equal baskets:** Ordering is irrelevant; matching frequency maps require no swaps and cost zero.
- **Duplicate surplus copies:** Half of the absolute frequency difference records exactly how many copies must leave one side, not the full difference.
- **Large total cost:** Up to $O(n)$ swaps may each cost near $10^9$, so fixed-width implementations need a 64-bit accumulator.

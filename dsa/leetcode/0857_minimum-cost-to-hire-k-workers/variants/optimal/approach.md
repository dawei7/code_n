## General
**A group is determined by one pay ratio**

If every selected worker is paid at a common rate $r$ per unit of quality, worker $i$ receives $r \cdot \texttt{quality[i]}$. Meeting that worker's minimum requires

$$
r \geq \frac{\texttt{wage[i]}}{\texttt{quality[i]}}.
$$

For a fixed group, the cheapest valid rate is therefore the largest wage-to-quality ratio among its members. Its cost is that ratio multiplied by the group's total quality.

**Sweep possible maximum ratios**

Sort workers by their individual required ratio in ascending order. When processing a worker with ratio $r$, all workers seen so far can be paid legally at rate $r$. Among them, the cheapest $k$-worker quality total is obtained by choosing the $k$ smallest qualities.

Maintain those qualities in a max-heap represented by negative values, along with their sum. Push each new quality; whenever the heap exceeds $k$, remove its largest quality. With exactly $k$ entries, `quality_sum * ratio` is the best cost using the current ratio as an upper pay threshold.

Every feasible group appears when its largest required ratio is reached. At that step all its workers are available, and the heap's quality sum is no larger than that group's sum. The recorded candidate is therefore no worse. Conversely, each recorded candidate selects $k$ available workers and pays them all at a sufficient ratio, so it is feasible. The minimum candidate is exactly optimal.

## Complexity detail
Sorting $n$ workers takes $O(n\log n)$ time. Each worker causes one heap insertion and at most one removal, each $O(\log k)$, so sorting dominates and total time is $O(n\log n)$. The sorted worker list and heap use $O(n)$ space.

## Alternatives and edge cases
- **Enumerate worker groups:** Checking all $\binom{n}{k}$ subsets is correct but exponential in the worst case.
- **Keep a sorted quality list:** It can identify the largest selected quality, but insertion and deletion may take linear time.
- **Min-heap of qualities:** The algorithm must evict the largest quality, so a max-heap is the direct choice.
- **One worker:** The minimum is simply the smallest individual wage.
- **Hire everyone:** The maximum individual ratio fixes the rate for the sum of all qualities.
- **Equal ratios:** The heap keeps the $k$ smallest qualities at that shared rate.
- **Large minimum wage, low quality:** Such a worker's high ratio may make otherwise small total quality expensive.
- **Floating-point output:** The accepted tolerance covers ordinary division rounding; all heap decisions use integer qualities.
- **Exactly $k$ workers:** Candidates are evaluated only when the heap contains exactly $k$ qualities.

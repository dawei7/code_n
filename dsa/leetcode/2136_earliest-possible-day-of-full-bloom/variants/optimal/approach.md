## General

**Start the longest growth phases first**

Plant seeds in descending order of `growTime`. Maintain the cumulative number
of planting days. When a seed's planting finishes, its bloom day is that
cumulative total plus its growth duration; the schedule finishes at the
maximum such value.

Splitting a seed's planting across nonconsecutive days offers no advantage:
moving its pieces together at its completion position does not delay any
earlier completion. It is therefore sufficient to reason about whole-seed
planting blocks.

Consider adjacent seeds $a$ then $b$ with $g_a<g_b$, after some fixed amount
of earlier planting. In that order, the pair's relevant completion maximum is
at least the completion of $b$, after both planting blocks plus $g_b$.
Swapping them lets $b$ begin growing after only its own planting block, while
$a$ finishes after both blocks with the no-larger tail $g_a$. The swap cannot
increase the pair's final bloom. Repeatedly removing such inversions yields
descending growth time, proving the greedy order optimal.

## Complexity detail

Let $n$ be the number of seeds. Sorting the paired durations takes
$O(n\log n)$ time, and the schedule scan takes $O(n)$. The sorted list of pairs
uses $O(n)$ space.

## Alternatives and edge cases

- **Repeatedly select the largest remaining growth time:** This produces the
  same optimal order but takes $O(n^2)$ time without a heap.
- **Sort by planting time:** Planting duration affects cumulative completion
  but not which autonomous wait should start first, so this order can be
  suboptimal.
- Equal growth times may appear in either relative order.
- For one seed, the answer is its planting time plus its growth time.
- The answer may exceed each individual duration because all planting work is
  serialized.

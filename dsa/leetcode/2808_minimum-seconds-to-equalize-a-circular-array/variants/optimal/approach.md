## General

**View each existing value as simultaneous spreading sources**

Fix a candidate final value $x$. Every position already containing $x$ spreads it one circular edge left and right per second. Between two consecutive occurrences at indices $i$ and $j$, let $d$ be their circular index distance. The $d-1$ interior positions are reached from both ends, so the last one needs

$$
\left\lfloor \frac{d}{2} \right\rfloor
$$

seconds. Therefore $x$ equalizes the whole array in half of its largest circular gap between consecutive occurrences.

**Measure every cyclic gap in one pass**

Store the indices of each value in increasing order. Consecutive entries give every ordinary gap. The wraparound gap from the last occurrence back to the first is `n + first - last`. Take the largest of these distances and divide it by two using integer division.

Minimize that time over all distinct values. Each index belongs to exactly one positions list, and the gaps across all lists total $n$, so evaluating every candidate still takes linear rather than quadratic time. The chosen minimum is achievable because propagation covers each gap from its two endpoints. It is also necessary because the midpoint of the largest gap cannot receive that value sooner.

## Complexity detail

Let $n$ be the array length. Building the occurrence lists takes $O(n)$ time and space. Scanning all consecutive and wraparound gaps examines each stored index a constant number of times, so total time is $O(n)$ and auxiliary space is $O(n)$.

## Alternatives and edge cases

- **Simulate every second:** Rewriting the entire array until it becomes constant can require $O(n^2)$ time and introduces choices that are difficult to coordinate optimally.
- **Evaluate each value with a full array scan:** This correctly measures distances but takes $O(nd)$ time for $d$ distinct values, becoming quadratic when all values differ.
- **Binary search the answer:** A feasibility check can determine whether every position lies near a source, but repeated checks add an unnecessary logarithmic factor.
- A singleton or already constant array has largest gap zero or one and returns `0`.
- With one occurrence of a candidate value, its only circular gap has length $n$, so it needs $\lfloor n/2 \rfloor$ seconds.
- The wraparound distance must be included; treating the array as linear can underestimate the uncovered arc.
- Simultaneous updates are essential: a value spreads only one edge per second, not through an arbitrarily long chain in one operation.

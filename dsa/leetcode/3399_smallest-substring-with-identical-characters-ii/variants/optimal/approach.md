## General

Fix a candidate maximum identical-block length $L$. Feasibility is monotone: any edited string satisfying $L$ also satisfies every larger limit. This permits binary search for the first feasible value from 1 through $n$, avoiding a candidate-by-candidate scan at the $10^5$ input limit.

Precompute the lengths of all maximal equal-character runs. When $L\ge2$, a run of length $r$ requires exactly

$$
\left\lfloor\frac{r}{L+1}\right\rfloor
$$

flips. A constructive placement changes every $(L+1)$st character, separating the original run into pieces no longer than $L$. In the other direction, each flip can break only the surrounding stretch, so every complete group of $L+1$ original characters forces one change. A changed character contributes at most one character to the opposite bit on either side, which cannot create a block longer than $L$ when $L\ge2$. The runs are therefore independent, and their required-flip counts can be summed.

The case $L=1$ needs separate treatment because the final string must alternate globally. Exactly two targets exist: `0101...` and `1010...`. Count mismatches against the first pattern. Since every position contains one of two bits, the second pattern has $n$ minus that many mismatches. The smaller count is the exact number of flips needed.

Use the total required flips as the binary-search predicate. A feasible midpoint keeps the midpoint and everything above it; an infeasible midpoint discards its entire lower prefix. The final shared bound is the smallest achievable longest block.

## Complexity detail

Let $n$ be the length of `s`. Run construction costs $O(n)$ time. Each predicate evaluation examines at most all runs or all characters, so it costs $O(n)$ time, and binary search evaluates $O(\log n)$ candidates. Total time is $O(n\log n)$ and the run-length list uses $O(n)$ auxiliary space.

The benchmark defines `size` as $n$ and uses 28, 56, and 112 characters, spanning 4x. Each string has a zero prefix of length $n/2$, followed by an alternating suffix, and permits no flips; consequently its optimum is $n/2$. The accepted method checks logarithmically many limits. A correct slower baseline checks every smaller candidate and fails only the scaling verdict.

## Alternatives and edge cases

- **Dynamic programming predicate:** For a chosen limit, track the resulting final bit and current run length while minimizing changes; this is correct but uses more state and larger constants.
- **Linear candidate search:** Reusing the predicate for $L=1,2,\ldots$ is correct but can require $O(n^2)$ time and is unsuitable for $n=10^5$.
- **Unfocused greedy flips:** Always splitting the currently longest run does not directly reveal the optimum because the flip budget is shared; a fixed target limit makes each run's cost precise.
- **Limit one:** The independent-run formula does not capture interactions across run boundaries; compare the entire string with both alternating patterns.
- **Zero operations:** The result equals the longest run already present in `s`.
- **Single character:** Every valid one-character input has answer one, regardless of the available budget.
- **Large inputs:** Store only run lengths; never enumerate edited strings or positions for every possible answer.
- **Unused budget:** Because operations are allowed at most `numOps` times, extra flips never need to be forced.

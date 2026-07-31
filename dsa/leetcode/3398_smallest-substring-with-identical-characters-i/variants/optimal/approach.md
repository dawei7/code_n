## General

For any proposed maximum block length $L$, feasibility is monotone: if at most `numOps` flips can make every identical run at most $L$, the same edited string also satisfies every larger limit. Therefore, binary-search the smallest feasible $L$ from 1 through $n$.

First record the lengths of the maximal equal-character runs. For $L\ge2$, a run of length $r$ needs

$$
\left\lfloor\frac{r}{L+1}\right\rfloor
$$

flips. Placing a flip after each group of $L$ unchanged characters breaks the run into legal pieces. Conversely, each flip can separate at most two such pieces, so every $L+1$ consecutive original characters require a flip. The changed character cannot create an illegal neighboring run when $L\ge2$: it contributes at most one character to the opposite bit on either side. Runs can consequently be counted independently, and summing this formula gives the minimum required operations.

The limit $L=1$ is different because the entire result must alternate. There are only two possible alternating strings, one beginning with `0` and one with `1`. Count mismatches against the first; because `s` is binary, the mismatch count against the other is $n$ minus that count. The smaller value is the exact number of flips needed for a longest run of one.

At each binary-search step, keep the feasible limits in the upper half and the infeasible limits in the lower half. When the bounds meet, their common value is the minimum achievable longest run.

## Complexity detail

Let $n$ be the length of `s`. Building the run-length list costs $O(n)$ time. A feasibility check costs $O(n)$ in the worst case, and binary search performs $O(\log n)$ checks, for $O(n\log n)$ total time. The stored run lengths use $O(n)$ auxiliary space.

The benchmark defines `size` as $n$ and uses 24, 48, and 96 characters, spanning 4x. Each workload has one length-$n/2$ zero run followed by an alternating suffix and allows no flips, so the optimum is $n/2$. The accepted method scans the run list for logarithmically many candidate limits. A correct slower baseline checks limits consecutively from 1 and fails only the scaling verdict.

## Alternatives and edge cases

- **Dynamic programming for a fixed limit:** Track the previous resulting bit and its current run length while minimizing flips. This is general but costs more state and work than the run formula.
- **Linear search over limits:** Testing $L=1,2,\ldots$ with the same predicate is correct, but it can take $O(n^2)$ time.
- **Greedy flips without a target limit:** Breaking the currently longest run does not directly determine the global optimum; binary search supplies the limit that makes local run costs meaningful.
- **Limit one:** Independent run division is invalid here because adjacent changed characters interact; compare against the two complete alternating patterns.
- **No operations:** The answer is the maximum original run length.
- **Single character:** The nonempty string always has answer one.
- **Unused operations:** The contract permits at most `numOps` flips, so an optimal result never needs to spend flips that provide no improvement.

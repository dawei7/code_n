## General

The operation is global for the chosen value. Although the statement describes maximal contiguous segments, the collection of all maximal `x`-segments covers every current occurrence of `x`. Consequently, choosing `x` updates every position whose value is currently `x`, including separated occurrences.

Consider a position that differs initially, so `nums[i] != target[i]`, and let its original value be `x`. That position cannot change until an operation chooses `x`: operations for other values do not include it. Every distinct original value found at a mismatched position therefore forces at least one operation.

This lower bound is attainable. Collect the distinct values

$$
D=\{\texttt{nums[i]}\mid \texttt{nums[i]}\ne\texttt{target[i]}\}.
$$

Choose every value in $D$ once, in any order. Until its value `x` is chosen, each initially mismatched position that started as `x` remains `x`; no other selection can alter it. The `x` operation then assigns that position its target value. A position fixed by an earlier operation also remains correct if its target value equals some value chosen later: the later operation simply assigns the same target value again. Thus created value collisions cannot undo progress, and after all values in $D$ have been selected, every position matches `target`.

The matching lower and upper bounds show that the minimum number of operations is exactly $\lvert D\rvert$. A single pass can build this set and return its size.

## Complexity detail

Let $N$ be the common array length and let $\lvert D\rvert$ be the number of distinct original values at mismatched positions. The scan performs expected constant-time hash-set work per position, for $O(N)$ expected time. The set uses $O(\lvert D\rvert)$ auxiliary space, which is $O(N)$ in the worst case.

The benchmark defines size as $N$. Every benchmark position is mismatched and has a distinct original value, forcing the optimal solution to scan and store all $N$ values. The slower control keeps the same distinct values in a list and linearly searches that list before each insertion, producing quadratic work.

## Alternatives and edge cases

- **Bounded-value boolean table:** Because values are at most $10^5$, a fixed seen array also gives $O(N+V)$ time and $O(V)$ space for value bound $V$; a set avoids initializing the entire domain.
- **Sort mismatched original values:** Sorting and counting distinct values is correct, but costs $O(N\log N)$ time and $O(N)$ storage when the sort is not in place.
- **Repeated list membership:** Comparing each mismatched value with a growing list of previous values is correct but can require $O(N^2)$ comparisons.
- **Arrays already equal:** The set $D$ is empty, so zero operations are required.
- **Separated occurrences of one value:** All maximal segments for the chosen value are updated in the same operation, so separation does not increase the answer.
- **Repeated mismatched positions:** Any number of mismatches with the same original value contribute only one operation.
- **Cycles between values:** Transformations such as `[1,2]` to `[2,1]` need one operation for each distinct mismatched original value; no extra temporary value is needed.
- **Values created by an earlier operation:** A later selection may include newly fixed positions, but assigning their corresponding target values leaves them correct.

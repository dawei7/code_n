## General

**Fix the middle index.** If `nums[i] = x` is the selected middle, the other four indices must be two of the $L=i$ positions to its left and two of the $R=n-i-1$ positions to its right. Begin with all

$$
\binom{L}{2}\binom{R}{2}
$$

choices and subtract precisely those in which $x$ is not the unique mode. Let $a$ and $b$ be the frequencies of $x$ strictly to the left and right. For every other value $y$, let $L_y$ and $R_y$ be its corresponding side frequencies.

**Classify every invalid choice.** If no additional $x$ is selected, $x$ occurs once and cannot be a unique mode. This removes

$$
\binom{L-a}{2}\binom{R-b}{2}.
$$

If two or more additional copies of $x$ are selected, then $x$ occurs at least three times among five elements and is automatically the unique mode. The only remaining invalid family selects exactly one additional $x$ and has another value occur at least twice among the other three positions.

For an additional $x$ chosen on the left, define aggregates over $y\ne x$:

$$
Q_R=\sum_y\binom{R_y}{2},\qquad
C=\sum_yL_yR_y,\qquad
T_R=\sum_yL_yR_y^2.
$$

The invalid count for this orientation is

$$
a\left((L-a)Q_R+(R-b)C-T_R\right).
$$

The first term makes the two right-side non-$x$ values equal. In the remaining case those two values differ, so the left-side non-$x$ value must match one of them; $(R-b)C-T_R$ counts exactly those matches without double counting. By symmetry, choosing the additional $x$ on the right contributes

$$
b\left((R-b)Q_L+(L-a)C-T_L\right),
$$

where $Q_L=\sum_y\binom{L_y}{2}$ and $T_L=\sum_yL_y^2R_y$, again excluding $x$.

**Maintain the sums while sweeping.** Frequency maps hold all $L_y$ and $R_y$. Alongside them, maintain the five global sums $Q_L$, $Q_R$, $\sum_yL_yR_y$, $\sum_yL_yR_y^2$, and $\sum_yL_y^2R_y$. Removing the current element from the right and later adding it to the left changes only that value's contribution, so every aggregate updates in constant expected time. Subtract the current middle value's own contribution to obtain each $y\ne x$ sum, add the valid count modulo $10^9+7$, and continue.

These invalid families are disjoint and exhaustive: $x$ is selected one, two, or at least three times. The first family removes the one-copy case, both oriented formulas remove exactly the tied-or-losing two-copy cases, and every at-least-three-copy selection remains valid. Thus the remainder is exactly the desired count.

## Complexity detail

Let $n$ be the array length and $d$ the number of distinct values. Each index performs a constant number of expected-time hash-map operations and arithmetic updates, giving expected $O(n)$ time. The two frequency maps store $O(d)\subseteq O(n)$ entries, so auxiliary space is $O(n)$.

The benchmark defines `size` as $n$ and uses 48, 144, and 288 elements, spanning 6x. Each tier repeats many values on both sides of typical middle positions. The accepted aggregate method remains linear, while a correct slower formulation scans every distinct value for each middle and must fail only the scaling verdict.

## Alternatives and edge cases

- **Enumerate five indices:** Direct enumeration costs $O(n^5)$ and is infeasible at the $10^5$ input limit.
- **Scan every distinct value per middle:** The same combinatorial families can be counted in $O(nd)$ time, but maintained moments remove this inner scan.
- **Use only total frequencies:** The third selected element fixes an index, so occurrences strictly before and after it must remain separate.
- **All values distinct:** The middle appears once in every selection, and the answer is zero.
- **All values equal:** Every five-index choice is valid, giving $\binom{n}{5}$ modulo $10^9+7$.
- **A competing pair:** When the middle value occurs exactly twice, any other value occurring twice or three times invalidates uniqueness.
- **At least three middle copies:** No other value can match that frequency in a sequence of length five, so the mode is necessarily unique.
- **Negative and large values:** Hash-map keys handle the full value range without coordinate-sized storage.

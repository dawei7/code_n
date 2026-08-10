## General

The solution builds valid permutations one comparison at a time. Actual chosen values are less important than their relative ranks, because each `I` or `D` condition compares only which of two adjacent values is larger.

Define `f[i][j]` as the number of permutations of $i+1$ distinct ranked values that satisfy the first $i$ characters of `s` and whose final value has rank $j$ among those $i+1$ values. Rank zero means smallest and rank $i$ means largest.

For zero pattern characters, the permutation has one value. Its only possible last rank is zero, so `f[0][0] = 1`.

**Why rank state is sufficient.** Suppose a valid length-$i$ relative ordering ends with old rank $k$, and a new final value of rank $j$ is appended among $i+1$ total values. Inserting a new rank changes absolute labels of some older elements, but it preserves all comparisons among them. The only new condition to check is between the previous final element and the new final element.

If the new rank $j$ is inserted:

- an old rank below $j$ remains below the new value;
- an old rank at least $j$ shifts upward and lies above the new value.

Therefore:

- For an increasing character `I`, the old last value must be smaller, so $k<j$.
- For a decreasing character `D`, the old last value must be larger, so $k\ge j$.

This gives the exact transitions.

For `I`:

$$
f[i][j]=\sum_{k=0}^{j-1} f[i-1][k].
$$

For `D`:

$$
f[i][j]=\sum_{k=j}^{i-1} f[i-1][k].
$$

The loops in the code implement these sums directly and reduce after each addition modulo $10^9+7$.

**A small example with `s = "D"`.** Initially `f[0][0]=1`. At $i=1$, a decreasing result can end only with new rank $j=0$, because the previous value must be above it. The sum includes old rank zero and gives one. Ending with new rank one has no old rank at least one and gives zero. Summing the row returns one, representing permutation `[1,0]`.

**Why relabeling ranks counts actual permutations.** Every permutation of values $0$ through $i$ has a unique rank at every position—its value itself is that rank within the complete set. Conversely, each sequence of distinct relative ranks corresponds to one permutation of those values. The insertion transition maps each shorter permutation and chosen new final rank to exactly one longer permutation: raise every old value at least $j$ by one, then append $j$.

No two source pairs produce the same longer permutation because removing its final value and compressing higher ranks recovers the unique preceding permutation and $j$. Thus the transition neither loses nor duplicates permutations.
The length-one base counts the sole empty-pattern permutation. Assume row $i-1$ correctly counts every valid permutation by final rank. Appending a new final rank preserves all earlier comparisons. The transition includes exactly predecessor ranks that satisfy the new `I` or `D` comparison, and the rank insertion is bijective. Therefore row $i$ correctly counts all valid permutations satisfying the first $i$ characters. After all $n$ characters, the final value may have any rank $0$ through $n$, so summing the last row produces the total.

The table uses size $(n+1)\times(n+1)$ even though row $i$ needs only columns $0$ through $i$. Unused cells remain zero.

## Complexity detail

The exact code has three nested scales: $i$ ranges to $n$, `j` ranges to $i$, and each transition explicitly sums up to $i$ predecessor ranks.

- **Time complexity of the exact solution:** $O(n^3)$.
- **Space complexity of the exact solution:** $O(n^2)$ for the table.

The manifest's $O(n^2)$ time and $O(n)$ space correspond to optimizing each row's range sums with prefix or suffix sums and retaining only the previous row. The current `solution.py` does not implement those optimizations.

## Alternatives and edge cases

- **Prefix/suffix-sum DP:** Precompute cumulative sums of the previous row so every `f[i][j]` transition is $O(1)$. Rolling two rows gives $O(n^2)$ time and $O(n)$ space, matching the manifest.
- **Enumerate all permutations:** This takes $(n+1)!$ candidates and is infeasible even for moderate $n$.
- **Memoized interval formulations:** Other rank-based recurrences are possible, but the ending-rank state makes prefix-sum optimization direct.
- **Single `I`:** Only permutation `[0,1]` is valid.
- **Single `D`:** Only `[1,0]` is valid.
- **All `I`:** Exactly one fully increasing permutation exists.
- **All `D`:** Exactly one fully decreasing permutation exists.
- **Mixed pattern:** Several ending ranks can have nonzero counts, so the final row must be summed.
- **Strict comparisons:** Equal values never occur because `perm` is a permutation of distinct integers.
- **Rank insertion shift:** Old ranks at least `j` move up by one; this is why the decreasing condition uses old `k >= j`.
- **Modulo:** Each transition addition is reduced, and the final row sum is reduced again.
- **Unused table cells:** Values above current row index stay zero and do not affect transitions.
- **Manifest mismatch:** The direct inner `k` loops must be counted; they prevent the exact code from being quadratic.

## General

**Interpret the score as a cyclic tour**

For a permutation `perm`, every term connects one selected value to the next:

$$
\left|\texttt{perm}[i]-\texttt{nums[perm}[i+1]\texttt{]}\right|,
$$

with the last element connecting back to `perm[0]`. Thus we must order all indices in one directed cycle, with transition cost from current index $a$ to next index $b$ equal to

$$
w(a,b)=\lvert a-\texttt{nums}[b]\rvert.
$$

This resembles a small traveling-salesperson dynamic program. The constraint $n\le14$ makes subset states feasible.

**Fix the first element to zero**

Rotating a cyclic permutation does not change any of its directed transitions or total score. Every cycle can be written with 0 first. Since 0 is the smallest possible first value, the lexicographically smallest representation of any cycle rotation begins with 0.

Therefore, the optimal answer may be searched with `perm[0] = 0` without losing any score optimum or lexicographically smaller result.

**Subset state**

`dfs(mask, pre)` is the minimum additional cost needed when:

- bits set in `mask` are indices already placed in the permutation;
- `pre` is the last placed index;
- the first index is fixed as 0.

If every bit is set, all indices have been used. The only remaining score term closes the cycle from `pre` to 0:

`abs(pre - nums[0])`.

Otherwise, choose an unvisited `cur` from 1 through $n-1$. Appending it contributes

`abs(pre - nums[cur])`

and leaves subproblem `dfs(mask | 1 << cur, cur)`. Taking the minimum over all choices yields the recurrence.

The condition `mask >> cur & 1 ^ 1` is true when bit `cur` is zero. In clearer parenthesized form, it asks whether `((mask >> cur) & 1) == 0`.

Caching is essential. Many different partial orders can reach the same set of visited indices and same final index; from that point onward, the optimal completion depends only on those two facts, not the earlier order.

**Reconstruct the lexicographically smallest optimal permutation**

Function `g(mask, pre)` appends `pre` to output `ans`. If the permutation is incomplete, it obtains optimal remaining cost `res = dfs(mask, pre)` and tests unvisited candidates `cur` in increasing numeric order.

A candidate can begin an optimal continuation exactly when

$$
\lvert\texttt{pre}-\texttt{nums[cur]}\rvert
+\operatorname{dfs}(\texttt{newMask},\texttt{cur})
=\texttt{res}.
$$

The first candidate satisfying this equality is the smallest possible next value among all optimal completions. The function recursively applies the same rule to the next position.

Lexicographic order is decided at the first differing position. With the current prefix fixed, choosing the smallest next value that still permits optimal total cost is always lexicographically best; no later choices can compensate for a larger value at this position. Induction makes the entire reconstructed permutation lexicographically smallest among all minimum-score permutations.

**Example of score alignment**

If the current chosen index is 1 and the next permutation value is 2, the transition cost is not `abs(nums[1] - nums[2])`. From the definition it is `abs(1 - nums[2])`. The DP uses `pre` directly on the left and indexes `nums` by `cur` on the right, matching the unusual score formula exactly.

For the final element, the next permutation value is the fixed 0, so closure is `abs(pre - nums[0])`. Forgetting this term would optimize an open path instead of the required cycle.


For any state, every valid completion chooses one currently unvisited next index and then a completion of the resulting smaller state. The recurrence considers all such next choices and, by induction on remaining indices, uses their minimum completion costs. It therefore returns the exact optimal remaining score.

Reconstruction only follows transitions whose immediate plus cached future cost equals that optimum. It always returns an optimal tour. Its ascending first-feasible choice establishes lexicographic minimality position by position.

## Complexity detail

There are at most $n2^n$ meaningful `(mask, pre)` states. Each computed state scans up to $n$ candidate next indices, so time is $O(n^2 2^n)$.

The cache stores $O(n2^n)$ integer results. Recursion depth is at most $n$, and the answer uses $O(n)$ space. Cache storage dominates, giving $O(n2^n)$ auxiliary space.

Reconstruction scans up to $n$ candidates at each of $n$ positions and performs cached lookups, adding $O(n^2)$ time, which is dominated by DP.

The code defines `dfs` and `g` before assigning `n`, but Python closures resolve `n` when the functions are called. `n` is assigned before `g(1, 0)` starts, so this is valid.

## Alternatives and edge cases

- **Enumerate every permutation:** It takes $O(n!)$ time, which is infeasible at $n=14$.
- **Bottom-up subset DP:** Fill mask/end states iteratively and store parent choices. It has the same asymptotic bounds but tie-aware reconstruction can require careful parent comparisons.
- **Store complete paths in DP:** This simplifies tie selection but greatly increases memory and comparison costs. Cost-only DP plus greedy reconstruction is cleaner.
- **Do not fix zero first:** It repeats every cycle under all rotations and complicates lexicographic comparison.
- **Greedy cheapest immediate edge:** It can block a much cheaper remaining tour; future cost must be included through DP.
- **Closing edge:** The base case must add the transition back to index 0.
- **n equals two:** Only one cycle order beginning with 0 exists, and the recurrence handles it directly.
- **Tied optimal next choices:** Ascending iteration and the first feasible choice enforce lexicographic minimality.
- **nums is a permutation:** Values are within 0 through $n-1$, but the DP treats transition costs exactly as defined rather than exploiting a nonexistent symmetric metric.
- **Asymmetric transition costs:** In general, `abs(a - nums[b])` differs from `abs(b - nums[a])`, so reversing a cycle need not preserve score.
- **Bit-test precedence:** The compact XOR condition is correct in Python, though explicit equality to zero would be easier to read.
- **Input preservation:** The method builds a separate result list and does not reorder `nums`.

## General

**One modified number can satisfy several targets at once.** A number is a multiple of every target in a subset exactly when it is a multiple of their least common multiple. If subset $T$ has

$$
L_T=\operatorname{lcm}(t\in T),
$$

then raising a value $v$ to the next multiple of $L_T$ costs

$$
(-v)\bmod L_T.
$$

This remainder expression is zero when $v$ is already divisible by $L_T$; otherwise it equals $L_T-(v\bmod L_T)$, the smallest nonnegative increment reaching a multiple.

The target count is at most four, so a bit mask can represent which target requirements are already covered.

**Precompute every subset LCM.** `full_mask` has one bit per target. `subset_lcm[mask]` stores the LCM of targets selected by `mask`. For a nonzero mask, the source extracts one set bit, removes it, and computes

`lcm(subset_lcm[mask ^ bit], target[index])`.

This builds all $2^m$ values from smaller masks, with the empty subset initialized to LCM identity one.

**Define DP over processed input elements.** `dp[covered]` is the minimum increments spent after some prefix of `nums` such that every target bit in `covered` has a multiple among the processed, possibly modified numbers. `dp[0] = 0` and all other states start at infinity.

For each `value`, `next_dp = dp.copy()` represents skipping modification of this number for coverage purposes. Even an unchanged number that already covers targets is also represented when a subset transition has zero increment.

From each reachable `covered` mask, the algorithm enumerates every nonempty subset of still-uncovered targets:

`remaining = full_mask ^ covered`.

Because `covered` contains only bits from `full_mask`, XOR here is equivalent to set difference. The standard update

`subset = (subset - 1) & remaining`

visits every nonempty submask.

For one subset, raising `value` to the next multiple of `subset_lcm[subset]` makes this single number satisfy all those targets. The transition updates `covered | subset` with the old cost plus the required increment.

**Why considering only uncovered targets is sufficient.** A number may also be divisible by targets already covered, but covering them again changes no state benefit. If an optimal modified value covers a mixture of old and new targets, its LCM may be larger than necessary; dropping already-covered requirements never increases the increment and preserves all needed coverage. Thus some equally good or better transition uses only the newly covered subset.

For `nums = [8,4]` and `target = [10,5]`, the subset containing both targets has LCM $10$. Raising $8$ to $10$ costs $2$ and moves directly from mask zero to the full mask, explaining why one value can satisfy both requirements.

**Why each input value is used at most once.** All transitions for one value read from the old `dp` and write into `next_dp`. They never chain from another state newly written for that same value. This prevents assigning two different final multiples to one array element. After all its alternatives are considered, `dp = next_dp` advances to the next element.
Every transition describes a legal decision: leave the value alone or increment it once to a multiple covering the chosen targets. Therefore, every finite DP cost is achievable.

Conversely, take an optimal assignment for a prefix. Consider its last processed value. The set of newly satisfied targets assigned to that value is some subset of the remaining bits before it; making the value the smallest suitable common multiple costs no more than its chosen final increment. The DP enumerates that transition from the optimal preceding state. Induction proves `dp[full_mask]` is the global minimum.

The large infinity sentinel safely exceeds any realistic answer and is used only to mark unreachable states; Python integers avoid overflow in LCM and cost arithmetic.

## Complexity detail

Let $m=\lvert\texttt{target}\rvert\le4$ and $n=\lvert\texttt{nums}\rvert$. Subset LCM precomputation costs $O(m2^m)$ in the manifest model.

For one input value, the total number of pairs `(covered, subset of remaining)` is $O(3^m)$: each target bit is either already covered, newly covered by this value, or still uncovered. Thus total time is $O(m2^m+n3^m)$.

The two DP arrays and LCM table each contain $2^m$ entries. Auxiliary space is $O(2^m)$, matching the manifest.

## Alternatives and edge cases

- **Assign one target per number:** This misses savings when one LCM multiple satisfies several targets.
- **Brute-force final values:** Multiples are unbounded. The next multiple of the relevant LCM is always the cheapest useful choice.
- **Recursive memoization:** It can use the same index-and-mask state but may inspect equivalent subset choices; iterative DP makes one-use-per-number explicit.
- **Already divisible:** `(-value) % multiple` is zero, so existing multiples are recognized without a branch.
- **Duplicate targets:** Separate bits may share a value, and their subset LCM remains that value. One number can cover both bits at zero additional conceptual cost.
- **Target value one:** Every integer is already its multiple, so transitions containing that target can cost zero.
- **Skipping a number:** Copying `dp` preserves all states even when modifying the current value is unhelpful.
- **One target:** The DP reduces to choosing the array value needing the fewest increments to its next target multiple.
- **Enough input values:** The constraint guarantees at least as many numbers as targets, but the algorithm can still cover several targets with one number.
- **No decrements:** The modulo formula deliberately chooses the next multiple at or above `value`, never a smaller one.

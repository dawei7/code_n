## General

**A choice from one pile must be a prefix**

Coins can be removed only from the top of a pile. Since `piles[i]` lists its coins from top to bottom, taking `h` coins from that pile means taking exactly its first `h` values. It is impossible to take a deeper coin while leaving a coin above it.

Therefore, the meaningful decisions for one pile are not arbitrary subsets. They are the prefixes of lengths zero through the pile's length. For a pile `nums`, define its prefix value

$$
P[h] = \sum_{t=0}^{h-1} \texttt{nums}[t],
$$

with `P[0] = 0`. Choosing option `h` spends `h` of the wallet's coin capacity and contributes `P[h]` value.

The exact solution constructs these values with `s = list(accumulate(nums, initial=0))`. The initial zero is crucial: it represents taking no coins from the current pile. If `nums = [1, 100, 3]`, then `s = [0, 1, 101, 104]`. The tempting value `100` alone does not appear because it cannot be reached without first removing the top coin worth `1`.

**Dynamic-programming state used by the code**

Let `f[i][j]` be the maximum total value obtainable by taking at most `j` coins from the first `i` piles. The words “at most” accurately describe the exact zero-initialized implementation. A state for a capacity that the first `i` piles cannot fill still has a meaningful value: it is the best value using however many coins are available up to that limit.

The table has `n + 1` rows and `k + 1` columns:

`f = [[0] * (k + 1) for _ in range(n + 1)]`.

Row zero means no piles have been considered. With no piles, the only obtainable value is zero regardless of the allowed capacity, so the all-zero base row correctly represents `f[0][j] = 0`.

Although the variant summary calls this an exact-count and rolling state, the stored Python code does not roll the rows and its zero initialization naturally gives an at-most-capacity interpretation. This distinction does not change the final answer because every coin value is positive and at least `k` coins exist overall. It does affect how intermediate states and space usage should be explained.

**Combine one pile with all earlier piles**

The outer loop `for i, nums in enumerate(piles, 1)` visits piles in order and numbers DP rows starting at one. For a capacity `j` from zero through `k`, the inner loop considers every prefix option `(h, w)` from `s`, where `h` is the number of coins taken from the current pile and `w = P[h]` is their total value.

Taking `h` current coins leaves capacity `j - h` for the previous `i - 1` piles. The best compatible earlier value is already stored in `f[i - 1][j - h]`. The combined candidate is

$$
\texttt{f}[i-1][j-h] + P[h].
$$

The update

`f[i][j] = max(f[i][j], f[i - 1][j - h] + w)`

keeps the best candidate among all feasible prefix lengths. When `h = 0`, `w = 0`, so the candidate copies the best result that ignores the current pile. Thus, a pile never has to contribute a coin.

Prefix lengths in `s` grow in ascending order because `enumerate` begins at zero. Once `j < h`, taking that prefix would exceed the capacity, and every later prefix is even longer. The `break` safely stops the inner loop.

**Why the recurrence covers every legal selection**

Consider any legal selection using at most `j` coins from the first `i` piles. It takes some number `h` from pile `i - 1`. The top-only rule means those coins must be exactly the length-`h` prefix, worth `P[h]`. After removing them, the rest of the selection uses at most `j - h` coins from the first `i - 1` piles, so its earlier value cannot exceed `f[i - 1][j - h]`. The transition for that same `h` produces a value at least as good as the chosen selection.

Conversely, every transition candidate is legal. The state `f[i - 1][j - h]` comes from the earlier piles, and the prefix `P[h]` comes from a different current pile. Their coin counts sum to at most `j`, and the current coins respect the top-to-bottom removal rule. Thus, the recurrence never invents an unreachable value.

Starting from the valid all-zero base row, these two directions show inductively that each completed row holds the best value for its first `i` piles and every capacity `j`.

**Why an at-most state returns an exactly-`k` answer**

The problem requires exactly `k` coins, while the implementation stores the best value for at most `k`. This is safe because all denominations are positive and the input guarantees that the piles contain at least `k` coins in total.

Suppose an allegedly optimal at-most-`k` selection used fewer than `k` coins. Since at least one additional accessible coin remains somewhere, it can be taken after removing any necessary coins above it; more directly, a legal selection of `k` total coins exists because one may distribute prefix lengths across the piles until their total is `k`. Extending from fewer coins by taking the next top coin of a nonempty remaining suffix adds a strictly positive value. Therefore, a solution using fewer than `k` coins cannot be optimal for capacity `k`. The maximum at-most value at `f[n][k]` is attained with exactly `k` coins.

The positivity guarantee is essential to this bridge. If negative-value coins were permitted, leaving capacity unused could be better than taking exactly `k`, and zero-initialized at-most states would not implement the required contract. Here every `piles[i][j] >= 1`, so the final return is sound.

**Walk through the central choice**

For `piles = [[1, 100, 3], [7, 8, 9]]` and `k = 2`, the first pile offers prefix options `(0, 0)`, `(1, 1)`, and `(2, 101)` within the capacity. After its row, `f[1][2] = 101`.

For the second pile, capacity two considers taking zero current coins and retaining `101`, taking one current coin worth `7` plus the best prior capacity one, or taking two current coins worth `15` plus prior capacity zero. The maximum remains `101`. The DP correctly sees that reaching the buried `100` requires spending both coin choices on the first pile.

**What the code stores and returns**

Every pile gets its own row, and rows are never overwritten. After all `n` piles are processed, `f[n][k]` represents the maximum value using at most `k` coins from all piles, which equals the required exact-`k` value by positivity. The method returns that single cell.

The implementation computes a fresh prefix list for one pile at a time. It does not store which `h` produced each maximum, so it returns only the value, not the chosen coins. That is exactly what the function contract requests.

## Complexity detail

Let

$$
C = \sum_{i=0}^{n-1} \lvert \texttt{piles}[i] \rvert
$$

be the total number of coins. Constructing all per-pile prefix lists over the course of the outer loop takes `O(C)` time.

For a pile containing `c_i` coins, each of the `k + 1` capacities considers at most `c_i + 1` prefix lengths. Summed across all piles, this is

$$
O\left(\sum_i (k+1)(c_i+1)\right).
$$

Every pile is nonempty, so `n \le C`. The expression simplifies to `O(kC)` under the problem constraints. The `O(C)` prefix construction is dominated by this bound. Thus, the exact solution's time complexity agrees with the manifest's `O(k * C)` declaration.

The exact Python solution allocates an `(n + 1)` by `(k + 1)` table, requiring `O(nk)` space. Its temporary prefix list uses `O(c_{\max})` space for the largest pile, which is at most `O(C)`. Peak auxiliary storage is therefore `O(nk + c_{\max})`, commonly stated as `O(nk + C)`.

The manifest states `O(k)` space and describes a rolling state, but this particular stored implementation does not perform that optimization. It reads only row `i - 1` while writing row `i`, so it could be rewritten with two length-`k + 1` rows for `O(k)` DP storage, but that is not what the exact solution file currently executes.

## Alternatives and edge cases

- **Two rolling DP rows:** Because row `i` depends only on row `i - 1`, retain a previous and current array and discard older rows. This preserves `O(kC)` time and reduces DP storage to `O(k)`; it matches the manifest claim but differs from the exact two-dimensional code explained above.
- **One in-place DP row:** Processing capacities in descending order can sometimes implement zero-one knapsack, but each pile offers mutually exclusive prefix choices. It requires careful use of the pre-pile row so two prefixes of the same pile are not combined; two separate rolling rows are clearer.
- **Top-down memoization:** Recursively choose a prefix length for each pile and cache states by pile index and remaining capacity. It evaluates the same recurrence with `O(nk)` memo storage but adds recursion overhead and can approach Python's recursion-depth limit when `n` is large.
- **Greedily take the currently largest top coin:** A small top coin may unlock a very valuable deeper coin, as `[1, 100, 3]` demonstrates. Judging only currently exposed values misses the value of committing to a prefix.
- **Treat all coins as freely selectable:** Sorting every denomination and taking the largest `k` violates pile order because a deep coin cannot be removed before all coins above it.
- **Take zero from a pile:** The initial prefix sum and `h = 0` transition are necessary. Some piles may be entirely skipped in an optimal distribution.
- **Capacity zero:** Every state `f[i][0]` stays zero because only `h = 0` is feasible.
- **Exactly all available coins:** When `k = C`, every pile must be exhausted, and the result is the sum of every denomination. The recurrence can select each full prefix.
- **One pile:** The only legal exact-`k` choice is its first `k` coins; the prefix enumeration selects that value.
- **Many one-coin piles:** Each pile has only options zero and one, reducing the recurrence to a familiar zero-one knapsack over positive coin values.
- **Large denomination behind small coins:** Prefix sums preserve the unlocking cost. The DP can choose the whole prefix when its combined value justifies consuming several of the `k` slots.
- **Positive-value assumption:** It guarantees the final at-most-capacity optimum uses exactly `k` coins. With zero or negative denominations, the DP state would need explicit reachability for exact counts.
- **Impossible intermediate exact counts:** Early rows may not contain `j` coins in total. Their zero-initialized entries are still valid under the at-most interpretation and can safely feed later transitions.
- **No reconstruction:** The table stores values only. If the actual coin choices were required, predecessor choices or a backward comparison pass would be needed, increasing bookkeeping.

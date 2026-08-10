## General

The task asks for the number of **combinations**, not the number of sequences. For example, using a coin of value one and then a coin of value two describes the same combination as choosing the two first and the one second. A correct dynamic program must therefore count each multiset of coins exactly once.

Let `m = len(coins)` and let `n = amount`. The solution builds a table `f` with `m + 1` rows and `n + 1` columns. Its central meaning is:

`f[i][j]` is the number of combinations that make total `j` using only the first `i` coin denominations.

This state definition deliberately restricts which denominations are available. That restriction creates a canonical ordering: a combination is counted when the algorithm considers its highest-indexed denomination, rather than once for every order in which its coins could be selected.

**Why the table begins with `f[0][0] = 1`.** With zero denominations, there is one way to form amount zero: choose no coins. This empty combination is a real counting base case. It is the starting point from which combinations such as one copy of a coin are constructed.

Every other entry in row zero remains zero. With no denominations, no positive amount can be formed. The table initialization already provides those impossible-state values, so no additional loop is needed.

**Add one denomination at a time.** The outer loop uses `enumerate(coins, 1)`. Therefore `i` ranges from one through `m`, and `x` is the newly available coin value `coins[i - 1]`. During this iteration, row `i - 1` is already complete and row `i` is being built.

For each target `j` from zero through `n`, every valid combination belongs to exactly one of two disjoint groups:

- it uses zero copies of coin `x`;
- it uses at least one copy of coin `x`.

The combinations in the first group use only the previous `i - 1` denominations. Their count is `f[i - 1][j]`, so the code first assigns:

`f[i][j] = f[i - 1][j]`.

For the second group, remove one copy of `x` from each combination. The remainder has total `j - x` and may still use any of the first `i` denominations, including more copies of `x`. This gives a one-to-one correspondence with the combinations counted by `f[i][j - x]`. When `j >= x`, the code adds that value:

`f[i][j] += f[i][j - x]`.

Notice that this second reference stays in the **same row**. That is precisely what models an unlimited supply of the current coin. If it referred to row `i - 1` instead, the current coin could be used at most once.

The inner loop moves `j` upward. Consequently, `f[i][j - x]` has already been computed when it is needed. An increasing amount order is essential for unbounded use; moving downward would preserve the old-row behavior and turn the update into a zero-or-one coin calculation.

**Why combinations are not double-counted.** At row `i`, the two groups are mutually exclusive because a combination either contains coin `x` or does not. Removing one `x` from the second group is reversible: add that coin back to recover the original combination. Thus the recurrence neither loses nor duplicates a combination.

The denomination loop also gives every combination one representation independent of selection order. For `coins = [1, 2]` and amount three, the combination containing one one and one two is introduced through the row for denomination two. It is not separately counted as “one then two” and “two then one,” because the state stores counts by allowed denomination set rather than by the last chronological choice.

**Small trace for `amount = 5` and `coins = [1, 2, 5]`.** After processing coin one, every amount from zero through five has one combination, made entirely from ones. Processing coin two adds another way for amount two, another for amount three, two additional ways for amount four, and two for amount five. Before coin five, `f[2][5]` is three. At `j = 5`, the new coin contributes `f[3][0] = 1`, representing the single coin five, so the final count becomes four.

The final cell `f[m][n]` uses all denominations and asks for exactly the requested amount, so it is returned. If no combination exists, every transition leading to that cell contributes zero and the result naturally remains zero.

The case `amount = 0` also follows directly from the state. Choosing no coins is one valid combination regardless of the available denominations. For each row, the “do not use `x`” assignment copies the preceding row's one into column zero, while the use-current-coin branch is impossible because every coin value is positive.

The recurrence is correct by progressing through the coin rows. Row zero has the stated counts. Assuming row `i - 1` is correct, partitioning row `i`'s combinations by whether they use `x` gives exactly the two recurrence terms, and their one-to-one interpretations prove every cell in row `i`. Repeating this argument reaches the returned full table cell.

## Complexity detail

Let $C$ be the number of coin denominations and $A$ be `amount`. The table contains $(C+1)(A+1)$ cells. The nested loops fill $C(A+1)$ of them, doing constant work per cell, so the running time is $O(CA)$.

The exact source allocates the full two-dimensional table, so its space consumption is $O(CA)$, not the $O(A)$ bound shown in the optimal manifest. The recurrence can be compressed to one row because it needs only the preceding row's current amount and the current row's smaller amount, but this particular implementation retains all rows. The final numeric answer is guaranteed to fit in a signed 32-bit integer, although intermediate storage in Python uses arbitrary-precision integers.

## Alternatives and edge cases

- **One-dimensional dynamic programming:** Initialize `dp[0] = 1`, loop over coins outside, and loop amounts upward inside. It preserves the same recurrence while reducing storage to $O(A)$ and matches the manifest's space claim.
- **Amount-first loop order:** Updating coins inside an outer amount loop counts different orders as distinct sequences, so it solves a permutation-counting problem rather than this combination problem.
- **Top-down memoization:** A state can choose to skip the current denomination or use it and remain at the same denomination. It has the same state count but adds recursion overhead and usually retains $O(CA)$ memo space.
- **Two-dimensional table:** It uses more memory than necessary, but exposes the denomination boundary explicitly and makes the no-current-coin and use-current-coin terms easy to verify.
- **Zero amount:** The empty choice is exactly one combination, represented by `f[0][0] = 1` and copied down column zero.
- **Coin larger than the current amount:** The condition `j >= x` fails, so only combinations that omit that coin are copied.
- **Coin larger than the requested amount:** It never contributes to any column, but does not invalidate combinations formed from other coins.
- **No achievable combination:** All contributing predecessor cells are zero, so the returned cell is zero without special handling.
- **Unique denominations:** The source guarantee prevents two equal-valued entries from being treated as separate coin types and artificially duplicating identical combinations.
- **Unlimited supply:** Referencing `f[i][j - x]` in the same row is the exact detail that permits repeated copies of `x`.

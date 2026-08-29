## General

**Combine independent tosses without enumerating outcomes**

Each coin has two outcomes, so explicitly listing all results would create \(2^n\) sequences. The task asks only for the probability of an exact head count, which means many sequences can be summarized by how many coins have been processed and how many heads they produced.

The table `f` has `n + 1` rows and `target + 1` columns. Its state is:

> `f[i][j]` is the probability that exactly `j` heads appear among the first `i` coins.

Before tossing any coins, getting zero heads is certain, so `f[0][0] = 1`. Getting a positive number of heads from zero coins is impossible, and those cells remain at their initialized zero.

**Split the next result into tail and head cases**

The loop `for i, p in enumerate(prob, 1)` treats `p` as the head probability of coin `i`, using one-based `i` for the table row.

To finish with exactly `j` heads after this coin, there are two mutually exclusive possibilities:

- The current coin is tails, with probability \(1-p\), and the previous \(i-1\) coins already had `j` heads.
- The current coin is heads, with probability \(p\), and the previous coins had `j - 1` heads.

Because tosses are independent, the probability along each case is a product. Because the cases cannot both happen on the same toss, their probabilities are added:

\[
f[i][j]
=(1-p)f[i-1][j]
+p f[i-1][j-1].
\]

For `j == 0`, the head case would ask for \(-1\) previous heads and is impossible. The exact code first assigns the tail contribution and adds the head contribution only under `if j`.

**Why the inner range stops at the possible count**

After \(i\) coins, more than \(i\) heads is impossible. The loop therefore reaches only `min(i, target)`. The expression `range(min(i, target) + 1)` includes zero and the upper feasible count.

Cells for impossible larger counts stay zero. This bound saves some recurrence work early in the table, although the full rectangular table has already been allocated.

**A small trace**

Suppose `prob = [0.4]` and `target = 1`. The base row is `[1, 0]`. For the coin with head probability 0.4:

- `f[1][0] = 0.6 * f[0][0] = 0.6`;
- `f[1][1]` receives zero from the tail case and \(0.4\cdot f[0][0]=0.4\) from the head case.

The returned value is 0.4.

For five fair coins and target zero, each row’s zero-head probability is multiplied by 0.5. After five rows it is \(0.5^5=0.03125\).

**Why the recurrence counts the exact probability**

Assume row \(i-1\) correctly describes the distribution of head counts for the first \(i-1\) coins. Every outcome of the first \(i\) coins with exactly \(j\) heads ends either in a tail or a head.

Removing a final tail leaves an outcome with \(j\) heads and multiplies its probability by \(1-p\). Removing a final head leaves an outcome with \(j-1\) heads and multiplies by \(p\). These groups are disjoint and cover all outcomes with \(j\) heads, so their sum is exactly `f[i][j]`. Induction from the base row establishes the whole table, and `f[n][target]` is the requested probability.

**Deterministic probabilities fit naturally**

If `p == 0`, the head contribution is zero and the distribution carries forward through the tail term. If `p == 1`, the tail contribution is zero and every reachable probability shifts one head to the right. No special branches are required.

**Floating-point behavior**

The table stores Python floating-point values. Repeated multiplication and addition may introduce small rounding error, but the problem accepts a tolerance of \(10^{-5}\). Probabilities remain between zero and one mathematically, though tiny representation deviations are possible in general floating arithmetic.

**The exact source uses the full table**

Only row \(i-1\) is required to calculate row \(i\), so the recurrence can be compressed. The shipped solution does not perform that compression: it creates all `n + 1` rows and retains them until return. Its explanation and complexity must reflect that actual allocation.

## Complexity detail

Let \(n=\lvert\texttt{prob}\rvert\) and \(t=\texttt{target}\). Constructing the table initializes \((n+1)(t+1)\) entries, which is \(O(nt)\) time and space. Filling reachable cells also takes at most \(O(nt)\) time. Total time is \(O(nt)\).

The exact two-dimensional table uses \(O(nt)\) auxiliary space. Loop variables are constant-sized. The manifest’s \(O(t)\) space describes a one-dimensional rolling implementation, not this shipped source.

## Alternatives and edge cases

- **One-dimensional DP:** Store probabilities for zero through `target` heads and update `j` from high to low. This preserves \(O(nt)\) time while reducing auxiliary space to \(O(t)\), matching the manifest.
- **Two rolling rows:** Keep the previous and current distributions. This also uses \(O(t)\) space and has a simpler update order than in-place one-dimensional DP.
- **Top-down memoization:** Cache states by coin index and remaining heads. It has the same \(O(nt)\) state count but adds recursion depth.
- **Exponential outcome enumeration:** Multiplying probabilities along every toss sequence is conceptually direct but costs \(O(2^n)\).
- **Target zero:** Only the all-tails outcome qualifies. The `j == 0` recurrence multiplies all tail probabilities correctly.
- **Target equals \(n\):** Only the all-heads outcome qualifies. Unreachable states stay zero until enough coins have been processed.
- **Probability zero:** That coin always contributes tails and cannot increase the head count.
- **Probability one:** That coin always contributes heads and shifts the distribution by one.
- **Impossible head counts in early rows:** The bounded inner loop skips them, leaving their preinitialized values at zero.
- **Numerical precision:** The accepted tolerance accommodates ordinary floating-point rounding. Arbitrary rounding during intermediate steps should be avoided.
- **Full-table memory:** For large \(n\) and \(t\), the two-dimensional list is materially larger than necessary even though the recurrence is optimal in time.

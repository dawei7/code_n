## General

**Keeping only the information that future numbers need**

The task may choose any subset, so there are exponentially many subsets in principle. Future decisions do not need to know the exact membership of an earlier subset, however. They need only two facts: its current sum and that sum's remainder modulo three. Among all subsets with the same remainder, only the one with the largest sum can ever be useful. If two partial subsets both have remainder one and one sum is larger, adding the same future numbers preserves their equal remainders and keeps the larger sum ahead.

This dominance rule reduces the state space to three possibilities per processed prefix. The exact source defines `f[i][j]` as the greatest sum obtainable from the first `i` numbers with remainder `j` modulo three.

Before processing anything, the empty subset has sum zero and remainder zero, so `f[0][0] = 0`. No subset of zero elements can have remainder one or two. Those impossible states are initialized to negative infinity with `[-inf] * 3`. Negative infinity is a useful sentinel because it can never win a maximum against a real nonnegative sum, and adding a finite input to it remains negative infinity.

**Deriving the take-or-skip transition**

When processing value `x`, there are exactly two choices for a subset ending with remainder `j`.

First, skip `x`. The best sum with remainder `j` remains `f[i - 1][j]`.

Second, take `x`. The previous subset must have a remainder that becomes `j` after adding `x`. If that previous remainder is $p$, then

$$
(p+x)\bmod 3=j.
$$

Solving modulo three gives $p=(j-x)\bmod 3$. Therefore the take candidate is `f[i - 1][(j - x) % 3] + x`. The code chooses the larger candidate:

`f[i][j] = max(f[i - 1][j], f[i - 1][(j - x) % 3] + x)`.

Python's modulo operator returns a nonnegative result for modulus three, so even when `j - x` is negative, the expression is a valid index zero, one, or two.

The loop `enumerate(nums, 1)` intentionally starts `i` at one. This lets `x` denote the next input number while row `i - 1` remains the fully computed previous prefix. All three entries of a new row read only from the preceding row, so choosing `x` once can never accidentally feed another state in the same iteration and choose it twice.

**Tracing how states evolve**

Suppose the only input is `[4]`. Initially the row is `[0, -inf, -inf]`. Skipping four keeps remainder-zero sum zero. Taking four from the remainder-zero state creates sum four with remainder one. No remainder-two subset becomes reachable. The final remainder-zero answer is zero, correctly representing the choice to select nothing.

For a slightly richer prefix `[1, 2]`, after processing one, the useful states are zero for remainder zero and one for remainder one. When two arrives, taking it alone creates remainder two with sum two, while taking it after the remainder-one sum creates remainder zero with sum three. Thus the state for remainder zero becomes three. The DP never enumerates explicit subset lists; it retains only the best representative of each remainder class.

For the full first example, values divisible by three can strengthen a state without changing its remainder, while values with remainders one and two move between the three columns. After every number is processed, `f[n][0]` is the largest reachable multiple of three, which is eighteen.

**Why retaining only the maximum is safe**

The correctness argument follows the prefix definition. The initialization lists exactly the subsets of an empty prefix. Assume row `i - 1` correctly stores the best sum for each remainder. Every subset of the first `i` values either excludes the new value `x` or includes it. Excluding it is covered by the skip candidate. Including it leaves, after removing `x`, a subset of the first `i - 1` values with remainder `(j - x) % 3`, covered by the take candidate.

Conversely, both candidates construct valid subsets of the first `i` values with remainder `j`. Taking their maximum therefore stores exactly the best such sum. By induction, the final row is correct for the entire array. A divisible sum has remainder zero, so returning `f[n][0]` answers the task.

All input values are positive, but the empty subset remains necessary. It guarantees that a valid result always exists and that the answer is zero when no nonempty subset has a sum divisible by three.

## Complexity detail

Let $n$ be the length of `nums`. The table has $n+1$ rows and exactly three columns. The nested loops compute three constant-time transitions for each of the $n$ values, so total time is $O(3n)=O(n)$.

The exact source allocates the full table with `n + 1` rows. It therefore uses $O(3(n+1))=O(n)$ auxiliary space. This differs from the variant manifest's $O(1)$ space claim. Because row `i` depends only on row `i - 1`, a different implementation could retain two three-entry rows or copy one three-entry state per input and achieve $O(1)$ space, but the shipped source does not perform that compression.

Each stored entry is either negative infinity or an integer sum. Under a fixed-width arithmetic model, table entries occupy constant space. Python integers grow with the number of bits in the sum, but the conventional problem analysis treats arithmetic on constraint-bounded sums as constant time.

The returned value uses no additional output structure. At the maximum $n=40{,}000$, the exact table contains about $120{,}003$ numeric references, which is linear and practical.

## Alternatives and edge cases

- **Rolling three-state DP:** Keep only the previous and current three remainders. It uses the identical recurrence and $O(n)$ time while reducing auxiliary space to $O(1)$.
- **In-place update with a snapshot:** Copy the three current values before processing each `x`, then update from the snapshot. Updating directly from already changed entries can reuse the same number more than once and is incorrect.
- **Greedy removal from the total:** Because every number is positive, one can sum everything and remove the cheapest remainder-fixing choice: one remainder-one value or two remainder-two values, and symmetrically for total remainder two. Tracking the two smallest values of each remainder gives $O(n)$ time and $O(1)$ space, but its proof is more specialized.
- **Sorting remainder groups:** Sorting values by remainder makes the greedy removal choices obvious but costs $O(n\log n)$ time and $O(n)$ space.
- **No positive divisible subset:** The empty subset yields zero, so the method never returns negative infinity for remainder zero.
- **All values divisible by three:** Every value can be included, and the remainder-zero state accumulates the total sum.
- **Single value not divisible by three:** Skipping it preserves zero as the answer.
- **Impossible predecessor states:** Adding `x` to `-inf` remains `-inf`, preventing an unreachable remainder from becoming a fake finite result.
- **Python modulo behavior:** `(j - x) % 3` is always zero, one, or two in Python. Languages with negative remainders may need normalization.
- **Positive-input assumption:** The recurrence itself also handles negative values, but the simple greedy alternatives rely strongly on every input being positive.

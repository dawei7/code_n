## General

**Model both endpoint choices**

At every operation, the current multiplier is fixed, but the chosen number may come from the left or right end of the remaining `nums` interval. A locally larger product is not necessarily globally best because removing one endpoint exposes a different value for later multipliers.

The exact solution uses cached recursion to explore both choices while merging repeated subproblems.

Its helper `f(i, j, k)` means: the maximum additional score obtainable when the remaining usable interval is `nums[i..j]` and the next multiplier is `multipliers[k]`.

**Use a zero base after all operations**

If `k >= m`, all multipliers have been used and no further score is added, so the helper returns zero.

The source also returns zero when `i >= n` or `j < 0`. Given the contract `n >= m` and legal transitions, these array-exhaustion checks are normally redundant before all multipliers are used, but they safely guard indexing.

The score may be negative, so zero is appropriate only after the required operation suffix is empty. Intermediate states do not compare against zero as an option to stop early; exactly `m` operations are forced through recursion.

**Take the current number from the left**

Choosing `nums[i]` contributes:

`nums[i] * multipliers[k]`.

That value is removed from the interval, so the next left boundary becomes `i + 1`. The right boundary stays `j`, and the next multiplier index is `k + 1`.

The complete left-choice score is:

`f(i + 1, j, k + 1) + nums[i] * multipliers[k]`.

**Take the current number from the right**

The symmetric choice contributes `nums[j] * multipliers[k]` and leaves interval `i..j-1`:

`f(i, j - 1, k + 1) + nums[j] * multipliers[k]`.

The helper returns the maximum of the left and right totals. These are exhaustive because the rules permit only the two current endpoints.

Negative values do not change the recurrence. A negative multiplier may make a negative endpoint desirable, and future multipliers can reverse which exposure is beneficial. Evaluating both branches captures all sign combinations.

**Why caching reduces the choice tree**

Without `@cache`, each of `m` levels branches twice, creating $2^m$ paths. Many paths reach the same remaining interval and multiplier index.

For example, choosing left then right leaves the same interval as choosing right then left after two operations, though the immediate scores differed. The optimal future value from that interval is identical and should be computed once.

The cache keys results by the argument triple `(i, j, k)`. A later call with the same state returns its stored integer immediately.

**Only two state dimensions are independent**

After `k` operations, suppose `i` numbers were taken from the left. Then `k - i` were taken from the right, so:

$$
j=n-1-(k-i).
$$

Thus reachable `j` is determined by `i` and `k`. Although the exact helper uses three parameters, it reaches only a triangular $O(m^2)$ set of meaningful states rather than $O(nm^2)$ arbitrary triples.

This relationship is also why a bottom-up solution can use a two-dimensional table or a one-dimensional rolling array.

**Trace the first example**

For `nums = [1,2,3]` and multipliers `[3,2,1]`, state `f(0,2,0)` compares taking one for score three against taking three for score nine.

The right choice leads to `f(0,1,1)`, which can take two from the right for four, then one for one. That path totals fourteen.

The recursion still evaluates left-based alternatives before taking the maximum, ensuring the result is proven rather than assumed from this positive example.

**Definition timing in Python**

The nested function is defined before local variables `n` and `m` are assigned in the surrounding method. Python closures resolve those names when the helper body executes, not when it is defined.

The first call occurs only after `n` and `m` have been assigned, so the references are valid.

**Why the recursion is correct**

For a state after all operations, zero additional score is exact. For any earlier state, every legal completion begins by choosing either the left endpoint or the right endpoint. The two recurrence branches add the correct current product and, by induction, the optimal future score for the resulting state.

Taking their maximum gives the optimal score for the current state. Therefore `f(0, n - 1, 0)` is the maximum score for the complete problem.

## Complexity detail

Let $m$ be the number of multipliers. Reachable states correspond to pairs `(k, i)` with `0 <= i <= k <= m`, so there are $O(m^2)$ states. Each is computed once and performs constant work besides two cached calls. Time complexity is $O(m^2)$, matching the manifest.

The `@cache` stores one result for each reachable argument triple, so exact memoization space is $O(m^2)$. Recursion depth is $O(m)$. Therefore the exact source's auxiliary-space bound is $O(m^2)$, not the manifest's stated $O(m)$.

An $O(m)$-space implementation requires bottom-up rolling DP that reuses one row. That optimization appears in the local editorial but is not present in this `solution.py`.

## Alternatives and edge cases

- **One-dimensional bottom-up DP:** Reuse the next operation row to achieve $O(m^2)$ time and $O(m)$ space, matching the manifest's target.
- **Two-dimensional bottom-up DP:** Avoid recursion with an explicit triangular table, using $O(m^2)$ space.
- **Uncached recursion:** It explores $2^m$ endpoint sequences and is infeasible for $m=300$.
- **Greedy current product:** It can expose poor endpoints for later multipliers and is not globally reliable.
- **All positive values and multipliers:** Greedy may look plausible, but DP remains necessary in general and still returns the best endpoint sequence.
- **Negative multiplier:** Pairing with a negative endpoint can create a positive contribution.
- **Exactly m operations:** No branch may stop early to avoid a negative product.
- **n greater than m:** Middle values can remain unused after all multipliers are consumed.
- **n equals m:** Every number is eventually selected, but multiplier-to-number order still depends on endpoint choices.
- **Equal endpoints:** Their current products tie, yet their future exposed intervals may lead to different results.
- **Single multiplier:** The recursion chooses the better product from the two endpoints.
- **Cached key redundancy:** `j` is derivable but still stored as part of each exact cache key.
- **Recursion depth:** At most 300 operation levels is typically manageable, though iterative DP removes stack dependence.
- **Input preservation:** Endpoint indices model removals without modifying `nums`.

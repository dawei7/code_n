## General

**A fruit has three mutually exclusive choices**

For each index `i`, a valid purchase plan may skip the fruit, buy it at full `price[i]`, or buy it once with one coupon for `price[i] // 2`. The total spending cannot exceed `maxAmount`, and at most `maxCoupons` discounted purchases are allowed.

The exact source uses top-down dynamic programming. Its cached state `dfs(i, j, k)` means:

“What maximum additional tastiness can be obtained from fruits `i` onward when `j` units of budget and `k` coupons remain?”

The initial call is `dfs(0, maxAmount, maxCoupons)`. When `i == len(price)`, no fruit remains, so the only possible additional tastiness is zero.

**Transition 1: skip the fruit**

The method begins with

`ans = dfs(i + 1, j, k)`.

Skipping spends nothing, uses no coupon, and gains no tastiness. Including it as the baseline is important because buying a fruit is optional. Even though tastiness is non-negative, a fruit may be unaffordable or may consume budget better reserved for a later, more valuable fruit.

**Transition 2: buy at full price**

If `j >= price[i]`, the fruit is affordable without a coupon. The candidate value is

`dfs(i + 1, j - price[i], k) + tastiness[i]`.

The remaining budget decreases by the full price, the coupon count stays unchanged, and the fruit's tastiness is added. Moving to `i+1` ensures this same fruit cannot be purchased again.

**Transition 3: buy with a coupon**

If `k` is nonzero and `j >= price[i] // 2`, the discounted purchase is affordable. The candidate becomes

`dfs(i + 1, j - price[i] // 2, k - 1) + tastiness[i]`.

Integer division implements the required rounding down. For an odd price such as 15, the coupon cost is 7, not 7.5 or 8. The condition checks the discounted cost rather than the original price, so a coupon can make an otherwise unaffordable fruit available.

The maximum over the three candidates is stored and returned. Although using a coupon on a zero-price fruit duplicates the no-coupon purchase while consuming a resource, taking a maximum makes the dominated choice harmless.

**Why the state contains enough information**

Future decisions depend on which fruit comes next, how much budget remains, and how many coupons remain. They do not depend on the detailed order of earlier purchases. Earlier choices affect the future only through `j` and `k`. This is the optimal-substructure property that makes the three-parameter state sufficient.

The `@cache` decorator prevents repeated computation. Many different purchase histories can arrive at the same triple `(i,j,k)`. Once the optimal continuation for that state is known, every history can reuse it.

**Why the recurrence is correct**

Take an optimal plan for state `dfs(i,j,k)`. Regarding fruit `i`, it must do exactly one of the three actions above: skip it, buy it fully, or buy it with a coupon. The latter two are included only when their budget and coupon requirements are satisfied. After that action, the remaining plan operates on fruit `i+1` with precisely the updated resources shown in the transition.

By definition, the corresponding recursive state returns the best continuation under those remaining resources. Thus each transition represents the best plan beginning with that action. Since every legal first action is considered, their maximum is optimal for the current state. The base case is trivially correct, and backward induction over `i` proves the initial result.

For `price = [10,20,20]`, `tastiness = [5,8,8]`, budget 20, and one coupon, one optimal branch buys the first fruit fully, leaving budget 10 and one coupon. It buys either later fruit with the coupon for 10, gaining total tastiness 13. The DP also considers buying one later fruit fully, skipping the first fruit, and every other feasible combination before choosing 13.

**The implementation differs from the manifest's storage description**

The local summary describes a descending iterative 0/1 knapsack with $O(kB)$ space. The protected file instead caches states for every fruit index. In the worst case, it can store $O(nkB)$ results, where $B=\texttt{maxAmount}$ and $k=\texttt{maxCoupons}+1$ as a count of possible coupon states. Its time bound matches the knapsack state count, but its space is not compressed to two dimensions.

The recursive form also uses up to $O(n)$ call-stack depth. With $n \le 100$, that depth is generally safe in Python.

## Complexity detail

Let $n$ be the number of fruits, $B=\texttt{maxAmount}$, and $K=\texttt{maxCoupons}$. There are at most

$$
(n+1)(B+1)(K+1)
$$

distinct cached states. Each performs at most three transitions and constant-time arithmetic, so time is $O(nBK)$, with the usual convention that adding one to each bounded dimension does not change the asymptotic expression.

The memoization cache can store $O(nBK)$ integers and tuple keys. The recursion stack adds $O(n)$ space, which is dominated when the state space is populated. Therefore the exact implementation uses $O(nBK)$ auxiliary space, not the manifest's $O(KB)$.

An iterative DP that processes fruits one at a time and updates coupon and budget dimensions in descending order can discard the index dimension and achieve $O(KB)$ space. Descending iteration is required there to prevent one fruit from being reused within its own update. The exact recursive code obtains the 0/1 guarantee instead by always advancing `i`.

## Alternatives and edge cases

- **Descending two-dimensional knapsack:** Maintain best tastiness by coupons used and budget spent, iterating both dimensions downward for each fruit. It matches the manifest's $O(nKB)$ time and $O(KB)$ space but requires careful separate full-price and coupon transitions.
- **Bottom-up DP with an index dimension:** Fill the same three-dimensional recurrence iteratively. It avoids recursion but retains $O(nKB)$ space unless layers are rolled.
- **Brute-force three choices per fruit:** Enumerating skip, full-price, and coupon choices directly takes up to $O(3^n)$ time. Memoization collapses histories that share remaining resources.
- **No coupons:** Only skip and full-price transitions are available, reducing the problem to ordinary 0/1 knapsack.
- **Zero budget:** Zero-priced fruits and fruits whose half price rounds to zero may still be purchased, so returning zero immediately would be incorrect.
- **Zero price:** A full-price purchase preserves budget. A coupon purchase also costs zero but wastes a coupon, so the maximum naturally prefers the no-coupon purchase unless both lead to an equal final result.
- **Zero tastiness:** Buying such a fruit cannot improve the objective and may consume resources. The skip transition ensures it need not be selected.
- **Odd price:** Coupon cost uses floor division exactly as required; price 15 becomes 7.
- **At most one purchase per fruit:** Every transition moves from `i` to `i+1`, so neither full-price nor coupon choices can revisit the same fruit.
- **At most one coupon per fruit:** The recurrence offers only one coupon transition for the current index, then advances.
- **Unused budget or coupons:** The goal maximizes tastiness rather than resource consumption. The DP may finish with either resource remaining.
- **Manifest mismatch:** The exact top-down cache retains the fruit-index dimension and therefore has $O(nBK)$ rather than $O(KB)$ auxiliary space.

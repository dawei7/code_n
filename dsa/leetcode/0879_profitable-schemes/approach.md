## General

Every crime has two effects: it consumes a fixed number of members and adds a fixed amount of profit. A scheme is a subset, so each crime can be either skipped or selected once. This is a constrained subset-counting problem, and the exact solution uses top-down dynamic programming with memoization.

The recursive state is `dfs(i, j, k)`:

- `i` is the index of the next crime to decide.
- `j` is the number of members already committed to selected crimes.
- `k` is the profit accumulated so far, capped at `minProfit`.

The return value is the number of valid ways to decide crimes from index `i` onward, given that current resource state.

**Why the profit is capped.** The requirement distinguishes only profit below the threshold from profit at least the threshold. Once accumulated profit reaches `minProfit`, its exact larger value cannot affect any future decision or final validity. Therefore the transition stores

```text
min(k + profit[i], minProfit)
```

instead of an unbounded sum. All profitable totals collapse into one state `k == minProfit`. This is both correct and essential for keeping the state space small.

For example, if the threshold is 5, profits 5, 8, and 100 are equivalent from the viewpoint of future validity: all have already satisfied the profit condition. They may still differ in which crimes produced them, but those distinct subsets are counted by separate recursive branches before their state results are combined.

**Skip the current crime.** Every state may exclude crime `i`. Skipping changes neither used members nor profit, so it contributes

```text
dfs(i + 1, j, k)
```

ways.

**Take the current crime when legal.** Selecting it is possible only if `j + group[i] <= n`. Members cannot participate in multiple crimes, so member requirements add across selected crimes, and the total may not exceed `n`. If legal, taking the crime contributes

```text
dfs(i + 1, j + group[i], min(k + profit[i], minProfit))
```

ways. Advancing `i` in both branches ensures no crime is selected twice.

The two branch counts are added because they describe disjoint subsets: one excludes crime `i` and the other includes it. No scheme can belong to both groups.

**Base case.** When `i >= len(group)`, every crime has received a decision. The subset is valid exactly when the capped profit equals `minProfit`. Member validity does not need another check because the take branch was allowed only while its total stayed at most `n`. The base returns one for a valid completed subset and zero otherwise.

This also handles `minProfit = 0` correctly. The initial state already has `k = 0 = minProfit`, so even the empty subset is profitable. Each legal combination of crimes is counted because all terminal states meet the capped-profit test.

**Why memoization is valid.** Different earlier subsets may reach the same triple $(i,j,k)$. Once there, the set of remaining crimes and all facts relevant to future choices are identical. The number of valid completions is therefore identical, so `@cache` can compute it once and reuse it.

Notice that memoization does not collapse the subsets themselves into one counted scheme. If two different earlier paths reach the same state, each caller adds the cached number of completions to its own branch total. The shared computation saves work while multiplicity is preserved by the recursion tree's additions.
At state $(i,j,k)$, every possible subset of remaining crimes either omits crime $i$ or includes it. The skip branch counts exactly the first group. If enough members remain, the take branch counts exactly the second group; otherwise that group contains no legal scheme. By induction on the number of undecided crimes, each recursive result counts all and only valid completions. The initial state $(0,0,0)$ therefore counts all profitable schemes.

The result is reduced modulo $10^9+7$ at every state. Modular addition preserves the final remainder, and early reduction prevents cached counts from growing unnecessarily large.

## Complexity detail

Let $m$ be the number of crimes, let $n$ be the member limit, and let $P=\texttt{minProfit}$. Possible states use $i$ in $0\ldots m$, `j` in $0\ldots n$, and capped `k` in $0\ldots P$. Each cached state performs constant work besides its recursive calls.

- **Time complexity:** $O(mn(P+1))$.
- **Space complexity of the exact cached solution:** $O(mn(P+1))$ for memoized states, plus $O(m)$ recursion depth.

The branch manifest's $O(n(P+1))$ space corresponds to a bottom-up formulation that rolls away the crime dimension. The exact `solution.py` retains `i` in every cache key, so its actual worst-case memory is three-dimensional rather than the rolling bound.

## Alternatives and edge cases

- **Bottom-up rolling DP:** Store counts by members used and capped profit, then process each crime in reverse state order. It reaches the same $O(mn(P+1))$ time and reduces space to $O(n(P+1))$, matching the manifest.
- **Full subset enumeration:** Trying all $2^m$ subsets becomes infeasible for 100 crimes and repeats the same resource states.
- **Track exact unbounded profit:** This creates unnecessary states. All profits at or above `minProfit` have identical future meaning and should be capped.
- **Iterate bottom-up states forward:** That can reuse the same crime multiple times in one processing pass. Reverse iteration is required for a subset choice when using one table.
- **`minProfit = 0`:** The empty subset is a valid scheme, as are all subsets satisfying the member limit. The capped initial state handles this naturally.
- **Crime requiring too many remaining members:** Its take branch is omitted, but its skip branch remains available.
- **Zero-profit crime:** Selecting it may create a distinct valid scheme even though `k` does not change. The include and exclude branches correctly count both choices.
- **Exactly `n` members:** The condition uses `<= n`, so consuming the complete available group is legal.
- **Profit exactly at the threshold:** It is capped to `minProfit` and accepted at the base.
- **Several paths to one state:** Caching shares their future calculation, while each incoming branch still contributes the number of completions separately.
- **Modulo arithmetic:** Counts, not scheme identities, are reduced. Addition modulo $10^9+7$ gives the required final remainder.
- **No profitable legal subset:** Every terminal branch returns zero, so the initial result is zero.

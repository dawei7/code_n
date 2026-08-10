## General

**Make one include-or-skip decision per index**

The array has at most 18 elements, so the exact solution explores the subset decision tree. At index $i$, it always explores the branch that excludes `nums[i]`. It explores the inclusion branch only when adding that value would not create a forbidden difference of $k$ with a value already selected.

Each index has its own decision even when values are equal. This is essential because subsets are distinguished by deleted indices.

**Track selected values with frequencies**

Counter `cnt` stores how many selected occurrences of each numeric value are currently present on the recursion path.

Before including value $x=\texttt{nums[i]}$, a forbidden pair could involve $x-k$ or $x+k$. The exact condition is

`cnt[x + k] == 0 and cnt[x - k] == 0`.

If both frequencies are zero, no already selected value differs from $x$ by exactly $k$, so inclusion is safe. If either is positive, including $x$ would immediately make the subset non-beautiful.

Because $k$ is positive, another selected copy of $x$ differs by zero and is allowed. The frequency count supports choosing multiple equal-valued occurrences correctly.

**Backtracking restores the path state**

For an allowed inclusion branch, the code increments `cnt[x]`, recursively processes the next index, and then decrements `cnt[x]`.

The decrement is necessary because after returning, recursion explores other branches in which this occurrence was not selected. Without restoration, selections from one branch would leak into another and falsely block values.

Counter entries whose count returns to zero remain in the Counter, but lookups test the numeric frequency, so zero-valued keys behave exactly like absent keys.

**Why only already selected values must be checked**

Every pair in a completed subset has a later-selected endpoint. When that endpoint is considered, the earlier endpoint is already represented in `cnt`. The include condition checks their possible difference.

If the condition passes at every inclusion, no forbidden pair exists in the completed subset. Conversely, any subset containing a forbidden pair would fail when the second of those two indices was considered, so that branch is never generated.

This proves pruning is exact: it removes all and only invalid subsets.

**Count leaves and remove the empty subset**

When `i >= len(nums)`, all index decisions have been made. Every surviving recursion path represents one beautiful subset, so `ans` increases by one.

The always-skip path represents the empty subset, which the problem excludes. Instead of subtracting at the return statement, the code initializes `ans = -1`. After all leaves are counted, this offset removes exactly the one empty subset.

For a one-element array, recursion has two leaves: skip and take. Starting at negative one and adding two yields one.

**Trace `[2,4,6]` with `k=2`**

If $2$ is selected, $4$ cannot later be selected because `cnt[4 - 2]` sees the chosen $2$. Value $6$ may still be selected because its forbidden neighbors are $4$ and $8$, neither chosen.

The valid nonempty leaves correspond to `[2]`, `[4]`, `[6]`, and `[2,6]`. All branches containing adjacent chain values $2,4$ or $4,6$ are pruned, giving answer four.

**Why checking both directions is needed**

The input is not sorted in the exact solution. A previously selected conflicting value may be $x-k$ or $x+k$ depending on encounter order.

If the array were sorted, only $x-k$ could have appeared earlier, but this DFS preserves input order and must check both.

**Exact implementation versus manifest**

The manifest describes grouping values by remainder modulo $k$ and applying weighted independent-set dynamic programming in $O(n\log n)$ time. The checked-in source does not group or sort. It performs exponential backtracking, which is viable only because $n\le18$.

The algorithm is still exact, but its complexity and teaching model must follow the recursion actually present.

## Complexity detail

In the worst case no conflicts occur, so both branches are explored at every index and there are $O(2^n)$ calls/leaves. Each call performs expected constant-time Counter operations, giving expected $O(2^n)$ time.

The recursion stack has depth $O(n)$, and the Counter stores at most $O(n)$ selected distinct values, so auxiliary space is $O(n)$. This differs from the manifest's polynomial-time grouped DP.

## Alternatives and edge cases

- **Remainder-chain DP:** Group equal values by remainder modulo $k$, sort each chain, and count independent selections in $O(n\log n)$ time, matching the manifest.
- **Enumerate masks then check pairs:** This also uses $2^n$ subsets but can spend $O(n^2)$ validating each; incremental Counter pruning is better.
- **Sort before backtracking:** Then only `x-k` needs checking, but sorting mutates input and does not change exponential worst-case size.
- **Duplicate values:** They may coexist because $k>0$, and each occurrence creates a distinct subset choice.
- **Single element:** Exactly one nonempty subset exists.
- **No conflicting pair anywhere:** Every nonempty subset is beautiful, giving $2^n-1$.
- **All values in a difference-`k` chain:** The recursion prunes adjacent-value combinations but permits values separated by multiples greater than one.
- **Empty subset:** Counted by the base case and canceled by initializing `ans=-1`.
- **Backtracking cleanup:** Decrementing the selected frequency is essential before sibling branches.
- **Manifest distinction:** The source is $O(2^n)$ recursion, not weighted chain DP.

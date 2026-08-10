## General

**Keep only the positions of the ones**

Swapping a one with an adjacent zero moves that one by exactly one index and costs exactly one move. The zeros do not need individual identities; they are simply the gaps through which selected ones travel.

The source builds

`arr = [i for i, x in enumerate(nums) if x]`,

so `arr[r]` is the original array position of the $r$-th one. These positions are strictly increasing. Let $m$ be `len(arr)`.

Any chosen group of $k$ ones can be considered in their left-to-right order because adjacent swaps do not require selected ones to cross. An optimal group can be taken as $k$ consecutive entries of `arr`: if a supposed selection skipped a one lying between two selected ones, that intervening one is already at least as well positioned to participate in the same consecutive block as an outer selected one. Thus the source checks every length-$k$ window of one positions.

**A consecutive target has fixed relative offsets**

Suppose one selected position is used as an anchor at array index `j`. If $x$ selected ones occupy the anchor and its left side, their target positions must be

$$
j-x+1,\;j-x+2,\;\ldots,\;j.
$$

If $y$ selected ones lie to the right, their targets must be

$$
j+1,\;j+2,\;\ldots,\;j+y.
$$

Together these form one uninterrupted block of $x+y=k$ positions. The source chooses

`x = (k + 1) // 2`

and

`y = k - x`.

Thus $x=\lceil k/2\rceil$ and $y=\lfloor k/2\rfloor$. For odd $k$, the anchor is the unique middle one. For even $k$, it is the left of the two middle ones.

**Why a median minimizes movement**

For a window of selected positions $p_r$, moving them into consecutive targets beginning at $T$ costs

$$
\sum_r \left|p_r-(T+r)\right|
=\sum_r\left|(p_r-r)-T\right|.
$$

The expression $p_r-r$ removes the one-position spacing that the final consecutive block must have. A sum of absolute deviations is minimized by a median of these adjusted values.

Because original one positions increase by at least one, the adjusted values `arr[r] - r` are non-decreasing. For an odd-size window, its middle adjusted value is the median. For an even-size window, any value between the two middle adjusted values is optimal; choosing the lower middle is valid. The source's anchor index `i` makes the target for `arr[i]` equal to its current position `j = arr[i]`, which corresponds exactly to choosing adjusted median `j - i`.

This derivation explains why the anchor need not be tried at every possible array location. Median optimality fixes a minimum-cost alignment for each selected window.

**Enumerate every valid median index**

There must be `x - 1` selected ones before the anchor and `y` after it. Therefore `i` begins at `x - 1`. The loop's stop is `len(arr) - y`, which is exclusive, so the largest visited `i` satisfies `i + y < len(arr)`.

The selected window is

`arr[i + 1 - x : i + 1 + y]`.

It contains $x$ entries through the anchor and $y$ entries after it, exactly $k$ in total. Since the constraint guarantees at least $k$ ones, this loop has at least one candidate.

**Use prefix sums for actual positions**

`s = list(accumulate(arr, initial=0))` creates a prefix-sum array with `s[0] = 0` and

$$
s[r]=\sum_{t=0}^{r-1}\texttt{arr}[t].
$$

For anchor `i`, the sum of the $x$ actual left-and-anchor positions is

`ls = s[i + 1] - s[i + 1 - x]`.

The sum of the $y$ actual positions strictly to the right is

`rs = s[i + 1 + y] - s[i + 1]`.

Both range sums are constant-time, allowing all windows to be evaluated in linear time rather than summing $k$ distances for each one.

**Derive the left movement formula**

The left target positions run from `j - x + 1` through `j`. Their arithmetic-series sum is

$$
\frac{(j+(j-x+1))x}{2}.
$$

That is the source expression `(j + j - x + 1) * x // 2`.

For each selected position at or left of the anchor, strict ordering of ones ensures its original position is no farther right than its corresponding target: moving from an earlier selected one to the anchor spans at least as many array indices as selected-one steps. Consequently all these contributions are target minus original, with no absolute-value branch. The total is

`a = target_left_sum - ls`.

**Derive the right movement formula**

The right target positions run from `j + 1` through `j + y`. Their sum is

$$
\frac{((j+1)+(j+y))y}{2},
$$

implemented as `(j + 1 + j + y) * y // 2`.

Actual selected ones on the right are at least as far right as their respective consecutive targets, so their movement is actual minus target. The source computes

`b = rs - target_right_sum`.

The candidate cost `a + b` counts one move for every crossed zero. Movements of different selected ones can be realized without crossing their order, so this distance sum is both a lower bound and an achievable number of adjacent swaps.

**Choose the best window**

`ans` starts at infinity. Every loop iteration evaluates one possible window of $k$ consecutive ones at its median-optimal consecutive placement and updates `ans = min(ans, a + b)`. Because every relevant selected window is visited and each receives its minimum alignment cost, the final `ans` is the global minimum.

For `k = 1`, `x=1` and `y=0`. Each candidate contains only its anchor, both movement sums are zero, and the method correctly returns zero.

## Complexity detail

Let $n$ be the length of `nums` and $m$ the number of ones. Extracting `arr` takes $O(n)$ time. Building its prefix sums takes $O(m)$, and the median loop has at most $m$ iterations with constant work each. Total time is $O(n+m)=O(n)$.

The position array and prefix-sum array each use $O(m)$ space. All remaining variables are scalar, so auxiliary space is $O(m)$ as stated by the manifest. Since $m\le n$, this is also $O(n)$ in the worst case.

Python integer arithmetic avoids overflow in the prefix sums and arithmetic-series products. The divisions are exact because the product of the count and the sum of the first and last terms of an integer arithmetic sequence is always even.

## Alternatives and edge cases

- **Simulate adjacent swaps:** Moving chosen ones one step at a time can take as many operations as the answer itself and is too slow for large arrays.
- **Evaluate each window in $O(k)$:** Sum distances directly to consecutive targets. It is conceptually simple but costs $O(mk)$ time; prefix sums remove the repeated work.
- **Adjusted-position array:** Explicitly build `arr[r] - r` and sum absolute deviations from its window median. This is an equivalent common formulation, though the exact source folds the spacing correction into arithmetic-series formulas.
- **Sliding-window cost recurrence:** Update the median cost as the window moves. It can also achieve linear time but requires careful parity handling.
- **`k = 1`:** No swap is needed, and the zero-length right range is handled by the prefix formulas.
- **Ones already consecutive:** Actual positions equal the target arithmetic sequences, so both `a` and `b` are zero.
- **Even `k`:** The source uses the left middle selected one; either middle interval gives a minimum absolute-deviation cost.
- **Odd `k`:** The anchor is the unique median selected one.
- **Exactly `k` ones total:** Only one window is evaluated, as every one must participate.
- **More than `k` ones:** Every consecutive window in `arr` is considered, allowing the algorithm to ignore distant ones.
- **Zeros at the ends:** They do not need to move unless crossed by a selected one; position distances count only necessary adjacent swaps.
- **Enough ones guarantee:** `k <= sum(nums)` ensures `ans` is updated from infinity before return.
- **No double-counting swaps:** Each selected one's displacement counts its crossings with zeros; selected ones preserve order and do not need to cross each other.
- **Prefix-sum boundaries:** The initial zero in `s` makes a range beginning at `arr[0]` use the same subtraction formula without a special case.

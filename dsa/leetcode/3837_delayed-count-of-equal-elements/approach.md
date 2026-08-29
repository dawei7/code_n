## General

**Identify the first eligible position exactly**

For index `i`, a matching position must satisfy

$$
i+k<j.
$$

Since indices are integers, the first eligible index is

$$
j=i+k+1.
$$

The `+1` is essential. Position `i + k` is still excluded by the strict inequality.

The delayed count asks only how many eligible suffix values equal `nums[i]`. If a frequency table contains exactly the elements from `i + k + 1` through the end, the answer is one dictionary lookup.

**Scan right to left so the eligible suffix grows by one**

As `i` decreases by one, the eligibility boundary also decreases by one:

$$
(i-1)+k+1=i+k.
$$

The new index gains exactly one additional eligible position compared with the previous index. This makes a right-to-left frequency scan natural.

The source maintains `cnt` with the invariant:

> Immediately before assigning `ans[i]`, `cnt` contains the frequencies of values at every index from `i + k + 1` through `n - 1`, and no earlier index.

It restores this invariant by adding the new boundary value:

`cnt[nums[i + k + 1]] += 1`.

It then reads:

`ans[i] = cnt[nums[i]]`.

That lookup counts exactly the eligible positions whose value equals the current one.

**Choose the correct starting index**

An index has at least one eligible position only when

$$
i+k+1\le n-1.
$$

Rearranging gives

$$
i\le n-k-2.
$$

The loop therefore begins at `n - k - 2` and descends to zero:

`range(n - k - 2, -1, -1)`.

Every index greater than `n - k - 2` has an empty eligible suffix and must receive zero. The source initializes `ans = [0] * n`, so these trailing positions are already correct and do not need loop iterations.

**Why adding before querying is correct**

At the first iteration, `i = n - k - 2`. Its first eligible position is:

$$
i+k+1=n-1.
$$

The counter starts empty, then adds `nums[n - 1]` before answering. It now represents exactly the one-element eligible suffix.

Suppose the invariant holds for index `i + 1`. Its counter contains positions from

$$
(i+1)+k+1=i+k+2
$$

through the end. When moving to `i`, the newly eligible boundary is `i + k + 1`. Adding that one value expands the represented range to the exact suffix required by `i`.

Querying before adding would omit the first legal position and create an off-by-one error.

**Trace the first example**

For `nums = [1,2,1,1]` and `k = 1`, the first processed index is

$$
4-1-2=1.
$$

At `i = 1`, add position `1+1+1=3`, whose value is 1. The counter is `{1: 1}`. Looking up current value 2 gives zero, so `ans[1] = 0`.

Move to `i = 0`. Add position `0+1+1=2`, another value 1. The counter now has two ones, representing indices 2 and 3. Since `nums[0] = 1`, `ans[0] = 2`.

Indices 2 and 3 were never looped because neither has a position more than one step after it. Their initialized answers remain zero. The result is `[2,0,0,0]`.

For `k = 0`, the first eligible position is `i + 1`. The same scan becomes the usual “count equal elements strictly to the right” algorithm.

**Counter behavior for unseen values**

`Counter()` returns zero for a missing key. If `nums[i]` does not appear in its eligible suffix, `cnt[nums[i]]` produces the correct answer zero without a separate membership test.

Reading a missing Counter key does not need a special initialization branch. The stored frequencies grow only as positions cross the delay boundary.

**Why every matching position is counted once**

For fixed `i`, the invariant includes a position `j` exactly when `j >= i + k + 1`, equivalent to `i + k < j`. Each such position was added once when it became the moving boundary and is never removed because future iterations move farther left and keep it eligible.

The lookup selects only positions with `nums[j] == nums[i]`. Therefore it counts every legal equal-value index once and excludes all too-close or unequal positions.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$. The loop runs $N-k-1$ times when that value is positive. Each iteration performs one expected $O(1)$ Counter increment and one expected $O(1)$ lookup. Worst-case time over allowed `k` is $O(N)$.

The answer list uses $O(N)$ required output space. The Counter stores at most one key per distinct value appearing in the maintained suffix, bounded by $O(N)$, so auxiliary space is also $O(N)$ in the worst case.

The source never constructs a separate suffix for each index and never examines the same eligible position anew for multiple queries; its frequency persists across the scan.

## Alternatives and edge cases

- **Direct nested counting:** For each `i`, scan from `i + k + 1` to the end. This is simple but costs $O(N^2)$ when `k` is small.
- **Positions list plus binary search:** Store sorted occurrence indices for each value, then binary-search the first index greater than `i + k`. This costs $O(N\log N)$ total and can answer arbitrary delayed queries.
- **Full suffix-frequency snapshots:** Building a map for every starting point supports lookup but can consume $O(N^2)$ copied state. The rolling Counter stores only the current suffix.
- **k equals zero:** Every equal occurrence strictly to the right is counted.
- **k equals n - 1:** No index has an eligible later position, the loop is empty, and all answers remain zero.
- **Strict inequality boundary:** Index `i + k` is excluded; adding `i + k + 1` is the correct first position.
- **Trailing indices:** Those with no eligible suffix retain the zero values created during answer initialization.
- **All values equal:** `ans[i]` equals the number of indices from `i + k + 1` through the end.
- **All values distinct:** Every Counter lookup for the current value returns zero.
- **One element:** The loop is empty for the only allowed `k = 0`, and the answer is `[0]`.
- **Missing Counter key:** It evaluates to zero naturally, matching “no eligible equal value.”

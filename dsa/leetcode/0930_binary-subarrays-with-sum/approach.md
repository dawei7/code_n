## General

For every subarray ending at the current position, its sum can be expressed as the difference of two prefix sums. This turns subarray counting into frequency lookup.

Let $P_r$ be the sum of elements before boundary $r$, with $P_0=0$. A subarray from index $\ell$ through $r-1$ has sum

$$
P_r-P_\ell.
$$

It equals `goal` exactly when

$$
P_\ell=P_r-\text{goal}.
$$

Therefore, when current running prefix sum is `s = P_r`, the number of valid subarrays ending here equals the number of earlier prefix sums equal to `s - goal`.

**Initialize the empty prefix.** Counter starts with `{0: 1}`. This represents prefix sum $P_0=0$ before reading any values. It allows a subarray beginning at index zero to be counted when its current prefix sum equals `goal`.

Without this entry, all valid subarrays starting at the first element would be missed.

**Process each value in order.**

1. Add `v` to running sum `s`.
2. Add `cnt[s - goal]` to `ans`.
3. Increment `cnt[s]` so this prefix can serve as a left boundary for later subarrays.

The query must occur before inserting the current prefix. This guarantees the chosen earlier prefix boundary precedes the current boundary and the represented subarray is nonempty.

For `goal = 0`, inserting first would count the current prefix against itself and create an empty subarray. The exact order avoids that error.

**Why multiplicity of prefix sums matters.** Different earlier boundaries can have the same prefix sum, especially because zeros do not change the sum. Each boundary defines a different subarray ending at the current position, so the Counter stores occurrence frequency rather than only membership.

For `nums = [0,0,0,0,0]` and goal 0, prefix sum remains zero. At successive positions, prior zero-prefix counts are 1, 2, 3, 4, and 5. Their sum is 15, matching all $\binom{6}{2}$ choices of two distinct prefix boundaries.

**Example `[1,0,1,0,1]` with goal 2.** As prefixes reach sums 1, 1, 2, 2, and 3, the lookup for current sum minus two finds the appropriate earlier boundaries. Repeated prefix sums created by zeros account for multiple start or end extensions, producing four subarrays.

At the third element, current prefix sum is 2 and the needed earlier prefix is 0. The initialized empty prefix supplies one subarray, `[1,0,1]`. At the fourth element, sum is still 2, so the same empty prefix supplies `[1,0,1,0]`. At the final element, sum is 3 and needed prefix is 1; that prefix occurred at two earlier boundaries, producing two more subarrays. The Counter turns these repeated-boundary choices into the correct multiplicity automatically.

**Why every valid subarray is counted once.** A nonempty subarray has unique left and right boundaries $(\ell,r)$. When the scan reaches right boundary $r$, Counter already contains prefix $P_\ell$. The sum equation makes it part of lookup `s-goal`, so the subarray contributes once. It cannot contribute at another iteration because its right boundary is unique.

Conversely, every prior prefix counted by the lookup defines a boundary $\ell<r$ whose difference from current prefix is exactly `goal`. It therefore corresponds to a real valid nonempty subarray.

The binary-array restriction is not necessary for prefix-frequency correctness; the same method works with arbitrary integers. Here it keeps prefix sums between zero and $n$ and also enables constant-space sliding-window alternatives.
Before processing a new value, `cnt` contains exact frequencies of all prefix sums through the previous boundary, and `ans` counts all valid subarrays ending before the current position. The lookup counts exactly newly ending subarrays, and then the current prefix is stored for future use. The invariant holds through the full array.

## Complexity detail

Let $n$ be the array length. Each value performs a constant expected number of Counter operations.

- **Time complexity:** $O(n)$ expected.
- **Space complexity of the exact solution:** $O(n)$ in the worst case for distinct prefix sums.

The manifest's $O(1)$ space corresponds to the editorial's binary-array sliding-window method. This exact Counter implementation retains prefix frequencies and is not constant-space.

## Alternatives and edge cases

- **At-most sliding windows:** For nonnegative arrays, count subarrays with sum at most `goal` minus those with sum at most `goal - 1`. This uses $O(1)$ space.
- **One-pass zero-prefix window method:** Track leading zeros around windows containing exactly `goal` ones. It also exploits binary values for constant space.
- **Enumerate every subarray:** Maintaining sums for all starts costs $O(n^2)$ time.
- **Use a set of prefix sums:** It loses multiplicity and undercounts repeated boundaries.
- **`goal = 0`:** Repeated zero prefixes must all be counted; query-before-increment prevents empty subarrays.
- **All zeros:** Result is $n(n+1)/2$.
- **Goal larger than total ones:** No lookup finds a feasible prior prefix, so result is zero.
- **Subarray begins at zero:** The initialized empty prefix counts it.
- **Repeated running sum:** Each occurrence represents a distinct boundary.
- **One element:** It contributes one exactly when its value equals `goal`.
- **Nonempty requirement:** Current prefix is inserted only after lookup.
- **Binary contract:** Prefix sums never decrease, but the Counter proof does not depend on monotonicity.
- **Manifest mismatch:** The selected implementation's hash table grows with prefix diversity even though another optimal approach uses constant space.

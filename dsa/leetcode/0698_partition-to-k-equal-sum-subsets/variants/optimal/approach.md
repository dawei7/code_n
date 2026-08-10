## General

The solution assigns the numbers one by one into `k` conceptual buckets. Each bucket represents one desired subset, and every bucket must finish with the same target sum.

Because all input values are positive, a partial bucket that exceeds the target can never be repaired by adding more numbers. This gives backtracking a strong pruning rule. Sorting large numbers first and skipping symmetric bucket choices prune additional repeated work.

**The necessary divisibility test**

If the total array sum is `T` and `k` equal-sum subsets exist, each subset must sum to

$$
s=\frac{T}{k}.
$$

The code computes `s, mod = divmod(sum(nums), k)`. If `mod` is nonzero, `T` is not divisible by `k`, so an integer equal target does not exist and the method returns `False` immediately.

If divisibility holds, `s` is the required bucket capacity.

**Why sorting descending helps**

`nums.sort(reverse=True)` places the largest values first.

Large values are the hardest to fit. Trying them early makes an impossible bucket exceed `s` near the top of the recursion, where abandoning a branch saves the most downstream work. If small values were placed first, many partial assignments could look plausible before a later large value revealed the conflict.

Sorting is a performance optimization, not a correctness requirement. Every input element still appears once and is assigned to exactly one bucket.

**State maintained by the recursion**

`cur` is a length-`k` array of current bucket sums. Initially all are zero.

`dfs(i)` asks whether elements `nums[i:]` can be assigned so that, together with the already placed prefix `nums[:i]` represented by `cur`, all buckets finish correctly.

At recursion level `i`, the code tries placing `nums[i]` into each bucket `j`:

1. add the value to `cur[j]`;
2. continue only if the new sum is at most `s`;
3. recursively place the next number;
4. if that choice fails, subtract the value to restore the previous state.

The subtraction is the backtracking step. Every alternative bucket must begin from exactly the same state that existed before the failed trial.

**Why exceeding the target is final**

All `nums` values are positive. Once `cur[j] > s`, assigning more remaining values can only increase that sum. The current placement cannot lead to a valid partition, so the recursive call is skipped.

With negative numbers, this pruning would be unsound because a later negative value could reduce an oversized bucket. The source's positivity guarantee is therefore material.

**Why the base case needs no explicit bucket checks**

When `i == len(nums)`, every number has been placed exactly once, and no bucket was ever allowed above `s`.

The sum across all bucket sums equals the total input sum:

$$
\sum_{j=0}^{k-1}\texttt{cur}[j]=ks.
$$

There are `k` buckets, each at most `s`. The only way their total can equal `ks` is for every bucket to equal `s`. Therefore, returning `True` immediately is correct.

Because all values are positive and `s > 0`, a bucket reaching `s` cannot be empty. The required nonempty condition follows automatically.

**Skipping symmetric bucket choices**

The condition

`if j and cur[j] == cur[j - 1]: continue`

avoids trying the current number in consecutive buckets that presently have the same sum.

Bucket labels do not matter. If buckets `j-1` and `j` have equal sums, placing `nums[i]` into one rather than the other produces states that differ only by swapping those bucket labels. Future numbers see only the multiset of remaining bucket capacities, so either both states can succeed or both fail.

Trying the first representative is sufficient.

This is especially powerful for empty buckets. At the beginning, all `k` bucket sums are zero, so the first number is tried only in bucket zero rather than in `k` equivalent empty buckets.

The check compares adjacent sums. The algorithm's sequence of assignments and backtracking keeps equal-sum buckets grouped sufficiently for this standard symmetry pruning at the choice point; more generally, the correctness principle is that any repeated current sum needs only one representative bucket.

**A successful example**

For `nums = [4, 3, 2, 3, 5, 2, 1]` and `k = 4`, the total is `20`, so `s = 5`. Sorting gives `[5, 4, 3, 3, 2, 2, 1]`.

- `5` fills the first bucket immediately.
- `4` enters the next empty bucket.
- A `3` begins another bucket.
- The next `3` begins the fourth.
- Later `2` values complete the two `3` buckets, and `1` completes the `4` bucket.

The completed sums are `[5, 5, 5, 5]`, so the base case returns true.

**Why the search is complete**

Ignoring symmetric duplicates, every assignment of each number to one of `k` buckets appears along some recursion branch. A branch is pruned only if a bucket exceeds `s`, which no valid solution can do with positive numbers, or if it duplicates an assignment obtainable by relabeling equal-sum buckets.

Thus no genuinely distinct valid partition is removed. If a partition exists, one representative branch reaches the base case. If the search exhausts all branches, no valid assignment exists.

## Complexity detail

Let `N = len(nums)`.

In the worst case, each of `N` values can be tried in up to `k` buckets. The symmetry and capacity checks substantially reduce practical work but do not create memoized states. A conservative worst-case time bound for this exact backtracking is

$$
O(k^N).
$$

Sorting costs `O(N\log N)` and is dominated by the exponential search. The literal code does not allocate a `2^N` memo table, so an `O(N2^N)` bound belongs to a different bitmask-DP implementation rather than this source.

The bucket array uses `O(k)` space. Recursion depth is `N` because one element is fixed per level. Sorting may also use implementation-dependent temporary memory. The principal auxiliary-space bound is

$$
O(N+k).
$$

## Alternatives and edge cases

- **Bitmask DP:** Store the current partial-bucket remainder for each subset of used elements. This gives `O(N2^N)` time and `O(2^N)` space and avoids revisiting equivalent used-element states.

- **Memoized backtracking:** Cache failed configurations, usually with a used-elements mask and current remainder. It can provide the bitmask-style bound while keeping recursive organization.

- **Largest number exceeds `s`:** After descending sort, every trial of that number exceeds every bucket's capacity, and symmetry quickly leads to `False`.

- **Total not divisible by `k`:** The method rejects before sorting or search.

- **`k = 1`:** The target is the total sum. All elements fit into the only bucket, so the method returns `True`.

- **`k = N`:** Positivity means every subset contains one number. A solution exists exactly when all values are equal; the backtracking discovers this.

- **Duplicate input values:** They are separate elements and must each be assigned, but descending order and equal bucket pruning reduce symmetric arrangements.

- **Input mutation:** `nums.sort(reverse=True)` changes the caller-provided list order.

- **Backtracking restoration:** `cur[j] -= nums[i]` must run after every failed trial, including a trial rejected for exceeding `s`.

- **Positive values:** They justify both capacity pruning and the claim that completed target-sum buckets are nonempty.

- **Identical empty buckets:** Trying only the first avoids `k` equivalent choices for the first placed value and similar duplication later.

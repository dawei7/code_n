## General

**Use a unique sliding window**

The desired erased segment must be contiguous and contain no duplicate values. For every right endpoint, the source maintains the earliest valid start `j` such that `nums[j:i]`—using Python’s half-open notation—contains unique elements.

Because every value is positive, the widest valid unique window ending at a fixed position also has the greatest sum among valid windows ending there. Removing positive elements from its left could only decrease the score. This positivity is what lets the method evaluate one canonical window per endpoint.

**Store last positions in one-based form**

`d` is an array indexed by value. It is initialized to zero, meaning “not seen.” The constraints make values at most $10^4$, so allocating through `max(nums)` is feasible.

The loop uses `enumerate(nums, 1)`, so current position `i` is one-based while `v = nums[i-1]`. After processing `v`, `d[v] = i` records one more than its zero-based index.

That representation is convenient because the index immediately after the old occurrence is exactly the stored one-based position.

**Move the start past a duplicate**

Before including current `v`, `d[v]` is zero if unseen or the one-based position of its most recent occurrence. The update

`j = max(j, d[v])`

moves the window start past that old occurrence when it lies inside the current window.

The `max` is essential. A last occurrence older than the current start has already been excluded due to another duplicate, and moving `j` backward would reintroduce invalid values.

After the update, the subarray from zero-based index `j` through `i - 1` contains no duplicate `v` and preserves uniqueness of all other values from the previous window.

**Get window sums from prefix sums**

`s` is the prefix-sum list with `s[0] = 0`. The sum of half-open subarray `nums[j:i]` is:

`s[i] - s[j]`.

The source computes this in constant time and updates `ans`. It then stores `d[v] = i` for future duplicates.

For `[4, 2, 4, 5, 6]`:

- after the first two values, the window is `[4,2]`;
- at the second `4`, its prior stored position is one, so `j` moves to one, leaving `[2,4]`;
- extending with five and six gives `[2,4,5,6]` with sum 17.

**The maintained invariant**

After processing position `i`:

- `j` is the smallest start that lies after every conflicting last occurrence relevant to the current suffix;
- `nums[j:i]` has all unique values;
- `d[v]` stores the latest one-based occurrence of every seen value;
- `ans` is the largest sum among canonical unique windows ending at or before `i - 1`.

When the next value arrives, only a duplicate of that new value can violate the previous window’s uniqueness. Moving `j` past its last occurrence restores the invariant.

**Why the maximum is correct**

Every maintained window is a valid unique subarray, so every score considered is achievable. For any valid unique subarray ending at current index, its start cannot precede the most recent conflicting occurrence, so it starts at or after `j`. Since all values are positive, the window beginning at the smallest valid `j` has sum at least as large as any shorter valid suffix ending there.

Thus `s[i]-s[j]` is the best score for each right endpoint. Taking the maximum over all endpoints returns the global optimum.

## Complexity detail

Let `n` be the array length and `V = max(nums)`. Computing `max(nums)` and building prefix sums take $O(n)$ time. Initializing `d` takes $O(V)$ time, and the loop takes $O(n)$. Total time is $O(n+V)$; with the fixed `V <= 10^4` domain this is commonly reported as $O(n)$.

`s` uses $O(n)$ space and `d` uses $O(V)$ space, for $O(n+V)$ auxiliary space. The manifest’s $O(n)$ notation treats the bounded value table as constant or assumes `V = O(n)`, but the exact parameterized bound includes both terms.

## Alternatives and edge cases

- **Set-based sliding window:** Remove left elements one at a time until the duplicate disappears while maintaining a running sum. It is $O(n)$ expected time and uses space proportional to current distinct values.
- **Hash map of last positions:** It avoids allocating through the maximum value and gives expected $O(n)$ time with $O(u)$ space for `u` distinct values.
- **Recompute each window sum:** Last positions locate starts in constant time, but resumming would make the method quadratic; prefix sums avoid that.
- **All values unique:** `j` remains zero and, because values are positive, the entire array gives the maximum sum.
- **All values equal:** Every new occurrence moves `j` to the prior position, so every window contains one value and the answer is that value.
- **Duplicate outside current window:** `max(j, d[v])` leaves `j` unchanged rather than moving backward.
- **One element:** The prefix difference returns that positive value, satisfying the exactly-one-subarray requirement.
- **Positive-values dependency:** If negatives were allowed, the widest unique window might not maximize sum; an additional optimization would be needed.
- **One-based last positions:** Zero remains an unambiguous unseen sentinel and a stored value directly equals the next legal start.
- **Large value domain:** A dictionary would be preferable if values were sparse and unbounded.
- **Input preservation:** The algorithm builds auxiliary arrays but does not alter `nums`.

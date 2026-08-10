## General

**Fix a left endpoint and extend the subarray**

The range of a subarray is its maximum minus its minimum. The exact source enumerates every subarray of length at least two, but avoids rescanning a subarray to rediscover those extremes.

For each starting index `i`, it initializes

`mi = mx = nums[i]`.

Then `j` moves from `i + 1` through the end. When `nums[j]` is added to the current subarray `nums[i...j]`, the new extremes are

`mi = min(mi, nums[j])`

and

`mx = max(mx, nums[j])`.

The range `mx - mi` is then added to `ans`.

This reuses the extremes from `nums[i...j - 1]`, so extending the right endpoint costs constant time.

**Why length-one subarrays are omitted safely**

The outer loop stops at `n - 2`, and the inner loop begins at `i + 1`. Therefore, the method never explicitly processes a one-element subarray.

Every one-element subarray has equal maximum and minimum, so its range is zero. Omitting these zero contributions does not change the required sum.

When the array itself has one element, the outer range is empty and the method returns the initialized zero.

**Trace a starting index**

For `nums = [1, 2, 3]` and `i = 0`, both extremes begin at 1.

- At `j = 1`, the maximum becomes 2 and minimum stays 1. The range of `[1, 2]` is 1.
- At `j = 2`, the maximum becomes 3 and minimum stays 1. The range of `[1, 2, 3]` is 2.

For `i = 1`, extending to `j = 2` gives range 1. The total is $1+2+1=4$. The three omitted singleton ranges are all zero.

Duplicates require no special treatment. In `[1, 3, 3]`, extending over the second 3 leaves the maximum unchanged, exactly as it should.

**Why every contribution is correct**

At the start of an inner iteration for endpoint `j`, `mi` and `mx` describe the preceding subarray from `i` through `j - 1`. Updating each with `nums[j]` produces the true minimum and maximum over `i...j`: the new value either becomes the extreme or the old extreme remains.

The difference added is consequently the exact range of that subarray.

Every subarray of length at least two has one unique pair of endpoints `i < j`, and the nested loops visit that pair exactly once. Singletons contribute zero. Thus `ans` equals the sum of all non-empty subarray ranges.

**Be honest about the exact branch implementation**

The branch manifest summary says that values are counted as maxima and minima with monotonic stacks, and it lists $O(n)$ time and $O(n)$ space. That is a valid follow-up technique, but it is not present in the exact solution file.

The executable source uses the two nested endpoint loops above. Its real complexity is quadratic time and constant auxiliary space. A faithful approach explanation cannot claim that stack contributions are being computed when no stack exists.

The constraints allow $n\le1000$, for which the quadratic implementation can be practical. It solves the main problem but does not satisfy the stated $O(n)$ follow-up.

**What the linear follow-up would change**

A monotonic-stack solution writes the total as the sum of all subarray maxima minus the sum of all subarray minima. For each index, previous/next greater or smaller boundaries count how many subarrays use that value as the chosen extreme. Careful strict versus non-strict comparisons assign duplicates exactly once.

That is a different algorithm with different data structures and tie rules. It belongs as an alternative here rather than being presented as the behavior of this source.

## Complexity detail

Let $n$ be the length of `nums`.

The number of endpoint pairs with `i < j` is $n(n-1)/2$. Each pair performs constant-time minimum, maximum, subtraction, and addition operations. The exact time complexity is therefore $O(n^2)$.

The source stores only `ans`, `n`, the two indices, and the current extremes. It allocates no structure proportional to $n$, so auxiliary space is $O(1)$.

The answer can be large because there are quadratically many subarrays and values may have magnitude $10^9$. Python integers expand safely; fixed-width languages should use a wide integer type.

## Alternatives and edge cases

- **Monotonic contribution stacks:** Count each value's subarrays as maximum and minimum to achieve $O(n)$ time and $O(n)$ space. This is the follow-up solution described by the manifest, not the exact source.
- **Recompute min and max for every subarray:** This adds another scan inside the endpoint loops and can cost $O(n^3)$. Carrying `mi` and `mx` avoids it.
- **Prefix sums:** They answer subarray sums, not subarray minima and maxima, so they do not directly solve range queries.
- **One element:** The only range is zero, and empty loops return zero.
- **All equal values:** Every maintained minimum equals maximum, so the result remains zero.
- **Negative values:** Min/max comparisons and their difference work without modification.
- **Duplicate extremes:** The direct enumeration does not need stack tie-breaking; it simply maintains the numeric extremes.
- **Length-one omission:** Safe only because every singleton range is exactly zero.
- **Large result:** Use a sufficiently wide accumulator outside Python.
- **Input preservation:** `nums` is read but never sorted or changed.
- **Manifest mismatch:** Complexity must follow the nested loops actually executed: $O(n^2)$ time and $O(1)$ auxiliary space.
- **Follow-up scope:** The source solves the required output correctly while not implementing the optional linear-time challenge.

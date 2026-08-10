## General

**Begin with the unconstrained maximum-sum selection**

After sorting `nums` in ascending order, the largest possible sum of any $k$ elements is the sum of `nums[-k:]`. Because subsequence order does not affect a sum, any selected values can later be viewed in their original order if needed; this problem returns only the sum.

If this maximum sum is even, it is immediately optimal under the parity constraint as well. No even-sum selection can exceed the unconstrained maximum.

The sort mutates `nums`, an observable detail of the exact source.

**An odd sum needs one parity-changing exchange**

When the top-$k$ sum is odd, its parity must be flipped. Replacing one selected value with one unselected value changes parity exactly when their parities differ.

There are two possible exchange types:

- remove the smallest selected even value and add the largest unselected odd value;
- remove the smallest selected odd value and add the largest unselected even value.

For either type, choosing the smallest removable value and largest incoming value minimizes the loss from the already maximum top-$k$ sum.

The scan of `nums[:n-k]` is ascending and repeatedly assigns candidates, so `mx1` ends as the largest unselected odd and `mx2` as the largest unselected even.

The selected slice is traversed in descending order. Repeated assignments make `mi2` the smallest selected odd and `mi1` the smallest selected even. The names are less informative than their actual parity roles.

The two repaired sums are `ans - mi1 + mx1` and `ans - mi2 + mx2`.

**Why one best exchange is sufficient**

The top $k$ values maximize sum before parity is considered. Every replacement with an unselected value can only preserve or reduce that sum.

An odd total needs an odd number of parity-changing exchanges. At least one is necessary. Performing extra exchanges adds nonnegative losses, so an optimum can be obtained by the least costly single valid parity swap. Comparing the best exchange of both parity directions finds it.

If an exchange type lacks either required parity, its sentinel infinity values make that candidate unusable. Including `-1` in `max` ensures a defined impossibility result.

Because all input values are nonnegative, every feasible even sum is at least zero. The final negative check cleanly distinguishes sentinel-driven impossibility.

**Why the result is correct**

The initially selected set is the global maximum-sum size-$k$ set. If even, returning it is optimal.

If odd, every feasible even selection differs by parity. Relative to the boundary between selected and unselected sorted values, the cheapest way to flip parity is to remove the smallest selected value of one parity and add the largest available unselected value of the other. The code evaluates both possible directions and returns the larger feasible repaired sum.

Thus it returns the largest even sum or `-1` when no parity-changing replacement exists.

**Trace both repair directions**

Take `nums = [4, 1, 5, 3, 1]` and `k = 3`. After sorting, the selected top values are 3, 4, and 5, whose sum is 12, so the method returns immediately.

For a case where the top sum is odd, imagine selected values containing a smallest even value 4 and a smallest odd value 7. Suppose the unselected side offers a largest odd value 3 and largest even value 2. Removing 4 and adding 3 loses one and flips parity; removing 7 and adding 2 loses five and also flips parity. Comparing the two repaired sums chooses the first.

It is not enough to look only for the globally smallest selected value. Its parity determines which unselected values can flip the sum. Likewise, the globally largest unselected value may have the wrong parity. The four parity-specific extrema contain exactly the information needed.

**Why the scans find the correct extrema**

The unselected prefix is ascending. Assigning `mx1` or `mx2` whenever a matching value appears leaves the last, and therefore largest, value of that parity.

The reversed selected suffix is descending. Repeatedly assigning the matching `mi` variable means the final assignment is the smallest selected value of that parity. No extra minimum or maximum comparisons are needed because sorting establishes the visit order.

## Complexity detail

Let $n$ be the length of `nums`.

Sorting dominates at $O(n\log n)$ time. The sums and scans are linear, so total time remains $O(n\log n)$.

Python sorting and the slices `nums[:n-k]`, `nums[-k:]`, and its reversal can use $O(n)$ auxiliary space in the worst case. This matches the manifest's $O(n)$ space bound.

## Alternatives and edge cases

- **Dynamic programming by chosen count and parity:** It can track best sums but costs $O(nk)$ without further optimization. Sorting reduces the repair to boundary candidates.
- **Heaps for top values by parity:** Possible, but more complex than sorting and scanning.
- **Top-$k$ sum already even:** Return immediately; any exchange cannot increase the unconstrained maximum.
- **All values odd:** A feasible sum exists exactly when $k$ is even; otherwise no opposite-parity replacement is available.
- **All values even:** Every size-$k$ sum is even, so the top-$k$ sum returns immediately.
- **`k == n`:** There are no unselected replacements. The total is returned if even and `-1` if odd.
- **Zero values:** Zero is even and participates normally.
- **Sentinel infinities:** Missing candidate types evaluate to negative infinity rather than being accidentally selected.
- **Input mutation:** `nums.sort()` leaves the caller's list sorted.
- **Subsequence wording:** Only the sum is returned, so restoring original positional order is unnecessary.
- **Both repair types impossible:** This means no size-$k$ selection can change the odd parity to even; the sentinel candidate `-1` is returned.

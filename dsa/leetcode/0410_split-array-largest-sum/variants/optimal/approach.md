## General

**Search for the answer, not for the cut positions**

There are $n-1$ gaps between adjacent array elements, and a split into exactly `k` non-empty subarrays chooses `k-1` of those gaps. Enumerating all choices is far too expensive. The useful change of perspective is to guess a value `mx` for the largest permitted subarray sum and ask a simpler yes-or-no question:

> Can the entire array be divided into at most `k` contiguous non-empty groups, with every group sum at most `mx`?

This feasibility question can be answered greedily in one pass. More importantly, its answer is monotone. If a limit `mx` is feasible, every larger limit is feasible because the same split still obeys the relaxed bound. If a limit is infeasible, every smaller limit is also infeasible. Therefore the possible limits form a sequence of `False` values followed by `True` values, and binary search can locate the first `True` value. That first feasible limit is precisely the minimum possible largest subarray sum.

The nonnegative constraint on `nums` is essential. It ensures that extending a subarray never decreases its sum and makes the greedy feasibility test valid.

**Why the search interval is complete**

The lower bound is `max(nums)`. Every element must belong to some subarray, so the subarray containing the largest element has a sum at least that element. No answer below this bound can work.

The upper bound is `sum(nums)`. Putting the entire array in one group gives that sum. When more groups are required, splitting a nonnegative array cannot increase the largest group beyond the total, so this is always a feasible ceiling. The true answer therefore lies in the inclusive integer interval `[max(nums), sum(nums)]`.

**The exact greedy feasibility test**

Inside `check(mx)`, `s` is the sum of the current group and `cnt` is the number of groups started. The implementation initializes them as `s, cnt = inf, 0`. The infinite sentinel intentionally forces the first array element to start the first real group:

1. For the first `x`, `s + x` is still infinite and is greater than the finite candidate `mx`.
2. The branch sets `s = x` and increments `cnt` to `1`.
3. After that forced start, `s` is an ordinary finite running sum.

For every later value `x`, the code first conceptually tries to append it to the current group by evaluating `s + x`. If this sum is at most `mx`, the condition `s > mx` is false after `s += x`, and the current group is extended. If it exceeds `mx`, the current group cannot accept `x`; the code resets `s = x` and increments `cnt`, starting a new group at exactly this element.

This unusual sentinel formulation is equivalent to starting with `s = 0` and `cnt = 1`, but it matches the shipped solution exactly and avoids a separate first-element case.

Because binary search never tests a value below `max(nums)`, every individual `x` is at most `mx`. Thus resetting `s` to `x` always creates a valid group. At the end, `cnt` is the number of groups used, not the number of cut positions, and `check` returns whether `cnt <= k`.

For `nums = [7,2,5,10,8]` and `mx = 18`, the greedy groups are `[7,2,5]` and `[10,8]`, so `cnt = 2` and the limit is feasible for `k = 2`. With `mx = 17`, the groups become `[7,2,5]`, `[10]`, and `[8]`; three groups are required, so the limit is infeasible.

**Why taking the longest possible current group minimizes the group count**

The feasibility scan never cuts while the next element still fits. This is not merely convenient. For a fixed limit, it produces the minimum possible number of groups.

Look at the first greedy group. It ends immediately before the first element that would make its sum exceed `mx`. Any valid split cannot place that next element in its first group, because it contains the same nonnegative prefix and would exceed the limit. Therefore no valid first group can extend farther than the greedy first group. After removing that prefix, the same argument applies to the remaining suffix. Repeating it shows that another valid partition cannot use fewer boundaries than the greedy partition.

Consequently, if greedy needs more than `k` groups, no arrangement can satisfy the limit with `k` groups. If greedy needs at most `k`, the limit is feasible.

The problem asks for exactly `k` groups while `check` accepts at most `k`. That apparent mismatch is safe. If greedy produces fewer than `k` groups, split existing non-empty groups at additional element boundaries. Since `k <= n`, enough boundaries exist. Because all values are nonnegative, replacing one group by two smaller contiguous pieces cannot make either piece's sum exceed the original group's sum. We can therefore refine an at-most-`k` solution into exactly `k` groups without violating `mx`.

**How `bisect_left` performs the binary search**

The expression `range(left, right + 1)` represents every candidate limit in increasing order while using constant storage. Python's `bisect_left` is called with target `True` and `key=check`. It applies `check` to selected range elements and searches the resulting monotone Boolean sequence for the first value not less than `True`. Since `False < True`, this is the first feasible candidate.

`bisect_left` returns an index into the range, rather than the candidate value itself. A range beginning at `left` has value `left + index` at that position, so the final expression

`left + bisect_left(range(left, right + 1), True, key=check)`

converts the discovered offset back into the actual minimized limit. The upper bound is known to be feasible, so a first `True` always exists.

**Why the returned value is optimal**

Let the returned limit be $L$. The feasibility test says $L$ can produce at most `k` groups and hence, by further splitting if needed, exactly `k` groups. So $L$ is achievable. Binary search chose the first feasible integer, meaning every value below $L$ is infeasible. No valid split can have a largest sum smaller than $L$. Achievability and this lower-bound argument together prove that $L$ is the minimized largest subarray sum.

## Complexity detail

Let $n$ be `len(nums)`, let $L = \max(\texttt{nums})$, and let $R = \sum \texttt{nums}$. One call to `check(mx)` scans all $n$ elements and performs constant work for each, so it costs $O(n)$ time.

Binary search examines $O(\log(R-L+1))$ candidate values. The total time is therefore

$$
O\bigl(n\log(R-L+1)\bigr),
$$

which is conventionally written as $O(n\log S)$ when $S = \sum \texttt{nums}$ is used as the numeric search bound. Computing `max(nums)` and `sum(nums)` adds two linear passes and does not change the final bound.

The feasibility scan stores only `s` and `cnt`. Python's `range` object represents its endpoints compactly; it does not allocate all values between `left` and `right`. Binary search also uses constant auxiliary state. The extra-space complexity is therefore $O(1)$.

This is a value-dependent or pseudo-polynomial logarithmic factor: the number of iterations depends on the magnitude of the sums, not only on the number of array elements. The logarithm keeps that dependence small; with the stated constraints, even a large total requires only a modest number of feasibility scans.

## Alternatives and edge cases

- **Dynamic programming over positions and group counts:** Prefix sums can support a recurrence that tries the final cut of each state. It directly models exactly `k` groups, but typical implementations take $O(k n^2)$ time and $O(kn)$ space, substantially more than the monotone answer search.
- **Enumerate all cut combinations:** Choosing `k-1` of `n-1` gaps is correct but combinatorial, so it becomes unusable long before the maximum constraints.
- **Greedy without binary search:** Greedy can minimize the number of groups for one proposed limit; it does not by itself reveal the smallest feasible limit. Binary search is what converts the decision procedure into an optimization algorithm.
- **Negative values:** The proof relies on nonnegative elements. With negative numbers, adding an element could lower a group sum, a greedy early cut might be wrong, and splitting a group could increase the maximum. The stated contract excludes this case.
- **`k == 1`:** Only the whole array is allowed, so the first feasible limit is `sum(nums)`. The same search and check handle it naturally.
- **`k == len(nums)`:** Every element can stand alone, so the answer is `max(nums)`, the lower search bound.
- **Zeros:** A zero can join either neighboring group without increasing its sum. Greedy may use fewer than exactly `k` groups, but zero-containing groups can still be split at element boundaries until the required count is reached.
- **All zeros:** Both search bounds are `0`; the one candidate is feasible, and the answer is `0`.
- **A single element:** The lower and upper bounds coincide with that element, and the sentinel starts exactly one valid group.
- **Off-by-one in the upper endpoint:** `right + 1` is necessary because Python ranges exclude their stop value. Omitting it would discard the always-feasible upper bound, especially breaking cases whose answer is `sum(nums)`.
- **Meaning of `cnt`:** Because `inf` forces the first start, `cnt` counts groups. In a more conventional initialization it is easy to count cuts instead and forget the final `+1`; understanding the sentinel prevents that error.

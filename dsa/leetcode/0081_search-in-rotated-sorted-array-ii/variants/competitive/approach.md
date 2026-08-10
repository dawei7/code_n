## General

**The intended source is a rotated inclusive binary search**

The intended algorithm maintains an inclusive interval `[left, right]` and chooses its midpoint. It first checks direct equality with `target`. If there is no equality, it uses the relationship between the midpoint and left endpoint to determine which sorted run contains the midpoint and which side can safely be discarded.

A rotated non-decreasing array consists of two ordered runs. When values are distinguishable, one of the halves around `mid` can be classified and searched by ordinary range comparisons. Duplicates create one special ambiguous case that shrinks the interval by one.

**Remove an ambiguous left duplicate safely**

After establishing `nums[mid] != target`, the source checks `nums[mid] == nums[left]`. If true, it increments `left`.

This is safe because `nums[left]` has the same value as the already checked midpoint and therefore is not the target either. Removing the left endpoint cannot discard a target occurrence. The equality prevents the algorithm from deciding reliably whether the midpoint belongs to the first or second sorted run, so a one-position reduction is the honest response.

Repeated equality can make this happen many times, producing linear worst-case behavior.

**Understand the combined choose-left condition**

The next condition has two cases joined by `or`, and either case means the target can only remain in the left half before `mid`.

First, if `nums[mid] > nums[left]`, the left half is strictly ordered. When `nums[left] <= target < nums[mid]`, the target's value lies inside that half, so `right = mid - 1` is correct. The upper comparison is strict because equality with `nums[mid]` was already rejected.

Second, if `nums[mid] < nums[left]`, the rotation lies in the left half and the interval from `mid` through `right` is the ordered right half. The expression `nums[mid] < target <= nums[right]` describes a target inside that right half. Its negation means the target is not there, so the algorithm chooses the left half with `right = mid - 1`.

If neither choose-left case applies, the target can only be to the right of `mid`, and `left = mid + 1` discards the midpoint and left portion.

**Why direct equality comes first**

Both subsequent updates exclude `mid`. Checking `nums[mid] == target` first prevents a found target from being discarded. It also supports the safe duplicate step: by the time equal midpoint and left values are seen, both are known not to equal the target.

The loop continues while `left <= right`, including single-element intervals. When no candidates remain, `left > right` and false is returned.

**Conditional correctness under integer midpoint arithmetic**

Assume `mid` is an integer index. At each iteration, direct equality proves success immediately. Equal left and middle values can discard `left` because both are known non-target values. Otherwise, strict comparison identifies whether the midpoint is in the first or second ordered run. The range tests select the only half whose ordered values and rotation position can still contain the target.

Each update removes at least one candidate while retaining any possible occurrence. The finite interval therefore empties or finds a match. This proves the intended membership result.

**The exact source uses Python 2 midpoint division**

The line `mid = left + (right - left) / 2` assumes division of two integers returns an integer. That was true for this non-negative arithmetic in Python 2. In Python 3, `/` always returns a float, even when the mathematical quotient is integral.

The very next operation attempts `nums[mid]`. Python lists reject float indices, so every valid nonempty input raises `TypeError` on the first iteration. Even a one-element list computes `mid` as `0.0`, which is not a legal list index.

A Python 3 repair must use `// 2` or a right shift. Once midpoint arithmetic is integral, all later boundary updates also remain integers and the intended algorithm operates as described.

**Why duplicates change the runtime guarantee**

With distinct or informative endpoint values, the algorithm chooses roughly half the interval. In an array such as `[1,1,1,1,1]` with absent target 2, the midpoint equals the left endpoint on every iteration. Only `left += 1` is possible, so the interval shrinks linearly. No comparison can tell which equal copy belongs to which side of the rotation.

This is not merely an implementation weakness: duplicates can erase the ordering information binary search needs. The intended method still benefits from logarithmic behavior when values reveal a sorted half, while accepting a linear worst case.

## Complexity detail

Under corrected integer midpoint semantics, informative iterations halve the interval, but ambiguous duplicate iterations may remove only one endpoint. Worst-case time is $O(n)$, matching the manifest; favorable behavior is $O(\log n)$. Only three indices are stored, so intended auxiliary space is $O(1)$.

For the exact Python 3 source, successful asymptotic bounds do not apply because the first list access uses a float index and raises `TypeError`. The manifest describes the intended Python 2 algorithm rather than executable behavior of the current file.

## Alternatives and edge cases

- **Python 3 repair:** Replace `/ 2` with `// 2` in midpoint calculation.
- **Right-endpoint classification:** Compare `nums[mid]` with `nums[right]` and shrink an ambiguous right duplicate; this is the strategy used by the optimal variant.
- **Trim both ends:** If left, middle, and right are equal and not the target, move both boundaries inward. It remains linear in the worst case.
- **Linear scan:** It avoids rotated-order logic but never receives the typical logarithmic benefit.
- **One element:** Intended integer search checks it once; exact Python 3 code still fails because `0.0` is not an index.
- **Midpoint target:** The first comparison returns true before any half classification.
- **Equal midpoint and left, absent value:** Incrementing left is safe because their shared value was already checked against target.
- **All duplicates:** Repeated one-step shrinking demonstrates worst-case linear time.
- **Unrotated input:** The ordered-half conditions reduce to standard binary-search decisions.
- **Target at a rotation boundary:** One of the ordered-run range tests retains the correct side.
- **Return annotation comment:** The docstring says integer return type, but the actual contract and return statements are Boolean.
- **Input preservation:** Intended search only reads `nums`.
- **Python-version fidelity:** The mathematical method is valid, but the selected file requires integer-division modernization before it can run.

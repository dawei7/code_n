## General

**Describe a continuous target as an interval**

An array of length $N$ is continuous exactly when its unique values are all integers in some interval

$$
[L,L+N-1].
$$

For a chosen target interval, every distinct existing value already inside it can stay. Every remaining array occurrence can be replaced with one of the interval values that is missing. Therefore operations equal

$$
N-\text{number of distinct existing values inside the interval}.
$$

The problem becomes finding a length-$N$ value interval containing as many distinct input values as possible.

**Remove duplicates before counting values to keep**

`nums = sorted(set(nums))` creates a sorted list of unique values. Duplicate input occurrences cannot both remain in a continuous result because the target requires uniqueness. Counting them twice inside a candidate interval would understate the necessary changes.

The original length is saved first in `n`. This distinction is essential: the target still needs $n$ elements even though the unique list may be shorter.

The assignment rebinds the local name and does not mutate the caller's input list.

**Use each unique value as a possible lower bound**

For index `i` and value `v`, consider target interval

`[v, v + n - 1]`.

`bisect_right(nums, v + n - 1)` returns the first index `j` after all unique values at most the interval's upper bound. Because `v=nums[i]` is the lower bound, unique values inside the interval occupy indices `i` through `j-1`.

Their count is `j - i`, so the required changes are `n - (j - i)`.

`ans` starts at `n` and retains the minimum candidate.

For `nums=[1,2,3,5,6]`, choose lower bound one and target interval one through five. Unique values one, two, three, and five already fit, so four values remain and only one occurrence must change, naturally becoming four. Choosing lower bound two gives interval two through six and also preserves four values. The method needs only the best preserved count, not the exact replacement assignment.

Either interval therefore certifies the same globally minimal one-operation answer.

**Why considering existing values as left endpoints is enough**

Take an optimal length-$N$ interval containing some set of input values. Slide its left boundary right until it reaches the smallest contained input value. No contained value leaves, the interval length remains $N$, and it may only gain usefulness at the right boundary.

Thus an equally good interval has a left endpoint equal to some unique input value. The loop considers it.

**Why the operation count is achievable**

Keep the `j-i` distinct in-range values. There are exactly `n-(j-i)` other occurrences: out-of-range values plus extra duplicates.

A length-$n$ interval contains $n$ distinct target integers, of which `j-i` are already occupied. Replace each other occurrence with a different missing target integer. One operation per occurrence completes a continuous array, so the formula is both a lower bound and achievable.

**Trace duplicates**

Suppose input is `[3,3,4,5,8]`, so $n=5$ and unique sorted values are `[3,4,5,8]`. For lower bound three, target interval is three through seven. Three distinct values stay; the duplicate three and out-of-range eight require two changes.

Counting both threes as already useful would incorrectly predict only one operation, which is why set conversion is mandatory.

**Why binary search is correct**

The unique list is sorted. `bisect_right` includes a value equal to `v+n-1`, matching the inclusive interval. It excludes the first larger value.

Every candidate therefore counts precisely the preserved distinct values for its target range.

## Complexity detail

Let $N$ be original length and $U$ the number of distinct values. Set construction is expected $O(N)$, sorting costs $O(U\log U)$, and $U$ binary searches cost $O(U\log U)$. Total is $O(N\log N)$.

The set and sorted unique list use $O(N)$ space in the worst case. The input list itself is not modified.

## Alternatives and edge cases

- **Sliding window on sorted unique values:** Move one right pointer monotonically while the span is below $N$, reducing the post-sort scan to $O(U)$.
- **Sort without deduplication:** Incorrectly treats duplicates as distinct values that can remain.
- **Try arbitrary integer lower bounds:** Unnecessary because an optimal interval can be shifted to begin at a contained value.
- **Already continuous:** One candidate contains $N$ unique values and returns zero.
- **All values equal:** Only one distinct value can remain, so $N-1$ operations are needed.
- **Single element:** Its one-value interval is already continuous.
- **Upper boundary equality:** Included by `bisect_right`.
- **Very large gaps:** At most a few values fit, and the rest are replaced directly.
- **Negative replacement values:** Operations permit any integer, though positive inputs already provide sufficient candidate anchors.
- **Original versus unique length:** Target width always uses original `n`.
- **No input mutation:** `sorted(set(nums))` creates new containers and rebinds the local variable.
- **Several optimal intervals:** Only their common minimum operation count matters.

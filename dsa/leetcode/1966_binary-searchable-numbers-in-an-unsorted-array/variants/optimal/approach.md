## General

**Characterize when no pivot can discard the target**

Fix target `nums[i] = x`. A pivot chosen to the left of $i$ remains in the same current contiguous sequence as $x$ until one of them is discarded. If that left pivot is greater than $x$, the algorithm takes the “pivot greater than target” branch and removes the pivot and everything to its right—including $x$. Therefore every value left of $i$ must be less than $x$.

Symmetrically, if any value to the right is less than $x$, choosing it as pivot takes the “pivot less than target” branch and removes that pivot and everything to its left, including $x$. Therefore every value right of $i$ must be greater than $x$.

These two conditions are also sufficient. Any left pivot is smaller, so it removes only itself and earlier positions while preserving the target. Any right pivot is larger, so it removes itself and later positions while preserving the target. Repeating arbitrary safe removals eventually selects $x$. Thus $x$ is guaranteed searchable exactly when:

$$
\max(\text{left values}) < x < \min(\text{right values}).
$$

Empty sides impose no restriction.

**Mark the left condition with a running maximum**

`ok` begins with one for every index. The forward scan maintains `mx`, the greatest value seen earlier.

If current `x < mx`, some earlier value is greater and can destroy the target, so `ok[i]` becomes zero. Otherwise `x` becomes the new running maximum.

Values are unique. Therefore equality with `mx` cannot occur at a later position; the source's strict comparison is sufficient.

The sentinel `-1000000` lies below the allowed minimum, so the first element always passes its empty-left condition.

**Mark the right condition with a running minimum**

The backward scan maintains `mi`, the smallest value seen to the right. If `nums[i] > mi`, a smaller right pivot exists and can discard the target, so the index is invalidated. Otherwise the current value becomes the new suffix minimum.

Sentinel `1000000` lies above every allowed value, so the final array element passes its empty-right condition.

An index stays one only when it is a prefix maximum and a suffix minimum in the strict unique-value sense. `sum(ok)` counts those guaranteed targets.

**Example**

For `[-1,5,2]`, the forward scan keeps all three initially except two, which is below previous maximum five. The backward scan invalidates five because smaller value two lies to its right. Negative one satisfies both conditions and is the only remaining one.

**Why current subarrays do not weaken the condition**

One might wonder whether a dangerous pivot could be removed before it gets chosen. Guarantee means every possible pivot sequence, so an adversary may choose the dangerous pivot immediately while the full array is present. Its existence is enough to make the target not guaranteed.

When no dangerous value exists, every possible pivot preserves the target as shown above. The property remains true in every smaller surviving contiguous interval because removing elements cannot introduce a new violating value. This completes the necessity-and-sufficiency proof.

**Follow an arbitrary safe pivot sequence**

Suppose the target is at index $i$ and satisfies both extrema conditions. If a pivot is selected left of $i$, its value is smaller than the target. The algorithm deletes that pivot and everything farther left, moving the surviving interval's left boundary rightward but not past $i$. If a pivot is selected right of $i$, its value is larger and the algorithm moves the right boundary leftward without crossing $i$.

At every iteration the target remains in the surviving interval. The interval strictly shrinks whenever the target itself is not chosen, so after finitely many steps the target must be selected. This proves “every possible pivot selection,” not merely the existence of one favorable sequence.

**Why both record conditions are needed**

Being a prefix maximum alone protects against dangerous left pivots but says nothing about the right. Being a suffix minimum alone protects only the right. A number must be both. For instance, the five in `[-1,5,2]` is a prefix maximum, but two on its right is smaller and can delete it; the backward pass catches that failure.

The array `ok` allows either pass to invalidate an index permanently. A zero never needs to become one again because one witnessed dangerous pivot is enough to disprove the guarantee.

## Complexity detail

Let $N$ be the array length.

The forward scan, backward scan, and final sum each take $O(N)$ time. Total time is $O(N)$.

The `ok` list stores $N$ flags, so auxiliary space is $O(N)$. Running extrema use constant space. A variant could combine prefix and suffix information differently but still needs some stored information unless mutating or performing additional passes.

## Alternatives and edge cases

- **Prefix and suffix arrays:** Explicitly store the maximum to each left and minimum to each right, then test every index. It is equivalent but uses two $O(N)$ arrays instead of one flag array.
- **Sort and compare positions:** With unique values, a searchable number occupies the same relative position under certain partition properties, but sorting costs $O(N\log N)$.
- **Simulate pivot choices:** The number of possible pivot sequences is exponential and unnecessary once the extrema criterion is derived.
- **Single element:** Both sides are empty, so it is guaranteed and the answer is one.
- **Strictly increasing array:** Every left value is smaller and every right value larger for every index, so all numbers count.
- **Strictly decreasing array:** Only when $N=1$ can an index satisfy both conditions; for longer arrays none count.
- **Negative values:** Sentinels are outside the stated range, so extrema initialization remains safe.
- **Unique-value dependency:** With duplicates, equality and pivot-removal behavior require carefully changing strict conditions, as the follow-up suggests.
- **Both extrema required:** A prefix record can still fail because of the suffix, and a suffix record can still fail because of the prefix.
- **Permanent invalidation:** Once either pass writes zero, the other pass cannot restore the guarantee.
- **Dangerous pivot first:** A single violating value proves failure because it may be selected before any helpful removal.
- **Finite progress:** Every non-target pivot removes itself, so a target that is never discarded must eventually be chosen.
- **Sum of flags:** Flags are integers zero or one, so summation directly returns the count.

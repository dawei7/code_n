## General

After removing `nums[left + 1:right]`, the retained array consists of a prefix
ending at `left` and a suffix beginning at `right`. It is strictly increasing
exactly when the retained prefix is strictly increasing, the retained suffix is
strictly increasing, and—when both are non-empty—`nums[left] < nums[right]`.

**Locate the longest usable prefix.** Move `left` across the initial strictly
increasing run. If it reaches the final element, the whole input is already
strictly increasing. Every non-empty subarray can then be removed, giving
$N(N+1)/2$ choices.

Otherwise, first count the `left + 2` removals that end at the final element:
their retained prefixes end at indices `-1` through `left`, where `-1` denotes
the empty prefix.

**Extend a strictly increasing suffix.** Start `right` at the final element and
move it left only while the suffix beginning there remains strictly increasing.
For each such suffix, decrease `left` until the retained prefix is empty or its
last value is smaller than `nums[right]`. Every prefix ending from `-1` through
this adjusted `left` can be joined to the current suffix, so it contributes
`left + 2` valid removals.

The prefix pointer never needs to move right. As the suffix grows leftward,
its new first value is smaller than the previous first value, so any prefix
that failed the bridge comparison before cannot become compatible later.
Consequently, each counted pair joins two internally increasing pieces with a
valid strict boundary, and every valid removal appears once for its unique
retained prefix and suffix.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$. Both pointers move only left-to-right or
right-to-left across the array once, so the running time is $O(N)$. The method
uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate and rebuild every remainder:** Testing each removed interval directly is simple and correct, but copying and scanning each remainder takes $O(N^3)$ time.
- **Prefix and suffix validity tables:** Checking every endpoint pair with precomputed increasing flags takes $O(N^2)$ time and $O(N)$ space; the monotonic compatibility boundary makes that extra enumeration unnecessary.
- **Already strictly increasing:** Every non-empty subarray is incremovable, including the whole array.
- **Empty retained side:** An empty prefix, empty suffix, or wholly empty remainder is strictly increasing and needs no bridge comparison.
- **Equal adjacent values:** Equality fails strict increase, both inside a retained side and across the newly formed boundary.
- **Single element:** Its only non-empty subarray is the whole array, so the answer is `1`.

## General

The exact solution creates a completely sorted reference array and asks where the original differs from that reference. This gives a direct characterization of the required interval:

> The shortest subarray that must be sorted starts at the first index whose value differs from the fully sorted array and ends at the last differing index.

Everything before the first mismatch is already exactly what the final sorted array needs. Everything after the last mismatch is also already correct. Every mismatch between those boundaries must be allowed to change, so the whole interval is necessary.

**Creating the target arrangement**

`arr = sorted(nums)` returns a new list containing the same values as `nums` in non-decreasing order. It does not mutate the input. Because sorting the whole original is the desired final condition, `arr` is an explicit model of the target arrangement.

Duplicates are handled naturally. Sorting does not require strict increase; equal adjacent values are valid. Comparing values position by position is sufficient even though equal elements are indistinguishable, because the sorted value sequence is unique as a sequence of values.

**Finding the first mismatch**

The left pointer begins at zero:

```python
while l <= r and nums[l] == arr[l]:
    l += 1
```

As long as the original value already equals the target at `l`, that position does not need to be included. Advancing `l` skips the longest matching prefix. The guard `l <= r` prevents the pointers from crossing and then indexing beyond the unresolved interval.

When this loop stops, either all positions matched, or `l` is the first index where the original differs from sorted order. Every index before `l` is already fixed and can remain outside the subarray.

**Finding the last mismatch**

The right pointer begins at the last index and moves left while values agree:

```python
while l <= r and nums[r] == arr[r]:
    r -= 1
```

This skips the longest matching suffix without crossing the left pointer. If an unsorted interval exists, `r` finishes at its final mismatch. Every index after `r` already equals its final target value and need not be sorted.

The result is `r - l + 1`, the inclusive interval length. If the whole array was already sorted, the first loop advances `l` to $n$ while $r=n-1$. The second loop does not run because `l <= r` is false. The expression becomes $(n-1)-n+1=0$, correctly representing that no subarray needs sorting.

**Why sorting exactly this interval works**

Let `arr` be the sorted copy, and suppose mismatches exist from $l$ through $r$. The prefix before $l$ and suffix after $r$ already equal `arr`. Also, `nums` and `arr` contain the same multiset of values globally. Since their outside portions are equal position by position, removing those equal outside values leaves the same multiset inside indices $[l,r]$ in both arrays.

Sorting `nums[l:r+1]` therefore arranges that remaining multiset exactly as the corresponding non-decreasing slice `arr[l:r+1]`. The outside positions stay unchanged and already equal `arr`. After the subarray sort, the entire array equals `arr` and is non-decreasing.

**Why no shorter interval can work**

Any index where `nums[i] != arr[i]` must be affected by the chosen operation. If a mismatching index lies outside the sorted subarray, its value never changes, so the final array cannot equal the uniquely determined sorted value sequence at that position.

In particular, every valid interval must include the first mismatch $l$ and the last mismatch $r$. Because the operation must act on one continuous subarray, including both endpoints forces it to include every index between them. Its length is therefore at least $r-l+1$. The proposed interval has exactly that length and works, so it is shortest.

For `[2,6,4,8,10,9,15]`, the sorted reference is `[2,4,6,8,9,10,15]`. Index 0 matches, so the first mismatch is index 1. Index 6 matches, while index 5 differs, so the last mismatch is index 5. The inclusive length is $5-1+1=5$, corresponding to `[6,4,8,10,9]`.

## Complexity detail

Let $n$ be the length of `nums`. Python’s `sorted` takes $O(n\log n)$ time in the general case and creates a new list of $n$ values. The two pointer scans together examine at most $O(n)$ positions. Sorting dominates, so the exact implementation takes $O(n\log n)$ time and $O(n)$ auxiliary space.

This is an important mismatch with the variant manifest, which declares $O(n)$ time and $O(1)$ space. Those bounds describe the constant-space boundary-discovery algorithm from the follow-up, but the exact protected source does not implement that algorithm: it explicitly calls `sorted(nums)` and stores `arr`. An accurate explanation must use the source’s actual $O(n\log n)$ time and $O(n)$ space rather than crediting it with an unrealized optimization.

Python’s sorting implementation may also use internal temporary memory, but the explicit $n$-element copy alone is enough to establish $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Linear-time constant-space boundary discovery:** Scan left-to-right while tracking the maximum seen; whenever a value is below that maximum, update the right boundary. Scan right-to-left while tracking the minimum seen; whenever a value is above that minimum, update the left boundary. This achieves the manifest’s $O(n)$ time and $O(1)$ space but is not the exact source shown here.
- **Monotonic stacks:** One increasing-stack pass finds the left boundary and one decreasing-stack pass finds the right. Time is $O(n)$ but stack space is $O(n)$.
- **Find disorder, then expand by its minimum and maximum:** Detect the first and last local inversions, find the interval’s minimum and maximum, and expand into the sorted prefix/suffix where needed. This is $O(n)$ and $O(1)$ but requires a careful multi-step proof.
- **Already sorted array:** Every position matches `arr`; crossed pointers make the returned length zero.
- **Single element:** It necessarily matches its sorted copy, so the answer is zero.
- **All values equal:** Non-decreasing order permits equality, every position matches, and the answer is zero.
- **Entire array reversed:** Usually the first and last positions mismatch, so the required interval is the whole array.
- **Duplicates near a boundary:** Looking only for a local inversion can choose a boundary that is too narrow. Comparing against the fully sorted sequence handles duplicate placement correctly.
- **Inclusive length:** Boundaries $l$ and $r$ are both included, so the formula must be $r-l+1$, not $r-l$.
- **Input preservation:** `sorted(nums)` returns a copy. Using `nums.sort()` would destroy the original before comparison unless another copy were made.
- **Metadata fidelity:** Do not describe this particular implementation as $O(n)$/$O(1)$. That improvement belongs to an alternative implementation, even though the manifest requests it.

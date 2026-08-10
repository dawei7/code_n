## General

**Removing elements means selecting a subsequence**

After arbitrary removals, the retained values stay in their original relative order. The desired mountain is therefore a subsequence of `nums`: it must strictly increase to some retained peak and then strictly decrease. Minimizing removals is equivalent to maximizing the length of such a mountain subsequence.

For every original index `i`, the source computes two lengths:

- `left[i]` is the longest strictly increasing subsequence ending at `i`;
- `right[i]` is the longest strictly decreasing subsequence starting at `i`.

If `i` is chosen as the peak, these two subsequences can be joined at `nums[i]`. Their combined length is `left[i] + right[i] - 1` because the peak belongs to both and must be counted once.

**Compute increasing lengths ending at each index**

Every `left[i]` starts at one, representing the subsequence containing only `nums[i]`. For each `i` from left to right, the inner loop examines every earlier index `j < i`.

If `nums[i] > nums[j]`, a strictly increasing subsequence ending at `j` can be extended with `nums[i]`. Its new length is `left[j] + 1`, and

`left[i] = max(left[i], left[j] + 1)`

keeps the best predecessor.

When `nums[i] <= nums[j]`, using `j` immediately before `i` would violate strict increase, so no transition is made. By the time `i` is processed, every `left[j]` it depends on is final.

**Compute decreasing lengths starting at each index**

The right array also begins with ones. Indices are now processed from right to left so that every later state is ready first. For a fixed `i`, the loop examines `j > i`.

If `nums[i] > nums[j]`, placing `nums[j]` after `nums[i]` makes a strict downward step. A decreasing subsequence starting at `j` can therefore be prefixed by `nums[i]`, giving length `right[j] + 1`. Taking the maximum over all valid later choices gives `right[i]`.

Although both recurrences use the comparison `nums[i] > nums[j]`, their directions differ: the left pass extends upward into `i`, while the right pass extends downward away from `i`.

**Reject endpoints and flat-sided peaks**

A valid mountain must have at least one increasing edge before its peak and at least one decreasing edge after it. Therefore a candidate index is valid only when `left[i] > 1` and `right[i] > 1`.

The generator expression filters on exactly these conditions. This prevents a largest increasing subsequence ending at the last element, with no descent, from being mistaken for a mountain. It likewise excludes a purely decreasing sequence whose “peak” would be its first retained value.

The problem guarantees that some mountain can be formed, so the filtered generator is nonempty and `max(...)` is safe.

**Why combining the two lengths is valid**

Take an increasing subsequence ending at `i` of length `left[i]` and a decreasing subsequence starting at `i` of length `right[i]`. All indices in the first part occur at or before `i`, and all indices in the second occur at or after `i`. Their only shared index is the peak. Concatenating them while including the peak once creates a valid mountain subsequence of length `left[i] + right[i] - 1`.

Conversely, any mountain subsequence has some original peak index `i`. Its increasing side cannot be longer than `left[i]`, and its decreasing side cannot be longer than `right[i]`. Therefore its total length is no greater than that same combined bound. Maximizing the bound across valid peaks finds the longest possible mountain subsequence.

If that maximum length is `L`, retaining those `L` elements and removing the other `n - L` produces a mountain. No solution can remove fewer, because that would retain a longer mountain subsequence than the maximum. The returned expression `n - max(...)` is thus the minimum removal count.

For `[1, 3, 1]`, the center has `left = 2` and `right = 2`, yielding mountain length three and zero removals. Equal neighboring values never extend either state because the comparisons are strict.

## Complexity detail

Let `n` be the array length. The left pass considers

$$
\sum_{i=1}^{n-1} i = O(n^2)
$$

index pairs. The right pass considers the same order of pairs. The final zipped maximum scans `n` entries. Total running time of this exact implementation is $O(n^2)$.

The two length arrays each contain `n` integers, so auxiliary space is $O(n)$. The generator used by `max` is lazy and does not allocate another length-`n` list.

The package manifest claims $O(n\log n)$ time, which corresponds to the editorial’s binary-search LIS method, not the nested-loop source shown here. The exact implementation is quadratic and remains practical under the given `n <= 1000` constraint.

## Alternatives and edge cases

- **Binary-search LIS profiles:** Maintain minimal tails while scanning left-to-right and right-to-left to compute per-index lengths in $O(n\log n)$ time and $O(n)$ space. This matches the manifest but is more subtle than the exact DP.
- **Try every removal subset:** This is exponential and ignores the subsequence structure captured by LIS/LDS states.
- **Use non-strict comparisons:** Replacing `>` with `>=` is incorrect because a mountain must be strictly increasing and strictly decreasing; equal adjacent retained values are forbidden.
- **Peak at an original endpoint:** It fails one of the `> 1` filters, even if removals could change surrounding indices. A valid retained peak still needs an original index on both sides.
- **Peak after removing many interior values:** Subsequence DP naturally skips arbitrary elements, so the increasing and decreasing sides need not be contiguous in `nums`.
- **Several possible peaks:** The generator evaluates all valid indices and keeps the one producing the longest mountain, regardless of peak value or position.
- **Duplicate values:** Equal values cannot extend a strict side, but different copies may participate through other smaller or larger predecessors.
- **Already a mountain:** Its natural peak produces combined length `n`, so the method returns zero.
- **Minimum mountain length three:** A candidate with `left == 2` and `right == 2` yields combined length three and is valid.
- **Guaranteed feasibility:** Without the guarantee, the filtered `max` could receive no values. A generalized implementation should then handle that case explicitly.
- **Input preservation:** The algorithm never sorts or reverses `nums`; all subsequence relationships use original order.

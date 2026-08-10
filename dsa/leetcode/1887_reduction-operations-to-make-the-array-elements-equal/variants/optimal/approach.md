## General

**The final value must be the original minimum.** An operation only lowers a current largest value to the next smaller distinct value already present. It never creates a value below the current minimum, and the minimum elements are never selected while a larger value exists. Therefore every element ultimately becomes the original minimum. The remaining question is how many distinct value levels each occurrence must descend.

**Sort values into a staircase.** After `nums.sort()`, equal values form contiguous groups and distinct values appear from smallest to largest. Moving left to right crosses one boundary whenever the current value differs from the previous value. If an element lies in the first distinct group, it is already at the minimum and needs zero reductions. An element in the second distinct group must descend one level, an element in the third group must descend two levels, and so on.

Variable `cnt` records how many distinct-value boundaries have been crossed so far. It starts at zero for the minimum group. `pairwise(nums)` yields each adjacent pair `(a, b)`. When `a != b`, `b` begins a new higher value group, so `cnt` increases by one. Whether or not the values differ, the code then adds `cnt` for occurrence `b` to `ans`.

**Why each occurrence's level count equals its operation count.** Consider an original value at the $k$-th distinct level above the minimum. The only values to which it can be reduced are successive next-largest values. To reach the minimum, that occurrence must be chosen once to cross each of the $k$ lower distinct boundaries. It cannot skip a level because an operation specifically replaces the current maximum with the next smaller distinct value. It cannot require more than one operation per boundary because one selection moves it exactly to the next level. Thus its total contribution is exactly $k$.

The actual global operation order interleaves different occurrences. A highest element may descend one step, join an existing group, and wait while other current maxima are processed. That interleaving does not change how many times each occurrence crosses a distinct level. Summing per-occurrence level counts therefore gives the same total as simulating the mandated smallest-index tie breaking.

**Trace `[1, 1, 2, 2, 3]`.** The array is already sorted. Pair `(1, 1)` crosses no boundary, so zero is added for the second one. Pair `(1, 2)` starts level one, so one is added for the first two. Pair `(2, 2)` remains at level one and adds another one for the second two. Pair `(2, 3)` starts level two and adds two for the three. The total is `0 + 1 + 1 + 2 = 4`, matching the four required operations.

**Understand what `pairwise` counts.** The first sorted element is not emitted as a second component and contributes zero, which is correct because it belongs to the minimum group. Every later element appears exactly once as `b`. Duplicate elements after the first in a group receive the same current `cnt`. The first element of a new group increments `cnt` before contribution, so it and all later duplicates in that group receive the newly correct level number.

**Why the smallest-index rule does not affect the answer.** When several maximum elements are equal, the rule specifies which occurrence descends first. Every occurrence in that maximum group must eventually descend to the next level before any lower level can become the unique maximum stage. Choosing one equal occurrence before another changes intermediate indices but not the number of selections. The sorted counting method intentionally ignores identities because only the total is requested.

**Why the sum is both necessary and achievable.** Every occurrence above the minimum must cross every lower distinct boundary, giving a lower bound equal to the accumulated level counts. The stated operation always moves one currently maximal occurrence down exactly one such boundary. Repeatedly applying it eventually performs all required crossings and no others. Therefore the lower bound is achieved, proving `ans` is the exact number of operations.

**Input mutation is explicit.** `nums.sort()` rearranges the caller-provided list. The challenge only asks for a count and does not require preserving order, so this is valid. A caller needing the original order would have to sort a copy. `pairwise` is lazy and does not allocate all adjacent pairs.

## Complexity detail

Let $n$ be the number of elements. Sorting costs $O(n\log n)$ time. `pairwise` then yields $n-1$ adjacent pairs, and the loop performs constant work for each, adding $O(n)$ time. The total is $O(n\log n)$.

Python's in-place Timsort may require $O(n)$ temporary auxiliary memory in the worst case. The answer, counter, and pairwise iterator use $O(1)$ additional state beyond the sort workspace. Thus the exact worst-case auxiliary bound is $O(n)$, matching the manifest, even though the input list itself is reused.

The maximum operation count occurs when all $n$ values are distinct: contributions are `0, 1, ..., n - 1`, totaling $n(n-1)/2$. For $n=5\cdot10^4$, that exceeds a signed 32-bit integer. Python handles it automatically; fixed-width implementations need a 64-bit accumulator.

## Alternatives and edge cases

- **Descending frequency accumulation:** Sort descending or count frequencies, maintain how many elements are currently above the next distinct level, and add that count at each boundary. This derives the same total from group sizes rather than per-occurrence levels.
- **Counting array:** Values are bounded by $5\cdot10^4$, so a frequency array can scan the value domain in $O(n+V)$ time and $O(V)$ space. It can outperform comparison sorting when the bounded range is exploited.
- **Simulate every operation:** Repeatedly finding and lowering one maximum directly performs the requested process but can be quadratic or worse without careful structures. Counting inevitable level crossings avoids mutation per operation.
- **All elements equal:** Sorting leaves no unequal adjacent pair, `cnt` remains zero, and the answer is zero.
- **Single element:** `pairwise` yields nothing, so zero is returned. The only element is already equal to every element in the array.
- **Duplicate groups:** Every occurrence in a distinct group receives the same number of lower levels. Duplicates affect the total through multiplicity, not through extra level boundaries.
- **Large gaps between values:** Reducing from `100` to `2` is one operation if `2` is the next smaller distinct value. Numeric distance is irrelevant; only the number of represented levels matters.
- **Smallest-index tie rule:** It determines the sequence of indices in a simulation but not the total count. No index tracking is required.
- **Input preservation:** The exact method sorts `nums` in place. Replace it with `sorted(nums)` if external code must observe the original ordering afterward.

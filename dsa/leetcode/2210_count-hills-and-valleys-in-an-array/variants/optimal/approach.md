## General

Equal adjacent values form one plateau and must count as a single hill or valley. Instead of searching left and right from every position, the exact solution processes only the final index of each plateau.

Variable `j` records a representative of the previous distinct plateau. At a processed plateau end `i`, `nums[i + 1]` is the next distinct value. Comparing these three values is enough.

**Why plateaus can be compressed**

Every index inside one equal run has the same value and the same closest non-equal values outside that run.

Therefore all of those indices are part of the same hill, the same valley, or neither. Counting more than one index from the run would double-count the same feature.

The algorithm chooses the run's final index as its one representative because the next array position is then immediately available as the right non-equal neighbor.

**Skip an index that is not the plateau end**

When `nums[i] == nums[i + 1]`, the equal run continues to the right. Index `i` cannot yet identify the closest non-equal right neighbor.

The code continues without changing `j`. This preserves the previous distinct plateau until the current run reaches its final position.

**Interpret `j` as the left distinct reference**

Initially `j = 0`. Each time a plateau end is processed, the code sets `j = i`.

For a normal internal plateau, this makes `nums[j]` the value of the immediately preceding distinct run when the next plateau end is reached. Any equal values between `j` and that later `i` belong to the later plateau and were skipped.

At the starting plateau, `j` may point to an equal value rather than a non-equal left neighbor. Both strict comparisons then fail, correctly preventing the boundary plateau from being counted when no left non-equal neighbor exists.

**Recognize a hill**

At a processed index `i`, the right neighbor `nums[i + 1]` differs because continuing equal values were skipped.

The condition

`nums[i] > nums[j] and nums[i] > nums[i + 1]`

says the plateau value exceeds both closest distinct neighbors. It is therefore one hill, and `ans` increases once.

**Recognize a valley**

The second condition checks strict inequality in the opposite direction:

`nums[i] < nums[j] and nums[i] < nums[i + 1]`.

When true, the plateau is below both surrounding distinct values and is one valley.

The hill and valley predicates cannot both be true for the same plateau, so using two independent `if` statements cannot add two.

**Handle the ending plateau**

The outer loop ends at index `len(nums) - 2`. If an equal run extends through the final element, every candidate index in that run is skipped because it equals its next element.

That is correct: the ending plateau has no non-equal neighbor on its right and cannot be a hill or valley.

If the penultimate position differs from the last, it is a complete internal plateau candidate with the final element as its right neighbor and is processed normally.

**Why every feature is counted exactly once**

Each internal equal run has one final index before a different value. The loop reaches that index once and compares its value against the preceding distinct plateau via `j` and the following distinct value via `i + 1`.

If both neighbors are lower, it adds one hill; if both are higher, it adds one valley; otherwise it adds nothing. Other indices of the run are skipped.

Boundary runs fail or are skipped because one required side is missing. Thus every qualifying hill or valley contributes exactly one and no nonqualifying run contributes.

For `[2,4,1,1,6,5]`, value four is processed as a hill. The first one is skipped because its plateau continues; the second one is processed as one valley. Six is then processed as a hill, yielding three.

## Complexity detail

The loop visits each internal index once and performs constant work. No backward or forward searches are repeated, so time is $O(n)$.

Only `ans`, `j`, `i`, and comparisons are stored, giving $O(1)$ auxiliary space. The input list is not modified. The manifest bounds match the exact solution.

## Alternatives and edge cases

- **Explicitly compress duplicates:** Build a new array containing one value per plateau, then count strict local extrema. It is conceptually simple but uses $O(n)$ extra space.
- **Scan for neighbors per index:** Searching left and right works but can cost $O(n^2)$ across long plateaus.
- **All values equal:** Every internal index is skipped, and the answer is zero.
- **Strictly increasing array:** Every internal value lies between its neighbors, so there are no hills or valleys.
- **Strictly decreasing array:** The same reasoning gives zero.
- **Starting plateau:** It lacks a distinct left neighbor and is not counted.
- **Ending plateau:** It lacks a distinct right neighbor and is not counted.
- **Single-element plateau:** It is processed immediately when its next value differs.
- **Long internal plateau:** Only its final index is evaluated.
- **Alternating values:** Every internal singleton may alternate between hill and valley.
- **Strict comparisons:** Equal neighboring plateau values are compressed rather than treated as higher or lower.
- **Two independent conditions:** Mutual exclusivity prevents double increment.
- **Input preservation:** The array remains unchanged; compression is logical through pointer `j`.

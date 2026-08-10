## General

**Find the two important positions in one scan**

Only the positions of the minimum and maximum matter. Their actual values are used to locate them, but the deletion count depends on how far their indices are from the two ends.

The variables `mi` and `mx` start at index 0. While enumerating `nums`:

- if `num < nums[mi]`, `mi` becomes the current index;
- if `num > nums[mx]`, `mx` becomes the current index.

The values are distinct, so for arrays longer than one there is one unique minimum index and one unique maximum index. For a one-element array, index 0 is both.

The two comparisons are independent `if` statements. That is appropriate because each current value is considered separately against the known extremes, and initialization handles the first element.

**Normalize the positions into left-to-right order**

After the scan, the code swaps the indices when `mi > mx`. From that point onward, `mi` is the leftmost of the two extreme-element positions and `mx` is the rightmost.

The variable names still originated as minimum and maximum indices, but after a swap their left/right ordering is what the formulas use. Whether the smaller value lies left or right is irrelevant; both elements must be deleted.

Normalizing once avoids writing symmetric formulas for both possible arrangements.

**There are only three useful deletion strategies**

Every deletion removes from the front or the back. With left important index `mi` and right important index `mx`, an optimal plan has one of three forms.

**Delete both from the front.** To remove the element at `mx`, the first `mx + 1` elements must be deleted. This automatically removes the element at `mi` because `mi <= mx`. The cost is

`mx + 1`.

**Delete both from the back.** To remove the element at `mi`, all elements from `mi` through `n - 1` must be deleted. This automatically includes `mx`. The cost is

`n - mi`.

**Split the deletions between both ends.** Delete from the front through `mi`, costing `mi + 1`, and from the back through `mx`, costing `n - mx`. The total is

`mi + 1 + n - mx`.

The source returns the minimum of these three values.

**Why no fourth strategy is needed**

After any sequence of front and back deletions, the undeleted elements, if any, form one contiguous interval of the original array. To exclude both important positions from that remaining interval:

- both may lie to the left of it, which is the front-only strategy;
- both may lie to the right, which is the back-only strategy;
- the left important position may lie to its left and the right important position to its right, which is the split strategy.

These cases are exhaustive.

Trying to remove the right important element from the front and the left important element from the back deletes overlapping ranges or the whole array. It cannot beat simply deleting both from one suitable side and is already dominated by the three candidates.

The order in which front and back deletions are interleaved does not change how many are needed. Only the final prefix length and suffix length matter.

**Trace the first example**

For `nums = [2, 10, 7, 5, 4, 1, 8, 6]`, the maximum lies at index 1 and minimum at index 5. After normalization, `mi = 1` and `mx = 5` even though those normalized names now describe positions rather than value roles.

The candidates are:

- front only: `5 + 1 = 6`;
- back only: `8 - 1 = 7`;
- split: `1 + 1 + 8 - 5 = 5`.

The split plan removes two elements from the front and three from the back, so the answer is 5.

For `nums = [0, -4, 19, 1, 8, -2, -3, 5]`, the important positions are 1 and 2. Front-only cost is 3, which beats the alternatives.

**Why the minimum of the formulas is correct**

Each of the three formulas describes a feasible deletion plan that removes both extremes. Therefore, their minimum is achievable.

Conversely, every feasible plan leaves a contiguous middle interval and belongs to one of the three positional categories above. Within each category, the corresponding formula deletes the shortest prefix, suffix, or pair needed to exclude the important indices. No plan in that category can use fewer deletions.

Thus no valid plan costs less than the minimum formula, while that minimum itself is feasible. The returned result is optimal.

The algorithm never removes elements physically and never mutates `nums`. It calculates only the least required count.

## Complexity detail

Let $n$ be the length of `nums`.

The single scan that finds both extreme indices takes $O(n)$ time. The optional swap and evaluation of three arithmetic expressions take $O(1)$ time. Total time complexity is $O(n)$.

Only `mi`, `mx`, `i`, and `num` are stored in addition to the input. No sorted copy or deletion simulation is created, so auxiliary space complexity is $O(1)$.

This is asymptotically optimal in time because determining the minimum and maximum positions in an unsorted array requires inspecting every element in the worst case.

## Alternatives and edge cases

- **Sort value-index pairs:** Sorting can locate the minimum and maximum but costs $O(n\log n)$ and adds storage or mutation. One scan finds both positions optimally.
- **Simulate deletions:** Trying front and back operations step by step obscures that only prefix and suffix lengths matter. The three formulas evaluate every meaningful plan directly.
- **Four directional combinations:** After ordering the indices, the supposed combination that takes the right position from the front and left position from the back is dominated and unnecessary.
- **Minimum lies after maximum:** The swap normalizes the positions, so the same formulas apply without caring which value is on which side.
- **One-element array:** `mi == mx == 0`. Front-only and back-only candidates both equal one, so the answer is correctly one.
- **Two-element array:** Both elements are the extremes, and two deletions are required; the formulas return two.
- **Extremes at opposite endpoints:** The split formula gives one deletion from each side, totaling two.
- **Both extremes near the front:** The front-only candidate usually wins because reaching the farther one removes both.
- **Both extremes near the back:** The back-only candidate symmetrically wins.
- **Distinctness guarantee:** It makes the minimum and maximum positions unique. The one-element case legitimately uses the same position for both roles.
- **No physical mutation:** Returning a count does not require constructing the remaining array or changing the input.
- **Off-by-one boundaries:** Deleting through index `mx` from the front costs `mx + 1`, while deleting from index `mi` through the back costs `n - mi`.

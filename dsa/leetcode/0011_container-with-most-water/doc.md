# Container With Most Water

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 11 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/container-with-most-water/) |

## Problem Description
### Goal
The array `height` describes vertical lines drawn at consecutive horizontal positions: line `i` extends from the baseline to `height[i]`. Choose two different lines to act as the sides of a container together with the baseline.

The distance between their indices is the container width, and the shorter selected line limits the water height, giving area `(right - left) * min(height[left], height[right])`. Return the greatest area obtainable from any pair. The lines remain vertical and fixed in their original positions; the container cannot be tilted or rearranged.

### Function Contract
**Inputs**

- `height`: `List[int]` containing at least two non-negative wall heights

**Return value**

An `int` equal to the maximum value of `(right - left) * min(height[left], height[right])`.

### Examples
**Example 1**

- Input: `height = [1, 8, 6, 2, 5, 4, 8, 3, 7]`
- Output: `49`

**Example 2**

- Input: `height = [1, 1]`
- Output: `1`

**Example 3**

- Input: `height = [4, 3, 2, 1, 4]`
- Output: `16`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Start with the only pair having maximum width**

Place one pointer at each end. This pair has the greatest possible width. Record its area, then decide which boundary can be discarded without losing a potentially better answer.

**Discard the shorter wall by dominance**

Suppose the left wall is no taller than the right wall. Any container that keeps the left wall and moves the right boundary inward has both a smaller width and a height no greater than the left wall. It therefore cannot beat the current pair. The left boundary may be safely discarded, so move it inward. Apply the symmetric argument when the right wall is shorter.

When heights are equal, either one can be discarded by the same dominance argument.

**What remains after each discard**

Before each iteration, every pair excluded from the interval has either already been measured or is dominated by a measured pair with at least its width and limiting height. Thus an unmeasured optimum, if one exists, still has both endpoints inside the current interval.

Each step removes one endpoint, so only $n - 1$ pairs are evaluated.

**Trace a representative input**

For `[4, 3, 2, 1, 4]`, the first and last walls have width 4 and limiting height 4, giving area 16. Since the heights are equal, discard either endpoint. Every later width is smaller and the recorded best remains 16.

**Why the shorter wall can be discarded**

Suppose the left wall is no taller than the right. Any alternative container that keeps this left wall but moves the right endpoint inward has smaller width, while its height remains capped by the same left wall. Its area therefore cannot exceed the pair just measured. The left endpoint has exhausted its best possible partner and may be discarded safely. The symmetric argument applies when the right wall is shorter.

Every pointer movement removes only an endpoint whose remaining pairs are dominated by an already evaluated pair. When the pointers meet, every possible container is either measured directly or dominated at the moment one endpoint was removed. The maximum recorded area is therefore global.

#### Complexity detail

One pointer moves inward on every iteration, so at most $n - 1$ pairs are evaluated. Area calculation and the discard decision are constant-time operations, giving $O(n)$ time. Only two pointers and the best area are stored, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Enumerate every pair:** directly evaluates the definition but requires $O(n^2)$ time.
- **Sort walls by height:** loses the essential interaction between original distance and height unless additional position structures are maintained.
- **Prefix or suffix maxima:** identify tall walls but do not by themselves decide the width-height trade-off; the dominance proof gives a simpler linear scan.
- Equal endpoint heights allow either endpoint to move: every pair retaining one of those equally short walls has smaller width and no larger limiting height.
- Zero-height walls are handled without special cases; they contribute zero area and are discarded by the same rule.

</details>

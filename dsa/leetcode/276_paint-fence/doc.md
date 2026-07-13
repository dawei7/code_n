# Paint Fence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 276 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/paint-fence/) |

## Problem Description
### Goal
Given `n` fence posts in a row and `k` available colors, assign one color to every post. The only restriction is that no run of three consecutive posts may all have the same color; two adjacent posts may share a color.

Return the number of distinct valid colorings, where choices at labeled post positions make arrangements different. Colors may be reused throughout the fence as long as the length-three restriction holds. Account for short fences where no triple exists and for small color counts that sharply limit later choices. The function returns the count rather than enumerating the color sequences.

### Function Contract
**Inputs**

- `n`: number of fence posts
- `k`: available colors

**Return value**

The number of valid colorings.

### Examples
**Example 1**

- Input: `n = 3, k = 2`
- Output: `6`

**Example 2**

- Input: `n = 1, k = 1`
- Output: `1`

**Example 3**

- Input: `n = 3, k = 1`
- Output: `0`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**The last two posts contain all needed history**

Track valid colorings whose last two posts have the same color and those whose last two differ. A new same-color ending must extend a previously different ending; a different ending may extend either state with any of $k - 1$ new colors.

After each post, `same` and `different` partition every valid coloring according to whether its final two colors match. Their sum is the complete valid count.

**State transitions enumerate every legal extension once**

A same-colored ending can arise only by extending a previously different ending with its final color. A different ending can extend either prior state using any of the $k - 1$ colors unlike the previous post. These cases are disjoint and exhaustive, while the forbidden third identical post appears in neither. Induction therefore preserves the exact count.

#### Complexity detail

Each additional post performs constant arithmetic, giving $O(n)$ time and $O(1)$ space.

#### Alternatives and edge cases

- **Enumerate all color sequences:** takes exponential time.
- **Recompute every prefix DP:** is correct but can take $O(n^2)$.
- One post has `k` choices; with one color, at most two posts can be painted validly.

</details>

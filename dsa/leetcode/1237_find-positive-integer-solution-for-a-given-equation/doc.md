# Find Positive Integer Solution for a Given Equation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1237 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Two Pointers, Binary Search, Interactive |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/) |

## Problem Description

### Goal

You receive a callable hidden function $f(x,y)$ and a target `z`. The function returns a positive integer for positive integer arguments and is strictly increasing in each argument: increasing either $x$ or $y$ while fixing the other strictly increases the result.

Return every positive integer pair `[x, y]` for which $f(x,y)=z$, in any order. The judge selects one of nine hidden formulas through `function_id`; cOde(n) uses that identifier to reproduce the same deterministic function fixture. All valid coordinates lie between $1$ and $1000$, and `z` lies between $1$ and $100$.

### Function Contract

**Inputs**

- `function_id`: An integer from $1$ through $9$ selecting the monotone function fixture.
- `z`: The target positive integer, where $1\le z\le100$.

Let $r$ be the number of returned solution pairs.

**Return value**

- All positive integer pairs `[x, y]` satisfying $f(x,y)=z$, in any order.

### Examples

**Example 1**

- Input: `function_id = 1`, `z = 5`
- Output: `[[1,4],[2,3],[3,2],[4,1]]`

Fixture $1$ uses $f(x,y)=x+y$.

**Example 2**

- Input: `function_id = 2`, `z = 5`
- Output: `[[1,5],[5,1]]`

Fixture $2$ uses $f(x,y)=xy$.

**Example 3**

- Input: `function_id = 5`, `z = 25`
- Output: `[[3,4],[4,3]]`

Fixture $5$ uses $f(x,y)=x^2+y^2$.

### Required Complexity

- **Time:** $O(z)$
- **Space:** $O(r)$

<details>
<summary>Approach</summary>

#### General

**Bound the relevant square.** Because $f$ has positive integer values and increases strictly by at least one whenever either integer argument increases, $f(x,y)\ge x+y-1$. Consequently, a pair equaling `z` cannot have either coordinate greater than `z`.

**Walk the monotone frontier.** Start at `[1, z]`, the upper-left corner of the relevant square. If `f(x, y) < z`, every point with the current or smaller $x$ and this $y$ is too small, so increment `x`. If the value is greater than `z`, every point at this $x$ and the current or larger $y$ is too large, so decrement `y`. On equality, record the pair and move both pointers inward.

Each comparison discards an entire row or column portion that monotonicity proves cannot contain a solution. The pointers never reverse, so every possible equality on the decreasing frontier is encountered exactly once, and no discarded coordinate can satisfy the target.

#### Complexity detail

`x` increases at most `z` times and `y` decreases at most `z` times, so the frontier walk makes $O(z)$ calls to the hidden function. Apart from the $r$ returned pairs, it stores only two pointers and the current value, giving $O(r)$ total output space and $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Check the full grid:** Trying every pair from $1$ through `z` is correct but takes $O(z^2)$ function calls.
- **Binary search each row:** Searching $y$ independently for every $x$ takes $O(z\log z)$ calls and repeats monotone work.
- **No solution:** The pointers cross without recording a pair, producing an empty list.
- **Multiple solutions:** Moving both pointers after equality is safe because strict monotonicity forbids another match in the same row or column.
- **Small target:** For `z = 1`, only `[1,1]` could possibly qualify.
- **Unknown formula:** The algorithm relies only on the callable interface and monotonicity, not on identifying the formula.

</details>

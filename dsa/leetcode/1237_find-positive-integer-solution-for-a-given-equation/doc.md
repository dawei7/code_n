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

Return every positive integer pair `[x, y]` for which $f(x,y)=z$, in any order. The judge supplies the selected hidden formula through the `CustomFunction.f(x, y)` interface. All valid coordinates lie between $1$ and $1000$, and `z` lies between $1$ and $100$.

### Function Contract

**Inputs**

- `customfunction`: A `CustomFunction` object exposing the strictly increasing method `f(x, y)`.
- `z`: The target positive integer, where $1\le z\le100$.

Authored JSON cases represent `customfunction` by an integer from $1$ through $9$; the offline judge converts that identifier into the corresponding deterministic interface object.

Let $r$ be the number of returned solution pairs.

**Return value**

- All positive integer pairs `[x, y]` satisfying $f(x,y)=z$, in any order.

### Examples

#### Example 1

- **Input:** `customfunction = 1`, `z = 5`
- **Output:** `[[1,4],[2,3],[3,2],[4,1]]`

Fixture $1$ uses $f(x,y)=x+y$.

#### Example 2

- **Input:** `customfunction = 2`, `z = 5`
- **Output:** `[[1,5],[5,1]]`

Fixture $2$ uses $f(x,y)=xy$.

#### Example 3

- **Input:** `customfunction = 5`, `z = 25`
- **Output:** `[[3,4],[4,3]]`

Fixture $5$ uses $f(x,y)=x^2+y^2$.

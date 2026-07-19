# Egg Drop With 2 Eggs and N Floors

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/egg-drop-with-2-eggs-and-n-floors/) |
| Frontend ID | 1884 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

A building has floors numbered from $1$ through $N$, and you have two identical eggs. An unknown threshold $f$ lies between $0$ and $N$, inclusive. An egg survives every drop from floor $f$ or below and breaks from every higher floor.

On each move, choose any still-unbroken egg and any building floor. A surviving egg can be reused, but a broken one is lost. Determine the smallest number of moves that guarantees identifying the exact value of $f$ for every possible threshold and every sequence of drop outcomes.

### Function Contract

**Inputs**

- `n`: the number $N$ of floors, where $1 \le N \le 1000$.

**Return value**

- Return the minimum worst-case number of egg drops needed to determine $f$ with certainty.

### Examples

**Example 1**

- Input: `n = 2`
- Output: `2`

Testing floors `1` and `2` distinguishes all three possible thresholds.

**Example 2**

- Input: `n = 100`
- Output: `14`

Fourteen moves can cover $14+13+\cdots+1=105$ floors, whereas thirteen cover only $91$.

**Example 3**

- Input: `n = 3`
- Output: `2`

Drop first from floor `2`; either outcome leaves at most one floor to test.

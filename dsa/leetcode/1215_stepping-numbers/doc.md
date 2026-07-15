# Stepping Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1215 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Backtracking, Breadth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/stepping-numbers/) |

## Problem Description

### Goal

An integer is a **stepping number** when the absolute difference between every pair of adjacent decimal digits is exactly $1$. Every single-digit integer is therefore a stepping number because it has no adjacent digit pair to violate the condition.

Given two integers `low` and `high`, return every stepping number in the inclusive range `[low, high]`. The returned list must be sorted in increasing order.

### Function Contract

**Inputs**

- `low`: The inclusive lower bound, with $0\le\texttt{low}\le	exttt{high}$.
- `high`: The inclusive upper bound, with $\texttt{high}\le2\cdot10^9$.

Let $S$ be the number of stepping numbers from $0$ through `high`, inclusive.

**Return value**

- A list of all stepping numbers in `[low, high]`, sorted in increasing order.

### Examples

**Example 1**

- Input: `low = 0`, `high = 21`
- Output: `[0,1,2,3,4,5,6,7,8,9,10,12,21]`

The two-digit results qualify because their adjacent digits differ by exactly $1$; all one-digit values qualify automatically.

**Example 2**

- Input: `low = 10`, `high = 15`
- Output: `[10,12]`

### Required Complexity

- **Time:** $O(S)$
- **Space:** $O(S)$

<details>
<summary>Approach</summary>

#### General

**Generate only numbers that can qualify.** A positive stepping number cannot begin with zero, so place the one-digit values `1` through `9` into a breadth-first queue. If a dequeued number ends in digit `d`, any longer stepping number with that prefix must append either `d - 1` or `d + 1`. Append only the digits that remain within `0` through `9`, and do not enqueue a child larger than `high`.

**Keep the requested order without a final sort.** Breadth-first processing visits all one-digit numbers before all two-digit numbers, then all three-digit numbers, and so on. Within a fixed length, parent prefixes are processed in increasing order and each parent's smaller child is enqueued before its larger child. The generated positive values are consequently visited in increasing order. Add a visited value to the answer exactly when it is at least `low`; handle `0` separately because leading zero is not used as a generation seed.

**Why the generation is complete and exact.** Removing the last digit from any positive multi-digit stepping number leaves a shorter positive stepping number. Repeating that removal eventually reaches its nonzero first digit, which is one of the queue seeds. At each reconstruction step, the removed digit must differ from the current last digit by exactly $1$, so the breadth-first transitions recreate the number. Conversely, every transition appends precisely such a digit, so it cannot create a non-stepping number. Range checks then retain exactly the required values.

#### Complexity detail

Each of the $S$ generated stepping numbers is enqueued and removed at most once, and each removal performs constant work. The time is $O(S)$. The answer and breadth-first queue together hold $O(S)$ values. The numeric digit length is bounded by the input constraint and does not add a larger term.

#### Alternatives and edge cases

- **Scan every integer in the range:** Checking adjacent digits of every candidate is straightforward but takes time proportional to the width of the numeric interval rather than to the much smaller set of stepping numbers.
- **Depth-first generation plus sorting:** The same prefix transitions can be explored recursively, but arbitrary depth-first order requires an additional sort and uses recursion stack space.
- **Digit dynamic programming:** A digit-DP formulation is useful when only a count is requested over enormous string bounds, but it is unnecessary when this problem must enumerate the actual values under a 32-bit-scale bound.
- **Zero:** Include `0` exactly when `low` is `0`; never use it as a prefix for longer numbers.
- **Single-digit interval:** Every value from `0` through `9` is a stepping number.
- **Boundary digits:** A number ending in `0` has only a `1` child, while one ending in `9` has only an `8` child.
- **Inclusive endpoints:** Values equal to `low` or `high` must be returned when they satisfy the digit rule.

</details>

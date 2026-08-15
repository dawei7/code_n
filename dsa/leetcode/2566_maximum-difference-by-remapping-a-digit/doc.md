# Maximum Difference by Remapping a Digit

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2566 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [maximum-difference-by-remapping-a-digit](https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/) |

## Problem Description

### Goal

Given a positive integer `num`, choose one decimal digit and remap it to another decimal digit. A remapping replaces every occurrence of the chosen source digit in `num`; the source and destination may be the same, in which case the value is unchanged.

Determine the largest value obtainable by one remapping and, independently, the smallest value obtainable by one remapping. The two choices do not need to use the same source or destination digits, and a remapped representation may begin with zeroes. Return the difference between the maximum and minimum values.

### Function Contract

**Inputs**

- `num`: A positive integer satisfying $1 \le \texttt{num} \le 10^8$.

**Return value**

- The maximum obtainable remapped value minus the minimum obtainable remapped value.

### Examples

#### Example 1

- **Input:** `num = 11891`
- **Output:** `99009`
- **Explanation:** Remapping every `1` to `9` produces `99899`, while remapping every `1` to `0` produces the representation `00890`, whose value is $890$.

#### Example 2

- **Input:** `num = 90`
- **Output:** `99`
- **Explanation:** Replacing `0` with `9` gives $99$, while replacing `9` with `0` gives $0$.

#### Example 3

- **Input:** `num = 999`
- **Output:** `999`
- **Explanation:** The maximum remains $999$, and remapping `9` to `0` makes the minimum $0$.

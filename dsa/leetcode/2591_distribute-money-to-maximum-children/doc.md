# Distribute Money to Maximum Children

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2591 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/distribute-money-to-maximum-children/) |

## Problem Description

### Goal

You have `money` dollars and must distribute all of it among exactly `children` children. Every child must receive at least one dollar, and no child is allowed to receive exactly four dollars.

Among all distributions satisfying those rules, maximize the number of children who receive exactly eight dollars. Return that maximum, or return `-1` when even one valid distribution is impossible. Children may receive amounts other than eight, including amounts greater than eight, provided no amount is four and no money remains undistributed.

### Function Contract

**Inputs**

- `money`: The total number of dollars, with $1 \leq \texttt{money} \leq 200$.
- `children`: The number of recipients, with $2 \leq \texttt{children} \leq 30$.

**Return value**

- The greatest possible number of children receiving exactly eight dollars, or `-1` if no valid distribution exists.

### Examples

**Example 1**

- Input: `money = 20, children = 3`
- Output: `1`

One valid optimum is `[8,9,3]`. Trying to give eight dollars to two children would force the last child to receive four dollars.

**Example 2**

- Input: `money = 16, children = 2`
- Output: `2`

Both children can receive exactly eight dollars.

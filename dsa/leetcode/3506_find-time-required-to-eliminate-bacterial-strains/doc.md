# Find Time Required to Eliminate Bacterial Strains

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3506 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Greedy, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-time-required-to-eliminate-bacterial-strains/) |

## Problem Description

### Goal

One white blood cell must eliminate every bacterial strain in `timeReq`. Eliminating strain $i$ occupies one cell for `timeReq[i]` time units. Once that task finishes, the cell is exhausted and cannot split or eliminate another strain. Strains may be assigned in any order, but one strain cannot be attacked by multiple cells.

Before accepting an elimination task, a cell may instead spend `splitTime` time units dividing into two cells. The two descendants then act simultaneously and may independently split again or eliminate one strain each. All activity on separate branches happens in parallel.

Choose the splitting schedule and strain assignments that minimize the time at which every strain has been eliminated. Return that minimum completion time, measured from the moment the initial single cell starts.

### Function Contract

**Inputs**

- `timeReq`: A list in which `timeReq[i]` is the time one cell needs to eliminate strain $i$.
- `splitTime`: The fixed time required for one cell to divide into two cells.

Let $n=\lvert\texttt{timeReq}\rvert$. The constraints are $2 \le n \le 10^5$, $1 \le \texttt{timeReq[i]} \le 10^9$, and $1 \le \texttt{splitTime} \le 10^9$.

**Return value**

Return the minimum possible time until all bacterial strains have been eliminated.

### Examples

#### Example 1

- **Input:** `timeReq = [10,4,5], splitTime = 2`
- **Output:** `12`
- **Explanation:** Split once. One descendant handles the 10-unit strain, while the other splits again and assigns the 4- and 5-unit strains to its two descendants. The last completion occurs at time $12$.

#### Example 2

- **Input:** `timeReq = [10,4], splitTime = 5`
- **Output:** `15`
- **Explanation:** After one 5-unit split, the two descendants eliminate the strains in parallel. The slower branch finishes at time $15$.

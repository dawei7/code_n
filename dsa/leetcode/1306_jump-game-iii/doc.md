# Jump Game III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1306 |
| Difficulty | Medium |
| Topics | Array, Depth-First Search, Breadth-First Search |
| Official Link | [LeetCode](https://leetcode.com/problems/jump-game-iii/) |

## Problem Description
### Goal
An array `arr` of non-negative integers and a starting index `start` define a jumping process. From a current index $i$, the value `arr[i]` permits a jump to either $i+\texttt{arr[i]}$ or $i-\texttt{arr[i]}$.

A jump may be taken only when its destination remains inside the array. Determine whether some sequence of legal jumps from `start` can reach any index whose stored value is 0. Indices may otherwise be revisited by the raw movement rules, so the search must handle cycles.

### Function Contract
**Inputs**

- `arr`: an array of length $n$, where $1 \le n \le 5\cdot10^4$.
- Each `arr[i]` satisfies $0 \le \texttt{arr[i]} < n$.
- `start`: the initial index, where $0 \le \texttt{start} < n$.

**Return value**

`true` if at least one zero-valued index is reachable from `start` through legal jumps; otherwise, `false`.

### Examples
**Example 1**

- Input: `arr = [4,2,3,0,3,1,2]`, `start = 5`
- Output: `true`
- Explanation: One valid route is $5\to4\to1\to3$, and `arr[3] = 0`.

**Example 2**

- Input: `arr = [4,2,3,0,3,1,2]`, `start = 0`
- Output: `true`

**Example 3**

- Input: `arr = [3,0,2,1,2]`, `start = 2`
- Output: `false`
- Explanation: The zero at index 1 exists but is not in the component reachable from index 2.

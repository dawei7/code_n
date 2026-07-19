# Number of Visible People in a Queue

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1944 |
| Difficulty | Hard |
| Topics | Array, Stack, Monotonic Stack |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-visible-people-in-a-queue/) |

## Problem Description
### Goal
$N$ people stand in a queue from left to right, and `heights[i]` is the height
of person $i$. Every height is distinct. A person may see only people located
to the right.

For indices $i<j$, person $i$ can see person $j$ exactly when every person
strictly between them is shorter than both endpoint people. Equivalently,

$$
\min(\texttt{heights[i]},\texttt{heights[j]})
>
\max_{i<k<j}\texttt{heights[k]}.
$$

Adjacent people can always see one another because no person stands between
them. Return, for every queue position, the number of visible people to its
right.

### Function Contract
**Inputs**

- `heights`: an array of $N$ distinct integers, where
  $1 \le N \le 10^5$ and every height is between 1 and $10^5$.

**Return value**

- An array `answer` of length $N$ where `answer[i]` is the number of people to
  the right that person $i$ can see.

### Examples
**Example 1**

- Input: `heights = [10, 6, 8, 5, 11, 9]`
- Output: `[3, 1, 2, 1, 1, 0]`

**Example 2**

- Input: `heights = [5, 1, 2, 3, 10]`
- Output: `[4, 1, 1, 1, 0]`

**Example 3**

- Input: `heights = [4, 3, 2, 1]`
- Output: `[1, 1, 1, 0]`

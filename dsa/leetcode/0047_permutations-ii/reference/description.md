## Description

Given a collection of numbers, `nums`, that might contain duplicates, return *all possible unique permutations **in any order**.*
### Function Contract

**Inputs**

- `nums`: An integer array whose values may repeat.

Let $n = \lvert\texttt{nums}\rvert$.

**Return value**

Return every unique complete ordering of the input multiset, in any order.

### Examples
#### Example 1

- **Input:** `nums = [1,1,2]`
- **Output:** ``
[[1,1,2],
[1,2,1],
[2,1,1]]
#### Example 2

- **Input:** `nums = [1,2,3]`
- **Output:** `[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]`
### Constraints

- $1 \le \text{nums.length} \le 8$

- $-10 \le \text{nums}[i] \le 10$
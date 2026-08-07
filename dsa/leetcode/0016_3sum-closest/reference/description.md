### 1. Description

Given an integer array `nums` of length `n` and an integer `target`, find three integers at **distinct indices** in `nums` such that the sum is closest to `target`.

Return *the sum of the three integers*.

You may assume that each input would have exactly one solution.

### 2. Function Contract

**Inputs**

- `nums`: The integer array from which three distinct positions are selected.
- `target`: The value the selected sum should approach.

Let $n = \lvert\texttt{nums}\rvert$.

**Return value**

Return the unique three-value sum closest to `target`.

### 3. Examples

#### Example 1

- **Input:** `nums = [-1,2,1,-4], target = 1`
- **Output:** `2`
- **Explanation:** The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#### Example 2

- **Input:** `nums = [0,0,0], target = 1`
- **Output:** `0`
- **Explanation:** The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

### 4. Constraints

- $3 \le \text{nums.length} \le 500$

- $-1000 \le \text{nums}[i] \le 1000$

- $-10^{4} \le target \le 10^{4}$
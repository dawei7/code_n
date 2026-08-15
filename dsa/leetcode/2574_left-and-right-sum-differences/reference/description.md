### 1. Description

You are given a **0-indexed** integer array `nums` of size `n`.

Define two arrays `leftSum` and `rightSum` where:

- $\text{leftSum}[i]$ is the sum of elements to the left of the index `i` in the array `nums`. If there is no such element, $\text{leftSum}[i] = 0$.

- $\text{rightSum}[i]$ is the sum of elements to the right of the index `i` in the array `nums`. If there is no such element, $\text{rightSum}[i] = 0$.

Return an integer array `answer` of size `n` where $\text{answer}[i] = |\text{leftSum}[i] - \text{rightSum}[i]|$.

### 2. Function Contract

**Inputs**

- `nums`: Input parameter (`List[int]`).

**Return value**

- Returns `List[int]`.

### 3. Examples

#### Example 1

- **Input:** `nums = [10,4,8,3]`
- **Output:** `[15,1,11,22]`
- **Explanation:** The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].

#### Example 2

- **Input:** `nums = [1]`
- **Output:** `[0]`
- **Explanation:** The array leftSum is [0] and the array rightSum is [0].
The array answer is [|0 - 0|] = [0].

### 4. Constraints

- $1 \le \text{nums.length} \le 1000$

- $1 \le \text{nums}[i] \le 10^{5}$

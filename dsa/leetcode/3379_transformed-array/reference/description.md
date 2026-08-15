### 1. Description

You are given an integer array `nums` that represents a circular array. Your task is to create a new array `result` of the **same** size, following these rules:

For each index `i` (where $0 \le i < \text{nums.length}$), perform the following **independent** actions:

- If $\text{nums}[i] > 0$: Start at index `i` and move $\text{nums}[i]$ steps to the **right** in the circular array. Set $\text{result}[i]$ to the value at the index where you land.

- If $\text{nums}[i] < 0$: Start at index `i` and move $abs(\text{nums}[i])$ steps to the **left** in the circular array. Set $\text{result}[i]$ to the value at the index where you land.

- If $\text{nums}[i] = 0$: Set $\text{result}[i]$ to $\text{nums}[i]$.

Return the new array `result`.

### 2. Function Contract

**Inputs**

- `nums`: Input parameter (`List[int]`).

**Return value**

- Returns `List[int]`.

### 3. Note

Since `nums` is circular, moving past the last element wraps around to the beginning, and moving before the first element wraps back to the end.

### 4. Examples

#### Example 1

- **Input:** nums = [3,-2,1,1]

- **Output:** [1,1,1,3]

- **Explanation:** 

- For $\text{nums}[0]$ that is equal to 3, If we move 3 steps to right, we reach $\text{nums}[3]$. So $\text{result}[0]$ should be 1.

- For $\text{nums}[1]$ that is equal to -2, If we move 2 steps to left, we reach $\text{nums}[3]$. So $\text{result}[1]$ should be 1.

- For $\text{nums}[2]$ that is equal to 1, If we move 1 step to right, we reach $\text{nums}[3]$. So $\text{result}[2]$ should be 1.

- For $\text{nums}[3]$ that is equal to 1, If we move 1 step to right, we reach $\text{nums}[0]$. So $\text{result}[3]$ should be 3.

#### Example 2

- **Input:** nums = [-1,4,-1]

- **Output:** [-1,-1,4]

- **Explanation:** 

- For $\text{nums}[0]$ that is equal to -1, If we move 1 step to left, we reach $\text{nums}[2]$. So $\text{result}[0]$ should be -1.

- For $\text{nums}[1]$ that is equal to 4, If we move 4 steps to right, we reach $\text{nums}[2]$. So $\text{result}[1]$ should be -1.

- For $\text{nums}[2]$ that is equal to -1, If we move 1 step to left, we reach $\text{nums}[1]$. So $\text{result}[2]$ should be 4.

### 5. Constraints

- $1 \le \text{nums.length} \le 100$

- $-100 \le \text{nums}[i] \le 100$

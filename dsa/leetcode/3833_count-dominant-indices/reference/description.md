### 1. Description

You are given an integer array `nums` of length `n`.

An element at index `i` is called **dominant** if: $\text{nums}[i] > average(nums[i + 1], nums[i + 2], ..., nums[n - 1])$

Your task is to count the number of indices `i` that are **dominant**.

The **average** of a set of numbers is the value obtained by adding all the numbers together and dividing the sum by the total number of numbers.

### 2. Function Contract

**Inputs**

- `nums`: An array of positive integers.

Let $N=\lvert\texttt{nums}\rvert$. For an eligible index $i<N-1$, its right suffix contains exactly $N-i-1$ elements.

**Return value**

Return the number of indices `i` whose value is strictly greater than the average of all elements at indices greater than `i`.

### 3. Note

: The **rightmost** element of any array is **not** **dominant**.

### 4. Examples

#### Example 1

- **Input:** nums = [5,4,3]

- **Output:** 2

- **Explanation:** 

- At index $i = 0$, the value 5 is dominant as $5 > average(4, 3) = 3.5$.

- At index $i = 1$, the value 4 is dominant over the subarray `[3]`.

- Index $i = 2$ is not dominant as there are no elements to its right. Thus, the answer is 2.

#### Example 2

- **Input:** nums = [4,1,2]

- **Output:** 1

- **Explanation:** 

- At index $i = 0$, the value 4 is dominant over the subarray `[1, 2]`.

- At index $i = 1$, the value 1 is not dominant.

- Index $i = 2$ is not dominant as there are no elements to its right. Thus, the answer is 1.

### 5. Constraints

- $1 \le \text{nums.length} \le 100$

- $1 \le \text{nums}[i] \le 100$​​​​​​​

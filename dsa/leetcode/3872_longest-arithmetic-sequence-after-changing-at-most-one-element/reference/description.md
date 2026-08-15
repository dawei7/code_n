### 1. Description

You are given an integer array `nums`.

A subarray is **arithmetic** if the difference between consecutive elements in the subarray is constant.

You can replace **at most one** element in `nums` with any **integer**. Then, you select an arithmetic subarray from `nums`.

Return an integer denoting the **maximum** length of the arithmetic subarray you can select.

### 2. Function Contract

**Inputs**

- `nums`: An array of integers from which a contiguous subarray will be selected.

At most one array position may receive any integer value. All other values and their order remain unchanged. A selected subarray with values $a_0,a_1,\ldots,a_{m-1}$ is arithmetic exactly when one integer difference $d$ satisfies $a_j-a_{j-1}=d$ for every $1\le j<m$.

Let $n=\lvert\texttt{nums}\rvert$.

**Return value**

Return the maximum attainable length of an arithmetic subarray. The result counts elements, not adjacent differences.

### 3. Examples

#### Example 1

- **Input:** nums = [9,7,5,10,1]

- **Output:** 5

- **Explanation:** 

- Replace $\text{nums}[3] = 10$ with 3. The array becomes `[9, 7, 5, 3, 1]`.

- Select the subarray `[<u>**9, 7, 5, 3, 1**</u>]`, which is arithmetic because consecutive elements have a common difference of -2.

#### Example 2

- **Input:** nums = [1,2,6,7]

- **Output:** 3

- **Explanation:** 

- Replace $\text{nums}[0] = 1$ with -2. The array becomes `[-2, 2, 6, 7]`.

- Select the subarray `[<u>**-2, 2, 6**</u>, 7]`, which is arithmetic because consecutive elements have a common difference of 4.

### 4. Constraints

- $4 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{5}$

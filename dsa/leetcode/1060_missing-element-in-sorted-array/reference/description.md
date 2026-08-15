### 1. Description

Given an integer array `nums` which is sorted in **ascending order** and all of its elements are **unique** and given also an integer `k`, return the $$k^{\text{th}}$$ missing number starting from the leftmost number of the array.

### 2. Function Contract

**Inputs**

- `nums`: a non-empty array of unique integers in ascending order.
- `k`: the one-based position of the requested missing number.

Let $N = \lvert\texttt{nums}\rvert$. Missing values are counted strictly after $\text{nums}[0]$, first through the gaps between stored values and then beyond $nums[N - 1]$ if necessary.

**Return value**

- The $k$th missing integer in that increasing sequence.

### 3. Examples

#### Example 1

- **Input:** `nums = [4,7,9,10], k = 1`
- **Output:** `5`
- **Explanation:** The first missing number is 5.

#### Example 2

- **Input:** `nums = [4,7,9,10], k = 3`
- **Output:** `8`
- **Explanation:** The missing numbers are [5,6,8,...], hence the third missing number is 8.

#### Example 3

- **Input:** `nums = [1,2,4], k = 3`
- **Output:** `6`
- **Explanation:** The missing numbers are [3,5,6,7,...], hence the third missing number is 6.

### 4. Constraints

- $1 \le \text{nums.length} \le 5 * 10^{4}$

- $1 \le \text{nums}[i] \le 10^{7}$

- `nums` is sorted in **ascending order,** and all the elements are **unique**.

- $1 \le k \le 10^{8}$

**Follow up:** Can you find a logarithmic time complexity (i.e., `O(log(n))`) solution?

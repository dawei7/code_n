### 1. Description

In some array `arr`, the values were in arithmetic progression: the values $arr[i + 1] - \text{arr}[i]$ are all equal for every $0 \le i < \text{arr.length} - 1$.

A value from `arr` was removed that **was not the first or last value in the array**.

Given `arr`, return *the removed value*.

### 2. Function Contract

**Inputs**

- `arr`: The remaining arithmetic-progression values in their original order.

Let $n = \lvert\texttt{arr}\rvert$. The original progression contained $n+1$ values, and exactly one interior value was removed. The input guarantee covers increasing, decreasing, and constant progressions.

**Return value**

Return the removed integer value. Because neither original endpoint was removed, $\text{arr}[0]$ and `arr[-1]` are the original first and last values.

### 3. Examples

#### Example 1

- **Input:** `arr = [5,7,11,13]`
- **Output:** `9`
- **Explanation:** The previous array was [5,7,**9**,11,13].
#### Example 2

- **Input:** `arr = [15,13,12]`
- **Output:** `14`
- **Explanation:** The previous array was [15,**14**,13,12].

### 4. Constraints

- $3 \le \text{arr.length} \le 1000$

- $0 \le \text{arr}[i] \le 10^{5}$

- The given array is **guaranteed** to be a valid array.
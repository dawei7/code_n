### 1. Description

Given an array of positive integers `arr` (not necessarily distinct), return *the **lexicographically** largest permutation that is smaller than* `arr`, that can be **made with exactly one swap**. If it cannot be done, then return the same array.

### 2. Function Contract

**Inputs**

- `arr`: Input parameter (`List[int]`).

**Return value**

- Returns `List[int]`.

### 3. Note

that a *swap* exchanges the positions of two numbers $\text{arr}[i]$ and $\text{arr}[j]$

### 4. Examples

#### Example 1

- **Input:** `arr = [3,2,1]`
- **Output:** `[3,1,2]`
- **Explanation:** Swapping 2 and 1.

#### Example 2

- **Input:** `arr = [1,1,5]`
- **Output:** `[1,1,5]`
- **Explanation:** This is already the smallest permutation.

#### Example 3

- **Input:** `arr = [1,9,4,6,7]`
- **Output:** `[1,7,4,6,9]`
- **Explanation:** Swapping 9 and 7.

### 5. Constraints

- $1 \le \text{arr.length} \le 10^{4}$

- $1 \le \text{arr}[i] \le 10^{4}$

### 1. Description

A sequence is **special** if it consists of a **positive** number of `0`s, followed by a **positive** number of `1`s, then a **positive** number of `2`s.

- For example, `[0,1,2]` and `[0,0,1,1,1,2]` are special.

- In contrast, `[2,1,0]`, `[1]`, and `[0,1,2,0]` are not special.

Given an array `nums` (consisting of **only** integers `0`, `1`, and `2`), return* the **number of different subsequences** that are special*. Since the answer may be very large, **return it modulo **$10^{9} + 7$.

A **subsequence** of an array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements. Two subsequences are **different** if the **set of indices** chosen are different.

### 2. Function Contract

**Inputs**

- `nums`: Input parameter (`List[int]`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** `nums = [0,1,2,2]`
- **Output:** `3`
- **Explanation:** The special subsequences are bolded [**<u>0</u>**,**<u>1</u>**,**<u>2</u>**,2], [**<u>0</u>**,**<u>1</u>**,2,**<u>2</u>**], and [**<u>0</u>**,**<u>1</u>**,**<u>2</u>**,**<u>2</u>**].

#### Example 2

- **Input:** `nums = [2,2,0,0]`
- **Output:** `0`
- **Explanation:** There are no special subsequences in [2,2,0,0].

#### Example 3

- **Input:** `nums = [0,1,2,0,1,2]`
- **Output:** `7`
- **Explanation:** The special subsequences are bolded:
- [**<u>0</u>**,**<u>1</u>**,**<u>2</u>**,0,1,2]
- [**<u>0</u>**,**<u>1</u>**,2,0,1,**<u>2</u>**]
- [**<u>0</u>**,**<u>1</u>**,**<u>2</u>**,0,1,**<u>2</u>**]
- [**<u>0</u>**,**<u>1</u>**,2,0,**<u>1</u>**,**<u>2</u>**]
- [**<u>0</u>**,1,2,**<u>0</u>**,**<u>1</u>**,**<u>2</u>**]
- [**<u>0</u>**,1,2,0,**<u>1</u>**,**<u>2</u>**]
- [0,1,2,**<u>0</u>**,**<u>1</u>**,**<u>2</u>**]

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $0 \le \text{nums}[i] \le 2$

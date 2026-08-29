### 1. Description

You are given an integer array `nums`.

Return the length of the **longest strictly increasing subsequence** in `nums` whose bitwise **AND** is **non-zero**. If no such **subsequence** exists, return 0.

### 2. Function Contract

**Inputs**

- `nums`: A nonempty array of nonnegative integers.

Let $N = \lvert\texttt{nums}\rvert$ and let $B = 30$, the number of bit positions needed to represent every permitted value from $0$ through $10^9$.

**Return value**

Return the maximum number of elements in a subsequence that is strictly increasing and whose cumulative bitwise AND is non-zero. A nonzero single element is a valid length-one subsequence. A zero by itself is not valid because its AND is zero.

### 3. Examples

#### Example 1

- **Input:** nums = [5,4,7]

- **Output:** 2

- **Explanation:** One longest strictly increasing subsequence is `[5, 7]`. The bitwise AND is $5 AND 7 = 5$, which is non-zero.

#### Example 2

- **Input:** nums = [2,3,6]

- **Output:** 3

- **Explanation:** The longest strictly increasing subsequence is `[2, 3, 6]`. The bitwise AND is $2 AND 3 AND 6 = 2$, which is non-zero.

#### Example 3

- **Input:** nums = [0,1]

- **Output:** 1

- **Explanation:** One longest strictly increasing subsequence is `[1]`. The bitwise AND is 1, which is non-zero.

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $0 \le \text{nums}[i] \le 10^{9}$

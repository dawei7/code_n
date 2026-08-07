### 1. Description

You are given an array `nums` consisting of `n` prime integers.

You need to construct an array `ans` of length `n`, such that, for each index `i`, the bitwise `OR` of $\text{ans}[i]$ and $\text{ans}[i] + 1$ is equal to $\text{nums}[i]$, i.e. $\text{ans}[i] OR (\text{ans}[i] + 1) = \text{nums}[i]$.

Additionally, you must **minimize** each value of $\text{ans}[i]$ in the resulting array.

If it is *not possible* to find such a value for $\text{ans}[i]$ that satisfies the **condition**, then set $\text{ans}[i] = -1$.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [2,3,5,7]

**Output:** [-1,1,4,3]

**Explanation:**

- For $i = 0$, as there is no value for $\text{ans}[0]$ that satisfies $\text{ans}[0] OR (\text{ans}[0] + 1) = 2$, so $\text{ans}[0] = -1$.

- For $i = 1$, the smallest $\text{ans}[1]$ that satisfies $\text{ans}[1] OR (\text{ans}[1] + 1) = 3$ is `1`, because $1 OR (1 + 1) = 3$.

- For $i = 2$, the smallest $\text{ans}[2]$ that satisfies $\text{ans}[2] OR (\text{ans}[2] + 1) = 5$ is `4`, because $4 OR (4 + 1) = 5$.

- For $i = 3$, the smallest $\text{ans}[3]$ that satisfies $\text{ans}[3] OR (\text{ans}[3] + 1) = 7$ is `3`, because $3 OR (3 + 1) = 7$.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [11,13,31]

**Output:** [9,12,15]

**Explanation:**

- For $i = 0$, the smallest $\text{ans}[0]$ that satisfies $\text{ans}[0] OR (\text{ans}[0] + 1) = 11$ is `9`, because $9 OR (9 + 1) = 11$.

- For $i = 1$, the smallest $\text{ans}[1]$ that satisfies $\text{ans}[1] OR (\text{ans}[1] + 1) = 13$ is `12`, because $12 OR (12 + 1) = 13$.

- For $i = 2$, the smallest $\text{ans}[2]$ that satisfies $\text{ans}[2] OR (\text{ans}[2] + 1) = 31$ is `15`, because $15 OR (15 + 1) = 31$.

</div>

### 4. Constraints

- $1 \le \text{nums.length} \le 100$

- $2 \le \text{nums}[i] \le 10^{9}$

- $\text{nums}[i]$ is a prime number.
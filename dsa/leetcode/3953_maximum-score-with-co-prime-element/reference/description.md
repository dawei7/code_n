### 1. Description

You are given an integer array `nums` of length `n` and an integer `maxVal`.

You **may** change any element in `nums` to any positive integer **less than or equal** to `maxVal`. Each such change costs 1.

Two integers are **co-prime** if their **greatest common divisor (GCD)** is 1.

After all modifications, you **must** choose an index `i` such that, $\text{nums}[i]$ is **co-prime** with every other element $\text{nums}[j]$.

Let:

- `selectedValue` be the final value of $\text{nums}[i]$ after modifications.

- `modificationCost` be the total number of elements changed.

The score is defined as $score = selectedValue - modificationCost$.

Return the **maximum** possible score.

### 2. Function Contract

**Inputs**

- `nums`: The original positive integer values.
- `maxVal`: The inclusive upper bound for every replacement value.

Let $n=\texttt{nums.length}$ and define

$U=\max(\texttt{maxVal},\max(\texttt{nums})).$

**Return value**

Return the maximum possible final selected value minus the number of changed array elements, subject to the selected value being co-prime with every other final element.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [3,4,6], maxVal = 5

**Output:** 4

**Explanation:**

Change $\text{nums}[2]$ from 6 to 5, which costs 1. Choose $\text{nums}[2] = 5$, since it is co-prime with 3 and 4.

- $selectedValue = 5$

- $modificationCost = 1$

- The score is $5 - 1 = 4$

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1,2,3], maxVal = 4

**Output:** 3

**Explanation:**

No modifications are required. Choose $\text{nums}[2] = 3$, since it is co-prime with 1 and 2.

- $selectedValue = 3$

- $modificationCost = 0$

- The score is $3 - 0 = 3$

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [2,2], maxVal = 1

**Output:** 1

**Explanation:**

Change $\text{nums}[0]$ from 2 to 1, which costs 1. Choose $\text{nums}[1] = 2$, since it is co-prime with 1.

- $selectedValue = 2$

- $modificationCost = 1$

- The score is ​​​​​​​$2 - 1 = 1$

</div>

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{5}$

- $1 \le maxVal \le 10^​​​​​​​5$
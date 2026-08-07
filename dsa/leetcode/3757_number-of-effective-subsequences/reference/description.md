### 1. Description

You are given an integer array `nums`.

The **strength** of the array is defined as the **bitwise OR** of all its elements.

A **subsequence** is considered **effective** if removing that subsequence **strictly decreases** the strength of the remaining elements.

Return the number of **effective subsequences** in `nums`. Since the answer may be large, return it **modulo** $10^{9} + 7$.

The bitwise OR of an empty array is 0.

### 2. Function Contract

**Inputs**

- `nums`: A nonempty array of positive integers whose index subsequences may be removed.

Let $n = \lvert\texttt{nums}\rvert$, and let $b$ be the number of set-bit positions in the bitwise OR of the full array. Removing a subsequence leaves the complementary indices in their original relative order. Duplicate values at distinct indices are counted as distinct subsequence choices.

**Return value**

Return the number of nonempty subsequences whose removal strictly lowers the bitwise OR of the remaining elements, reduced modulo $10^9+7$.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,2,3]

**Output:** 3

**Explanation:**

- The Bitwise OR of the array is $1 OR 2 OR 3 = 3$.

- Subsequences that are effective are:

		<li>`[1, 3]`: The remaining element `[2]` has a Bitwise OR of 2.

- `[2, 3]`: The remaining element `[1]` has a Bitwise OR of 1.

- `[1, 2, 3]`: The remaining elements `[]` have a Bitwise OR of 0.

	</li>
- Thus, the total number of effective subsequences is 3.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [7,4,6]

**Output:** 4

**Explanation:**​​​​​​​

- The Bitwise OR of the array is $7 OR 4 OR 6 = 7$.

- Subsequences that are effective are:

		<li>`[7]`: The remaining elements `[4, 6]` have a Bitwise OR of 6.

- `[7, 4]`: The remaining element `[6]` has a Bitwise OR of 6.

- `[7, 6]`: The remaining element `[4]` has a Bitwise OR of 4.

- `[7, 4, 6]`: The remaining elements `[]` have a Bitwise OR of 0.

	</li>
- Thus, the total number of effective subsequences is 4.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [8,8]

**Output:** 1

**Explanation:**

- The Bitwise OR of the array is $8 OR 8 = 8$.

- Only the subsequence `[8, 8]` is effective since removing it leaves `[]` which has a Bitwise OR of 0.

- Thus, the total number of effective subsequences is 1.

</div>
#### Example 4

<div class="example-block">
**Input:** nums = [2,2,1]

**Output:** 5

**Explanation:**

- The Bitwise OR of the array is $2 OR 2 OR 1 = 3$.

- Subsequences that are effective are:

		<li>`[1]`: The remaining elements `[2, 2]` have a Bitwise OR of 2.

- `[2, 1]` (using $\text{nums}[0]$, $\text{nums}[2]$): The remaining element `[2]` has a Bitwise OR of 2.

- `[2, 1]` (using $\text{nums}[1]$, $\text{nums}[2]$): The remaining element `[2]` has a Bitwise OR of 2.

- `[2, 2]`: The remaining element `[1]` has a Bitwise OR of 1.

- `[2, 2, 1]`: The remaining elements `[]` have a Bitwise OR of 0.

	</li>
- Thus, the total number of effective subsequences is 5.

</div>

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{6}$
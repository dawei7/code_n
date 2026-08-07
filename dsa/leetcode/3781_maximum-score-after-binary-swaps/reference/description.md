### 1. Description

You are given an integer array `nums` of length `n` and a binary string `s` of the same length.

Initially, your score is 0. Each index `i` where $s[i] = '1'$ contributes $\text{nums}[i]$ to the score.

You may perform **any** number of operations (including zero). In one operation, you may choose an index `i` such that $0 \le i < n - 1$, where $s[i] = '0'$, and $s[i + 1] = '1'$, and swap these two characters.

Return an integer denoting the **maximum possible score** you can achieve.

### 2. Function Contract

**Inputs**

- `nums`: A nonempty array of positive integer score values.
- `s`: A binary string with the same length as `nums`.

Let $N=\lvert\texttt{nums}\rvert=\lvert s\rvert$. Swaps change only the positions of the characters in `s`; they do not reorder `nums`, change the number of ones, or allow a one to move rightward across a zero.

**Return value**

Return the maximum sum of $\text{nums}[i]$ over positions that can contain `'1'` after any number of legal `"01" -> "10"` swaps, including no swaps.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [2,1,5,2,3], s = "01010"

**Output:** 7

**Explanation:**

We can perform the following swaps:

- Swap at index $i = 0$: `"01010"` changes to `"10010"`

- Swap at index $i = 2$: `"10010"` changes to `"10100"`

Positions 0 and 2 contain `'1'`, contributing $\text{nums}[0] + \text{nums}[2] = 2 + 5 = 7$. This is maximum score achievable.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [4,7,2,9], s = "0000"

**Output:** 0

**Explanation:**

There are no `'1'` characters in `s`, so no swaps can be performed. The score remains 0.

</div>

### 4. Constraints

- $n = \text{nums.length} = \text{s.length}$

- $1 \le n \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{9}$

- $s[i]$ is either `'0'` or `'1'`
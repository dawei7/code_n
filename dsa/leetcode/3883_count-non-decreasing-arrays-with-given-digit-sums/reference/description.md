### 1. Description

You are given an integer array `digitSum` of length `n`.

An array `arr` of length `n` is considered **valid** if:

- $0 \le \text{arr}[i] \le 5000$

- it is **non-decreasing**.

- the **sum of the digits** of $\text{arr}[i]$ **equals** $\text{digitSum}[i]$.

Return an integer denoting the number of **distinct valid arrays**. Since the answer may be large, return it modulo $10^{9} + 7$.

An array is said to be **non-decreasing** if each element is greater than or equal to the previous element, if it exists.

### 2. Function Contract

**Inputs**

- `digitSum`: An array whose entry at index `i` is the required decimal digit sum of $\text{arr}[i]$.

Let $n=\lvert\texttt{digitSum}\rvert$, let $U=5001$ be the number of permitted values, and let $D(x)$ denote the sum of the decimal digits of $x$. A candidate array must satisfy $0\le\texttt{\text{arr}[i]}\le5000$, $\texttt{arr[i-1]}\le\texttt{\text{arr}[i]}$ whenever $i>0$, and $D(\texttt{\text{arr}[i]})=\texttt{\text{digitSum}[i]}$ at every index.

Arrays are distinct when they differ at one or more positions.

**Return value**

Return the number of distinct valid arrays, reduced modulo $1{,}000{,}000{,}007$.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** digitSum = [25,1]

**Output:** 6

**Explanation:**

Numbers whose sum of digits is 25 are 799, 889, 898, 979, 988, and 997.

The only number whose sum of digits is 1 that can appear after these values while keeping the array non-decreasing is 1000.

Thus, the valid arrays are `[799, 1000]`, `[889, 1000]`, `[898, 1000]`, `[979, 1000]`, `[988, 1000]`, and `[997, 1000]`.

Hence, the answer is 6.

</div>
#### Example 2

<div class="example-block">
**Input:** digitSum = [1]

**Output:** 4

**Explanation:**

The valid arrays are `[1]`, `[10]`, `[100]`, and `[1000]`.

Thus, the answer is 4.

</div>
#### Example 3

<div class="example-block">
**Input:** digitSum = [2,49,23]

**Output:** 0

**Explanation:**

There is no integer in the range [0, 5000] whose sum of digits is 49. Thus, the answer is 0.

</div>

### 4. Constraints

- $1 \le \text{digitSum.length} \le 1000$

- $0 \le \text{digitSum}[i] \le 50$
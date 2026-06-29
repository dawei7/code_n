# Guddu on a Date

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | KS2 |
| Difficulty Rating | 1525 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1500 to 1600 difficulty problems |
| Official Link | [KS2](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1600/problems/KS2) |

---

## Problem Statement

Guddu likes a girl that loves playing with numbers. She agreed to go on a date with Guddu, but only if he can solve the following problem:

An integer is *round* if it is greater than $0$ and the sum of its digits in decimal representation is a multiple of $10$. Find the $N$-th smallest round integer.

However, Guddu does not like playing with numbers at all and he is unable to solve this problem, so he begs you to solve it for him. In return, he will definitely give you a treat.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains a single integer $N$.

### Output
For each test case, print a single line containing the $N$-th round integer. It is guaranteed that this number is smaller than $2^{64}$.

### Constraints
- $1 \le T \le 10^5$
- $1 \le N \le 10^{18}$

### Subtasks
**Subtask #1 (30 points):**
- $1 \le T \le 10$
- $1 \le N \le 10^5$

**Subtask #2 (70 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
1
2
```

**Output**

```text
28
```

**Explanation**

**Example case 1:** The smallest round integer is $19$ and the second smallest is $28$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Guddu on a Date Practice Problem in 1400 to 1600 difficulty problems](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1600/problems/KS2)

### [](#problem-statement-1)Problem Statement:

Find the N-th smallest “round integer”. A round integer is defined as:

- It is greater than 0.

- The sum of its digits is a multiple of 10.

### [](#approach-2)Approach:

#### [](#step-1-sum-of-digits-calculation-3)**Step 1: Sum of Digits Calculation**

For any given number `n`, the first thing we need to do is calculate the sum of its digits. This can be done easily by repeatedly extracting the last digit and adding it to a sum.

We keep repeating this process until the number becomes zero.

#### [](#step-2-check-if-sum-of-digits-is-divisible-by-10-4)**Step 2: Check if Sum of Digits is Divisible by 10**

After calculating the sum of the digits of `n`, we check if this sum is divisible by 10. If it is, then the number is already “round”, and we don’t need to modify it.

#### [](#step-3-find-the-next-round-integer-5)**Step 3: Find the Next Round Integer**

If the sum of the digits is not divisible by 10, we need to adjust the number to make the sum divisible by 10. To do this:

- Calculate the remainder of the sum when divided by 10: `sum % 10`.

- The next number will be formed by adding a digit to `n` such that the new sum of digits becomes divisible by 10. To achieve this, we append a digit `d` such that `(sum + d) % 10 == 0`. This can be done by computing `d = (10 - (sum % 10)) % 10`. This ensures that the sum of digits of `n` plus the digit `d` will be divisible by 10.

#### [](#step-4-output-the-result-6)**Step 4: Output the Result**

We output the number formed by appending the digit `d` to the number `n`.

### [](#complexity-7)Complexity:

- **Time Complexity:** The number of digits of `n` is `O(log⁡ n)`, so calculating the sum of digits requires `O(log ⁡n)` time.

- **Space Complexity:** `O(1)` No extra space is used.

</details>

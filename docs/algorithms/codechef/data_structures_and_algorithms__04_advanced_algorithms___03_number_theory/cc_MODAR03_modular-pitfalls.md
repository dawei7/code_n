# Modular Pitfalls

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MODAR03 |
| Difficulty Band | Number theory |
| Path | Data Structures and Algorithms |
| Lesson | Modular Arithmetic |
| Official Link | [MODAR03](https://www.codechef.com/learn/course/number-theory/LINTDSA06/problems/MODAR03) |

---

## Problem Statement

You are given an array $arr$ consisting of $N$ integers. Your task is to compute the sum of the squares of the elements in the array, and then return the result modulo $10^9+7$.

---

## Input Format

The first line contains one integer $T$
 ($1≤T≤1000$
) — the number of test cases.

The second line of each test case contains one integer n
 ($1≤N≤10^4$
) — the length of the array $arr$
.

The third line of each test case contains $N$
 integers $arr_1,arr_2,…,arr_n$
 ($1≤|arr_i|≤10^{18}$
) — array $arr$
.

---

## Output Format

For each test case, output on a new line the sum of square of elements of the array, modulo $10^9 + 7$.

---

## Examples

**Example 1**

**Input**

```text
2
5
2 34 4 56 76
3
23 7 21
```

**Output**

```text
10088
1019
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
2 34 4 56 76
```

**Output for this case**

```text
10088
```



#### Test case 2

**Input for this case**

```text
3
23 7 21
```

**Output for this case**

```text
1019
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Modular Pitfalls in Number theory](https://www.codechef.com/learn/course/number-theory/LINTDSA06/problems/MODAR03?tab=statement)

### [](#problem-statement-1)Problem Statement:

You are given an array arr consisting of N integers. Your task is to compute the sum of the squares of the elements in the array, and then return the result modulo 10^9+7.

### [](#approach-2)Approach:

- **Modular Arithmetic**: Since the numbers can be very large (up to 10^{18}, and squaring them could result in even larger numbers, we must handle computations with modulo 10^9+7 to avoid overflow.

- For each number in the array compute their **modulo** so that you can compute their squares efficiently.

- Iterate through the array, compute the square of each element, and take the **modulo** at every step to avoid overflow and store it in `sum`.

### [](#complexity-3)Complexity:

- **Time Complexity:** `O(N)` Iterating through the array once to compute the sum of squares

- **Space Complexity:** `O(1)` No extra space required.

</details>

# Counting Divisors - I

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PRIMEFACT06 |
| Difficulty Band | Number theory |
| Path | Data Structures and Algorithms |
| Lesson | Prime Factorization |
| Official Link | [PRIMEFACT06](https://www.codechef.com/learn/course/number-theory/LINTDSA02/problems/PRIMEFACT06) |

---

## Problem Statement

Given a positive integer $N$, the objective is to return the count of divisors of the number $N$ including the number $1$ and the number $N$ itself.

For example, if $x=18$, the correct answer is $6$ because its divisors are $1, 2, 3, 6, 9,18$.

Note that we want to also count factors which aren't prime.

---

## Input Format

The first line contains a single integer $T$ denoting the number of testcase

The only line of each test case contains an integer $N$ whose divisor count has to be returned.

---

## Output Format

For each integer, print the number of its divisors.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 1000$

---

## Examples

**Example 1**

**Input**

```text
3
16
17
18
```

**Output**

```text
5
2
6
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
16
```

**Output for this case**

```text
5
```



#### Test case 2

**Input for this case**

```text
17
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
18
```

**Output for this case**

```text
6
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Counting Divisors - I in Number theory](https://www.codechef.com/learn/course/number-theory/LINTDSA02/problems/PRIMEFACT06)

### [](#problem-statement-1)Problem Statement:

Given a positive integer N, the objective is to return the count of divisors of the number N including the number 1 and the number N itself.

For example, if x=18, the correct answer is 6 because its divisors are 1,2,3,6,9,18.

Note that we want to also count factors which aren’t prime.

### [](#approach-2)Approach:

The approach to counting divisors of a number n is based on the fact that divisors come in pairs. For every divisor i of n, there exists a corresponding divisor \frac{n}{i} ​ . By iterating only up to \sqrt{n} ​, we efficiently find all divisors, as any divisor greater than \sqrt{n} ​ would have already been paired with a divisor smaller than \sqrt{n} .

- **Check for divisibility**: For each number i from 1 to \sqrt{n} ​, if i divides n evenly, then:

- i is a divisor.

- \frac{n}{i} ​ is also a divisor unless i is the square root of n, in which case it only gets counted once.

- **Count divisors**: If i is a divisor, add both  i and \frac{n}{i} ​ to the divisor count, unless they are the same.

### [](#complexity-3)Complexity:

- **Time Complexity:** O(\sqrt{N} ) We are iterating from `1` to \sqrt{n} ​, which takes \sqrt{n} ​ iterations.

- **Space Complexity:** O(1) No extra space needed.

</details>

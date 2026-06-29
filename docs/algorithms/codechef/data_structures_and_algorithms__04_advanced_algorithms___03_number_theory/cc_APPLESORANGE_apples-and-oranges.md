# Apples and oranges

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | APPLESORANGE |
| Difficulty Rating | 1040 |
| Difficulty Band | Number theory |
| Path | Data Structures and Algorithms |
| Lesson | GCD and LCM |
| Official Link | [APPLESORANGE](https://www.codechef.com/learn/course/number-theory/LINTDSA04/problems/APPLESORANGE) |

---

## Problem Statement

Rushitote went to a programming contest to distribute apples and oranges to the contestants.
He has $N$ apples and $M$ oranges, which need to be divided **equally** amongst the contestants. Find the maximum possible number of contestants such that:
- Every contestant gets an equal number of apples; and
- Every contestant gets an equal number of oranges.

Note that every fruit with Rushitote *must* be distributed, there cannot be any left over.

For example, $2$ apples and $4$ oranges can be distributed equally to two contestants, where each one receives $1$ apple and $2$ oranges.
However, $2$ apples and $5$ oranges can only be distributed equally to one contestant.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of each test case contains two space-separated integers $N$ and $M$ — the number of apples and oranges, respectively.

---

## Output Format

For each test case, output on a new line the answer: the maximum number of contestants such that everyone receives an equal number of apples and an equal number of oranges.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N , M \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
3
1 5
2 4
4 6
```

**Output**

```text
1
2
2
```

**Explanation**

**Test case $1$:** There's only one apple, so distributing to more than one person is impossible.

**Test case $2$:** As explained in the statement, $2$ people can each receive $1$ apple and $2$ oranges.

**Test case $3$:** $2$ people can each receive $2$ apples and $3$ oranges. It's not possible to distribute equally to more than two people.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 5
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
2 4
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
4 6
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Apples and oranges in Number theory](https://www.codechef.com/learn/course/number-theory/LINTDSA04/problems/APPLESORANGE)

### [](#problem-statement-1)Problem Statement:

Rushitote wants to distribute **N** apples and **M** oranges equally among contestants. The goal is to find the maximum number of contestants such that each contestant gets an equal number of apples and oranges without any leftovers.

### [](#approach-2)Approach:

- The solution is to find the greatest common divisor (GCD) of **N** and **M**, as it represents the maximum number of contestants who can evenly divide both the apples and oranges. Each contestant will get **N/GCD(N, M)** apples and **M/GCD(N, M)** oranges.

- To calculate the GCD: **GCD(a, b) = GCD(b, a % b)** This means the GCD of two numbers doesn’t change if the larger number is replaced by its remainder when divided by the smaller number. The process keeps reducing the size of the numbers, eventually reaching a remainder of 0.

### [](#complexity-3)Complexity:

- **Time Complexity:** `O(log(min(N, M)))` The algorithm reduces one of the numbers by at least half at every step, making it very efficient for even large numbers.

- **Space Complexity:** `O(1)` No extra space required.

</details>

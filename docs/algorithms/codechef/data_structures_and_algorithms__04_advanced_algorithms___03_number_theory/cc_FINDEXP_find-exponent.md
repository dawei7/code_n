# Find Exponent

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FINDEXP |
| Difficulty Band | Number theory |
| Path | Data Structures and Algorithms |
| Lesson | Modular Arithmetic |
| Official Link | [FINDEXP](https://www.codechef.com/learn/course/number-theory/LINTDSA06/problems/FINDEXP) |

---

## Problem Statement

Given three integers $a$, $b$, and $m$, find $a^b \mod m$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The only line of each test case consists of three integers - $a, b, m$.

---

## Output Format

For each test case, output on a new line the answer.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq a,b,m \leq 10^6$

---

## Examples

**Example 1**

**Input**

```text
3
2 4 100
2 4 6
3 2 2
```

**Output**

```text
16
4
1
```

**Explanation**

**Test case 1:** $2^4$ = 16, and 16 mod 100 = 16.

**Test case 2:** $2^4$ = 16, and 16 mod 10 = 6.

**Test case 3:** $3^2$ = 9, and 9 mod 2 = 1.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 4 100
```

**Output for this case**

```text
16
```



#### Test case 2

**Input for this case**

```text
2 4 6
```

**Output for this case**

```text
4
```



#### Test case 3

**Input for this case**

```text
3 2 2
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [ModEx Suite in Number theory](https://www.codechef.com/learn/course/number-theory/LINTDSA06/problems/MODAR02)

### [](#problem-statement-1)Problem Statement:

Given three integers a, b, and m, find a^b mod m.

### [](#approach-2)Approach:

- Your code implements the efficient calculation of a^b mod m using modular exponentiation (also known as “exponentiation by squaring”). This approach is optimal for computing large powers under a modulus.

- See how to calculate modular exponentiation: [ModEx Suite in Number theory](https://www.codechef.com/learn/course/number-theory/LINTDSA06/problems/MODAR02)

### [](#complexity-3)Complexity:

- **Time Complexity:** * The loop in `modexp` runs while `b > 0`, and the number of iterations is proportional to the number of bits in `b`. Since `b` is reduced by half each time (`b>>=1`), the number of iterations is `O(log⁡ b)`

- **Space Complexity:** `O(1)` No extra space needed.

</details>

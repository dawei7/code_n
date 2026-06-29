# Equalize AB

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | EQUALIZEAB |
| Difficulty Rating | 1069 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [EQUALIZEAB](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/EQUALIZEAB) |

---

## Problem Statement

You are given two numbers $A$ and $B$ along with an integer $X$. In one operation you can do one of the following:
- Set $A = A + X$ and $B = B - X$
- Set $A = A - X$ and $B = B + X$

Determine if you can make $A$ and $B$ equal after applying the operation any number of times (possibly zero).

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first and only line of each test case contains two space-separated integers $A, B$ and $X$ — the parameters mentioned in the statement.

---

## Output Format

For each test case, output `YES` if you can make $A$ and $B$ equal after applying the operation any number of times (possibly zero). Otherwise, output `NO`.

You can output each letter in any case i.e. `YES`, `yes`, `yEs` are all considered the same.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq A, B, X \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
4
5 7 1
3 4 2
4 4 6
2 5 3
```

**Output**

```text
YES
NO
YES
NO
```

**Explanation**

**Test Case 1:** The initial values of $(A, B)$ is $(5, 7)$. We can perform the following operation: $(5,7) \xrightarrow{A = A + X, B = B - X} (6,6)$.

**Test Case 2:** It can be proven that we can not make $A$ equal to $B$ using the given operations.

**Test Case 3:** $A$ and $B$ are already equal.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 7 1
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
3 4 2
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
4 4 6
```

**Output for this case**

```text
YES
```



#### Test case 4

**Input for this case**

```text
2 5 3
```

**Output for this case**

```text
NO
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/EQUALIZEAB)

[Contest: Division 1](https://www.codechef.com/LTIME112A/problems/EQUALIZEAB)

[Contest: Division 2](https://www.codechef.com/LTIME112B/problems/EQUALIZEAB)

[Contest: Division 3](https://www.codechef.com/LTIME112C/problems/EQUALIZEAB)

[Contest: Division 4](https://www.codechef.com/LTIME112D/problems/EQUALIZEAB)

***Author:*** [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec)

***Tester:*** [Hriday](https://www.codechef.com/users/the_hyp0cr1t3)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

1069

#
[](#prerequisites-3)PREREQUISITES:

Basic math

#
[](#problem-4)PROBLEM:

You are given A, B, and X. In one move, you can increase either A or B by X and reduce the other by X. Is it possible to make A equal to B?

#
[](#explanation-5)EXPLANATION:

It is possible to make A and B equal if and only if 2X divides A-B.

Proof

Note that making any move does not change the value of (A-B) modulo 2X, since:

- (A+X) - (B-X) \equiv A-B + 2X \equiv A-B \pmod {2X}

- (A-X) - (B+X) \equiv A-B - 2X \equiv A-B \pmod {2X}

If A = B eventually, then of course A-B must be 0 modulo 2X, i.e, 2X divides A-B.

Also, if 2X divides A-B, then A and B can be made equal as follows:

- If A = B, nothing needs to be done

- If A \gt B, add X to B and subtract X from A

- If A \lt B, add X to A and subtract X from B

In either case, A and B are brought closer together by 2X. Since their difference is a multiple of 2X, eventually they will become equal.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    a, b, x = map(int, input().split())
    print('Yes' if (a-b)%(2*x) == 0 else 'No')
``

</details>

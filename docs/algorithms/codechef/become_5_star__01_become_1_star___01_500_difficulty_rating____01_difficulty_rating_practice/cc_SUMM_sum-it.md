# Sum it

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SUMM |
| Difficulty Rating | 308 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [SUMM](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/SUMM) |

---

## Problem Statement

Bob received an assignment from his school: he has two numbers $A$ and $B$, and he has to find the sum of these two numbers.
Alice, being a good friend of Bob, told him that the answer to this question is $C$.
Bob doesn't completely trust Alice and asked you to tell him if the answer given by Alice is correct or not.
If the answer is correct print `"YES"`, otherwise print `"NO"` (without quotes).

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of each test case consists of three space-separated integers $A, B,$ and $C$.

---

## Output Format

For each test case, output on a new line the answer: `YES` if Alice gave the right answer, and `NO` otherwise.

Each character of the output may be printed in either uppercase or lowercase, i.e, the outputs `Yes`, `YES`, `yEs` and `yes` will be treated as equivalent.

---

## Constraints

- $1 \leq T \leq 100$
- $0 \leq A , B , C \leq 100$

---

## Examples

**Example 1**

**Input**

```text
3
1 2 3
4 5 9
2 3 6
```

**Output**

```text
YES
YES
NO
```

**Explanation**

**Test case $1$:** $1+2 = 3$, so Alice's answer is correct.

**Test case $2$:** $4+5 = 9$, so Alice's answer is correct.

**Test case $3$:** $2+3=5$ which doesn't equal $6$, so Alice's answer is incorrect.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 2 3
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
4 5 9
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
2 3 6
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

[Practice](https://www.codechef.com/problems/SUMM)

[Contest: Division 1](https://www.codechef.com/START72A/problems/SUMM)

[Contest: Division 2](https://www.codechef.com/START72B/problems/SUMM)

[Contest: Division 3](https://www.codechef.com/START72C/problems/SUMM)

[Contest: Division 4](https://www.codechef.com/START72D/problems/SUMM)

***Author:*** [still_me](https://www.codechef.com/users/still_me)

***Testers:*** [the_hyp0cr1t3](https://www.codechef.com/users/the_hyp0cr1t3), [rivalq](https://www.codechef.com/users/rivalq)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given A, B, C check if A+B = C.

#
[](#explanation-5)EXPLANATION:

This is a direct application of `if` statements: print `YES` if `A+B == C` and `NO` otherwise.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(1) per testcase.

#
[](#code-7)CODE:

Code (Python)
``for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print('Yes' if a+b == c else 'No')
``

</details>

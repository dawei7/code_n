# Miami GP

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | F1RULE |
| Difficulty Rating | 487 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [F1RULE](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/F1RULE) |

---

## Problem Statement

Chef has finally got the chance of his lifetime to drive in the $F1$ tournament. But, there is one problem. Chef did not know about the [107% rule](https://en.wikipedia.org/wiki/107%25_rule) and now he is worried whether he will be allowed to race in the main event or not.

Given the fastest finish time as $X$ seconds and Chef's finish time as $Y$ seconds, determine whether Chef will be allowed to race in the main event or not.

Note that, Chef will only be allowed to race if his finish time is within **107%** of the fastest finish time.

---

## Input Format

- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains of a single line of input, two space separated integers $X$ and $Y$ denoting the fastest finish time and Chef's finish time respectively.

---

## Output Format

For each test case, output $\texttt{YES}$ if Chef will be allowed to race in the main event, else output $\texttt{NO}$.

You may print each character of the string in uppercase or lowercase (for example, the strings $\texttt{YeS}$, $\texttt{yEs}$, $\texttt{yes}$ and $\texttt{YES}$ will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 2\cdot 10^4$
- $1 \leq X \leq Y \leq 200$

---

## Examples

**Example 1**

**Input**

```text
4
1 2
15 16
15 17
100 107
```

**Output**

```text
NO
YES
NO
YES
```

**Explanation**

**Test case $1$:** The fastest car finished in $1$ second. Thus, Chef should have finished on or before $1.07$ seconds to ensure qualification but he finished in $2$ seconds. Hence, Chef will not be allowed to race in the main event.

**Test case $2$:** The fastest car finished in $15$ seconds. Thus, Chef should have finished on or before $16.05$ seconds to ensure qualification and he managed to finish in $16$ seconds. Hence, Chef will be allowed to race in the main event.

**Test case $3$:** The fastest car finished in $15$ seconds. Thus, Chef should have finished on or before $16.05$ seconds to ensure qualification but he finished in $17$ seconds. Hence, Chef will not be allowed to race in the main event.

**Test case $4$:** The fastest car finished in $100$ seconds. Thus, Chef should have finished on or before $107$ seconds to ensure qualification and he finished just in time for qualification. Hence, Chef will be allowed to race in the main event.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 2
```

**Output for this case**

```text
NO
```



#### Test case 2

**Input for this case**

```text
15 16
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
15 17
```

**Output for this case**

```text
NO
```



#### Test case 4

**Input for this case**

```text
100 107
```

**Output for this case**

```text
YES
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/F1RULE)

[Contest: Division 1](https://www.codechef.com/MAY221A/problems/F1RULE)

[Contest: Division 2](https://www.codechef.com/MAY221B/problems/F1RULE)

[Contest: Division 3](https://www.codechef.com/MAY221C/problems/F1RULE)

[Contest: Division 4](https://www.codechef.com/MAY221D/problems/F1RULE)

***Author:*** [Tejas Pandey](https://www.codechef.com/users/tejas_adm)

***Testers:*** [Satyam](https://www.codechef.com/users/satyam_343), [Abhinav Sharma](https://www.codechef.com/users/inov_360)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

To be calculated

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef participates in a qualifying F1 race. The fastest finish time is X seconds, and Chef’s finish time is Y seconds.

According to the 107% rule, Chef will qualify to the main event if his time is at most 107% of the fastest time. Will Chef qualify?

#
[](#explanation-5)EXPLANATION:

This is a simple implementation problem which only requires the checking of one condition — whether Y is at most 107% of X.

The easiest way to do this is to calculate 107% of X and check whether Y exceeds it, i.e, check if Y \leq 1.07 \cdot X.

The safest way to implement this, however, is to multiply both sides of the above equation by 100 and check if 100 Y \leq 107 X — this avoids any annoying errors which may pop up by comparing floating-point numbers (in this problem, X and Y are small enough that `float` and `double` may be safely used, but it isn’t always the case, and writing safe code is a good practice).

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(1) per test.

#
[](#code-7)CODE:

Python
``for _ in range(int(input())):
	x, y = map(int, input().split())
	if 100*y <= 107*x:
		print('YES')
	else:
		print('NO')
``

</details>

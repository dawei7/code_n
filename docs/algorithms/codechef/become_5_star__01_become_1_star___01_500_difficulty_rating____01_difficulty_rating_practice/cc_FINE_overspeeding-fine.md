# Overspeeding Fine

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FINE |
| Difficulty Rating | 335 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [FINE](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/FINE) |

---

## Problem Statement

Chef was driving on a highway at a speed of $X$ km/hour.

To avoid accidents, there are fine imposed on overspeeding as follows:
- No fine if the speed of the car $\leq 70$ km/hour.
- Rs $500$ fine if the speed of the car is strictly greater than $70$ and $\leq 100$.
- Rs $2000$ fine if the speed of the car is strictly greater than $100$.

Determine the fine Chef needs to pay.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single integer $X$ denoting the speed of Chef's car.

---

## Output Format

For each test case, output the fine paid by Chef.

---

## Constraints

- $1 \leq T \leq 200$
- $1 \leq X \leq 200$

---

## Examples

**Example 1**

**Input**

```text
7
40
110
70
100
69
101
85
```

**Output**

```text
0
2000
0
500
0
2000
500
```

**Explanation**

**Test case $1$:** The speed is $\leq 70$. Thus, Chef does not need to pay any fine.

**Test case $2$:** The speed is greater than $100$. Thus, Chef needs to pay $2000$ as fine.

**Test case $3$:** The speed is $\leq 70$. Thus, Chef does not need to pay any fine.

**Test case $4$:** The speed is greater than $70$ and $\leq 100$. Thus, Chef needs to pay $500$ as fine amount.

**Test case $5$:** The speed is $\leq 70$. Thus, Chef does not need to pay any fine.

**Test case $6$:** The speed is greater than $100$. Thus, Chef needs to pay $2000$ as fine.

**Test case $7$:** The speed is greater than $70$ and $\leq 100$. Thus, Chef needs to pay $500$ as fine amount.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
40
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
110
```

**Output for this case**

```text
2000
```



#### Test case 3

**Input for this case**

```text
70
```

**Output for this case**

```text
0
```



#### Test case 4

**Input for this case**

```text
100
```

**Output for this case**

```text
500
```



#### Test case 5

**Input for this case**

```text
69
```

**Output for this case**

```text
0
```



#### Test case 6

**Input for this case**

```text
101
```

**Output for this case**

```text
2000
```



#### Test case 7

**Input for this case**

```text
85
```

**Output for this case**

```text
500
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/FINE)

[Contest: Division 1](https://www.codechef.com/JAN231A/problems/FINE)

[Contest: Division 2](https://www.codechef.com/JAN231B/problems/FINE)

[Contest: Division 3](https://www.codechef.com/JAN231C/problems/FINE)

[Contest: Division 4](https://www.codechef.com/JAN231D/problems/FINE)

***Author:*** [utkarsh_25dec](https://www.codechef.com/users/utkarsh_25dec)

***Testers:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093), [tabr](https://www.codechef.com/users/tabr)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given Chef’s speed on a highway, determine the fine he has to pay.

#
[](#explanation-5)EXPLANATION:

This is a direct application of `if` conditions.

The statement gives three conditions to check for the answer, so check each of them and output the appropriate answer:

- If X \leq 70, the answer is 0.

- If 70 \lt X \leq 100, the answer is 500.

- If X \gt 100, the answer is 2000.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(1) per testcase.

#
[](#code-7)CODE:

Code (Python)
``for _ in range(int(input())):
    x = int(input())
    if x <= 70: print(0)
    elif x <= 100: print(500)
    else: print(2000)
``

</details>

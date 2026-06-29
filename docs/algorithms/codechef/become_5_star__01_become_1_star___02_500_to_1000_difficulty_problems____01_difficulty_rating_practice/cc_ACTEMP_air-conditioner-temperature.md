# Air Conditioner Temperature

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ACTEMP |
| Difficulty Rating | 584 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [ACTEMP](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/ACTEMP) |

---

## Problem Statement

There are three people sitting in a room - Alice, Bob, and Charlie. They need to decide on the temperature to set on the air conditioner. Everyone has a demand each:

- Alice wants the temperature to be at least $A$ degrees.
- Bob wants the temperature to be at most $B$ degrees.
- Charlie wants the temperature to be at least $C$ degrees.

Can they all agree on some temperature, or not?

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line which contains three integers - $A, B, C$.

---

## Output Format

For each test case, output on a new line, "Yes" or "No". "Yes", if they can decide on some temperature which fits all their demands. Or "No", if no temperature fits all their demands.

You may print each character of the string in either uppercase or lowercase (for example, the strings `NO`, `nO`, `No`, and `no` will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq A, B, C \leq 100$

---

## Examples

**Example 1**

**Input**

```text
4
30 35 25
30 35 40
30 35 35
30 25 35
```

**Output**

```text
Yes
No
Yes
No
```

**Explanation**

**Test Case 1:** Alice wants the temperature to be $\ge 30$, Bob wants it to be $\le 35$, and Charlie wants it to be $\ge 25$. The temperatures $30, 31, 32, 33, 34, 35$ all satisfy all their demands. So they can choose any of these 6 temperatures, and so the answer is "Yes".

**Test Case 2:** Alice wants the temperature to be $\ge 30$, Bob wants it to be $\le 35$, and Charlie wants it to be $\ge 40$. A number can't be both $\ge 40$, and $\le 35$. So there is no temperature that satisfies all their demands. So the answer is "No".

**Test Case 3:** Alice wants the temperature to be $\ge 30$, Bob wants it to be $\le 35$, and Charlie wants it to be $\ge 35$. The temperature $35$ satisfies all their demands. So the answer is "Yes".

**Test Case 4:** Alice wants the temperature to be $\ge 30$, Bob wants it to be $\le 25$, and Charlie wants it to be $\ge 35$. A number can't be both $\ge 30$, and $\le 25$. So there is no temperature that satisfies all their demands. So the answer is "No".

**Separated test cases**

#### Test case 1

**Input for this case**

```text
30 35 25
```

**Output for this case**

```text
Yes
```



#### Test case 2

**Input for this case**

```text
30 35 40
```

**Output for this case**

```text
No
```



#### Test case 3

**Input for this case**

```text
30 35 35
```

**Output for this case**

```text
Yes
```



#### Test case 4

**Input for this case**

```text
30 25 35
```

**Output for this case**

```text
No
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/ACTEMP)

[Contest: Division 1](https://www.codechef.com/START52A/problems/ACTEMP)

[Contest: Division 2](https://www.codechef.com/START52B/problems/ACTEMP)

[Contest: Division 3](https://www.codechef.com/START52C/problems/ACTEMP)

[Contest: Division 4](https://www.codechef.com/START52D/problems/ACTEMP)

***Author:*** [CodeChef Admin](https://www.codechef.com/users/admin)

***Preparer:*** [Souradeep Paul](https://www.codechef.com/users/souradeep1999)

***Testers:*** [Takuki Kurokawa](https://www.codechef.com/users/tabr), [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

584

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Alice wants the air conditioner to be set to at least A degrees, Bob wants it to be set to at most B degrees, and Charlie wants it to be set to at least C degrees.

Is there a temperature that satisfies all three?

#
[](#explanation-5)EXPLANATION

A simple application of `if` conditions: note that Alice and Bob can be simultaneously satisfied if and only if A \leq B. Similarly, Charlie and Bob can be simultaneously satisfied if and only if C \leq B.

So,

- The answer is “Yes” if both A \leq B and C \leq B hold

- The answer is “No” otherwise.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print('yes' if max(a, c) <= b else 'no')
``

</details>

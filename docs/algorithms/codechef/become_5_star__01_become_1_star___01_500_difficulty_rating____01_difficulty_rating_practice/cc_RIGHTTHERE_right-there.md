# Right There

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RIGHTTHERE |
| Difficulty Rating | 299 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [RIGHTTHERE](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/RIGHTTHERE) |

---

## Problem Statement

*If you wanna party, if you, if you wanna party \
Then put your hands up*

Chef wants to host a party with a total of $N$ people.
However, the party hall has a capacity of $X$ people. Find whether Chef can host the party.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two space-separated integers $N$ and $X$  — the total number of people and the capacity of the party hall.

---

## Output Format

For each test case, output on a new line, `YES`, if Chef can host the party and `NO` otherwise.

Each character of the output may be printed in either uppercase or lowercase. That is, the strings `NO`, `no`, `nO`, and `No` will be treated as equivalent.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N, X \leq 10$

---

## Examples

**Example 1**

**Input**

```text
4
2 5
4 3
6 6
10 9
```

**Output**

```text
YES
NO
YES
NO
```

**Explanation**

**Test case $1$:** Chef wants to host a party with $2$ people. Since the capacity of the hall is $5$, he can host the party.

**Test case $2$:** Chef wants to host a party with $4$ people. Since the capacity of the hall is $3$, he can not host the party.

**Test case $3$:** Chef wants to host a party with $6$ people. Since the capacity of the hall is $6$, he can host the party.

**Test case $4$:** Chef wants to host a party with $10$ people. Since the capacity of the hall is $9$, he can not host the party.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 5
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
4 3
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
6 6
```

**Output for this case**

```text
YES
```



#### Test case 4

**Input for this case**

```text
10 9
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

[Practice](https://www.codechef.com/problems/RIGHTTHERE)

[Contest: Division 1](https://www.codechef.com/START93A/problems/RIGHTTHERE)

[Contest: Division 2](https://www.codechef.com/START93B/problems/RIGHTTHERE)

[Contest: Division 3](https://www.codechef.com/START93C/problems/RIGHTTHERE)

[Contest: Division 4](https://www.codechef.com/START93D/problems/RIGHTTHERE)

***Author:*** [notsoloud](https://www.codechef.com/users/notsoloud)

***Tester & Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

299

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef wants to host N people for a party, but the party hall has a capacity of X people.

Can Chef host the party?

#
[](#explanation-5)EXPLANATION:

For everyone to fit within the hall’s capacity, N \leq X must hold.

So, the answer is `Yes` if N \leq X and `No` otherwise.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per testcase.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    n, x = map(int, input().split())
    print('Yes' if n <= x else 'No')
``

</details>

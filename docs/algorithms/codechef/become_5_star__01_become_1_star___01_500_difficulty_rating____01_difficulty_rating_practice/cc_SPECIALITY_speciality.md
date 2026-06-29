# Speciality

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SPECIALITY |
| Difficulty Rating | 434 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [SPECIALITY](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/SPECIALITY) |

---

## Problem Statement

On every CodeChef user's profile page, the list of problems that they have set, tested, and written editorials for, is listed at the bottom.

Given the number of problems in each of these $3$ categories as $X, Y,$ and $Z$ respectively (where all three integers are **distinct**), find if the user has been most active as a `Setter`, `Tester`, or `Editorialist`.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of three space-separated integers $X, Y,$ and $Z$ - the number of problems they have set, tested, and written editorials for.

---

## Output Format

For each test case, output in a new line:
- `Setter`, if the user has been most active as a setter.
- `Tester`, if the user has been most active as a tester.
- `Editorialist`, if the user has been most active as an editorialist.

Note that the output is case-insensitive. Thus, the strings `SETTER`, `setter`, `seTTer`, and `Setter` are all considered the same.

---

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq X, Y, Z \leq 100$, where $X, Y,$ and $Z$ are **distinct**.

---

## Examples

**Example 1**

**Input**

```text
4
5 3 2
1 2 4
2 5 1
9 4 5
```

**Output**

```text
Setter
Editorialist
Tester
Setter
```

**Explanation**

**Test case $1$:** The number of problems that the user has set is greater than the number of problems tested or written editorials for. Thus, the user is most active as setter.

**Test case $2$:** The number of problems that the user has written editorials for, is greater than the number of problems set or tested. Thus, the user is most active as editorialist.

**Test case $3$:** The number of problems that the user has tested is greater than the number of problems set or written editorials for. Thus, the user is most active as tester.

**Test case $4$:** The number of problems that the user has set is greater than the number of problems tested or written editorials for. Thus, the user is most active as setter.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 3 2
```

**Output for this case**

```text
Setter
```



#### Test case 2

**Input for this case**

```text
1 2 4
```

**Output for this case**

```text
Editorialist
```



#### Test case 3

**Input for this case**

```text
2 5 1
```

**Output for this case**

```text
Tester
```



#### Test case 4

**Input for this case**

```text
9 4 5
```

**Output for this case**

```text
Setter
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/SPECIALITY)

[Contest: Division 1](https://www.codechef.com/START59A/problems/SPECIALITY)

[Contest: Division 2](https://www.codechef.com/START59B/problems/SPECIALITY)

[Contest: Division 3](https://www.codechef.com/START59C/problems/SPECIALITY)

[Contest: Division 4](https://www.codechef.com/START59D/problems/SPECIALITY)

***Author:*** [Kanhaiya Mohan](https://www.codechef.com/users/notsoloud)

***Tester:*** [Takuki Kurokawa](https://www.codechef.com/users/tabr)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given the number of problems a CodeChef user has set, tested, and written editorials for (X, Y, Z respectively), find out which one a user has been most prolific at.

#
[](#explanation-5)EXPLANATION:

Since there are only 3 values and all of them are distinct, `if` conditions can be used to check for the answer.

- If X \gt Y and X \gt Z, the answer is “Setter”.

- If Y \gt X and Y \gt Z, the answer is “Tester”.

- If Z \gt X and Z \gt Y, the answer is “Editorialist”.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    x, y, z = map(int, input().split())
    if x > max(y, z):
        print('Setter')
    elif y > max(x, z):
        print('Tester')
    else:
        print('Editorialist')
``

</details>

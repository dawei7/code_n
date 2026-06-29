# Waiting Time

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | WAITTIME |
| Difficulty Rating | 319 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [WAITTIME](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/WAITTIME) |

---

## Problem Statement

Chef is eagerly waiting for a piece of information. His secret agent told him that this information would be revealed to him after $K$ weeks.

$X$ days have already passed and Chef is getting restless now. Find the number of **remaining** days Chef has to wait for, to get the information.

It is guaranteed that the information has not been revealed to the Chef yet.

---

## Input Format

- The first line of input will contain an integer $T$ — the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two space-separated integers $K$ and $X$, as described in the problem statement.

---

## Output Format

For each test case, output the number of remaining days that Chef will have to wait for.

---

## Constraints

- $1 \leq T \leq 500$
- $1 \leq K \leq 10$
- $1 \leq X \lt 7\cdot K$

---

## Examples

**Example 1**

**Input**

```text
4
1 5
1 6
1 1
1 2
```

**Output**

```text
2
1
6
5
```

**Explanation**

**Test case $1$:** The information will be revealed to the Chef after $1$ week, which is equivalent to $7$ days. Chef has already waited for $5$ days, so he needs to wait for $2$ more days in order to get the information.

**Test case $2$:** The information will be revealed to the Chef after $1$ week, which is equivalent to $7$ days. Chef has already waited for $6$ days, so he needs to wait for $1$ more day in order to get the information.

**Test case $3$:** The information will be revealed to the Chef after $1$ week, which is equivalent to $7$ days. Chef has already waited for $1$ day, so he needs to wait for $6$ more days in order to get the information.

**Test case $4$:** The information will be revealed to the Chef after $1$ week, which is equivalent to $7$ days. Chef has already waited for $2$ days, so he needs to wait for $5$ more days in order to get the information.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 5
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
1 6
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
1 1
```

**Output for this case**

```text
6
```



#### Test case 4

**Input for this case**

```text
1 2
```

**Output for this case**

```text
5
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START43A/problems/WAITTIME)

[Contest Division 2](https://www.codechef.com/START43B/problems/WAITTIME)

[Contest Division 3](https://www.codechef.com/START43C/problems/WAITTIME)

[Contest Division 4](https://www.codechef.com/START43D/problems/WAITTIME)

Setter: [Lavish Gupta](https://www.codechef.com/users/lavish_adm)

Tester: [Nishank Suresh](https://www.codechef.com/users/iceknight1093), [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

Editorialist: [Pratiyush Mishra](https://www.codechef.com/users/foxy7)

#
[](#difficulty-2)DIFFICULTY:

To be Calculated

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef is eagerly waiting for a piece of information. His secret agent told him that this information would be revealed to him after K weeks.

X days have already passed and Chef is getting restless now. Find the number of **remaining** days Chef has to wait for, to get the information.

It is guaranteed that the information has not been revealed to the Chef yet.

#
[](#explanation-5)EXPLANATION:

Since we are expected to get information in K weeks, this implies that we will get information in (7 \times K) days. Now since X days have already been passed, so the remaining days, we have to wait are:

(7 \times K) - X

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1), for each test case.

#
[](#solution-7)SOLUTION:

[Editorialist’s Solution](http://p.ip.fi/dssG)

[Tester1’s Solution](http://p.ip.fi/4vtz)

[Tester2’s Solution](http://p.ip.fi/aUXd)

</details>

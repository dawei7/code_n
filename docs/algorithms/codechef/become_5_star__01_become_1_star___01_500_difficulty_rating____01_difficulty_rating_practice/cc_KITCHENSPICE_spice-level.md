# Spice Level

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | KITCHENSPICE |
| Difficulty Rating | 390 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [KITCHENSPICE](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/KITCHENSPICE) |

---

## Problem Statement

Each item in Chef’s menu is assigned a spice level from $1$ to $10$. Based on the spice level, the item is categorised as:
- `MILD`: If the spice level is less than $4$.
- `MEDIUM`: If the spice level is greater than equal to $4$ but less than $7$.
- `HOT`: If the spice level is greater than equal to $7$.

Given that the spice level of an item is $X$, find the category it lies in.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of an integer $X$ — the spice level of the item.

---

## Output Format

For each test case, output on a new line, the category that the item lies in.

You may print each character in uppercase or lowercase. For example, `HOT`, `hot`, `Hot`, and `hOT` are all considered the same.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq X \leq 10$

---

## Examples

**Example 1**

**Input**

```text
4
4
1
6
9
```

**Output**

```text
MEDIUM
MILD
MEDIUM
HOT
```

**Explanation**

**Test case $1$:** The spice level is greater than $4$ but less than $7$. Thus, it is in `MEDIUM` category.

**Test case $2$:** The spice level is less than $4$. Thus, it is in `MILD` category.

**Test case $3$:** The spice level is greater than $4$ but less than $7$. Thus, it is in `MEDIUM` category.

**Test case $4$:** The spice level is greater than $7$. Thus, it is in `HOT` category.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
```

**Output for this case**

```text
MEDIUM
```



#### Test case 2

**Input for this case**

```text
1
```

**Output for this case**

```text
MILD
```



#### Test case 3

**Input for this case**

```text
6
```

**Output for this case**

```text
MEDIUM
```



#### Test case 4

**Input for this case**

```text
9
```

**Output for this case**

```text
HOT
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/KITCHENSPICE)

[Contest: Division 1](https://www.codechef.com/START70A/problems/KITCHENSPICE)

[Contest: Division 2](https://www.codechef.com/START70B/problems/KITCHENSPICE)

[Contest: Division 3](https://www.codechef.com/START70C/problems/KITCHENSPICE)

[Contest: Division 4](https://www.codechef.com/START70D/problems/KITCHENSPICE)

***Author:*** [notsoloud](https://www.codechef.com/users/notsoloud)

***Testers:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093), [satyam_343](https://www.codechef.com/users/satyam_343)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

390

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given the spice level of an item on Chef’s menu, decide whether it is `MILD`, `MEDIUM`, or `HOT`.

#
[](#explanation-5)EXPLANATION:

This is a standard application of `if` conditions. Given X, simply check which one of the three conditions it satisfies:

- If X \lt 4, the answer is `MILD`

- If 4 \leq X \lt 7, the answer is `MEDIUM`

- If 7 \leq X, the answer is `HOT`

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(1) per testcase.

#
[](#code-7)CODE:

Code (Python)
``for _ in range(int(input())):
    x = int(input())
    if x < 4: print('Mild')
    elif x < 7: print('Medium')
    else: print('Hot')
``

</details>

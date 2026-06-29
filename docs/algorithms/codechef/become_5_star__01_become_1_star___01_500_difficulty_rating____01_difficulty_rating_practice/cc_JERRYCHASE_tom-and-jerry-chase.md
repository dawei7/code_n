# Tom and Jerry Chase

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | JERRYCHASE |
| Difficulty Rating | 298 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [JERRYCHASE](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/JERRYCHASE) |

---

## Problem Statement

In a classic chase, Tom is running after Jerry as Jerry has eaten Tom's favourite food.

Jerry is running at a speed of $X$ metres per second while Tom is chasing him at a speed of $Y$ metres per second. Determine whether Tom will be able to catch Jerry.

Note that initially Jerry is not at the same position as Tom.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two space-separated integers $X$ and $Y$ — the speeds of Jerry and Tom respectively.

---

## Output Format

For each test case, output on a new line, `YES`, if Tom will be able to catch Jerry. Otherwise, output `NO`.

You can print each character in uppercase or lowercase. For example `NO`, `no`, `No`, and `nO` are all considered the same.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \le X, Y \le 10$

---

## Examples

**Example 1**

**Input**

```text
4
2 3
4 1
1 1
3 5
```

**Output**

```text
YES
NO
NO
YES
```

**Explanation**

**Test case $1$:** Jerry is running at the speed of $2$ metres per second while Tom is chasing him at the speed of $3$ metres per second. Since Jerry's speed is less than Tom's, Tom will eventually catch Jerry.

**Test case $2$:** Jerry is running at the speed of $4$ metres per second while Tom is chasing him at the speed of $1$ metres per second. Since Jerry's speed is higher than Tom's, Tom will never be able to catch Jerry.

**Test case $3$:** Jerry is running at the speed of $1$ metre per second while Tom is chasing him at the speed of $1$ metre per second. Since Jerry's speed is same as that of Tom's and both of them are not at the same position, Tom will never be able to catch Jerry.

**Test case $4$:** Jerry is running at the speed of $3$ metres per second while Tom is chasing him at the speed of $5$ metres per second. Since Jerry's speed is less than Tom's, Tom will eventually catch Jerry.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 3
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
4 1
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
1 1
```

**Output for this case**

```text
NO
```



#### Test case 4

**Input for this case**

```text
3 5
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

[Practice](https://www.codechef.com/problems/JERRYCHASE)

[Contest: Division 1](https://www.codechef.com/START77A/problems/JERRYCHASE)

[Contest: Division 2](https://www.codechef.com/START77B/problems/JERRYCHASE)

[Contest: Division 3](https://www.codechef.com/START77C/problems/JERRYCHASE)

[Contest: Division 4](https://www.codechef.com/START77D/problems/JERRYCHASE)

***Author:*** [notsoloud](https://www.codechef.com/users/notsoloud)

***Testers:*** [iceknight1093](https://www.codechef.com/users/iceknight1093), [rivalq](https://www.codechef.com/users/rivalq)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Jerry is running away from Tom at X metres per second; while Tom is chasing at Y metres oer second.

Will Tom catch Jerry eventually?

#
[](#explanation-5)EXPLANATION:

As long as Tom is strictly faster than Jerry, Jerry will eventually be caught.

So, the answer is `Yes` if X \lt Y and `No` otherwise; which can be checked using `if` conditions.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    x, y = map(int, input().split())
    print('Yes' if x < y else 'No')
``

</details>

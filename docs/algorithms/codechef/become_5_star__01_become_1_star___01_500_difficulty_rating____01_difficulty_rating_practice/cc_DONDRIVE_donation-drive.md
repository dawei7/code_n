# Donation Drive

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DONDRIVE |
| Difficulty Rating | 272 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [DONDRIVE](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/DONDRIVE) |

---

## Problem Statement

A blood drive aims to collect $N$ number of blood donations.
The drive has collected $X$ donations so far.
Find the remaining number of donations needed to reach the target.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case contains two space-separated integers $N$ and $X$ — the number of required donations and the number of collected donations, respectively.

---

## Output Format

For each test case, output on a new line, the remaining number of donations needed to reach the target.

---

## Constraints

- $1 \leq T \leq 200$
- $1 \leq X \le N \leq 20$

---

## Examples

**Example 1**

**Input**

```text
4
5 2
3 3
5 4
7 5
```

**Output**

```text
3
0
1
2
```

**Explanation**

**Test case $1$:** The drive aims to collect $5$ donations and has collected $2$ already. Thus, they need to collect $3$ more donations to reach the target.

**Test case $2$:** The drive aims to collect $3$ donations and has collected $3$ already. Thus, they need to collect no more donations to reach the target.

**Test case $3$:** The drive aims to collect $5$ donations and has collected $4$ already. Thus, they need to collect $1$ more donation to reach the target.

**Test case $4$:** The drive aims to collect $7$ donations and has collected $5$ already. Thus, they need to collect $2$ more donations to reach the target.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 2
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
3 3
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
5 4
```

**Output for this case**

```text
1
```



#### Test case 4

**Input for this case**

```text
7 5
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/DONDRIVE)

[Contest: Division 1](https://www.codechef.com/START95A/problems/DONDRIVE)

[Contest: Division 2](https://www.codechef.com/START95B/problems/DONDRIVE)

[Contest: Division 3](https://www.codechef.com/START95C/problems/DONDRIVE)

[Contest: Division 4](https://www.codechef.com/START95D/problems/DONDRIVE)

***Author:*** [notsoloud](https://www.codechef.com/users/notsoloud)

***Tester:*** [satyam_343](https://www.codechef.com/users/satyam_343)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

272

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

A blood drive aims to collect N donations, of which X have been collected so far.

How many more are needed to reach their target?

# [](#explanation-5)EXPLANATION:

X out of N donations are done, which leaves N-X remaining.

So, the answer is N-X.

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per testcase.

# [](#code-7)CODE:

Editorialist's code (Python)
``testcases = int(input())
for t in range(testcases):
    n, x = map(int, input().split())
    print(n - x)
``

</details>

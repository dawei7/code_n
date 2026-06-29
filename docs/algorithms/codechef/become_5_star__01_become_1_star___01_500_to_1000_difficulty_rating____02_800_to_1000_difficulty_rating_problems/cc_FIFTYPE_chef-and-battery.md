# Chef and Battery 

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FIFTYPE |
| Difficulty Rating | 901 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [FIFTYPE](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/FIFTYPE) |

---

## Problem Statement

Chef's phone has a battery level of $N$ percent.
Each minute:
- If the phone is on charging, the battery level **increases** by $2\%$.
- Otherwise, the battery level **decreases** by $3\%$.

Find the **minimum** time in which Chef can make the battery level reach **exactly** $50\%$.
Note that the battery level should always lie in the range $0$ to $100$ (both included).

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of single lines of input $N$ - the current battery level of Chef's phone.

---

## Output Format

For each test case, output on a new line the **minimum** time in which Chef can make the battery level reach **exactly** $50\%$.

---

## Constraints

- $1 \leq T \leq 1000$
- $0 \leq N \leq 100$

---

## Examples

**Example 1**

**Input**

```text
4
51
50
23
0
```

**Output**

```text
2
0
16
25
```

**Explanation**

**Test case $1$:** Chef can use his phone for $1$ minute. Thus, the battery drops to $48\%$.
Then, he can charge it for $1$ minute. Thus, the battery reaches exactly $50\%$.

**Test case $2$:** The battery level is already at $50\%$.

**Test case $3$:** Chef can charge the battery for $15$ minutes and use it for $1$ minute.
Thus, after $16$ minutes, the battery will be $50\%$ .

**Test case $4$:** Chef can charge the battery for $25$ minutes to reach the battery level of $50\%$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
51
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
50
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
23
```

**Output for this case**

```text
16
```



#### Test case 4

**Input for this case**

```text
0
```

**Output for this case**

```text
25
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/FIFTYPE)

[Contest: Division 1](https://www.codechef.com/START86A/problems/FIFTYPE)

[Contest: Division 2](https://www.codechef.com/START86B/problems/FIFTYPE)

[Contest: Division 3](https://www.codechef.com/START86C/problems/FIFTYPE)

[Contest: Division 4](https://www.codechef.com/START86D/problems/FIFTYPE)

***Author:*** [notsoloud](https://www.codechef.com/users/notsoloud)

***Tester:*** [yash_daga](https://www.codechef.com/users/yash_daga)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

901

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef’s phone battery is currently at N percent, and he wants it to reach exactly 50 percent.

Each minute, the battery can either increase by 2 percent, or decrease by 3 percent.

What’s the minimum time needed for the battery to reach 50 percent?

#
[](#explanation-5)EXPLANATION:

There is an obvious greedy simulation approach here:

- If the battery is \gt 50, reduce it by 3.

- If the battery is \lt 50, increase it by 2.

- If the battery equals 50, stop.

This greedy is correct, and so directly simulating it is enough to get AC.

This simulation can be done using a `while` loop and `if` conditions.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    ans = 0
    while n != 50:
        if n > 50: n -= 3
        else: n += 2
        ans += 1
    print(ans)
``

</details>

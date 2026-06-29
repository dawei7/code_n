# Snapchat

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SNAPCHAT |
| Difficulty Rating | 965 |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [SNAPCHAT](https://www.codechef.com/practice/course/arrays/ARRAYSPRO/problems/SNAPCHAT) |

---

## Problem Statement

The most popular feature on snapchat is *Snapchat Streak*.
A *streak* is maintained between two people if **both** of them send **at least one** snap to each other **daily**.
If, on any day, either person forgets to send at least one snap, the streak breaks and the streak count is set to $0$.

Chef and Chefina like maintaining their snapchat streak. You observed the snap count of both of them for $N$ consecutive days.
On the $i^{th}$ day, Chef sent $A_i$ snaps to Chefina while Chefina sent $B_i$ snaps to Chef.

Find the **maximum** streak count they achieved in those $N$ days.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains an integer $N$ — the number of days you observed.
    - The second lines contains $N$ space-separated integers — $A_1, A_2, \ldots, A_N$, the number of snaps Chef sent to Chefina on the $i^{th}$ day.
    - The third lines contains $N$ space-separated integers — $B_1, B_2, \ldots, B_N$, the number of snaps Chefina sent to Chef on the $i^{th}$ day.

---

## Output Format

For each test case, output on a new line, the **maximum** streak count they achieved in those $N$ days.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 1000$
- $0 \leq A_i, B_i \leq 100$

---

## Examples

**Example 1**

**Input**

```text
4
3
3 1 2
2 4 1
2
0 0
10 10
4
5 4 0 2
3 1 1 0
5
0 1 1 2 0
1 1 0 0 3
```

**Output**

```text
3
0
2
1
```

**Explanation**

**Test case $1$:** For all $3$ days, both Chef and Chefina sent at least one snap per day. Thus, at the end of third day, the streak count is $3$.

**Test case $2$:** Chef did not send any snap to Chefina. Thus, at the streak count remains $0$ on both days.

**Test case $3$:** For the first two days, both Chef and Chefina send at least one snap per day. Thus, at the end of second day, the streak count is $2$.
On the end of third day, since Chef did not send any snap, the streak count becomes $0$.
On the end of fourth day, since Chefina did not send any snap, the streak count remains $0$.

**Test case $4$:**
- On the end of first day, since Chef did not send any snap, the streak count remains $0$.
- On second day, both Chef and Chefina sent at least one snap. Thus, the streak count becomes $1$.
- On the end of third day, since Chefina did not send any snap, the streak count becomes $0$.
- On the end of fourth day, since Chefina did not send any snap, the streak count remains $0$.
- On the end of fifth day, since Chef did not send any snap, the streak count remains $0$.

The maximum streak count over $5$ days is $1$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
3 1 2
2 4 1
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
2
0 0
10 10
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
4
5 4 0 2
3 1 1 0
```

**Output for this case**

```text
2
```



#### Test case 4

**Input for this case**

```text
5
0 1 1 2 0
1 1 0 0 3
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/SNAPCHAT)

[Contest: Division 1](https://www.codechef.com/START71A/problems/SNAPCHAT)

[Contest: Division 2](https://www.codechef.com/START71B/problems/SNAPCHAT)

[Contest: Division 3](https://www.codechef.com/START71C/problems/SNAPCHAT)

[Contest: Division 4](https://www.codechef.com/START71D/problems/SNAPCHAT)

***Author:*** [notsoloud](https://www.codechef.com/users/notsoloud)

***Testers:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093), [rivalq](https://www.codechef.com/users/rivalq)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

965

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

On the i-th day, Chef sent A_i snaps to Chefina, and Chefina sent B_i snaps to Chef.

What is their longest streak?

#
[](#explanation-5)EXPLANATION:

Let’s call the i-th day *good* if A_i \gt 0 **and** B_i \gt 0.

The longest streak is then nothing but the longest consecutive set of good days.

One way of computing this is as follows:

- Let cur denote the length of the current segment of good days. Initially, cur = 0.

- Let ans denote the final answer. Initially, ans = 0.

- Then, for each i from 1 to N:

- If the i-th day is good, increase cur by 1. Otherwise, reset cur to 0.

- Then, set ans = \max(ans, cur)

In the end, ans is the answer.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N) per testcase.

#
[](#code-7)CODE:

Code (Python)
``for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans, cur = 0, 0
    for i in range(n):
        if a[i] > 0 and b[i] > 0: cur += 1
        else: cur = 0
        ans = max(ans, cur)
    print(ans)
``

</details>

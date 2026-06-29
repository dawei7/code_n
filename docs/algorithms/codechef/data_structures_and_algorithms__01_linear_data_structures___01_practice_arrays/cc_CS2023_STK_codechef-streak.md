# CodeChef Streak

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CS2023_STK |
| Difficulty Rating | 1009 |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [CS2023_STK](https://www.codechef.com/practice/course/arrays/ARRAYS/problems/CS2023_STK) |

---

## Problem Statement

CodeChef offers a feature called *streak count*. A streak is maintained if you solve **at least one** problem daily.

Om and Addy actively maintain their streaks on CodeChef. Over a span of $N$ consecutive days, you have observed the count of problems solved by each of them.

Your task is to determine the **maximum** streak achieved by Om and Addy and find who had the longer maximum streak.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains an integer $N$ — the number of days.
    - The second line of each test case contains $N$ space-separated integers, the $i^{th}$ of which is $A_i$, representing the problems solved by Om on the $i^{th}$ day.
    - The third line of each test case contains $N$ space-separated integers, the $i^{th}$ of which is $B_i$, representing the problems solved by Addy on the $i^{th}$ day.

---

## Output Format

For each test case, output:
- `OM`, if Om has longer maximum streak than Addy;
- `ADDY`, if Addy has longer maximum streak than Om;
- `DRAW`, if both have equal maximum streak.

You may print each character in uppercase or lowercase. For example, `OM`, `om`, `Om`, and `oM`, are all considered the same.

---

## Constraints

- $1 \leq T \leq 10^{5}$
- $1 \leq N \leq 10^{5}$
- $0 \leq A_i, B_i \leq 10^{9}$
- The sum of $N$ over all test cases won't exceed $6\cdot 10^{5}$.

---

## Examples

**Example 1**

**Input**

```text
3
6
1 7 3 0 2 13
0 2 3 4 5 0
3
1 3 4
3 1 2
5
1 2 3 0 1
1 2 0 2 3
```

**Output**

```text
Addy
Draw
Om
```

**Explanation**

**Test case $1$:** Om has a maximum streak of $3$ days, while Addy has a maximum streak of $4$ days.

**Test case $2$:** Both have the same maximum streak of $3$ days.

**Test case $3$:** Addy has a maximum streak of $2$ days and Om has a maximum streak of $3$ days.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
6
1 7 3 0 2 13
0 2 3 4 5 0
```

**Output for this case**

```text
Addy
```



#### Test case 2

**Input for this case**

```text
3
1 3 4
3 1 2
```

**Output for this case**

```text
Draw
```



#### Test case 3

**Input for this case**

```text
5
1 2 3 0 1
1 2 0 2 3
```

**Output for this case**

```text
Om
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CS2023_STK)

[Contest: Division 1](https://www.codechef.com/START94A/problems/CS2023_STK)

[Contest: Division 2](https://www.codechef.com/START94B/problems/CS2023_STK)

[Contest: Division 3](https://www.codechef.com/START94C/problems/CS2023_STK)

[Contest: Division 4](https://www.codechef.com/START94D/problems/CS2023_STK)

***Author:*** [himanshu154](https://www.codechef.com/users/himanshu154)

***Tester:*** [jay_1048576](https://www.codechef.com/users/jay_1048576)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given the solve counts of Om and Addy on each of N days, find which one among them had the longer streak.

#
[](#explanation-5)EXPLANATION:

First, let’s try to find Om’s longest streak of solving problems.

That is, we want to find the longest subarray of A that contains only non-zero elements.

That can be done by iterating across the array and maintaining the current length of a non-zero subarray.

In particular,

- Let \text{cur} be a variable denoting the current length of a non-zero subarray.

Initially, \text{cur} = 0.

- Then, for each i from 1 to N:

- If A_i \gt 0, increase \text{cur} by 1.

- Else, set \text{cur} to 0.

The maximum value of \text{cur} ever reached is the number we’re looking for.

Let this value be \text{mx}_A.

Similarly, Addy’s maximum streak can be found by applying this algorithm to array B, giving us the value \text{mx}_B.

Finally, compare \text{mx}_A and \text{mx}_B, and print `Om`, `Addy`, or `Draw` depending on which one is higher or if they’re equal.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per testcase.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    amx, bmx = 0, 0
    cura, curb = 0, 0
    for i in range(n):
        if a[i] == 0: cura = 0
        else: cura += 1

        if b[i] == 0: curb = 0
        else: curb += 1

        amx = max(amx, cura)
        bmx = max(bmx, curb)
    print('Om' if amx > bmx else ('Addy' if amx < bmx else 'Draw'))
``

</details>

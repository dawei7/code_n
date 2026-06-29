# Card Swipe

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CARDSWIPE |
| Difficulty Rating | 1172 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [CARDSWIPE](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/CARDSWIPE) |

---

## Problem Statement

In the bustling CodeChef office, the entrance is equipped with a high-tech card swipe system. Each employee is assigned a unique ID card that they use to swipe in and out of the building.

The system records every swipe, capturing the first swipe of an ID as in, second as out, third as in, and so on.
Given an array $A$ consisting of $N$ IDs denoting $N$ swipes throughout the day, find the **maximum** number of people in the office at any time.

Note that there is nobody inside the office before the first swipe.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains an integer $N$ — the number of swipes throughout the day.
    - The next line contains $N$ space-separated integers denoting the ID of the $i^{th}$ swipe.

---

## Output Format

For each test case, output on a new line, the **maximum** number of people in the office at any time.

---

## Constraints

- $1 \leq T \leq 2\cdot 10^5$
- $1 \leq N \leq 2\cdot 10^5$
- $1 \leq A_i \leq N$
- The sum of $N$ over all test cases won't exceed $10^6$.

---

## Examples

**Example 1**

**Input**

```text
4
4
1 2 2 1
4
1 1 1 2
5
3 5 2 4 1
5
1 2 1 5 4
```

**Output**

```text
2
2
5
3
```

**Explanation**

**Test case $1$:** Consider the following order of swipes:
- Person $1$ swipes and enters the office.
- Person $2$ swipes and enters the office.
- Person $2$ swipes and leaves the office.
- Person $1$ swipes and leaves the office.

Thus, the maximum number of people in the office at any time is $2$.

**Test case $2$:** Consider the following order of swipes:
- Person $1$ swipes and enters the office.
- Person $1$ swipes and leaves the office.
- Person $1$ swipes and enters the office.
- Person $2$ swipes and enters the office.

Thus, the maximum number of people in the office at any time is $2$.

**Test case $3$:** Five people swipe and enter the office. Thus, the maximum number of people in the office is $5$.

**Test case $4$:** Consider the following order of swipes:
- Person $1$ swipes and enters the office.
- Person $2$ swipes and enters the office.
- Person $1$ swipes and leaves the office.
- Person $5$ swipes and enters the office.
- Person $4$ swipes and enters the office.

Thus, the maximum number of people in the office at any time is $3$. Their IDs are $2, 5,$ and $4$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
1 2 2 1
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
4
1 1 1 2
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
5
3 5 2 4 1
```

**Output for this case**

```text
5
```



#### Test case 4

**Input for this case**

```text
5
1 2 1 5 4
```

**Output for this case**

```text
3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CARDSWIPE)

[Contest: Division 1](https://www.codechef.com/START99A/problems/CARDSWIPE)

[Contest: Division 2](https://www.codechef.com/START99B/problems/CARDSWIPE)

[Contest: Division 3](https://www.codechef.com/START99C/problems/CARDSWIPE)

[Contest: Division 4](https://www.codechef.com/START99D/problems/CARDSWIPE)

***Author:*** [notsoloud](https://www.codechef.com/users/notsoloud)

***Tester:*** [satyam_343](https://www.codechef.com/users/satyam_343)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

1172

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

You’re given a sequence of N swipe-ins and swipe-outs to a building.

Find the maximum number of people in it, at any point of time.

# [](#explanation-5)EXPLANATION:

Let \texttt{cur} denote the number of people currently in the building.

Initially, \texttt{cur} = 0.

Then, for each 1 \leq i \leq N:

- If A_i is not inside the building, this is an in-swipe.

So, \texttt{cur} will increase by 1.

- Otherwise, A_i was already inside the building, and this is an out-swipe.

\texttt{cur} will decrease by 1.

The final answer is the maximum value of \texttt{cur} across the entire process.

We only need to quickly check whether A_i is already inside the building or not.

This can be done, for example, with a `mark` array.

That is, keep an array `mark` of length N, where `mark[x] = 1` means person x is inside the building, and `mark[x] = 0` otherwise.

Then,

- When person A_i enters, set `mark[a[i]] = 1`.

- When person A_i exits, set `mark[a[i]] = 0`.

Each enter/exit is handled in \mathcal{O}(1) time, for a solution in \mathcal{O}(N) overall.

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per testcase.

# [](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    a = [0]*(n + 1)
    inside, ans = 0, 0
    for x in map(int, input().split()):
        if a[x] == 1: inside -= 1
        a[x] ^= 1
        if a[x] == 1: inside += 1
        ans = max(ans, inside)
    print(ans)
``

</details>

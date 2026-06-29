# Dracula Eats

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEAT |
| Difficulty Rating | 763 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [CHEAT](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/CHEAT) |

---

## Problem Statement

*Eat, drink, and be scary*

There are $N$ spooky days left until Halloween.
Dracula dines at a mysterious restaurant that changes its spooky menu daily. He particularly enjoys what they serve on Tuesday.

Today is Monday, so he wishes to calculate how many times he can indulge in his favourite menu in the next $N$ days **(including today)** before Halloween.

Note that Dracula follows the standard $7$-day calendar, with Tuesday immediately following Monday.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The only line of each test case contains a single integer $N$, denoting the number of spooky days.

---

## Output Format

For each test case, output on a new line the number of times Dracula would have had his favorite meal after $N$ days.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 1000$

---

## Examples

**Example 1**

**Input**

```text
4
1
10
15
16
```

**Output**

```text
0
2
2
3
```

**Explanation**

**Test case $1$:** The first day is Monday, and Dracula has only one day. So, no Tuesdays are encountered, and the answer is $0$.

**Test case $2$:** The first day is Monday, so the second and ninth days are Tuesdays.
Dracula can eat his favorite meal twice.

**Test case $3$:** Once again, the second and ninth days are Tuesday, so in $15$ days, Dracula still gets to eat his favorite meal only twice.

**Test case $4$:** After the ninth day, the $16$-th day is also a Tuesday. So, this time Dracula gets to eat his favorite meal three times - on days $2, 9, 16$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
10
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
15
```

**Output for this case**

```text
2
```



#### Test case 4

**Input for this case**

```text
16
```

**Output for this case**

```text
3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CHEAT)

[Contest: Division 1](https://www.codechef.com/START105A/problems/CHEAT)

[Contest: Division 2](https://www.codechef.com/START105B/problems/CHEAT)

[Contest: Division 3](https://www.codechef.com/START105C/problems/CHEAT)

[Contest: Division 4](https://www.codechef.com/START105D/problems/CHEAT)

***Author:*** [shubham0105](https://www.codechef.com/users/shubham0105)

***Tester:*** [raysh07](https://www.codechef.com/users/raysh07)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

763

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

Given N, compute the number of Tuesdays in the next N days if the first day is a Monday.

# [](#explanation-5)EXPLANATION:

A week has seven days, and the first Tuesday is on day 2.

So, the Tuesdays occur at days 2, 9, 16, 23, \ldots

Since N \leq 1000, it suffices to run a loop and iterate through all possibilities till you reach N.

Alternately, some simple math says that the answer is

\left\lceil \frac{N-1}{7} \right\rceil

where \left\lceil \ \ \right\rceil denotes the ceiling function.

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per testcase.

# [](#code-7)CODE:

Editorialist's code (Python, brute force)
``for _ in range(int(input())):
    n = int(input())
    ans = 0
    for x in range(2, n+1, 7): ans += 1
    print(ans)
``

Editorialist's code (Python, formula)
``for _ in range(int(input())):
    n = int(input())
    print((n-1+6)//7) # ceil(a/b) = (a+b-1)//b
``

</details>

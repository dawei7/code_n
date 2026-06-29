# Cost of Groceries

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | KITCHENCOST |
| Difficulty Rating | 799 |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [KITCHENCOST](https://www.codechef.com/practice/course/arrays/ARRAYSPRO/problems/KITCHENCOST) |

---

## Problem Statement

Chef visited a grocery store for fresh supplies. There are $N$ items in the store where the $i^{th}$ item has a freshness value $A_i$ and cost $B_i$.

Chef has decided to purchase **all** the items having a freshness value **greater than equal to** $X$. Find the total cost of the groceries Chef buys.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $X$ — the number of items and the minimum freshness value an item should have.
    - The second line contains $N$ space-separated integers, the array $A$, denoting the freshness value of each item.
    - The third line contains $N$ space-separated integers, the array $B$, denoting the cost of each item.

---

## Output Format

For each test case, output on a new line, the total cost of the groceries Chef buys.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N, X \leq 100$
- $1 \leq A_i, B_i \leq 100$

---

## Examples

**Example 1**

**Input**

```text
4
2 20
15 67
10 90
3 1
1 2 3
1 2 3
3 100
10 90 50
30 7 93
4 50
12 78 50 40
40 30 20 10
```

**Output**

```text
90
6
0
50
```

**Explanation**

**Test case $1$:** Item $2$ has freshness value greater than equal to $X = 20$. Thus, Chef buys item $2$. The total cost is $90$.

**Test case $2$:** Items $1, 2,$ and $3$ have freshness value greater than equal to $X = 1$. Thus, Chef buys all $3$ items. The total cost is $1+2+3 = 6$.

**Test case $3$:** No item has freshness value greater than equal to $X = 100$. Thus, Chef buys no items.

**Test case $4$:** Items $2$ and $3$ have freshness value greater than equal to $X = 50$. Thus, Chef buys items $2$ and $3$. The total cost is $30+20 = 50$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 20
15 67
10 90
```

**Output for this case**

```text
90
```



#### Test case 2

**Input for this case**

```text
3 1
1 2 3
1 2 3
```

**Output for this case**

```text
6
```



#### Test case 3

**Input for this case**

```text
3 100
10 90 50
30 7 93
```

**Output for this case**

```text
0
```



#### Test case 4

**Input for this case**

```text
4 50
12 78 50 40
40 30 20 10
```

**Output for this case**

```text
50
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/KITCHENCOST)

[Contest: Division 1](https://www.codechef.com/START70A/problems/KITCHENCOST)

[Contest: Division 2](https://www.codechef.com/START70B/problems/KITCHENCOST)

[Contest: Division 3](https://www.codechef.com/START70C/problems/KITCHENCOST)

[Contest: Division 4](https://www.codechef.com/START70D/problems/KITCHENCOST)

***Author:*** [notsoloud](https://www.codechef.com/users/notsoloud)

***Testers:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093), [satyam_343](https://www.codechef.com/users/satyam_343)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

799

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

There are N items in a grocery store, the i-th of which has freshness A_i and cost B_i. What is the cost of buying all items with a freshness of at least X?

#
[](#explanation-5)EXPLANATION:

It is enough to do what is asked for:

Iterate i from 1 to N, and if A_i \geq X, add B_i to the answer.

This can be done with the help of a `for` loop and an `if` statement.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N) per testcase.

#
[](#code-7)CODE:

Code (Python)
``for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if a[i] >= x: ans += b[i]
    print(ans)
``

</details>

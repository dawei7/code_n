# Hungry Chef

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BURGERS2 |
| Difficulty Rating | 1187 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [BURGERS2](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/BURGERS2) |

---

## Problem Statement

Chef is very hungry. So, Chef goes to a shop selling burgers. The shop has $2$ types of burgers:
- Normal burgers, which cost $X$ rupees each
- Premium burgers, which cost $Y$ rupees each (where $Y \gt X$)

Chef has $R$ rupees. Chef wants to buy **exactly** $N$ burgers. He also wants to maximize the number of premium burgers he buys. Determine the number of burgers of both types Chef must buy.

Output $-1$ if it is not possible for Chef to buy $N$ burgers.

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first and only line of each test case contains four space-separated integers $X$, $Y$, $N$ and $R$ — the cost of a normal burger, the cost of a premium burger, the number of burgers Chef wants to buy and the amount of money Chef has.

---

## Output Format

For each test case, output on a new line two integers: the number of normal burgers and the number of premium burgers Chef must buy satisfying the given conditions.

Output $-1$ if he cannot buy $N$ burgers.

---

## Constraints

- $1 \leq T \leq 10^4$
- $1 \le X \lt Y \le 1000$
- $1 \le N \le 10^6$
- $1 \le R \le 10^9$

---

## Examples

**Example 1**

**Input**

```text
4
2 10 4 12
4 8 10 50
99 100 5 10
9 10 10 200
```

**Output**

```text
4 0
8 2
-1
0 10
```

**Explanation**

**Test case $1$:** Chef has to buy $4$ normal burgers only. Even if he buys $1$ premium burger, he would not be able to buy $4$ burgers.

**Test case $2$:** Chef can buy $8$ normal burgers and $2$ premium burgers.

**Test case $3$:** It is not possible for Chef to buy $5$ burgers.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 10 4 12
```

**Output for this case**

```text
4 0
```



#### Test case 2

**Input for this case**

```text
4 8 10 50
```

**Output for this case**

```text
8 2
```



#### Test case 3

**Input for this case**

```text
99 100 5 10
```

**Output for this case**

```text
-1
```



#### Test case 4

**Input for this case**

```text
9 10 10 200
```

**Output for this case**

```text
0 10
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest](https://www.codechef.com/JULY222/)

[Practice](https://www.codechef.com/problems/BURGERS2)

**Setter:** [jeevanjyot](https://www.codechef.com/users/jeevanjyot)

**Testers:** [tejas10p](https://www.codechef.com/users/tejas10p), [rivalq](https://www.codechef.com/users/rivalq)

**Editorialist:** [hrishik85](https://www.codechef.com/users/hrishik85)

#
[](#difficulty-2)DIFFICULTY:

1187

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef is very hungry. So, Chef goes to a shop selling burgers. The shop has 2 types of burgers:

- Normal burgers, which cost X rupees each

- Premium burgers, which cost Y rupees each (where Y \gt X)

Chef has R rupees. Chef wants to buy **exactly** N burgers. He also wants to maximize the number of premium burgers he buys. Determine the number of burgers of both types Chef must buy.

Output -1 if it is not possible for Chef to buy N burgers.

#
[](#explanation-5)EXPLANATION:

The least amount that the Chef definitely needs is (X \times N). If R is less than this amount, we output -1

If the count of burgers purchased are x (normal burgers) and y (premium burgers), then we have the equation R \geq x \times X + y \times Y

R \geq (N - y) \times X + y \times Y

y \leq (R -(N\times X)) \div (Y-X)

Also - y \leq N

Once y is computed, we can output (N-y, y)

#
[](#time-complexity-6)TIME COMPLEXITY:

Time complexity is O(1).

#
[](#solution-7)SOLUTION:

Editorialist's Solution
``t=int(input())
for _ in range(t):
    X,Y,N,R = map(int,input().split())
    if (N*X)>R:
        print(-1)
    else:
        #R=X*(N-y)+Y*y
        y = min((R-N*X)//(Y-X),N)
        x = N - y
        print(x,y)
``

</details>

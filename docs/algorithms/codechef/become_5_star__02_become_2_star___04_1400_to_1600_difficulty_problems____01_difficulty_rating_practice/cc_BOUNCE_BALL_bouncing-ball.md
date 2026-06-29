# Bouncing Ball

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BOUNCE_BALL |
| Difficulty Rating | 1607 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1500 to 1600 difficulty problems |
| Official Link | [BOUNCE_BALL](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1600/problems/BOUNCE_BALL) |

---

## Problem Statement

You are given an array $A$ of length $N$, where each element represents either empty ground ($A_i = 0$) or a wall (a positive integer indicating the height of the wall).

You can place a ball on any empty ground (that is, choose an index $i$ with $A_i = 0$) and push it either to the right or to the left.
When the ball hits a wall, it decreases the height of the wall it hit by $1$, and then bounces back in the opposite direction. If the wall's height reaches $0$, it becomes empty ground.
The ball continues to move until it goes out of bounds.

Determine the number of ways to place and push the ball so that all walls are destroyed. Two ways are considered different if either the starting index of the ball or the direction of the push is different.

---

## Input Format

- The first line contains a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains a single integer $N$, denoting the size of the array $A$.
    - The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.
$A_i = 0$ means the $i$-th position is empty ground, and $A_i \gt 0$ denotes a wall of height $A_i$ at position $i$.

---

## Output Format

For each test case, print on a new line a single integer representing the number of ways all walls can be destroyed.

---

## Constraints

- $1 \leq T \leq 10^4$
- $3 \leq N \leq 10^5$
- $0 \leq A_i \leq 10^9$
- The sum of $N$ over all test cases won't exceed $2\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
4
1 0 0 2
5
1 1 0 1 1
5
2 4 0 5 0
3
1000 0 999
```

**Output**

```text
2
2
1
1
```

**Explanation**

**Test case $1$:** The ball can be placed at position $2$ or $3$ and pushed to the right.
- The ball hits the wall at position $4$, making its height $1$. It then bounces to the left direction.
- The ball hits the wall at position $1$, making its height $0$. It then bounces in the right direction.
- The ball hits the wall at position $4$, making its height $0$. Now, all the walls have height $0$.

It can be shown that there are no other ways to destroy all the walls.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
1 0 0 2
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
5
1 1 0 1 1
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
5
2 4 0 5 0
```

**Output for this case**

```text
1
```



#### Test case 4

**Input for this case**

```text
3
1000 0 999
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/BOUNCE_BALL)

[Contest: Division 1](https://www.codechef.com/START146A/problems/BOUNCE_BALL)

[Contest: Division 2](https://www.codechef.com/START146B/problems/BOUNCE_BALL)

[Contest: Division 3](https://www.codechef.com/START146C/problems/BOUNCE_BALL)

[Contest: Division 4](https://www.codechef.com/START146D/problems/BOUNCE_BALL)

***Author:*** [detective_dots](https://www.codechef.com/users/detective_dots)

***Tester:*** [mexomerf](https://www.codechef.com/users/mexomerf)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

TBD

# [](#prerequisites-3)PREREQUISITES:

Prefix sums

# [](#problem-4)PROBLEM:

There are N positions, each either contains a wall with height A_i or is empty.

You can place a ball at an empty index and push it either left or right.

When the ball hits a wall, it will reduce the wall’s height by 1 and then move in the opposite direction.

If a wall’s height reaches 0, it’s considered destroyed, and the ball can then pass over it.

Find the number of starting moves that result in every wall eventually being destroyed.

# [](#explanation-5)EXPLANATION:

Suppose we place a ball at index i, and push it left.

Observe that the ball will first hit a wall to the left of index i, then a wall to the right of index i, then a wall to the left, then a wall to the right, and so on - that is, it will alternate between hitting a wall to the left and to the right of index i.

Let L be the *total* height of all walls to the left of index i, and R be the total height of all walls to the right.

The ball’s bounce then alternately reduces L and R by 1.

When either L or R reach 0, there are no more walls on that side - so the ball will not hit anything and go out of bounds.

Our aim is to destroy every wall. This means *both* L and R should be 0 when the ball goes out of bounds.

Since we push the ball left from index i, and L and R decrease by 1 alternately, this is possible if and only if L = R, or L = R+1.

Similarly, if we initially push the ball right instead, it will destroy every wall if and only if L = R or L+1 = R.

Both cases are easy to check if we know L and R.

Note that L is simply the sum of all A_j for 1 \leq j \lt i, while R is the sum of A_j for indices i \lt j \leq N.

Both of these can be computed in constant time using prefix sums.

# [](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N) per testcase.

# [](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    pref = a[:]
    for i in range(1, n):
        pref[i] += pref[i-1]

    ans = 0
    for i in range(1, n-1):
        if a[i] != 0: continue
        if pref[i-1] - (pref[n-1] - pref[i]) == 0: ans += 2
        elif abs(pref[i-1] - (pref[n-1] - pref[i])) == 1: ans += 1
    if sum(a) == 0: ans += 4 # account for 1 and N
    print(ans)
``

</details>

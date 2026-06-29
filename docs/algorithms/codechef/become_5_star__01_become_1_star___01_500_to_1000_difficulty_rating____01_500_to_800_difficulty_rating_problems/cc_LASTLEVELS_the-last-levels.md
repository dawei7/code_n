# The Last Levels

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LASTLEVELS |
| Difficulty Rating | 679 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [LASTLEVELS](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/LASTLEVELS) |

---

## Problem Statement

Chef is playing a videogame, and is getting close to the end. He decides to finish the rest of the game in a single session.

There are $X$ levels remaining in the game, and each level takes Chef $Y$ minutes to complete. To protect against eye strain, Chef also decides that every time he completes $3$ levels, he will take a $Z$ minute break from playing. Note that there is no need to take this break if the game has been completed.

How much time (in minutes) will it take Chef to complete the game?

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of input will contain three space-separated integers $X$, $Y$, and $Z$.

---

## Output Format

For each test case, output on a new line the answer — the length of Chef's gaming session.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq X \leq 100$
- $5 \leq Y \leq 100$
- $5 \leq Z \leq 15$

---

## Examples

**Example 1**

**Input**

```text
4
2 12 10
3 12 10
7 20 8
24 45 15
```

**Output**

```text
24
36
156
1185
```

**Explanation**

**Test case 1: 2 12 10**
- X = 2 (2 levels remain)
- Y = 12 (each level takes 12 minutes)
- Z = 10 (Chef would take a 10-minute break every 3 levels, but since there are only 2 levels, no break is needed)

Since there are only 2 levels, and no break is needed (because Chef takes a break only after every 3 levels).

The total time = X × Y = 2 × 12 = 24 minutes.

**Test case 3: 7 20 8**
- X = 7 (7 levels remain)
- Y = 20 (each level takes 20 minutes)
- Z = 8  (Chef takes an 8-minute break after every 3 levels)

Now, let's break this down: \
Chef completes the first 3 levels: 3 x 20 = 60 minutes.\
After completing these 3 levels, Chef takes an 8-minute break.\
Chef completes another 3 levels: 3 x 20 = 60 minutes. \
After completing these 3 levels, Chef takes another 8-minute break.\
Now, Chef completes the remaining 1 level: 1 x 20 = 20 minutes.

So, the total time = 60 + 8 + 60 + 8 + 20 = 156  minutes.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 12 10
```

**Output for this case**

```text
24
```



#### Test case 2

**Input for this case**

```text
3 12 10
```

**Output for this case**

```text
36
```



#### Test case 3

**Input for this case**

```text
7 20 8
```

**Output for this case**

```text
156
```



#### Test case 4

**Input for this case**

```text
24 45 15
```

**Output for this case**

```text
1185
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest](https://www.codechef.com/LTIME110/)

[Practice](https://www.codechef.com/problems/LASTLEVELS)

**Setter:** [iceknight1093](https://www.codechef.com/users/iceknight1093)

**Testers:** [gamegame](https://www.codechef.com/users/gamegame)

**Editorialist:** [hrishik85](https://www.codechef.com/users/hrishik85)

#
[](#difficulty-2)DIFFICULTY:

679

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef is playing a videogame, and is getting close to the end. He decides to finish the rest of the game in a single session.

There are X levels remaining in the game, and each level takes Chef Y minutes to complete. To protect against eye strain, Chef also decides that every time he completes 3 levels, he will take a Z minute break from playing. Note that there is no need to take this break if the game has been completed.

How much time (in minutes) will it take Chef to complete the game?

#
[](#explanation-5)EXPLANATION:

The total time to complete **only** the levels = X \times Y

The number of gaps if X is not divisible by 3 are Gaps = X \div 3 (rounded  down to the closest integer)

The number of gaps if X is divisible by 3 are Gaps  = (X \div 3) - 1

Hence - total time to complete the game = X \times Y + Gaps \times Z

#
[](#time-complexity-6)TIME COMPLEXITY:

Time complexity is O(1).

#
[](#solution-7)SOLUTION:

Editorialist's Solution
``t=int(input())
for _ in range(t):
    x,y,z=map(int,input().split())
    gap=0
    if x%3==0:
        gap = (x//3)-1
    else:
        gap= (x//3)
    print(x*y+gap*z)
``

</details>

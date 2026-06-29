# Endless Appetizers

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MOZZ |
| Difficulty Rating | 752 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [MOZZ](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/MOZZ) |

---

## Problem Statement

*Life is a like a box of of mozzarella sticks. You never know what you're gonna get, but you can predict with [100 percent](https://www.gawker.com/my-14-hour-search-for-the-end-of-tgi-fridays-endless-ap-1606122925) accuracy that it will be a mozzarella stick.*

Chef's colleague issued a challenge to Chef: "If you eat more than $X$ mozzarella sticks, I'll give you $30$ rupees for each extra one you eat".
For example, if $X = 5$ and Chef eats $8$ sticks, he would receive $90$ rupees because he ate $3$ *extra* sticks.

You know that the restaurant serves $Y$ mozzarella sticks per plate.
You also know that Chef received $R$ rupees from his colleague as a result of the challenge.

What's the **maximum** number of plates of mozzarella sticks that Chef could have ordered?

**Note:**
- Chef won't order a new plate till he finishes eating all the sticks from the previous one.
- However, it's possible that Chef didn't finish all the sticks from the *final* plate he ordered.
See the explained examples below for more clarification.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of one line of input, containing three space-separated integers $X, Y, $ and $R$ — the lower limit on the number of sticks, the number of sticks on a single plate, and the money received by Chef.

---

## Output Format

For each test case, output on a new line the answer: the maximum number of plates Chef could have ordered.

---

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq X \leq 100$
- $1 \leq Y \leq 10$
- $0 \leq R \leq 3\cdot 10^4$
- It is guaranteed that $R$ is a multiple of $30$.

---

## Examples

**Example 1**

**Input**

```text
4
7 5 30
16 5 0
15 9 120
23 1 2130
```

**Output**

```text
2
4
3
94
```

**Explanation**

**Test case $1$:** Chef received $30$ rupees; meaning he ate $1$ extra stick.
Since $X = 7$, this means he must've eaten exactly $8$ sticks.
At $5$ sticks per plate, Chef would need $2$ plates to eat $8$ sticks (and two sticks from the second plate will remain uneaten).

**Test case $2$:** Chef received $0$ rupees. Since $X = 16$, this means he ate $\leq 16$ sticks.
The maximum he could've eaten is exactly $16$; and this would require $4$ plates since each plate has $5$ sticks.

**Test case $3$:** Chef received $120$ rupees, meaning he ate $4$ extra sticks.
This makes for a total of $15 + 4 = 19$ sticks, and at $9$ sticks per plate he would need $3$ plates.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
7 5 30
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
16 5 0
```

**Output for this case**

```text
4
```



#### Test case 3

**Input for this case**

```text
15 9 120
```

**Output for this case**

```text
3
```



#### Test case 4

**Input for this case**

```text
23 1 2130
```

**Output for this case**

```text
94
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/MOZZ)

[Contest: Division 1](https://www.codechef.com/START99A/problems/MOZZ)

[Contest: Division 2](https://www.codechef.com/START99B/problems/MOZZ)

[Contest: Division 3](https://www.codechef.com/START99C/problems/MOZZ)

[Contest: Division 4](https://www.codechef.com/START99D/problems/MOZZ)

***Author:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

***Tester:*** [satyam_343](https://www.codechef.com/users/satyam_343)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

752

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

Chef receives 30 rupees for each mozzarella stick he eats past the X-th one.

You know that Chef received R rupees, and each plate contains Y sticks.

Find the maximum number of plates Chef could’ve ordered.

# [](#explanation-5)EXPLANATION:

Chef received 30 rupees for each extra stick he ate.

Since he received R rupees in total, the number of extra sticks he ate is \frac{R}{30}.

This means the total number of sticks he ate is X + \frac{R}{30}.

Let this number be \text{tot}.

Each plate contains Y sticks.

So, Chef needs to order enough plates to have Y sticks in total.

The number of plates needed to do this is exactly

\left\lceil \frac{\text{tot}}{Y} \right\rceil

where \left\lceil \ \ \right\rceil denotes the [ceiling function](https://codeforces.com/blog/entry/113633).

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per testcase.

# [](#code-7)CODE:

Editorialist's code (Python)
``from math import ceil
for _ in range(int(input())):
    x, y, r = map(int, input().split())
    eaten = x + r//30
    print(int(ceil(eaten / y)))
``

</details>

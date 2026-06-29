# Chef and Candies

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFCAND |
| Difficulty Rating | 570 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [CHEFCAND](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/CHEFCAND) |

---

## Problem Statement

There are $N$ children and Chef wants to give them $1$ candy each. Chef already has $X$ candies with him. To buy the rest, he visits a candy shop. In the shop, packets containing **exactly** $4$ candies are available.

Determine the **minimum** number of candy packets Chef must buy so that he is able to give $1$ candy to each of the $N$ children.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of each test case contains two integers $N$ and $X$ — the number of children and the number of candies Chef already has.

---

## Output Format

For each test case, output the **minimum** number of candy packets Chef must buy so that he is able to give $1$ candy to each of the $N$ children.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N, X \leq 100$

---

## Examples

**Example 1**

**Input**

```text
4
20 12
10 100
10 9
20 9
```

**Output**

```text
2
0
1
3
```

**Explanation**

**Test Case $1$:** Chef must buy $2$ more packets after which he will have $20$ candies which will be enough to distribute $1$ candy to each of the $20$ children.

**Test Case $2$:** Chef does not need to buy more packets since he already has $100$ candies which are enough to distribute $1$ candy to each of the $10$ children.

**Test Case $3$:** Chef must buy $1$ more packet after which he will have $13$ candies which will be enough to distribute $1$ candy to each of the $10$ children.

**Test Case $4$:** Chef must buy $3$ more packets after which he will have $21$ candies which will be enough to distribute $1$ candy to each of the $20$ children.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
20 12
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
10 100
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
10 9
```

**Output for this case**

```text
1
```



#### Test case 4

**Input for this case**

```text
20 9
```

**Output for this case**

```text
3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest](https://www.codechef.com/JULY221/)

[Practice](https://www.codechef.com/problems/CHEFCAND)

**Setter:** [jeevanjyot](https://www.codechef.com/users/jeevanjyot)

**Testers:** [satyam_343](https://www.codechef.com/users/satyam_343), [rivalq](https://www.codechef.com/users/rivalq)

**Editorialist:** [hrishik85](https://www.codechef.com/users/hrishik85)

#
[](#difficulty-2)DIFFICULTY:

570

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

There are N children and Chef wants to give them 1 candy each. Chef already has X candies with him. He can buy packets containing exactly 4 candies each.

We have to determine the  **minimum** number of candy packets Chef must buy so that he is able to give 1 candy to each of the N children.

#
[](#explanation-5)EXPLANATION:

Chef already has X candies with him.

Ideally, he needs (N - X) new candies.

Since he can only buy in packets of 4, he will end up buying (N-X)/4 packets rounded up to the nearest integer.

One caveat here is that if N \leq X, then the Chef doesn’t need to buy anything.

#
[](#time-complexity-6)TIME COMPLEXITY:

Time complexity is O(1).

#
[](#solution-7)SOLUTION:

Editorialist's Solution
``import math
t=int(input())
for _ in range(t):
    N,X=map(int,input().split())
    print(math.ceil((max((N-X),0)/4)))
``

</details>

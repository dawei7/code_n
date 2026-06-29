# Chef Fantasy 11

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FIZZBUZZ2303 |
| Difficulty Rating | 739 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [FIZZBUZZ2303](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/FIZZBUZZ2303) |

---

## Problem Statement

All of Chef's friends are playing fantasy cricket based upon the ODI World Cup, and Chef would like to join them.

For a certain cricket match, Chef has decided upon his team of $11$ players. However, he hasn't yet decided who should be the captain and who should be the vice-captain.

He's narrowed his decision down to $N$ players out of the $11$, from which he'll choose one to be the captain and one to be the vice captain.
How many different choices does he have?

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and the only line of each testcase contains a single integer $N$, the number of players Chef is considering.

---

## Output Format

For each test case, output on a new line the number of possible choices of captain and vice-captain.

---

## Constraints

- $1 \leq T \leq 10$
- $2 \leq N \leq 11$

---

## Examples

**Example 1**

**Input**

```text
2
2
3
```

**Output**

```text
2
6
```

**Explanation**

**Test case $1$:** With $N = 2$, there are only two possibilities: one of the players must be selected as the captain, and the other will become the vice-captain.

**Test case $2$:** It can be shown that there are $6$ possibilities in total for captain/vice-captain choices.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
3
```

**Output for this case**

```text
6
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/FIZZBUZZ2303)

[Contest: Division 1](https://www.codechef.com/START106A/problems/FIZZBUZZ2303)

[Contest: Division 2](https://www.codechef.com/START106B/problems/FIZZBUZZ2303)

[Contest: Division 3](https://www.codechef.com/START106C/problems/FIZZBUZZ2303)

[Contest: Division 4](https://www.codechef.com/START106D/problems/FIZZBUZZ2303)

***Authors:*** [naisheel](https://www.codechef.com/users/naisheel), [jalp1428](https://www.codechef.com/users/jalp1428)

***Tester:*** [tabr](https://www.codechef.com/users/tabr)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

739

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

Chef has 11 players, and needs to designate one of them to be the captain and another to be vice-captain.

He’s narrowed his choices down to N players. How many possibilities are there in total?

# [](#explanation-5)EXPLANATION:

One of these N players, one will be the captain and one will be the vice-captain.

There are N choices for who to choose as captain; then Chef is left with N-1 players among whom one will become vice-captain.

For each captain choice, there are N-1 vice-captain choices; and so with N initial choices for captain, the total number of possibilities is N\cdot (N-1).

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per testcase.

# [](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    print(n * (n-1))
``

</details>

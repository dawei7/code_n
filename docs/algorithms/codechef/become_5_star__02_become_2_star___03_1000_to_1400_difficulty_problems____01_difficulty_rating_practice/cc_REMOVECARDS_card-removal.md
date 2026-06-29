# Card Removal

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | REMOVECARDS |
| Difficulty Rating | 1039 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [REMOVECARDS](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/REMOVECARDS) |

---

## Problem Statement

You have $N$ cards placed in front of you on the table. The $i^{th}$ card has the number $A_i$ written on it.

In one move, you can **remove** any one card from the remaining cards on the table.

Find the **minimum** number of moves required so that all the cards remaining on the table have the **same** number written on them.

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer $N$ — the number of cards on the table.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \dots, A_N$ where $A_i$ is the number written on the $i^{th}$ card.

---

## Output Format

For each test case, output the **minimum** number of moves required so that all the cards remaining on the table have the same number written on them.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \le N \le 100$
- $1 \le A_i \le 10$

---

## Examples

**Example 1**

**Input**

```text
3
5
1 1 2 2 3
4
8 8 8 8
6
5 6 7 8 9 10
```

**Output**

```text
3
0
5
```

**Explanation**

**Test case $1$:** The minimum number of moves required such that all remaining cards have same values is $3$:
- Move $1$: Remove a card with number $1$. Remaining cards are $[1, 2, 2, 3]$.
- Move $2$: Remove a card with number $1$. Remaining cards are $[2, 2, 3]$.
- Move $3$: Remove a card with number $3$. Remaining cards are $[2, 2]$.

**Test case $2$:** All cards have the same number initially. Thus, no moves are required.

**Test case $3$:** The minimum number of moves required such that all remaining cards have same values is $5$:
- Move $1$: Remove a card with number $5$. Remaining cards are $[6, 7, 8, 9, 10]$.
- Move $2$: Remove a card with number $6$. Remaining cards are $[7, 8, 9, 10]$.
- Move $3$: Remove a card with number $7$. Remaining cards are $[8, 9, 10]$.
- Move $4$: Remove a card with number $8$. Remaining cards are $[9, 10]$.
- Move $5$: Remove a card with number $9$. Remaining cards are $[10]$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
1 1 2 2 3
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
4
8 8 8 8
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
6
5 6 7 8 9 10
```

**Output for this case**

```text
5
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/REMOVECARDS)

[Contest: Division 1](https://www.codechef.com/START60A/problems/REMOVECARDS)

[Contest: Division 2](https://www.codechef.com/START60B/problems/REMOVECARDS)

[Contest: Division 3](https://www.codechef.com/START60C/problems/REMOVECARDS)

[Contest: Division 4](https://www.codechef.com/START60D/problems/REMOVECARDS)

***Author:*** [Jeevan Jyot Singh](https://www.codechef.com/users/jeevanjyot)

***Tester:*** [Tejas Pandey](https://www.codechef.com/users/tejas10p)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

1039

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

There are N cards on a table, each with an integer from 1 to 10 written on them. What’s the least number of cards that you need to remove so that every remaining card has the same number on it?

#
[](#explanation-5)EXPLANATION:

Since each card has a value between 1 and 10, the remaining cards can only have values in this range too.

Suppose we fix x, the value of the remaining cards. Then, it is optimal to remove all cards except those that have x written on them. The number of such cards can be found with a simple loop, going through each element of the array and checking whether it equals x or not.

Find this value for each x from 1 to 10. The final answer is the minimum of all these computed values.

Faster solutions exist, but are not needed to get AC on this problem.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    freq = [0] * 11
    for x in a:
        freq[x] += 1
    print(n - max(freq))
``

</details>

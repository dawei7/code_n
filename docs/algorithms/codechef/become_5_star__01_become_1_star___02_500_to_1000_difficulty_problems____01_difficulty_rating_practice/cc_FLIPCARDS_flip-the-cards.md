# Flip the cards

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FLIPCARDS |
| Difficulty Rating | 641 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [FLIPCARDS](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/FLIPCARDS) |

---

## Problem Statement

There are $N$ cards on a table, out of which $X$ cards are face-up and the remaining are face-down.

In one operation, we can do the following:
- Select any one card and flip it (i.e. if it was initially face-up, after the operation, it will be face-down and vice versa)

What is the minimum number of operations we must perform so that all the cards face in the same direction (i.e. either all are face-up or all are face-down)?

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first and only line of each test case contains two space-separated integers $N$ and $X$ — the total number of cards and the number of cards which are initially face-up.

---

## Output Format

For each test case, output the minimum number of cards you must flip so that all the cards face in the same direction.

---

## Constraints

- $1 \leq T \leq 5000$
- $2 \leq N \leq 100$
- $0 \leq X \leq N$

---

## Examples

**Example 1**

**Input**

```text
4
5 0
4 2
3 3
10 2
```

**Output**

```text
0
2
0
2
```

**Explanation**

**Test Case 1:** All the cards are already facing down. Therefore we do not need to perform any operations.

**Test Case 2:** $2$ cards are facing up and $2$ cards are facing down. Therefore we can flip the $2$ cards which are initially facing down.

**Test Case 3:** All the cards are already facing up. Therefore we do not need to perform any operations.

**Test Case 4:** $2$ cards are facing up and $8$ cards are facing down. Therefore we can flip the $2$ cards which are initially facing up.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 0
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
4 2
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
3 3
```

**Output for this case**

```text
0
```



#### Test case 4

**Input for this case**

```text
10 2
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/FLIPCARDS)

[Contest: Division 1](https://www.codechef.com/LTIME112A/problems/FLIPCARDS)

[Contest: Division 2](https://www.codechef.com/LTIME112B/problems/FLIPCARDS)

[Contest: Division 3](https://www.codechef.com/LTIME112C/problems/FLIPCARDS)

[Contest: Division 4](https://www.codechef.com/LTIME112D/problems/FLIPCARDS)

***Author:*** [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec)

***Tester:*** [Hriday](https://www.codechef.com/users/the_hyp0cr1t3)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

641

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

There are N cards, out of which X are face-down. How many cards do you need to flip so that every card faces the same direction?

#
[](#explanation-5)EXPLANATION:

To make every card face-down, we need to flip each of the N-X cards that are currently face-up.

To make every card face-up, we need to flip each of the X cards that are currently face-down.

Making every card face the same way thus needs the minimum of these two values, i.e, \min(X, N-X) flips.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    n, k = map(int, input().split())
    print(min(k, n-k))
``

</details>

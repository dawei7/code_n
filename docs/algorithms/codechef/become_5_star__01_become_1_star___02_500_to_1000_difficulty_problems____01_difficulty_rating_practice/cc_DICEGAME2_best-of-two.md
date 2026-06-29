# Best of Two

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DICEGAME2 |
| Difficulty Rating | 789 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [DICEGAME2](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/DICEGAME2) |

---

## Problem Statement

Alice and Bob are playing a game. Each player rolls a standard six-sided die three times.
The score of a player is calculated as the sum of the two highest rolls. The player with the higher score wins. If both players have the same score, the game ends in a tie.

Determine the winner of the game or if it is a tie.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case contains six space-separated integers $A_1$,  $A_2$,  $A_3$,  $B_1$, $B_2$ and $B_3$ — the values Alice gets in her $3$ dice rolls, followed by the values which Bob gets in his $3$ dice rolls.

---

## Output Format

For each test case, output on a new line `Alice` if Alice wins, `Bob` if Bob wins and `Tie` in case of a tie.

Note that you may print each character in uppercase or lowercase. For example, the strings `tie`, `TIE`, `Tie`, and `tIe` are considered identical.

---

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq A_1, A_2, A_3, B_1, B_2, B_3 \leq 6$

---

## Examples

**Example 1**

**Input**

```text
3
3 2 5 6 1 1
4 4 5 6 4 1
6 6 6 6 6 1
```

**Output**

```text
Alice
Bob
Tie
```

**Explanation**

**Test Case $1$:** Alice's score is $8 = (3 + 5)$ which is greater than Bob's score $7 = (6 + 1)$.

**Test Case $2$:** Alice's score is $9 = (5 + 4)$ which is less than Bob's score $10 = (6 + 4)$.

**Test Case $3$:** Alice's score is $12 = (6 + 6)$ which is same as Bob's score $12 = (6 + 6)$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 2 5 6 1 1
```

**Output for this case**

```text
Alice
```



#### Test case 2

**Input for this case**

```text
4 4 5 6 4 1
```

**Output for this case**

```text
Bob
```



#### Test case 3

**Input for this case**

```text
6 6 6 6 6 1
```

**Output for this case**

```text
Tie
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/DICEGAME2)

[Contest: Division 1](https://www.codechef.com/START97A/problems/DICEGAME2)

[Contest: Division 2](https://www.codechef.com/START97B/problems/DICEGAME2)

[Contest: Division 3](https://www.codechef.com/START97C/problems/DICEGAME2)

[Contest: Division 4](https://www.codechef.com/START97D/problems/DICEGAME2)

***Author:*** [yash_daga](https://www.codechef.com/users/yash_daga)

***Tester:*** [jay_1048576](https://www.codechef.com/users/jay_1048576)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

789

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

Alice and Bob roll 3 regular 6-sided dice each, and obtain values A_1, A_2, A_3 and B_1, B_2, B_3, respectively.

A player’s score is the sum of the maximum two values they obtain.

Find out who has a larger score.

# [](#explanation-5)EXPLANATION:

Let A denote Alice’s score, and B denote Bob’s score.

They can be found as follows:

A = A_1 + A_2 + A_3 - \min(A_1, A_2, A_3) \\
B = B_1 + B_2 + B_3 - \min(B_1, B_2, B_3)

The idea here is that to find the sum of the largest two values, we can instead take the sum of all three values, then remove the smallest one.

Once A and B are found, compare them using an `if` condition and print `Alice`, `Bob`, or `Tie` appropriately.

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per testcase.

# [](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    a1, a2, a3, b1, b2, b3 = map(int, input().split())
    alice, bob = a1+a2+a3 - min(a1, a2, a3), b1+b2+b3 - min(b1, b2, b3)
    print('Alice' if alice > bob else ('Bob' if alice < bob else 'Tie'))
``

</details>

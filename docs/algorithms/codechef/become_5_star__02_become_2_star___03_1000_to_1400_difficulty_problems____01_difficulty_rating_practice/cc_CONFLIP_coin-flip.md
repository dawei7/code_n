# Coin Flip

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CONFLIP |
| Difficulty Rating | 1135 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [CONFLIP](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/CONFLIP) |

---

## Problem Statement

**Little Elephant** was fond of inventing new games. After a lot of research, Little Elephant came to know that most of the animals in the forest were showing less interest to play the multi-player games. Little Elephant had started to invent single player games, and succeeded in inventing the new single player game named **COIN FLIP**.

In this game the player will use $N$ coins numbered from $1$ to $N$, and all the coins will be facing in "Same direction" (Either **Head** or **Tail**), which will be decided by the player before starting of the game.

The player needs to play $N$ rounds. In the $k$-th round the player will flip the face of the all coins whose number is less than or equal to $k$. That is, the face of coin $i$ will be reversed, from **Head** to **Tail**, or, from **Tail** to **Head**, for $i \le k$.

Elephant needs to guess the total number of coins showing a particular face after playing $N$ rounds. Elephant really becomes quite fond of this game **COIN FLIP** so Elephant plays $G$ times. Please help the Elephant to find out the answer.

### Input:
- The first line of input contains an integer $T$, denoting the number of test cases. Then $T$  test cases follow.

- The first line of each test contains an integer $G$, denoting the number of games played by Elephant. Each of the following $G$ lines denotes a single game, and contains $3$ space-separated integers $I$, $N$, $Q$, where $I$ denotes the initial state of the coins, $N$ denotes the number of coins and rounds, and $Q$, which is either $1$, or $2$ as explained below.

Here $I=1$ means all coins are showing **Head** in the start of the game, and $I=2$ means all coins are showing **Tail** in the start of the game. $Q=1$ means Elephant needs to guess the total number of coins showing **Head** in the end of the game, and $Q=2$ means Elephant needs to guess the total number of coins showing Tail in the end of the game.

### Output:
For each game, output one integer denoting the total number of coins showing the particular face in the end of the game.

### Constraints:

$1 \le T \le 10$

$1 ≤ G ≤ 2000$

$1 ≤ N ≤ 10$

$1 ≤ I ≤ 2$

$1 ≤ Q ≤ 2$

---

## Examples

**Example 1**

**Input**

```text
1
2
1 5 1
1 5 2
```

**Output**

```text
2
3
```

**Explanation**

In the 1st game in Example,
$I=1$, so initial arrangement of coins are H H H H H,
and now Elephant will play 5 rounds and coin faces will be changed as follows<
After the 1st Round: T H H H H
After the 2nd Round: H T H H H
After the 3rd Round: T H T H H
After the 4th Round: H T H T H
After the 5th Round: T H T H T
Finally Q=1, so we need to find the total number of coins showing Head, which is 2

In the 2nd game in Example:
This is similar to the 1st game, except Elephant needs to find the total number of coins showing **Tail**.
So the Answer is $3$. (Please see the final state of the coins in the $1^{st}$ game)

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK

[Practice](http://www.codechef.com/problems/CONFLIP)

[Contest](http://www.codechef.com/NOV12/problems/CONFLIP)

# DIFFICULTY

CAKEWALK

# PREREQUISITES

Ad Hoc, Simple Math

# PROBLEM

In the game of Coin Flip there are initially **N** coins on the table. All these coins are either showing **Heads** or **Tails.** Let us say that the coins are arranged in a line, numbered from **1** to **N**.

You have to perform **N** operations in which you flip all the coins from position **1** to **i** in the **ith** round. You are to report the number of **Heads** / **Tails** after all the operations are complete.

# QUICK EXPLANATION

It is easy to see that at the end of the game the coins would be in alternating positions, starting with either **Heads** or **Tails**. Therefore, either

`
HTHTHTHT...
`

Or,

`
THTHTHTH...
`

Therefore, you can easily deduce the number of **Heads** or **Tails** at the end of the game.

# EXPLANATION

First, let us prove that the situation at the end of the game is indeed, alternating **Heads** and **Tails**.

Each coin is flipped a fixed number of times.

- The first coin has been flipped **N** times. Once in each round.

- The second coin has been flipped **N-1** times. Once in each round except the first.

- And so on…

- The last coin has been flipped **once**.

We use the following insights,

- A coin flipped **even number of times**, will show the **same side**, as it did initially.

- A coin flipped **odd number of times**, will show the **opposite side**, of the one it did initially.

Now Let us consider two cases.

## N is even

We can use the following insights,

- All the coins at **odd positions** will be in their **initial configuration**.

- All the coins at **even positions** will be **opposite** to their initial configuration.

- There are as many even positions as there are odd positions.

Hence, no matter what the initial position is

- **The number of coins facing Head and Tail are equal.**

Thus, the answer will always be **N/2**, for the query of **Heads** as well as **Tails**.

## N is odd

We can use the following insights,

- All the coins at **even positions** will be in their **initial configuration**.

- All the coins at **odd positions** will be **opposite** to their initial configuration.

- There are **floor(N/2)** coins in even positions, and **ceil(N/2)** coins in odd positions.

Hence, no matter what the initial position is

- **The number of coins that match the initial configuration are equal to floor(N/2).**

- **The number of coins that do not match the initial configuration are equal to ceil(N/2).**

Thus, assuming integer division, the answer will be **N/2**, for the query that matches the initial configuration. Otherwise the answer will be **N/2 + 1**.

This can be summerized as in the code below.

`
if (N % 2 == 0 || I == Q)
    print(N/2)
else
    print(N/2 + 1)
`

# SETTERS SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2012/November/Setter/CONFLIP.c).

# TESTERS SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2012/November/Tester/CONFLIP.c).

</details>

# The Lead Game

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TLG |
| Difficulty Rating | 790 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [TLG](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/TLG) |

---

## Problem Statement

The game of billiards involves two players knocking 3 balls around
on a green baize table. Well, there is more to it, but for our
purposes this is sufficient.

 The game consists of several rounds and in each round both players
obtain a score, based on how well they played. Once all the rounds
have been played, the total score of each player is determined by
adding up the scores in all the rounds and the player with the higher
total score is declared the winner.

 The Siruseri Sports Club organises an annual billiards game where
the top two players of Siruseri play against each other. The Manager
of Siruseri Sports Club decided to add his own twist to the game by
changing the rules for determining the winner. In his version, at the
end of each round, the **cumulative score** for each player is calculated, and the leader and her current lead are found. Once
all the rounds are over the player who had the maximum lead at the
end of any round in the game is declared the winner.

Consider the following score sheet for a game with 5 rounds:

Round
    Player 1
    Player 2

1
    140
    82

2
    89
    134

3
    90
    110

4
    112
    106

5
    88
    90

The total scores of both players, the leader and the lead after
each round for this game is given below:

Round
    Player 1
    Player 2
    Leader
    Lead

1
    140
    82
    Player 1
    58

2
    229
    216
    Player 1
    13

3
    319
    326
    Player 2
    7

4
    431
    432
    Player 2
    1

5
    519
    522
    Player 2
    3

Note that the above table contains the cumulative scores.

 The winner of this game is Player 1 as he had the maximum lead (58
at the end of round 1) during the game.

 Your task is to help the Manager find the winner and the winning
lead. You may assume that the scores will be such that there will
always be a single winner.  That is, there are no ties.

Input

 The first line of the input will contain a single integer N (N
≤ 10000) indicating the number of rounds in the game.  Lines
2,3,...,N+1 describe the scores of the two players in the N rounds.
Line i+1 contains two integer Si and Ti, the scores of the Player 1
and 2 respectively, in round i.  You may assume that 1 ≤ Si ≤
1000 and 1 ≤ Ti ≤ 1000.

Output

 Your output must consist of a single line containing two integers
W and L, where W is 1 or 2 and indicates the winner and L is the
maximum lead attained by the winner.

---

## Examples

**Example 1**

**Input**

```text
5
140 82
89 134
90 110
112 106
88 90
```

**Output**

```text
1 58
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/TLG)

**Author:** [ADMIN](http://www.codechef.com/users/admin)

**Editorialist:** [SUSHANT AGARWAL](http://www.codechef.com/users/sushant96)

### DIFFICULTY:

EASY

### PREREQUISITES:

Basic looping,Arrays

### PROBLEM:

At the end of each round the leader and her current lead are calculated. Once all the rounds are over the player who had the maximum lead at the end of any round in the game is declared the winner.

### EXPLANATION:

Create two arrays(Player1-Stores the scores of player 1 in all the rounds)[a1,a2,a3…an] and (Player2-Stores the scores of player 2 in all the rounds)[b1,b2,b3…bn].

Create a third array “Lead” such that the i’th element of Lead is ((a1+a2…+ai) - (b1+b2…bi)).

Create a fourth array “modulus lead” such that the i’th element of this array is the modulus of the i’th element of “Lead”.

Find the maximum element of “modulus lead”.This is the maximum lead attained by the winner.If the element in the corresponding position of “lead” is positive then player 1 is the winner,otherwise player 2 is.

### EDITORIALIST’S SOLUTION:

Editorialist’s solution can be found [here](http://www.codechef.com/viewsolution/5609600).

</details>

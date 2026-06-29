# Chef and Card Game

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CRDGAME |
| Difficulty Rating | 1125 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [CRDGAME](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/CRDGAME) |

---

## Problem Statement

Chef is playing a card game with his friend Morty Smith.

The rules of the game are as follows:
 - There are two piles of cards, pile $A$ and pile $B$, each with $N$ cards in it. Pile $A$ belongs to Chef and pile $B$ belongs to Morty.
 - Each card has one positive integer on it
 - The ‘power’ of a card is defined as the sum of digits of the integer on that card
 - The game consists of $N$ rounds
 - In each round, both players simultaneously draw one card each from the top of their piles and the player who draws the card with higher power wins this round and gets a point. If the powers of both players' cards are equal then they get $1$ point each.
 - The winner of the game is the player who has more points at the end of $N$ rounds. If both players have equal number of points then the game ends in a draw.

The game is now over and Chef has told Morty to find the winner. Unfortunately, this task is too complex for him. Help Morty find the winner.

### Input:

- First line will contain $T$, number of testcases.
- The first line of each test case will contain $N$, the number of rounds played.
- The $i^{th}$ of the next $N$ lines of each test case will contain $A_i$ and $B_i$, the number on the card drawn by Chef and Morty respectively in round $i$.

### Output:
For each test case, output two space separated integers on a new line:
Output
 - $0$ if Chef wins,
 - $1$ if Morty wins,
 - $2$ if it is a draw,
followed by the number of points the winner had.
(If it is a draw then output either player’s points).

### Constraints
- $1 \leq T \leq 1000$
- $1 \leq N \leq 100$
- $1 \leq A_i, B_i \leq 10^9$

### Subtasks
- $100$ points : No additional constraints

---

## Examples

**Example 1**

**Input**

```text
2
3
10 4
8 12
7 6
2
5 10
3 4
```

**Output**

```text
0 2
2 1
```

**Explanation**

**Test Case** $1$:

**Round** $1$:

Chef’s card has power $1+0$ = $1$,
Morty’s card has power $4$.
Therefore, Morty wins the round.

**Round** $2$:

Chef’s card has power $8$,
Morty’s card has power $1 + 2$ = $3$.
Therefore, Chef wins the round.

**Round** $3$:

Chef’s card has power $7$,
Morty’s card has power $6$.
Therefore, Chef wins the round.

Therefore, Chef wins the game with $2$ points (Morty has $1$ point).

**Test Case** $2$:

**Round** $1$:

Chef’s card has power $5$,
Morty’s card has power $1 + 0 = 1$.
Therefore, Chef wins the round.

**Round** $2$:

Chef’s card has power $3$,
Morty’s card has power $4$.
Therefore, Morty wins the round.

Therefore, the game ends in a draw and both players have $1$ point each.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Contest Link](https://www.codechef.com/JULY20B/problems/CRDGAME)

Author: [Aryan Agarwala](https://www.codechef.com/users/aryanag_adm)

Tester: [Encho Misev](https://www.codechef.com/users/enchom)

Editorialist: [Rajarshi Basu](https://www.codechef.com/users/rajarshi_basu)

# DIFFICULTY:

Cakewalk

# PROBLEM:

There are two players, each with a deck of N \leq 100 cards. Strength of a card is defined as sum of digits of number A_i \leq 10^9 written on that card. There will be N rounds. In each round, either player will draw the first card on their respective decks. The one with higher strength wins and get 1 point. If both have the same strength, both get 1 point. We have to report who wins after N rounds are over.

# EXPLANATION:

We just simulate the process. We iterate over the cards one by one and see whose strength is more. We keep 2 variables to keep track of the score of each person.

In the end, we just compare the scores and output accordingly.

The only important part if finding the sum of digits. The following is a sample code to do that, in ***C++***.

``void digitSum(int num){
    int sum = 0;
    while(num > 0){// That means the number has no digits left.
        sum += num %10; // This extracts the last digit.
        num /= 10; // This Removes the last digit.
    }
    return sum;
}
``

# SOLUTION:

Setter's code

</details>

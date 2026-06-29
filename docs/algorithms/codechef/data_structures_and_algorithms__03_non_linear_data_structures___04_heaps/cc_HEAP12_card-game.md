# Card Game

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | HEAP12 |
| Difficulty Band | Heaps |
| Path | Data Structures and Algorithms |
| Lesson | Learn Heaps |
| Official Link | [HEAP12](https://www.codechef.com/learn/course/heaps/LIHP02/problems/HEAP12) |

---

## Problem Statement

Sebastian is playing a card game. At any given moment on two things can happen:
- Either Sebastian receives a card
- Or Sebastian puts a card
Each card has a power which is denoted by an integer P.
Sebastian is a very aggressive player and loves overwhelming players with his strongest card.
Any time Sebastian has to put a card he will always put the strongest card in his hands.
You are given the moves of the game as input in the following format.
- '+' denoting Sebastian receives a card followed by it's power.
- '-' denoting Sebastian has to put a card.
Print the power of the card Sebastian puts each time he has to put a card.
Use Heap to solve this question.

---

## Input Format

- The first line of input will contain a single integer $N$, denoting the number turns.
- Followed by $N$ lines of input.
    - Each line either contains the character '+' followed by it's power $P_i$, or the character '-' denoting it's Sebastian's turn to put a card.

---

## Output Format

Print the power of the card Sebastian puts each time it's his turn to put a card.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 100$
- $1 \leq M \leq N\cdot(N-1)/2$
- $1 \leq u_i, v_i \leq N$
- $u_i \neq v_i$ for each $1 \leq i \leq M$.
- The sum of $N$ over all test cases won't exceed $100$.

---

## Examples

**Example 1**

**Input**

```text
10
+ 7
+ 18
+ 3
+ 15
+ 1
-
-
+ 92
- 
-
```

**Output**

```text
18
15
92
7
```

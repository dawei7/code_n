# Recruit Villagers

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | VILLINE |
| Difficulty Rating | 1270 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [VILLINE](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/VILLINE) |

---

## Problem Statement

WW3 is near and Gru wants to recruit minions for his team. Gru went to the planet of minions to recruit minions, he saw that there are two villages separated by a river. He cannot recruit minions from both villages because then his team will have internal conflicts.

Gru is now in a dilemma about which village to recruit as he wants to have the strongest possible team.

You are given coordinates of houses on the planet. Each house has exactly one minion and his power is given. The planet of minion is considered as a 2-D plane and the river is denoted by a straight line ( $y=mx+c$ ).
$Note:$ None of the houses are situated on the river.
###Input:

- First-line will contain $N$, number of houses.
- Second-line will contain two integers, $m$ and $c$ denoting the river.
- Next $N$ lines will have exactly 3 integers $X[i], Y[i], P[i]$ denoting the coordinates of houses and the power of minion in that house

###Output:
- Print the maximum power of the team which Gru can recruit.

###Constraints
- $1 \leq N \leq 10^5$
- $-10^4 \leq m,c \leq 10^4$
- $-10^4 \leq X[i], Y[i] \leq 10^4$
- $ 1 \leq P[i] \leq 10^4$

---

## Examples

**Example 1**

**Input**

```text
3
1 0
0 5 5
0 6 5
0 -8 20
```

**Output**

```text
20
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

**VILLINE**  - [ Recruit Villagers ENIGMA-Plinth’20 ](https://www.codechef.com/PLIT2020/problems/VILLINE)

**Author**  - [priyam2k ](https://www.codechef.com/users/Priyam2k)

**Editorialist**  - [Priyam Khandelwal ](https://www.codechef.com/users/priyam2k)

### DIFFICULTY:

Easy

### PREREQUISITES:

Basic Maths

### PROBLEM:

Given an equation of a line and n points and their associated values, find what is the maximum sum of values on either side of the line.

### Explanation

It is well known that if you put a point in the equation of a line, there are 3 possible cases.

1.) Value comes out to be 0 i.e. Point is on the line.

2.) Value comes out to be positive i.e. Point is on one side of the line.

3.) Value comes out to be negative i.e. Point is on the other side of the line.

So, you have to sum all the positive values together and all negative values together, then find which is greater.

### Author solution

[Author’s Solution ](https://pastebin.com/qywvJVrj)

</details>

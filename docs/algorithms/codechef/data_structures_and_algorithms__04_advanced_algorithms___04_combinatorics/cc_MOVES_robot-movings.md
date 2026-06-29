# Robot Movings

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MOVES |
| Difficulty Rating | 1668 |
| Difficulty Band | Combinatorics |
| Path | Data Structures and Algorithms |
| Lesson | Conceptual Problems |
| Official Link | [MOVES](https://www.codechef.com/learn/course/combinatorics/COMBI05/problems/MOVES) |

---

## Problem Statement

Given a square table sized $N$ x $N$ (rows and columns are indexed from 1) with a robot on it. \
The robot has a mission of moving from cell (1, 1) to cell ($N$, $N$) using only the directions "right" or "down". \
You are requested to find the number of different ways for the robot using exactly $K$ turns. \
The answer should be given with modulo $10^9+7$.

#### Note:
We define a "turn" as a right move followed immediately by a down move, or a down move followed immediately by a right move.

---

## Constraints

* $ 3 \leq N \leq 5000 $
* $ 1 \leq K \leq  2N - 1 $
* $ \text{Number of test cases} \leq 5000 $

---

## Examples

**Example 1**

**Input**

```text
3
4 2
4 3
5 3
```

**Output**

```text
4
8
18
```

**Explanation**

Explanation for the first sample test case: 4 ways are **RRDDDR, RDDDRR, DRRRDD, DDRRRD** ('R' or 'D' represents a right or down move respectively).

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 2
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
4 3
```

**Output for this case**

```text
8
```



#### Test case 3

**Input for this case**

```text
5 3
```

**Output for this case**

```text
18
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINKS

[Practice](http://www.codechef.com/problems/MOVES/)

[Contest](http://www.codechef.com/DEC11/problems/MOVES/)

### DIFFICULTY

EASY

### EXPLANATION

Suppose that the robot always takes the “right” move at first. We could easily see that a way of robot reaching cell (N, N) is just a set of cells in which the robot takes “turns”. This set is chosen by selecting a combination of K/2 column indices and (K-1)/2 row indices among N-2 indices each dimension. It is easily computed by formula C(K/2, N-2) * C((K-1)/2, N-2). At last, we double the result of this formula to get the last result (because the table is a square one so it is totally the same in case the robot takes the “down” move at first).

The last problem is compute the Combination formula as fast as possible. In this case we have to compute the result modulo 1,000,000,007 which is a prime, so we just use a power function to fast compute that (in logarithmic time).

### SETTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2011/December/Setter/MOVES.pas).

### TESTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2011/December/Tester/MOVES.cpp).

</details>

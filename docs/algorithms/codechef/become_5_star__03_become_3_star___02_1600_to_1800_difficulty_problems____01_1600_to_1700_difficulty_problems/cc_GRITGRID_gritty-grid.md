# Gritty Grid

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | GRITGRID |
| Difficulty Rating | 1691 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1600 to 1700 difficulty problems |
| Official Link | [GRITGRID](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1700/problems/GRITGRID) |

---

## Problem Statement

Alice and Bob are trapped in a grid having $N$ rows and $M$ columns. Alice is currently at cell $(1, 1)$ and Bob is at cell $(N, M)$ and they both want to meet each other at any common cell. But they have some restrictions in the way they can move and meet:

A _step_ is defined as moving to an adjacent cell from the current cell that the person is in. So in a single step, if a person is at $(X, Y)$ they may move to any one of the following cells, provided that they are inside the grid's boundaries - $(X + 1, Y)$, $(X, Y + 1)$, $(X - 1, Y)$, $(X, Y - 1)$.

A _move_ for Alice is defined to be **exactly** $X$ steps. And a _move_ for Bob is defined to be **exactly** $Y$ steps.

They can only meet at the common cell after **Alice** has just completed her move i.e. they should not meet in the middle of anyone's move or at the end of Bob's move. The first time that they meet should be right after a move of Alice, and they stop moving after that.

Alice makes a move first, then Bob makes a move, and they alternate like this.

Alice and Bob want to know if it is possible to meet with these restrictions. Please help Alice and Bob by telling them whether they would be able to meet each other if they stick to these restrictions.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line of input containing four integers: $N$, $M$, $X$ and $Y$ denoting the number of rows, number of columns, number of steps in Alice's one move and the number of steps in Bob's one move respectively.

---

## Output Format

For each test case, output in a single line $\texttt{YES}$ if they would be able to meet each other at a common cell, else output $\texttt{NO}$.

You may print each character of the string in uppercase or lowercase (for example, the strings $\texttt{YeS}$, $\texttt{yEs}$, $\texttt{yes}$ and $\texttt{YES}$ will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N, M \leq 10^6$
- $1 \leq X, Y \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
4
2 2 2 1
2 2 1 1
2 2 1 2
2 3 3 3
```

**Output**

```text
Yes
No
Yes
Yes
```

**Explanation**

**Test case 1:** Alice is initially at $(1, 1)$, and Bob is at $(2, 2)$. In Alice's first _move_, she has to take $2$ _steps_ - she can choose to go from $(1, 1) \rightarrow (1, 2) \rightarrow (2, 2)$. And so at the end of Alice's first move, Alice and Bob meet, and they stop. So the answer is Yes.

**Test case 2:** Alice is initially at $(1, 1)$, and Bob is at $(2, 2)$. In Alice's first _move_, she has to take $1$ _step_ - she can choose to go from $(1, 1) \rightarrow (1, 2)$, or $(1, 1) \rightarrow (2, 1)$. Similarly for Bob. But you can check that no matter what they do, they can't coordinate in such a way that they meet only after Alice's move. So the answer is No.

**Test case 3:** Alice is initially at $(1, 1)$, and Bob is at $(2, 2)$. In Alice's first _move_, she has to take $1$ _step_ - she can choose to go from $(1, 1) \rightarrow (1, 2)$. Then in Bob's move, he has to take $2$ steps - he can choose to go from $(2, 2) \rightarrow (2, 1) \rightarrow (2, 2)$. Then in Alice's second move, she can choose to go from $(1, 2) \rightarrow (2, 2)$. And so at the end of Alice's second move, Alice and Bob meet, and they stop. So the answer is Yes.

**Test case 4:** Alice is initially at $(1, 1)$, and Bob is at $(2, 3)$. In Alice's first _move_, she has to take $3$ _steps_ - she can choose to go from $(1, 1) \rightarrow (1, 2) \rightarrow (1, 3) \rightarrow (2, 3)$. And so at the end of Alice's first move, Alice and Bob meet, and they stop. So the answer is Yes.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 2 2 1
```

**Output for this case**

```text
Yes
```



#### Test case 2

**Input for this case**

```text
2 2 1 1
```

**Output for this case**

```text
No
```



#### Test case 3

**Input for this case**

```text
2 2 1 2
```

**Output for this case**

```text
Yes
```



#### Test case 4

**Input for this case**

```text
2 3 3 3
```

**Output for this case**

```text
Yes
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/FLIPFAIL)

[Contest: Division 1](https://www.codechef.com/START52A/problems/FLIPFAIL)

[Contest: Division 2](https://www.codechef.com/START52B/problems/FLIPFAIL)

[Contest: Division 3](https://www.codechef.com/START52C/problems/FLIPFAIL)

[Contest: Division 4](https://www.codechef.com/START52D/problems/FLIPFAIL)

***Author:*** [S. Manuj Nanthan](https://www.codechef.com/users/munch_01)

***Preparer:*** [Tejas Pandey](https://www.codechef.com/users/tejas10p)

***Testers:*** [Takuki Kurokawa](https://www.codechef.com/users/tabr), [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

1691

#
[](#prerequisites-3)PREREQUISITES:

Observation

#
[](#problem-4)PROBLEM:

On an N\times M grid, Alice starts at cell (1, 1) and Bob starts at cell (N, M). Alice moves X steps at a time, and Bob moves Y steps at a time.

Is it possible for Alice and Bob to reach the same cell at the end of Alice’s move?

#
[](#explanation-5)EXPLANATION

Working out a few examples should give you the idea that the only things that really matter are the parities of N, M, X, and Y.

Since N, M \geq 2, there are only two cases to consider (and no edge cases):

- The answer is “Yes” if at least one of X and Y has the same parity as N+M

- The answer is “No” otherwise

Proof

Let d = N-1 + M-1.

We claim that the answer is “Yes” If and only if d has the same parity as at least one of \{X,  Y\}. Note that d has the same parity as N+M.

The parity of the manhattan distance between Alice and Bob after the first move is (d-x)\pmod 2. After the second move, it is (d-x-y)\pmod 2, and so on. This sequence is:

d, d-x, d-x-y, d-y, d, d-x, \ldots

The points where it is the end of Alice’s turns are d-x, d-y, d-x, d-y, \ldots

If the distance is zero after Alice’s move, we need this to be 0. So, d should have the same parity as at least one of \{X, Y\}. If not, the answer is definitely “No”.

Now, we show that this condition is also sufficient.

First, note that if X is odd, Alice can always be made to move exactly one square on her turn. Similarly, Bob can do this when Y is odd.

-
**Case 1:** If Y is even: We make Bob stay at (N, M) always. Since even X and odd d cannot be the case (since Y is already even), we can always make Alice reach (N, M).

-
**Case 2a:** If Y is odd, and X is even, and if d \gt X: We make Alice stay at (1, 1) throughout the beginning, and make Bob reduce the Manhattan distance by 1 in each move. When the distance between them becomes exactly X, Alice moves and meets Bob.

-
**Case 2b:** If Y is odd, and X is even, and if d \leq X: Either Alice can meet in the first move itself, or Bob reduces the distance by 1, and then Alice meets Bob on the next move (Note that since N, M \geq 2, the d \geq 2, and so it can be reduced by 1 by Bob without meeting Alice).

-
**Case 3:** If Y is odd, and X is odd: This means that d is also odd. So, we just make Alice and Bob reduce the distance by 1 at each move, and eventually Alice will be the person to meet Bob in her move.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
	n, m, x, y = map(int, input().split())
	print('yes' if x%2 == (n+m)%2 or y%2 == (n+m)%2 else 'no')
``

</details>

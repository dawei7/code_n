# Make that Array!

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SWAPGAME |
| Difficulty Rating | 2323 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [SWAPGAME](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/SWAPGAME) |

---

## Problem Statement

Chef is given two arrays $A$ and $B$, each having $N$ elements.

In one move, Chef can choose an index $i$ $(1 \leq i \leq N-1$), get $(A_i - A_{i+1})$ points, and then swap $A_i$ and $A_{i+1}$.

**For example:** If Chef has the array - $[10, 7,5]$ and Chef chooses index $1$ during his move, he will get $10 - 7 = 3$ points and the new array will become $[7 , 10 ,5]$

Can you help Chef in finding the maximum number of points he can get while converting the array $A$ into array $B$?

$\textbf{Note:}$ It is guaranteed in the input that there exists a sequence of moves which can convert array $A$ into $B$.

---

## Input Format

- The first line of input contains a single integer $T$, denoting the number of testcases. The description of the $T$ testcases follows.
- The first line of each test case contains a single integer $N$ denoting the number of elements in $A$ and $B$.
- The second line of each test case contains $N$ space separated integers $A_1, A_2,..., A_N$.
- The third line of each test case contains $N$ space separated integers $B_1, B_2,..., B_N$.

---

## Output Format

For each test case, print a single line containing one integer, which is the maximum number of points that Chef can get while converting the array $A$ into array $B$

---

## Constraints

- $1 \leq T \leq 5 \cdot 10^4$
- $2 \leq N \leq 5 \cdot 10^5$
- $1 \leq A_i \leq 10^5$
- $1 \leq B_i \leq 10^5$
- The sum of $N$ over all test cases does not exceed $5 \cdot 10^5$

---

## Examples

**Example 1**

**Input**

```text
3
2
1 2
2 1
3
3 2 1
1 2 3
3
1 2 3
1 2 3
```

**Output**

```text
-1
4
0
```

**Explanation**

**Test Case $1$:** Chef can choose $i = 1$ in the first move, get $1 - 2 = -1$ points and swap $A_1$ and $A_2$. After this move, $A$ is converted into $B$. We can prove that there exists no other sequence of moves which can result in higher score while converting $A$ into $B$.

**Test Case $2$:** One possible sequence of moves is the following:
- Choose $i = 2$. Total points $= 1$, and $A$ will become $[3, 1, 2]$.
- Choose $i = 1$. Total points $= 1 + 2$, and $A$ will become $[1, 3, 2]$.
- Choose $i = 2$. Total points $= 1 + 2 + 1$, and $A$ will become $[1, 2, 3]$.

There are other possible sequences of moves which can result in total $4$ points, but no such sequence exists which can result in more than $4$ points, and simultaneously convert $A$ into $B$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
1 2
2 1
```

**Output for this case**

```text
-1
```



#### Test case 2

**Input for this case**

```text
3
3 2 1
1 2 3
```

**Output for this case**

```text
4
```



#### Test case 3

**Input for this case**

```text
3
1 2 3
1 2 3
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest - Division 3](https://www.codechef.com/START13C/problems/SWAPGAME)

[Contest - Division 2](https://www.codechef.com/START13B/problems/SWAPGAME)

[Contest - Division 1](https://www.codechef.com/START13A/problems/SWAPGAME)

#
[](#difficulty-2)DIFFICULTY:

EASY

#
[](#problem-3)PROBLEM:

Given arrays A and B of size N. You can swap A_i and A_{i+1} with cost A_i-A_{i+1}. Determine the minimum total cost to make A equal to B.

#
[](#explanation-4)EXPLANATION:

Suppose we do a number of swaps to A to make it equal to B, and the element at index i in the original array is now at index pos_i.

I claim that the total cost incurred in the above case equals \sum A_i(pos_i-i).

Proof

Let pos_i represent the current position of, the element at index i in the original array. Initially, pos_i=i for all i.

Everytime we swap element A_i (of the original array) with the element A_j to its right:

-
pos_i increases by 1,

-
pos_{j} decreases by 1,

- the cost increases by A_i-A_{j}\implies the cost increases by A_i and decreases by A_{j}.

We can therefore notice that everytime pos_i is increased by 1, the cost increases by A_i. Similarly, the cost decreases by A_i everytime pos_i is decreased by 1.

In the end, the total number of times the cost increases by A_i is equal to pos_i-i (the cost decreases if pos_i-i is negative).

Therefore, we can calculate the cost contributed by each A_i separately and then add them together, giving us the equation \sum A_i(pos_i-i).

When the elements of A are distinct, array pos is unique and the total cost is therefore fixed. What about the case when A has repeating elements?

I claim that any sequence of swaps that makes A equal B has the same total cost. That is, say there exists i,j\space(i\ne j) such that A_i=A_j. Then, the total cost to rearrange A such that A_i and A_j are at indices pos_j and pos_i (instead of pos_i and pos_j) is the same.

(The proof of this is trivial and left to the reader as an exercise).

Therefore, given A and B, it suffices to find any *valid* mapping pos such that B_{pos_i} = A_i. We can then use the equation given above to calculate the answer.

Implementation

Create array of pairs C = \{(A_1, 1), (A_2,2),\dots,(A_N,N)\} and D = \{(B_1, 1), (B_2,2),\dots,(B_N,N)\}.

Sort the elements of C and D by the first value of their pairs, in ascending order (breaking ties arbitrarily). Then, since arrays A and B have the same elements, it is easy to see that the first value of C_i equals the first value of D_i for all i.

So, set the value of pos_{C_i.second} as D_i.second, for all i. The validity of this mapping can be shown trivially.

#
[](#time-complexity-5)TIME COMPLEXITY:

We sort the array of pairs C and D in O(N\log N) each. We then iterate from 1 to N once, to generate the array pos and calculate the answer. The total time complexity is therefore

O(2\times N\log N+N) \approx O(N\log N)

per test case.

#
[](#solutions-6)SOLUTIONS:

Editorialist’s solution can be found [here](https://www.codechef.com/viewsolution/51720249).

***Experimental:** For evaluation purposes, please rate the editorial (1 being poor and 5 excellent)*

- 1

- 2

- 3

- 4

- 5

0
voters

</details>

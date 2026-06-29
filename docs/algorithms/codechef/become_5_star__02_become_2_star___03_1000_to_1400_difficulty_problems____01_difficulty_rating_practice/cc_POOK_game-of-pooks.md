# Game of Pooks

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | POOK |
| Difficulty Rating | 1121 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [POOK](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/POOK) |

---

## Problem Statement

We have found a new chess character — pook. It has the qualities of both a rook and a pawn. Specifically, treating the chessboard to be an $N\times N$ grid where $(i, j)$ denotes the intersection of the $i$-th row and the $j$-th column, a pook placed at square $(x, y)$ threatens the following squares:
- $(i, y)$ for every $1 \leq i \leq N$
- $(x, i)$ for every $1 \leq i \leq N$
- $(x+1, y-1)$, if $x \lt N$ and $y \geq 2$
- $(x+1, y+1)$, if $x \lt N$ and $y \lt N$

Find the **maximum** number of pooks that can be placed on an empty $N \times N$ chessboard such that none of them threaten each other.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases. Then the test cases follow.
- Each test case consists of a single line of input, containing a single integer $N$.

---

## Output Format

For each test case, output in a single line the maximum number of pooks that can be placed on the chessboard such that they don't threaten each other.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
3
1
2
3
```

**Output**

```text
1
1
2
```

**Explanation**

**Test case $1$:** There is a single square, so we have a single pook.

**Test case $2$:** We can only place one pook. No matter where the first is placed, placing a second will lead to one of the two being threatened.

**Test case $3$:** Placing $2$ pooks on a $3\times 3$ grid is easy — for example, place one at $(1, 2)$ and another at $(3, 3)$. It can be shown that placing three is not possible.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
2
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
3
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

[Contest Division 3](https://www.codechef.com/COOK141C/problems/POOK)

[Contest Division 4](https://www.codechef.com/COOK141D/problems/POOK)

**Setter and Editorialist :**  [Yashodhan Agnihotri](https://www.codechef.com/users/zappelectro)

#
[](#difficulty-2)DIFFICULTY:

1121

#
[](#prerequisites-3)PREREQUISITES:

None.

#
[](#problem-4)PROBLEM:

Find the maximum number of pooks on an N x N chessboard such that none of them threaten each other. A Pook has the properties of both, a pawn and a rook.

#
[](#explanation-5)EXPLANATION:

We will see 4 cases here. The three cases of N = 1,2,3 need to be handled separately while N \geq 4 will follow the answer of the [N-Queen Problem](https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/). Since we can place atmost N unthreatening rooks on a N x N chessboard, therefore as a Pook has all the properties of Rooks, we would be able to place atmost N pooks as well.

The answer for the N-Queen problem for N greater than 4 is N queens, therefore our answer will also be the same here.

N = 1

Since there is just one square, we can place 1 pook in it.

N = 2

Here, we can place just 1 pook, since all the other three squares will be threatened by it.

N = 3

Here, however you place the pooks, you cannot place more than 2 pooks on the board.

N >= 4

Here, the answer is same as the N-Queen Problem i.e N pooks.

#
[](#solutions-6)SOLUTIONS:

Setter's Solution
``#include<bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin >> t;
	while (t--) {
		int n;
		cin >> n;
		if (n == 2 || n == 3)
			cout << n - 1 << "\n";
		else
			cout << n << "\n";
	}
	return 0;
}
``

For doubts, please leave them in the comment section, I’ll address them.

</details>

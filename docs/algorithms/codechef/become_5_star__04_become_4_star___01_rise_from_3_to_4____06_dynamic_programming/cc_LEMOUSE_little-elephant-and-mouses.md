# Little Elephant and Mouses

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LEMOUSE |
| Difficulty Rating | 1941 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Dynamic Programming |
| Official Link | [LEMOUSE](https://www.codechef.com/practice/course/3to4stars/LP3TO406/problems/LEMOUSE) |

---

## Problem Statement

It is well-known that the elephants are afraid of mouses. The Little Elephant from the Zoo of Lviv is not an exception.

The Little Elephant is on a board **A** of **n** rows and **m** columns (0-based numeration). At the beginning he is in cell with coordinates **(0; 0)** and he wants to go to cell with coordinates **(n-1; m-1)**. From cell **(x; y)** Little Elephant can go either to **(x+1; y)** or **(x; y+1)**.

Each cell of the board contains either **1** or **0**. If **A[i][j] = 1**, then there is a single mouse in cell **(i; j)**. Mouse at cell **(i; j)** scared Little Elephants if and only if during the path there was at least one such cell **(x; y)** (which belongs to that path) and **|i-x| + |j-y| <= 1**.

Little Elephant wants to find some correct path from **(0; 0)** to **(n-1; m-1)** such that the number of mouses that have scared the Little Elephant is minimal possible. Print that number.

### Input

First line contains single integer **T** - the number of test cases. Then **T** test cases follow. First line of each test case contain pair of integers **n** and **m** - the size of the board. Next **n** lines contain **n** strings, each of size **m** and consisted of digits **0** and **1**.

### Output

In **T** lines print **T** integer - the answers for the corresponding test.

### Constraints

**1** <= **T** <= **50**

**2** <= **n, m** <= **100**

---

## Examples

**Example 1**

**Input**

```text
2
3 9
001000001
111111010
100100100
7 9
010101110
110110111
010011111
100100000
000010100
011011000
000100101
```

**Output**

```text
9
10
```

**Explanation**

**Example case 1: **
The optimized path is: (0, 0) -> (0, 1) -> (0, 2) -> (0, 3) -> (0, 4) -> (0, 5) -> (0, 6) -> (0, 7) -> (0, 8) -> (1, 8) -> (2, 8). The mouses that scared the Little Elephant are at the following cells: (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 7), (0, 2), (0, 8).

**Example case 2: **
The optimized path is: (0, 0) -> (1, 0) -> (1, 1) -> (2, 1) -> (2, 2) -> (3, 2) -> (3, 3) -> (4, 3) -> (4, 4) -> (5, 4) -> (5, 5) -> (6, 5) -> (6, 6) -> (6, 7) -> (6, 8). The 10 mouses that scared the Little Elephant are at the following cells: (0, 1), (1, 0), (1, 1), (2, 1), (3, 3), (4, 4), (5, 4), (5, 5), (6, 6), (6, 8).

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 9
001000001
111111010
100100100
7 9
010101110
```

**Output for this case**

```text
9
```



#### Test case 2

**Input for this case**

```text
110110111
010011111
100100000
000010100
011011000
000100101
```

**Output for this case**

```text
10
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Problem Link:

[Practice](http://www.codechef.com/problems/LEMOUSE)

[Contest](http://www.codechef.com/JUNE13/problems/LEMOUSE)

# Difficulty:

Simple

# Pre-requisites:

Dynamic Programming

# Problem:

Little Elephant is coordinates (0, 0) of a NxM grid A. A[i][j] = 0 if there is no mouse in cell (i, j), else it is 1, if there is a single mouse. LE is scared of a mouse if he moves into a position (x, y) where the distance between himself and the mouse <= 1. Given that he needs to reach the bottom right corner of the grid (N-1, M-1), and that he takes only right/down moves, find the minimum number of mice he will be scared by along such a path.

# Explanation:

In order to solve this, let us first make a visualization: each mouse casts a “shadow” of length 1 in all four directions. Thus, LE gets scared of a mouse iff his path passes through its “shadow”. Note that if it passes through the mouse itself, then it would have had to come through some shadow, and further it would go through some shadow, so we can consider it as if it has passed through the shadow only.

Thus, let us assume that we have a shadow grid, where shadow[i][j] = Number of mice that cast a shadow on cell (i, j). Finding the number of mice that LE is scared of, is then just summing up values of shadow!!

Well, *nearly* that.

The fact is, we are double-counting. In case the path that LE takes crosses the same mouse’s shadow more than once, we would be counting that shadow twice as if it had come from different mice. We should ensure that we subtract such “shadows” from our answer.

When will we be double-counting a single mouse’s shadow?

There are essentially just two cases.

Case 1: You pass through the mouse yourself. Then you are clearly counting it’s shadow for when you come near the mouse, as well as when you go away from it!

Case 2: You turn a corner, and count the shadow of the mouse opposite that corner twice.

The above “Case 2” is as follows (“E” is the path taken by LE, M is the mouse location)

``
...
...
...EE
...ME
.....

``

In the above, you would count M’s shadow once from top, once from right. Similarly, you could be in the following symmetric case as well:

``
...
...
..EM..
..EE..
......

``

In this case also, you are counting M’s shadow twice. You need to handle such double counting cases.

But then, how would you handle it? How would you tell if you’ve “turned a corner” or not? This is where DP states help. Instead of most DP, which would have N x M type states, you should here keep N x M x 2 states, where the extra “2” tells you whether you have come from “up” or from “left”. Given this, you will be able to tell where you have come from, and where to look for a double-count mouse.

Let DP[i][j][0] = Minimum number of scared mice with destination (i, j) assuming you came from the left,

and DP[i][j][1] = Minimum number of scared mice with destination (i, j) assuming you came from the top.

Pseudocode follows:

``
fillShadows(N, M, Mouse[][])
//Assuming Shadow[i][j] = 0 for all i, j
	for(i = 0; i < N; i++)
		for(j = 0; j < M; j++)
			if(Mouse[i][j] == 1)
				//check you don't exceed the grid here
				Shadow[i-1][j]++
				Shadow[i][j-1]++
				Shadow[i+1][j]++
				Shadow[i][j+1]++
	return Shadow;

doDP()
	DP[0][0][0] = DP[0][0][1] = Shadow[0][0] - Mouse[0][0]
	for(i = 0; i < N; i++)
		for(j = 0; j < M; j++)
			//ensure everything is "within the grid" while computing
			DP[i][j][0]=Shadow[i][j]-Mouse[i][j] + min(DP[i][j-1][0], DP[i][j-1][1] - Mouse[i-1][j])
			DP[i][j][1]=Shadow[i][j]-Mouse[i][j] + min(DP[i-1][j][0] - Mouse[i][j-1], DP[i-1][j][1])
	output min(DP[N-1][M-1][0], DP[N-1][M-1][1]) + Mouse[0][0] + Mouse[N-1][M-1]

``

In the above DP calculation, we have Shadow[i][j] - Mouse[i][j] terms common to both. If we have come from the left, we need to consider a mouse above us when our previous move was from top. If we have come from the top, we need to consider a mouse to the left of us, when our previous move was from the left.

The only remaining boundary cases are when there is/are mice on the points (0, 0) or (N-1, M-1), in which case we have removed our “double count” mice already when we haven’t even double-counted them, so we should add them back.

Thus, the overall time complexity is O(N * M) per test-case.

This was a rather beautiful problem, and although one approach has been described here in the Editorial, I’m sure a lot of people would have come up with their own interesting variations.

# Setter’s Solution:

Can be found [here](http://www.codechef.com/download/Solutions/2013/June/Setter/LEMOUSE.cpp)

# Tester’s Solution:

Can be found [here](http://www.codechef.com/download/Solutions/2013/June/Tester/LEMOUSE.cpp)

</details>

# Moving Segments

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SEGDIR |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Basic Graph Theory - Trees, DFS, BFS |
| Official Link | [SEGDIR](https://www.codechef.com/practice/course/3to4stars/LP3TO401/problems/SEGDIR) |

---

## Problem Statement

$N$ line segments (numbered $1$ through $N$) are placed on the $x$-axis. For each valid $i$, the $i$-th segment starts at $x = L_i$ and ends at $x = R_i$.

At the time $t = 0$, all segments start moving; for each valid $i$, the $i$-th segment starts moving with speed $V_i$. You need to assign a direction - left or right - to the movement of each segment, i.e. choose a sign for each $V_i$ (not necessarily the same for all segments). The resulting movement must satisfy the following condition: at the time $t = 10^{10000}$, there are no two segments that touch or intersect.

Decide if it is possible to assign directions to the segments in such a way that the above condition is satisfied.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- $N$ lines follow. For each $i$ ($1 \le i \le N$), the $i$-th of these lines contains three space-separated integers $L_i$, $R_i$ and $V_i$.

### Output
For each test case, print a single line containing the string `"YES"` if it is possible to assign the directions in a valid way or `"NO"` if it is impossible.

### Constraints
- $1 \le T \le 100$
- $1 \le N \le 1,000$
- $1 \le L_i \lt R_i \le 10^9$ for each valid $i$
- $1 \le V_i \le 10^9$ for each valid $i$
- the sum of $N$ over all test cases does not exceed $2,000$

---

## Examples

**Example 1**

**Input**

```text
2
4
5 7 2
4 6 1
1 5 2
6 8 1
4
1 2 1
1 2 1
1 2 1
1 2 1
```

**Output**

```text
YES
NO
```

**Explanation**

**Example case 1:** We can assign the direction *left* to the $1$-st and $2$-nd segment and *right* to the $3$-rd and $4$-th segment.

**Example case 2:** There is no valid way to assign directions to segments.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
5 7 2
4 6 1
1 5 2
6 8 1
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
4
1 2 1
1 2 1
1 2 1
1 2 1
```

**Output for this case**

```text
NO
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Moving Segments](https://www.codechef.com/practice/course/3to4stars/LP3TO401/problems/SEGDIR)

### [](#problem-statement-1)Problem Statement -

N line segments (numbered 1 through N) are placed on the x-axis. For each valid i, the i-th segment starts at x = L_i and ends at x = R_i.

At the time t = 0, all segments start moving; for each valid i, the i-th segment starts moving with speed V_i. You need to assign a direction - left or right - to the movement of each segment, i.e. choose a sign for each V_i (not necessarily the same for all segments). The resulting movement must satisfy the following condition: at the time t = 10^{10000}, there are no two segments that touch or intersect.

Decide if it is possible to assign directions to the segments in such a way that the above condition is satisfied.

### [](#approach-2)Approach -

To check if segments can move without intersecting, we use a sweeping line approach to detect overlaps. Each segment has a start and end point on the `x-axis`, moving at a specified speed. We group segments by speed to handle those with identical speeds together. Sorting segments by speed, we then track overlaps using a `frequency map`, which increments at each segment’s start and decrements after its end. By calculating a running total with this map, we detect areas where three or more segments overlap, indicating inevitable collisions. If this `count` never reaches three, a collision-free arrangement is possible.

### [](#time-complexity-3)Time Complexity -

O(NlogN), due to sorting and the `frequency map` operations.

### [](#space-complexity-4)Space Complexity -

O(N), for storing segment intervals and `frequency maps`.

</details>

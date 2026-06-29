# Fencing

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FENCE |
| Difficulty Rating | 1696 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1600 to 1700 difficulty problems |
| Official Link | [FENCE](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1700/problems/FENCE) |

---

## Problem Statement

There is a field with plants — a grid with $N$ rows (numbered $1$ through $N$) and $M$ columns (numbered $1$ through $M$); out of its $NM$ cells, $K$ cells contain plants, while the rest contain weeds. Two cells are adjacent if they have a common side.

You want to build fences in the field in such a way that the following conditions hold for each cell that contains a plant:
- it is possible to move from this cell to each adjacent cell containing a plant without crossing any fences
- it is impossible to move from this cell to any cell containing weeds or to leave the grid without crossing any fences

The fences can only be built between cells or on the boundary of the grid, i.e. on the sides of cells. The total length of the built fences is the number of pairs of side-adjacent cells such that there is a fence built on their common side plus the number of sides of cells on the boundary of the grid which have fences built on them. Find the minimum required total length of fences that need to be built.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains three space-separated integers $N$, $M$ and $K$.
- $K$ lines follow. Each of these lines contains two space-separated integers $r$ and $c$ denoting that the cell in row $r$ and column $c$ contains a plant.

### Output
For each test case, print a single line containing one integer — the minimum required length of fences.

### Constraints
- $1 \le T \le 10$
- $1 \le N, M \le 10^9$
- $1 \le K \le 10^5$
- $1 \le r \le N$
- $1 \le c \le M$
- the cells containing plants are pairwise distinct

### Subtasks
**Subtask #1 (30 points):** $1 \le N, M \le 1,000$

**Subtask #2 (70 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
2
4 4 9
1 4
2 1 
2 2
2 3
3 1
3 3
4 1
4 2
4 3
4 4 1
1 1
```

**Output**

```text
20
4
```

**Explanation**

**Example case 1:** The field looks like this ('x' denotes a cell containing a plant, '.' denotes a cell containing weeds):
```
...x
xxx.
x.x.
xxx.
```
An optimal solution is to build fences around the topmost plant (with length $4$), around the remaining eight plants (with length $12$) and around the hole between them (with length $4$). The total length is $4+12+4 = 20$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 4 9
1 4
2 1
2 2
2 3
3 1
```

**Output for this case**

```text
20
```



#### Test case 2

**Input for this case**

```text
3 3
4 1
4 2
4 3
4 4 1
1 1
```

**Output for this case**

```text
4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**PROBLEM LINK**:

[Practice](https://www.codechef.com/problems/FENCE)

[Contest, div. 1](https://www.codechef.com/APRIL19A/problems/FENCE)

[Contest, div. 2](https://www.codechef.com/APRIL19B/problems/FENCE)

**Author:** [Ashish Gupta](http://www.codechef.com/users/ashishgup)

**Tester:** [Zhong Ziqian](http://www.codechef.com/users/fjzzq2002)

**Editorialist:** [Oleksandr Kulkov](http://www.codechef.com/users/melfice)

**DIFFICULTY**:

SIMPLE

**PREREQUISITES**:

Basic data structures

**PROBLEM**:

You’re given N\times M grid, K cells in this grid contain a plant. You’re going to build a fence between each pair of adjacent cells u and v such that exactly one of these cells contains plant. Also fence must be built on the boundary of the grid if adjacent cell to this boundary contains plant.

**EXPLANATION**:

Let’s keep a two-dimensional map in which for cell (x,y) we will keep 1 if it contains plant and 0 otherwise. When you add a new plant (x,y) you have to check all the adjacent cells:

\{(x+1,y),(x,y+1),(x-1,y),(x,y-1)\}

For each cell which doesn’t contain a plant you have to add 1 to the answer and for each cell which contains a plant you should subtract 1. In first case you have to create a fence to separate our cell from that neighbor and in the second case you have to remove the fence because both adjacent cells are plants now. Possible implementation:

``int N, M, K;
cin >> N >> M >> K;
map<int, map<int, int>> A;
int ans = 0;
int dx[] = {1, 0, -1, 0};
int dy[] = {0, 1, 0, -1};
while(K--) {
	int x, y;
	cin >> x >> y;
	for(int i = 0; i < 4; i++) {
		int nx = x + dx[i];
		int ny = y + dy[i];
		ans += A[nx][ny] ? -1 : 1;
	}
	A[x][y] = 1;
}
cout << ans << endl;
``

**AUTHOR’S AND TESTER’S SOLUTIONS**:

Author’s solution can be found [here](https://ideone.com/Q8qcwV).

Tester’s solution can be found [here](https://ideone.com/pyit6f).

Editorialist’s solution can be found [here](https://ideone.com/1WkUno).

</details>

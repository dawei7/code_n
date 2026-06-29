# Subtree Removal

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SUBREM |
| Difficulty Rating | 2010 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Basic Graph Theory - Trees, DFS, BFS |
| Official Link | [SUBREM](https://www.codechef.com/practice/course/3to4stars/LP3TO401/problems/SUBREM) |

---

## Problem Statement

You are given a rooted tree with $N$ nodes (numbered $1$ through $N$); node $1$ is the root. Each node has a value; let's denote the value of node $i$ by $A_i$.

You may perform the following operation any number of times (including zero): choose any node which still exists in the tree and remove the whole subtree of this node including itself.

Let's define the *profit* as the sum of values of all nodes which currently exist in the tree minus $X \cdot k$, where $k$ denotes the number of times this operation was performed. Find the maximum possible profit.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $X$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.
- Each of the following $N-1$ lines contains two space-separated integers $u$ and $v$ denoting that nodes $u$ and $v$ are connected by an edge.

### Output
For each test case, print a single line containing one integer — the maximum profit.

### Constraints
- $1 \le T \le 10$
- $1 \le N \le 10^5$
- $1 \le X \le 10^9$
- $1 \le u, v \le N$
- $|A_i| \le 10^9$ for each valid $i$
- the graph described on the input is a tree

### Subtasks
**Subtask #1 (30 points):** $1 \le N \le 1,000$

**Subtask #2 (70 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
1
3 5
1 -5 -10
1 2
2 3
```

**Output**

```text
-4
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**PROBLEM LINK**:

[Practice](https://www.codechef.com/problems/SUBREM)

[Contest, div. 1](https://www.codechef.com/APRIL19A/problems/SUBREM)

[Contest, div. 2](https://www.codechef.com/APRIL19B/problems/SUBREM)

**Author:** [Ashish Gupta](http://www.codechef.com/users/ashishgup)

**Tester:** [Zhong Ziqian](http://www.codechef.com/users/fjzzq2002)

**Editorialist:** [Oleksandr Kulkov](http://www.codechef.com/users/melfice)

**DIFFICULTY**:

SIMPLE

**PREREQUISITES**:

DFS

**PROBLEM**:

You’re given tree on N vertices, each node has assigned value A_i. You may choose any node in the tree and remove all its descendants and the node itself. Your profit for that will be equal to the sum of values still existing in the tree minus X \cdot k where k is number of deletions and X is given number. You have to find the maximum possible profit.

**QUICK EXPLANATION**:

As simple as dp_v = \max\left(A_v+\sum\limits_{u \in \text{children}_v} dp_u, -X\right).

**EXPLANATION**:

Maintain dp_v to be best possible sum you may get from subtree of v. You will either drop subtree or not, in first case it’s -X and in second case it’s A_v plus sum of dp_u over all children of v:

``int dfs(int v = 1, int p = 1) {
	int res = 0;
	for(auto u: g[v]) {
		if(u != p) {
			res += dfs(u, v);
		}
	}
	return max(A[v] + res, -x);
}
``

**AUTHOR’S AND TESTER’S SOLUTIONS**:

Author’s solution can be found [here](https://ideone.com/CANQF1).

Tester’s solution can be found [here](https://ideone.com/EkupL2).

Editorialist’s solution can be found [here](https://ideone.com/9ni4kK).

</details>

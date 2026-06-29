# Treeversion

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TREEVERS |
| Difficulty Rating | 2453 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Basic Graph Theory - Trees, DFS, BFS |
| Official Link | [TREEVERS](https://www.codechef.com/practice/course/3to4stars/LP3TO401/problems/TREEVERS) |

---

## Problem Statement

You are given a rooted tree with $N$ nodes (numbered $1$ through $N$); the root is node $1$. For each valid $i$, node $i$ has weight $w_i$, which is either $0$ or $1$.

We want to traverse the tree using depth first search. The order in which the nodes are visited is not uniquely defined, since we may visit the children of each node in an arbitrary order. Formally, the pseudocode of DFS-traversal is:
```
function DFS(node n):
	node n is visited
	for each node s (s is a son of n) in some order:
		call DFS(s)
	return
call DFS(root)
```

For each possible DFS-traversal of the tree, consider the sequence of weights of nodes in the order in which they are visited; each node is visited exactly once, so this sequence has length $N$. Calculate the number of inversions for each such sequence. The minimum of these numbers is the *treeversion* of our tree.

Find the treeversion of the given tree.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ space-separated integers $w_1, w_2, \ldots, w_N$.
- Each of the following $N-1$ lines contains two space-separated integers $x$ and $y$ denoting that nodes $x$ and $y$ are connected by an edge.

### Output
For each test case, print a single line containing one integer — the treeversion of the given tree.

### Constraints
- $1 \le T \le 1,000$
- $1 \le N \le 10^5$
- $0 \le w_i \le 1$ for each valid $i$
- $1 \le x, y \le N$
- the graph on the input is a tree
- the sum of $N$ over all test cases does not exceed $10^6$

### Subtasks
**Subtask #1 (50 points)**:
- $1 \le N \le 1,000$
- the sum of $N$ over all test cases does not exceed $10,000$

**Subtask #2 (50 points)**: original constraints

---

## Examples

**Example 1**

**Input**

```text
1
3
1 0 1
1 2
1 3
```

**Output**

```text
1
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](https://www.codechef.com/problems/TREEVERS)

[Contest](https://www.codechef.com/LTIME76A/problems/TREEVERS)

**Author:** [Erfan AliMohammadi](https://www.codechef.com/users/erfaniaa)

**Tester & Editorialist:** [Hussain Kara Fallah](https://www.codechef.com/users/deadwing97)

### PROBLEM EXPLANATION

You are given a rooted tree with N nodes (numbered 1 through N); the root is node 1. For each valid i, node i has weight w_i, which is either 0 or 1.

We want to traverse the tree using depth-first search. The order in which the nodes are visited is not uniquely defined, since we may visit the children of each node in an arbitrary order. At the moment we enter a node, we immediately append its weight to our special sequence.

Find a DFS order that would yield a special sequence with minimum inversions possible.

### DIFFICULTY:

Easy-Medium

### CONSTRAINTS

(1 \leq n \leq 10^5)

### PREREQUISITES:

Graph Theory

### QUICK EXPLANATION:

Let’s solve each subtree and assume that the root of some random subtree is x. Note that we need to solve each child of x separately and find the best value for its subtree. After that for merging them to form the DFS-order of subtree rooted at x, sort them using a comparator that takes 2 roots (P,Q) as arguments and checks if its better to concatenate DFS sequence of P then Q or vice versa and picks the choice with less inversions.

### EXPLANATION:

First of all, we need to run a DFS to find the number of zeroes as well the number of ones in each subtree.

The DFS sequence of a subtree rooted at a random node is made of the concatenation of children sequences in some order we need to figure. So note here that the inner inversions inside each of these smaller sequences would remain the same no matter how we order these sequences while forming the sequence of the parent. What we are adding as a penalty is the mutual effect of sequences on each other.

This leads us to a dynamic programming approach (you can call it so actually).

When solving a subtree rooted at x let’s solve all children subtrees and find their optimal sequences and then find a way to order them.

To order children of a subtree’s root, we are going to use a classic greedy comparator. Let’s imagine that we have 2 children of our current root (p,q)

We would put p before q in the sequence if and only if:

ones_p*zeroes_q<zeroes_p*ones_q

which means check inversions if we put p then q and vice-versa and pick the cheapest scenario. This comparator is intuitive and self explanatory.

The proof behind it is that it maintains transitivity (a \leq b \leq c) implies (a \leq c) [read here](https://en.wikipedia.org/wiki/Total_order)

So we already know the number of zeroes and ones in each subtree, all we need to do when processing a certain subtree root is to sort the children with this comparator and then concatenate them and conclude with final result.

Our final answer would be the dp_1

Check implementation for details.

### AUTHOR’S AND TESTER’S SOLUTIONS:

**EDITORIALIST’s solution**: Can be found [here](https://pastebin.com/tQL8tJ38)

</details>

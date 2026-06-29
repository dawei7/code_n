# Shortest Path in Binary Trees

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BINTREE |
| Difficulty Rating | 1413 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Graphs |
| Official Link | [BINTREE](https://www.codechef.com/practice/course/3to4stars/LP3TO403/problems/BINTREE) |

---

## Problem Statement

Consider an infinite full binary tree (each node has two children except the leaf nodes) defined as follows. For a node labelled **v** its left child will be labelled **2*v** and its right child will be labelled **2*v+1**. The root is labelled as **1**.

You are given **N** queries of the form **i j**. For each query, you have to print the length of the shortest path between node labelled **i** and  node labelled **j**.

### Input

First line contains **N**, the number of queries. Each query consists of two space separated integers **i** and **j** in one line.

### Output

For each query, print the required answer in one line.

### Constraints

- **1** ≤ **N** ≤ **105**

- **1** ≤ **i,j** ≤ **109**

---

## Examples

**Example 1**

**Input**

```text
3
1 2
2 3
4 3
```

**Output**

```text
1
2
3
```

**Explanation**

For first query, 1 is directly connected to 2 by an edge. Hence distance 1.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 2
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
2 3
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
4 3
```

**Output for this case**

```text
3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/BINTREE)

[Contest](http://www.codechef.com/APRIL14/problems/BINTREE)

**Author:** [Lalit Kundu](http://www.codechef.com/users/darkshadows)

**Tester:** [Shiplu Hawlader](http://www.codechef.com/users/shiplu) and [Mahbubul Hasan](http://www.codechef.com/users/white_king)

**Editorialist:** [Lalit Kundu](http://www.codechef.com/users/darkshadows)

### DIFFICULTY:

EASY

### PREREQUISITES:

[Binary Tree](http://en.wikipedia.org/wiki/Binary_tree)

[Lowest Common Ancestor](http://en.wikipedia.org/wiki/Lowest_common_ancestor)

### PROBLEM:

Given infinite full binary tree (each node has two children except leaf nodes), for queries of form (i,j) [i,j <= 10^9] print the length of shortest path between nodes labelled i and j.

Root is labelled 1. For each node labelled v, it’s left child is labelled 2*v and right child, 2*v+1.

### QUICK EXPLANATION:

We convert i,j to base 2 (without leading zeroes)

Let i in base 2 be = a1a2…an

Let j in base 2 be = b1b2…bm

If ap=bp for all p<=k, then our answer is (n+m-2*k).

### EXPLANATION:

If we are at a node labelled v, if we move left we get 2*v ie. append a 0 to binary representation of v. If we move right we get 2*v+1 ie. append a 1 to binary representation of v. Thus from binary value of a node v, we completely know the path taken from the root.

For example, Node 10 in binary is 1010, here first 1 is root node, next is 0, means a left turn, next 1 means are right child, next 0 means a left child.

We convert i,j to base 2 (without leading zeroes)

Let i in base 2 be = a1a2…an

Let j in base 2 be = b1b2…bm

If ap=bp for all p<=k, means their Lowest Common Ancestor(LCA) in binary is a0a1…ak. So the distance between i and j is dist(i,LCA(i,j))+dist(j,LCA(i,j)).

Since i in base 2 has n digits, the distance between i and LCA(i,j) will be (n-k). Since those are the extra steps taken from LCA moving towards node.

Therefore our answer is (n-k)+(m-k).

For example, i=10, j=13.

i in base2 = 1010

j in base2 = 1101

So, k=1 and our answer is 4-1+4-1=6.

Complexity for each query= log2(i)+log2(j).

### AUTHOR’S AND TESTER’S SOLUTIONS:

To be updated soon.

</details>

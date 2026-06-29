# Right side view of Binary tree

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RIGTHSIDE |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Binary Trees |
| Official Link | [RIGTHSIDE](https://www.codechef.com/learn/course/trees/BTREESPRO/problems/RIGTHSIDE) |

---

## Problem Statement

Given the $root$ of a binary tree, imagine standing on the **right side** of the tree. Return an array of the values of the nodes you can see ordered from top to bottom.

**Notes:**

* Return the rightmost node value at each depth level (top → bottom).
* Expected solutions commonly use BFS level-order traversal or DFS with depth tracking.

---

### Function Declaration

- Function Name

  * $rightSideView$ — This function returns the list of node values visible when viewing a binary tree from the right side.

- Parameters

  * $root$: A pointer to the root node of the binary tree.
  The binary tree may contain $0$ to $100$ nodes, and each node contains an integer value or may be null (`-1` in level-order input).

- Return Value

  * Returns an array containing the values of the rightmost nodes at each depth level of the binary tree.
  * The values are ordered from **top to bottom**, representing the nodes visible from the right side.

---

### Constraints

* $1 \leq T \leq 1000$
* $0 \leq N \leq 100$
* $-100 \leq \text{Node.val} \leq 100$
* Level-order input may contain `-1` indicating a null node.

---

---

## Input Format

* The first line of input contains a single integer $T$, denoting the number of test cases.
* Each test case consists of **two lines of input**:

  * The first line contains a single integer $N$ - size of the array that contains nodes and empty leaf nodes.
  * The second line contains $N$ space-separated integers representing the **level-order traversal** of the tree, where
    **`-1` denotes a null child**.

---

---

## Output Format

For each test case, output on a new line the **right side view** of the binary tree —
a sequence of space-separated integers representing the values of the nodes visible from the right side.

---

---

## Constraints

* $1\leq T \leq 1000
* The number of nodes in the tree is in the range $[0, 100]$.
* $-100 \leq \text{Node.val} \leq 100$

---

## Examples

**Example 1**

**Input**

```text
3
7
10 5 15 3 7 -1 20
7
1 2 3 4 5 6 7
5
1 -1 2 -1 3
```

**Output**

```text
10 15 20
1 3 7
1 2 3
```

**Explanation**

* For the first test case:
```
    10
   /  \
  5    15
 / \     \
3   7     20
```
From the right side you see 10, then 15, then 20.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
7
10 5 15 3 7 -1 20
```

**Output for this case**

```text
10 15 20
```



#### Test case 2

**Input for this case**

```text
7
1 2 3 4 5 6 7
```

**Output for this case**

```text
1 3 7
```



#### Test case 3

**Input for this case**

```text
5
1 -1 2 -1 3
```

**Output for this case**

```text
1 2 3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## 1. Problem Summary

You are given the root of a binary tree. Imagine standing on the right side of the tree and looking inward. At every depth level from top to bottom, only the rightmost visible node is seen. The task is to return the values of these nodes in order.

The tree may be empty. Node values lie within the range [−100, 100], and the total number of nodes is at most 100.

---

## 2. Key Insight

For each depth level of the binary tree, exactly one node is visible from the right side. That node is the **last node encountered at that level** when performing a left-to-right traversal, or the **first node encountered** if doing a right-first DFS.

Thus, the core objective is to capture exactly one node per level:
the rightmost node.

There are two common and valid approaches:

---

## 3. Approach 1: Level Order Traversal (BFS)

This method processes the tree level by level.

1. Use a queue to perform a level-order traversal.
2. For each level:

   * Process all nodes in that level.
   * Record the value of the last node processed.
     This corresponds to the rightmost node at that level.
3. Continue until the entire tree has been traversed.

This is the idea used in the provided solution.

### Complexity

* Time: O(N), since every node is visited once.
* Space: O(W), where W is the maximum width of the tree (worst case O(N)).

---

## 4. Approach 2: Depth-First Search with Depth Tracking (DFS)

This method explores the tree depth-first, prioritizing the right subtree before the left.

1. Perform a recursive DFS.
2. Visit right child first, then left child.
3. Maintain a list that stores the first node visited at each depth.

   * Since right children are visited first, the first node seen at each depth is the visible one.
4. Continue until all nodes have been processed.

### Complexity

* Time: O(N)
* Space: O(H) for recursion depth, where H is the height of the tree.

---

## 5. Correctness

Both BFS and DFS ensure that exactly one node per tree level is recorded and that this node is the correct rightmost visible one. BFS guarantees this by taking the last node of each level, while DFS guarantees this by prioritizing the right subtree and storing the first visited node at each depth.

---

## 6. Edge Cases

1. **Empty tree**: Return an empty list.
2. **Tree with a single node**: The answer contains that single value.
3. **Left-skewed tree**: Each level has only one node, so that node is visible.
4. **Right-skewed tree**: All nodes are visible.
5. **Mixed trees**: Subtrees may be unbalanced; visibility still depends solely on the rightmost node per level.

---

## 7. Summary

The task is to extract the rightmost node of each depth level of a binary tree. Both BFS (level order) and DFS (right-prioritized) approaches solve the problem efficiently in linear time. The BFS approach naturally aligns with the structure of the tree levels, while the DFS approach leverages depth and traversal order to achieve the same result.

</details>

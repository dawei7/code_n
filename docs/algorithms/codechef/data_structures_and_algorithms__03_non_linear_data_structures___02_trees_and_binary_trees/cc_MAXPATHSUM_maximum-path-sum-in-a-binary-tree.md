# Maximum Path Sum in a Binary Tree

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MAXPATHSUM |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Binary Trees |
| Official Link | [MAXPATHSUM](https://www.codechef.com/learn/course/trees/BTREESPRO/problems/MAXPATHSUM) |

---

## Problem Statement

A **path** in a binary tree is a sequence of nodes where each pair of consecutive nodes is directly connected by an edge. A node can appear in the path **only once**. The path does not necessarily have to go through the root.

The **path sum** is the sum of all node values in the path.

Given the `root` of a binary tree, return the **maximum path sum** among all possible **non-empty** paths.

---

### Function Declaration

- **Function Name**
  - $maxPathSum$

- **Parameters**
  - $root$: The root node of the binary tree.

- **Return Value**
  - Returns an integer representing the maximum path sum among all possible non-empty paths in the binary tree.

---

### Constraints
- The number of nodes in the tree is in the range $[1, (3 \times 10^{4})]$.
- $-1000 \leq \text{Node.val} \leq 1000$

---

---

## Input Format

* The first line of input contains a single integer $T$, denoting the number of test cases.
* Each test case consists of **two lines of input**:

  * The first line contains a single integer $N$ — the number of nodes in the binary tree.
  * The second line contains $N$ space-separated integers representing the **level-order traversal** of the tree, where
    **NULL denotes a null child**.

---

---

## Output Format

For each test case, output on a new line a single integer —
the **maximum path sum** in the given binary tree.

---

---

## Examples

**Example 1**

**Input**

```text
2
5
5 4 8 11 13
3
2 NULL NULL
```

**Output**

```text
30
2
```

**Explanation**

* **First test case:**
  The maximum path sum is `30`, obtained by choosing the path `8 -> 5 -> 4 -> 13`.
  This path gives the highest possible sum among all valid paths in the tree.

* **Second test case:**
  The maximum path sum is `2`, achieved by selecting the single node `[2]`.
  Including $NULL$ would decrease the total sum, so it is excluded.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
5 4 8 11 13
```

**Output for this case**

```text
30
```



#### Test case 2

**Input for this case**

```text
3
2 NULL NULL
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## Problem Restatement

Given a binary tree where each node contains an integer value (which may be negative), a path is defined as a sequence of connected nodes where no node appears more than once. The path does not need to pass through the root.

The task is to compute the maximum possible sum of values along any non-empty path in the tree.

---

## Key Observations

1. A path can start and end at any two nodes.
2. The path must follow parent–child connections.
3. The path may include both left and right subtrees of a node.
4. Negative values can reduce the total sum and should be avoided unless unavoidable.
5. The answer must include at least one node.

---

## Naive and Brute Force Approaches

### 1. Enumerate All Possible Paths

One can attempt to:

* Choose every node as a starting point.
* Explore all downward paths from that node.
* Track the sum of each path.

This approach quickly becomes impractical:

* Number of paths is exponential.
* Repeated computations across overlapping subtrees.

Time complexity is exponential and unsuitable for large trees.

---

### 2. Dynamic Programming with Postorder Traversal (Optimal Approach)

This is the most efficient and widely accepted solution.

#### Core Insight

For every node, consider two different values:

1. Maximum path sum starting at this node and extending upward to its parent.
2. Maximum path sum passing through this node (possibly including both children).

These two values serve different purposes and must be handled separately.

---

#### Contribution from a Node

For each node:

* Compute the maximum sum that can be extended to its parent.
* This extension can include:

  * The node alone.
  * The node plus the best contribution from either left or right subtree.
* If a subtree contributes a negative sum, it is ignored.

This value is returned to the parent.

---

#### Updating the Global Answer

At each node, calculate:

* Node value
* Best contribution from left subtree
* Best contribution from right subtree

The sum of all three represents the best path passing through this node.

This value is used to update the global maximum.

---

#### Why This Works

* Every possible path in the tree has a highest (or turning) node.
* That node is exactly where both sides of the path meet.
* Evaluating every node as a turning point guarantees correctness.

---

#### Complexity

* Time complexity: O(N)
* Space complexity: O(H), where H is the height of the tree (recursion stack)

---

## Alternative Approaches

### 3. Bottom-Up Dynamic Programming (Tree DP)

This approach explicitly defines states:

* DP[node][0]: maximum downward path starting at node
* DP[node][1]: maximum path anywhere in subtree rooted at node

This is conceptually similar to the postorder approach but uses explicit DP definitions.

Time and space complexity remain linear.

---

### 4. Iterative Postorder Traversal

Instead of recursion, a stack can be used to perform postorder traversal.

This avoids recursion depth limits and is useful for very deep or skewed trees.

The logic remains the same:

* Compute contributions from children before processing the parent.

---

### 5. All-Negative Tree Handling

In trees where all values are negative:

* The best path is the maximum single node value.
* Ignoring negative contributions ensures correctness.
* Initializing the global answer to the minimum possible value guarantees the correct result.

---

## Common Pitfalls

1. Returning a path that includes both children to the parent.

   * A parent path can only extend through one child.
2. Forgetting that paths do not have to include the root.
3. Incorrect handling of negative values.
4. Assuming paths must be root-to-leaf.

</details>

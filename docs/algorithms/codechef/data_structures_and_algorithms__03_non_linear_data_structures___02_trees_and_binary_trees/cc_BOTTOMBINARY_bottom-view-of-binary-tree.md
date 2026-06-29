# Bottom view of binary tree

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BOTTOMBINARY |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Binary Trees |
| Official Link | [BOTTOMBINARY](https://www.codechef.com/learn/course/trees/BTREESPRO/problems/BOTTOMBINARY) |

---

## Problem Statement

You are given the **root** of a binary tree.
Your task is to return the **bottom view** of the tree.

The **bottom view** represents the set of nodes that are visible when the tree is viewed from **below**.

For nodes that lie at the same horizontal distance from the root, **the one appearing later in the level order traversal** (i.e., lower in the tree) will be visible in the bottom view.

Return the nodes from **leftmost to rightmost**.

---
### Function Declaration

- **Function Name**
  - $bottomView$

- **Parameters**
  - $root$: Pointer to the root node of the binary tree (`TreeNode*`).

- **Return Value**
  - Returns a vector of integers representing the bottom view of the binary tree, ordered from leftmost to rightmost.

---

### Constraints
* $1 \leq \text{Number of Nodes} \leq 10^{4}$
* $-10^{3} \leq \text{Node.val} \leq 10^{3}$

---

---

## Input Format

* The first line contains a single integer $T$, denoting the number of test cases.
* Each test case consists of **two lines of input**:

  * The first line contains a single integer $N$ — the number of nodes in the binary tree.
  * The second line contains $N$ space-separated values representing the **level-order traversal** of the tree.
    Use **`null`** (or `-1` if preferred) to denote missing children.

---

---

## Output Format

* For each test case, output on a new line the **bottom view** of the binary tree.
* Print the node values from **leftmost to rightmost**, separated by spaces.

---

---

## Examples

**Example 1**

**Input**

```text
1
7
15 10 20 8 12 16 25
```

**Output**

```text
8 10 16 20 25
```

**Explanation**

Visible nodes from bottom are: \
Leftmost -> 8 \
Then -> 10 \
Then -> 16 (hides 15) \
Then -> 20 \
Then -> 25 (rightmost)

**Example 2**

**Input**

```text
1
7
1 2 3 4 5 6 7
```

**Output**

```text
4 2 6 3 7
```

**Example 3**

**Input**

```text
1
9
50 30 70 20 40 60 80 null 25
```

**Output**

```text
20 25 60 70 80
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## Problem Understanding

You are given the **root of a binary tree**, and you need to find the **bottom view** of it.

### What does "Bottom View" mean?

Imagine you are standing **below** the binary tree and looking **upwards**.
You can only see the **lowest (deepest)** nodes at each **horizontal position**.

So, for each **horizontal distance** from the root:

* The node that appears **lowest in the tree** (i.e., has the greatest depth or appears later in level order) will be visible.

Finally, you must output all such visible nodes **from leftmost to rightmost**.

---

## 📚 Key Concept: Horizontal Distance (HD)

* The **root** node is considered to be at **horizontal distance = 0**.
* The **left child** has `HD = parent’s HD - 1`.
* The **right child** has `HD = parent’s HD + 1`.

So, every node in the tree has a **unique (or overlapping)** horizontal distance value.

---

## Approach (Conceptual Steps)

### Step 1. Assign a horizontal distance (HD) to each node

Perform a **level order traversal (BFS)** of the tree and track:

* The **node**
* Its **horizontal distance (HD)** from the root

This ensures that nodes at the same level are processed **from top to bottom and left to right**.

---

### Step 2. Maintain a mapping

Create a **map** or **dictionary** to keep track of:

```
horizontal_distance → node_value
```

Whenever a new node is visited:

* If another node already exists at the same horizontal distance, **replace it** with the current one.
  (Because the current node is deeper or appears later in BFS, so it hides the earlier one.)

---

### Step 3. Perform BFS traversal

Use a **queue** for level order traversal:

1. Start with the root node at `HD = 0`.
2. For each node dequeued:

   * Store or overwrite its value in the map using its HD.
   * Add its left child with `HD - 1`.
   * Add its right child with `HD + 1`.

This ensures that deeper nodes overwrite shallower ones naturally.

---

### Step 4. Collect and sort results

Once traversal is complete:

* Extract all keys (horizontal distances) from the map.
* Sort them in **ascending order**.
* Output their corresponding node values in this order.

---

## Time and Space Complexity

| Aspect    | Explanation                                                                                   | Complexity     |
| --------- | --------------------------------------------------------------------------------------------- | -------------- |
| **Time**  | Each node is visited once during BFS traversal. Sorting the map keys adds a small extra cost. | **O(N log N)** |
| **Space** | The map and queue store up to N nodes in the worst case.                                      | **O(N)**       |

Here, **N** = number of nodes in the binary tree.

---

## Example Walkthrough

### Input:

```
15 10 20 8 12 16 25
```

### Tree:

```
         15
       /    \
     10      20
    /  \    /  \
   8   12  16  25
```

### Horizontal Distances:

```
        0 → 15
   -1 → 10, +1 → 20
   -2 → 8,  0 → 12, +2 → 25, 0 → 16
```

### Bottom-most nodes for each HD:

| HD | Visible Node         |
| -- | -------------------- |
| -2 | 8                    |
| -1 | 10                   |
| 0  | 16 (hides 15 and 12) |
| +1 | 20                   |
| +2 | 25                   |

### Output:

```
8 10 16 20 25
```

---

## Edge Cases to Consider

1. **Single Node Tree**
   Only one node → bottom view = [root value]

2. **Left Skewed Tree**
   Every node only has a left child → bottom view = [all nodes top to bottom]

3. **Right Skewed Tree**
   Every node only has a right child → bottom view = [all nodes top to bottom]

4. **Tree with Nulls (Sparse Tree)**
   Missing children should not affect HD tracking — handle `"null"` or absent children properly.

---

## Summary

| Step | Description                    |
| ---- | ------------------------------ |
| 1    | Assign horizontal distances    |
| 2    | Traverse level order (BFS)     |
| 3    | Update bottom-most node per HD |
| 4    | Sort by HD and output values   |

---

### Intuition Recap

The “bottom view” is essentially a **projection of the tree** onto a **horizontal axis**, keeping only the **deepest nodes** at each x-coordinate.

</details>

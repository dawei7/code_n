# Vertical Order Traversal of Binary Tree

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | VERTICALTRAV |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Binary Trees |
| Official Link | [VERTICALTRAV](https://www.codechef.com/learn/course/trees/BTREESPRO/problems/VERTICALTRAV) |

---

## Problem Statement

You are given a binary tree represented in **level order traversal**.
Your task is to return its **vertical order traversal**.

* Assume the root of the tree is at position `(row = 0, col = 0)`.
* For a node at `(row, col)`:

  * Its **left child** will be at `(row + 1, col - 1)`
  * Its **right child** will be at `(row + 1, col + 1)`

The **vertical order traversal** groups nodes column by column:

* Start from the **leftmost column** and move to the rightmost.
* Within the same column:

  * Nodes are sorted first by their row (top to bottom).
  * If multiple nodes share the same row and column, order them by value.

You need to output the vertical order traversal for each test case.

---

### Function Declaration

- **Function Name**
  - $verticalTraversal$

- **Parameters**
  - $root$: A pointer to the root node of the binary tree.

- **Return Value**
  - Returns a 2D list of integers where each inner list represents a vertical column of the binary tree.
  - Nodes are ordered from top to bottom, and for nodes sharing the same position, by increasing value.
  - Columns are ordered from leftmost to rightmost.

---

### Constraints

$1 \leq t \leq 10$ \
$1 \leq n \leq 1000$ \
$0 \leq \text{Node.val} \leq 1000$

---

---

## Input Format

* The first line contains a single integer $T$, denoting the number of test cases.
* Each test case consists of **two lines of input**:

  * The first line contains a single integer $N$ — the length of the 2D list of integers containing the level order traversal of the binary tree.
  * The second line contains $N$ space-separated values representing the **level-order traversal** of the tree.
    Use **`null`** (or `-1` if preferred) to denote a missing child.

---

---

## Output Format

For each test case, output on a new line the **vertical order traversal** of the tree, formatted as a list of lists.
Each inner list corresponds to one vertical column from leftmost to rightmost.

---

---

## Constraints

$1 \leq t \leq 10$ \
$1 \leq n \leq 1000$ \
$0 \leq \text{Node.val} \leq 1000$

---

## Examples

**Example 1**

**Input**

```text
1
7
5 3 8 1 4 7 9
```

**Output**

```text
[[1],[3],[5,4,7],[8],[9]]
```

**Explanation**

The binary tree is:

```
        5
      /   \
     3     8
    / \   / \
   1   4 7   9
```

* Column -2: `[1]`
* Column -1: `[3]`
* Column 0: `[5, 4, 7]`  -> 5 is at row 0, 4 & 7 at row 2 (sorted by value -> 4 before 7)
* Column 1: `[8]`
* Column 2: `[9]`

**Example 2**

**Input**

```text
1
11
10 5 15 2 7 null 20 null null 6 8
```

**Output**

```text
[[2],[5,6],[10,7],[15,8],[20]]
```

**Explanation**

The binary tree is:

```
         10
       /    \
      5      15
     / \       \
    2   7       20
       / \
      6   8
```

* Column -2: `[2]`
* Column -1: `[5, 6]`
* Column 0: `[10, 7]`
* Column 1: `[15, 8]`
* Column 2: `[20]`

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## Problem Understanding

You are given a **binary tree**, and you must return its **vertical order traversal** — that is, group nodes by their **column index**, from **left to right**.

Each node has a **row** and a **column** coordinate:

* Root is at position `(row = 0, col = 0)`.
* Left child → `(row + 1, col - 1)`
* Right child → `(row + 1, col + 1)`

You must:

1. Group nodes having the same `col`.
2. Within the same column:

   * Sort nodes first by their **row** (top to bottom).
   * If multiple nodes have same row and column → sort by **value**.
3. Return all columns from **leftmost** to **rightmost**.

---

## Key Insight

Each node’s placement is determined by its **(row, col)** coordinates.

So, if we could record **every node’s value** along with its `(row, col)`, then sorting and grouping would give the exact traversal order.

---

##  Step-by-Step Solution Approach

### **Step 1: Traverse the Tree**

Perform a **DFS (Depth-First Search)** or **BFS (Level-Order Traversal)** starting from the root.

For every node visited:

* Record a tuple `(col, row, value)`.

Example:
If the tree is:

```
      5
     / \
    3   8
   / \ / \
  1  4 7  9
```

We record:

```
(0,0,5), (-1,1,3), (1,1,8), (-2,2,1), (0,2,4), (0,2,7), (2,2,9)
```

---

### **Step 2: Sort the Recorded Nodes**

Sort all recorded tuples with the following priority:

1. `col` (ascending)
2. `row` (ascending)
3. `value` (ascending)

After sorting, nodes automatically appear in the correct **vertical traversal order**.

---

### **Step 3: Group by Column**

Once sorted, group nodes having the same `col` value together.

Using the example above:

| Column | Nodes     |
| :----: | :-------- |
|   -2   | [1]       |
|   -1   | [3]       |
|    0   | [5, 4, 7] |
|    1   | [8]       |
|    2   | [9]       |

Hence, the final result:

```
[[1], [3], [5,4,7], [8], [9]]
```

---

## Complexity Analysis

Let `N` = number of nodes in the tree.

* **Traversal:** `O(N)` — visit each node once.
* **Sorting:** `O(N log N)` — sorting based on `(col, row, value)`.
* **Grouping:** `O(N)` — collect values by column.

**Overall Time Complexity:** `O(N log N)`
**Space Complexity:** `O(N)` for storing node data.

---

## Edge Cases

1. **Single Node Tree**

   ```
   Input: [5]
   Output: [[5]]
   ```

2. **Left-Skewed Tree**

   ```
   Every node only has a left child.
   Columns: all negative.
   ```

3. **Right-Skewed Tree**

   ```
   Every node only has a right child.
   Columns: all positive.
   ```

4. **Duplicate Values**
   Sorting by value ensures correct ordering within same row & col.

5. **Sparse Tree**
   Missing nodes represented by `null` — they simply don’t contribute to traversal.

6. **Large Input (up to 1000 nodes)**
   Efficient sorting and grouping handle it comfortably.

---

## Intuition Recap

* Think of **columns** as vertical slices of the tree.
* Each node “falls” into a column based on how far left/right it is.
* Sorting by `(col, row, value)` perfectly captures the problem’s rule set.
* Grouping by column completes the answer.

---

## Final Takeaway

This problem combines:

* **Tree traversal**
* **Coordinate mapping**
* **Multi-key sorting**
* **Grouped output construction**

The trick is not in traversal, but in **how you record and sort the positional data**.

</details>

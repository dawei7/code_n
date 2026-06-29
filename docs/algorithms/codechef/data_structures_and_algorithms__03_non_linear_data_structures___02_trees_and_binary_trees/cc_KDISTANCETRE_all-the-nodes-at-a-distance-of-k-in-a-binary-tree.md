# All the Nodes at a distance of K in a Binary Tree

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | KDISTANCETRE |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Binary Trees |
| Official Link | [KDISTANCETRE](https://www.codechef.com/learn/course/trees/BTREESPRO/problems/KDISTANCETRE) |

---

## Problem Statement

You are given the **root** of a binary tree, a **target node** (`TreeNode* target`), and an integer **k**.
Your task is to **return all node values that are exactly $k$ edges away** from the target node.

The nodes can be in any direction — **upward or downward** — and the answer can be returned **in any order**.

### Function Declaration

- **Function Name**
  - $distanceK$

- **Parameters**
  - $root$: Pointer to the root node of the binary tree (`TreeNode*`).
  - $target$: Pointer to the target node in the binary tree (`TreeNode*`).
  - $k$: An integer representing the exact number of edges distance from the target node.

- **Return Value**
  - Returns a vector of integers containing the values of all nodes that are exactly $k$ edges away from the target node.
  - The order of values in the returned vector does **not** matter.

----

### Constraints
- $1 \leq \text{Number of nodes} \leq 500$
- $0 \leq \text{Node.val} \leq 500$
- All node values are $\textbf{unique} $
- $\text{target}$ is guaranteed to be one of the node values
- $0 \leq k \leq 1000$

---

## Input Format

* The first line of input contains a single integer $T$, denoting the number of test cases.
* Each test case consists of multiple lines of input:

  * The first line of each test case contains three space-separated integers:

    * the **number of nodes** in the tree,
    * the **target node value**,
    * the **value of $k$**.

  * The next line contains the level-order traversal of the binary tree, consisting of node values where $null$ represents a null/absent child.

---

## Output Format

For each test case, output on a new line all node values that are **exactly $k$ edges away** from the target node.
The values may be printed in **any order**.

---

## Examples

**Example 1**

**Input**

```text
1
11 7 2
10 5 15 2 7 null 18 null null 6 8
```

**Output**

```text
2 10
```

**Explanation**

```
          10
         /  \
        5    15
       / \     \
      2   7     18
         / \
        6   8

```

The nodes that are 2 edges away from node `7` are `2` and `10`.

**Example 2**

**Input**

```text
1
3 2 1
1 2 3
```

**Output**

```text
1
```

**Explanation**

```
   1
  / \
 2   3

```
Nodes at distance 1 from node `2` are `1` (the parent).

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## **Problem Restatement**

You are given a binary tree, a target node, and an integer `K`.
Your task is to find **all nodes that are exactly `K` edges away** from the target node —
in **any direction** (upward or downward).

---

## **Intuition**

The challenge here is that the distance can go:

* **Downward** — into the subtree of the target node.
* **Upward** — through the parent, possibly into sibling subtrees.

A typical recursive traversal can easily go *down* the tree,
but finding *upward* nodes requires knowledge of parent relationships.

---

## **Core Idea**

To handle both directions, we think of the problem as two parts:

1. **Downward traversal** —
   Starting from the target node, find all nodes at depth `K` below it.

2. **Upward traversal** —
   Move upward towards the ancestors, and from each ancestor, look into the **opposite subtree** to find nodes that are `(K - distance_to_target - 1)` away.

---

## **Step-by-Step Approach**

### **Step 1: Locate the Target Node**

* Traverse the tree to find the target node.
* Once found, we will explore both *downward* and *upward* from it.

---

### **Step 2: Downward Search (Simple DFS)**

* If we move downward from a node:

  * When `K == 0`, record that node’s value.
  * Otherwise, recursively explore left and right children with `K - 1`.

This finds all nodes *below* the target.

---

### **Step 3: Upward Search (Backtracking)**

* To explore upward:

  * Recursively return the **distance** from the current node to the target.
  * When the target is found, return `0` to its parent.
  * Each ancestor computes:

    * Distance = child’s distance + 1
    * If `distance == K`, the ancestor itself is `K` away — record it.
    * Otherwise, look into the **opposite subtree** for nodes that are `(K - distance - 1)` away.

This way, the recursion naturally propagates distances upward.

---

### **Step 4: Combine Both Searches**

* Start from the root.
* Perform the upward traversal:

  * It will automatically call downward searches when needed.
* Include the results from the downward search from the target itself.

---

## **Complexity Analysis**

| Aspect               | Complexity | Explanation                                          |
| -------------------- | ---------- | ---------------------------------------------------- |
| **Time Complexity**  | O(N)       | Each node is visited once in both searches combined. |
| **Space Complexity** | O(H)       | Recursive stack space (H = tree height).             |
| **Auxiliary Data**   | None       | No need for parent maps or extra structures.         |

Even though we conceptually “go up and down,” each node is processed at most a constant number of times.

---

## **Edge Cases**

1. **K = 0** → Only the target node itself.
2. **Target is the root** → Only downward traversal.
3. **Target is a leaf** → Upward search through ancestors.
4. **K > Tree Height** → No nodes at that distance → Empty output.
5. **Tree with one node** → Only possible if `K = 0`.
6. **Unbalanced tree** → Works fine due to recursive backtracking.

---

## **Example Walkthrough**

### Example:

```
          10
         /  \
        5    15
       / \     \
      2   7     18
         / \
        6   8
```

**Target = 7, K = 2**

### Step 1: Downward from 7

Nodes at distance 2 below 7 → `None` (only 6 and 8 are distance 1)

### Step 2: Upward from 7

* Parent = 5 → distance 1

  * Look into opposite subtree (2) for `K - 1 - 1 = 0` → Add `2`
* Grandparent = 10 → distance 2 → Add `10`

  * Look into right subtree of 10 (15) for `K - 2 - 1 = -1` → ignore

**Result:** `[2, 10, 6, 8, 15]`

---

## **Key Insights**

* The key trick is to **combine a downward DFS** and a **backtracking upward DFS** that returns distance values.
* No need for explicit parent pointers — recursion itself carries parent information.
* The problem is a clean example of **two-directional tree traversal using recursion**.

---

## **Summary**

| Concept              | Description                                         |
| -------------------- | --------------------------------------------------- |
| Problem Type         | Binary Tree + Distance Search                       |
| Core Idea            | DFS with distance tracking both upward and downward |
| Time Complexity      | O(N)                                                |
| Space Complexity     | O(H)                                                |
| Data Structures Used | None (just recursion)                               |
| Edge Cases           | K=0, leaf targets, large K                          |

</details>

# Minimum time take to burn a BT from a given node

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BURNBT |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Binary Trees |
| Official Link | [BURNBT](https://www.codechef.com/learn/course/trees/BTREESPRO/problems/BURNBT) |

---

## Problem Statement

You are given the **root** of a binary tree and a **target node value**. Suppose the target node catches fire at time `t = 0`.

In each **1 second**, the fire spreads from any burning node to all **directly connected nodes** — that is, to its **left child**, **right child**, and **parent**.

Your task is to determine the **minimum time required** to completely burn the entire binary tree.

---

### Rules of Fire Spread:

* Fire spreads simultaneously to **all connected nodes** every second.
* The tree is **connected** (no isolated nodes).
* All node values are **unique**.

---

## Input Format

* The first line contains a single integer $T$, denoting the number of test cases.
* Each test case consists of **two lines of input**:

  * The first line contains two space-separated integers:

    * $N$ — the number of nodes in the binary tree
    * $X$ — the value of the target node from which the fire starts
  * The second line contains $N$ space-separated values representing the **level-order traversal** of the tree.
    Use **`-1`** (or `null`) to denote missing children.

---

## Output Format

* For each test case, output on a new line a single integer —
the **minimum time required to burn the entire binary tree** starting from node $X$.

---

## Constraints

- $1 \leq \text{Number of Nodes} \leq 10^4$
- $-10^5 \leq \text{Node.val} \leq 10^5$
- All node values are $\textbf{unique}$

---

## Examples

**Example 1**

**Input**

```text
1
7 10
10 5 15 2 7 -1 20
```

**Output**

```text
2
```

**Explanation**

```
        10
       /  \
      5    15
     / \     \
    2   7     20
```

* At `t = 0`: Node `10` is on fire.
* At `t = 1`: Nodes `5` and `15` catch fire.
* At `t = 2`: Nodes `2`, `7`, and `20` catch fire.

**Example 2**

**Input**

```text
1
11 4
7 3 9 1 5 8 -1 -1 -1 4 6
```

**Output**

```text
5
```

**Explanation**

```
        7
       / \
      3   9
     / \  /
    1  5 8
      / \
     4   6
```

**Fire Spread:**

* `t = 0`: Node `4` burns.
* `t = 1`: Node `5` burns.
* `t = 2`: Nodes `3` and `6` burn.
* `t = 3`: Nodes `1` and `7` burn.
* `t = 4`: Nodes `9` burn.
* `t = 5`: Nodes `8` burn.

**Example 3**

**Input**

```text
1
8 3
1 2 3 4 -1 5 -1 6
```

**Output**

```text
4
```

**Explanation**

```
        1
       / \
      2   3
     /   /
    4   5
   /
  6
```

**Fire Spread:**

* `t = 0`: Node `3` burns.
* `t = 1`: Nodes `1` and `5` burn.
* `t = 2`: Node `2` burns.
* `t = 3`: Node `4` burns.
* `t = 4`: Node `6` burns.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## Problem Understanding

You are given the root of a **binary tree** and a **target node value**.

When the target node catches fire, the fire spreads every second to **all directly connected nodes** — its:

* **Left child**
* **Right child**
* **Parent**

You must find the **minimum time (in seconds)** required to burn the entire tree.

---

## Example

### Example 1:

**Input:**

```
Tree: [1, 2, 3, 4, null, 5, 6, null, 7]
Target = 1
```

**Visualization:**

```
        1
      /   \
     2     3
    /     / \
   4     5   6
  /
 7
```

**Burn sequence:**

* Second 0 → Node 1 burns.
* Second 1 → Nodes 2, 3 burn.
* Second 2 → Nodes 4, 5, 6 burn.
* Second 3 → Node 7 burns.

**Answer: 3 seconds**

---

### Example 2:

**Input:**

```
Tree: [1, 2, 3, null, 5, null, 4]
Target = 4
```

**Visualization:**

```
        1
      /   \
     2     3
      \     \
       5     4
```

**Burn sequence:**

* Second 0 → Node 4 burns.
* Second 1 → Node 3 burns.
* Second 2 → Node 1 burns.
* Second 3 → Node 2 burns.
* Second 4 → Node 5 burns.

**Answer: 4 seconds**

---

## Key Idea

The fire spreads to **adjacent nodes** each second — this is the same as performing a **Breadth-First Search (BFS)** from the target node, where each level represents 1 second.

However, the tree is **not bidirectional** by default.
You can move to left and right children easily, but not to the parent.

So the main challenge is to also **move upward** during traversal.
That means we must first build **parent references** for each node.

---

## Step-by-Step Solution

### Step 1: Build parent mapping

Use a **level-order traversal (BFS)** starting from the root:

* Store for each node: `parent[node] = parentNode`
* Simultaneously find the pointer/reference to the target node.

At the end:

* We can move to `node->left`, `node->right`, and `parent[node]`.

---

### Step 2: Simulate the burning process

Now perform another BFS starting from the **target node**:

* Use a queue to keep track of all currently burning nodes.
* For each node in the queue:

  * Burn its unvisited neighbors (left, right, parent).
* Each level of BFS takes **1 second**.
* Continue until all nodes are burned.

Keep a counter `time` that increments after each full BFS level.

---

## Time & Space Complexity

| Operation        | Complexity                         |
| ---------------- | ---------------------------------- |
| Build parent map | **O(N)**                           |
| BFS to burn tree | **O(N)**                           |
| **Total**        | **O(N)**                           |
| Space            | **O(N)** (for map, queue, visited) |

Here, `N` is the number of nodes in the tree.

---

## Edge Cases

1. **Single node tree**

   ```
   Tree: [1], Target = 1 → Output: 0
   ```

   (No other nodes to burn.)

2. **Target not found in the tree**
   → Output should be `0` or `Invalid`, depending on problem definition.

3. **Skewed tree (like a linked list)**
   Fire spreads in one direction → time = number of nodes − 1

4. **All left or all right children**
   Ensures code handles missing children correctly.

5. **Empty tree**
   → Output = 0

---

## Concept Recap

| Concept                 | Description                               |
| ----------------------- | ----------------------------------------- |
| **Tree Traversal**      | Used to map parents.                      |
| **BFS Level Traversal** | Each level = 1 second in fire spread.     |
| **Visited Map**         | Prevents revisiting already burned nodes. |
| **Parent Pointers**     | Allow fire to move upward.                |

---

## Final Intuition

Think of the binary tree as an **undirected graph**, where each edge represents a connection that allows the fire to spread in one second.
Once you build these bidirectional edges (via parent pointers), the problem becomes a **multi-level BFS** starting from the target node.

The **height of the farthest node** (in BFS distance) from the target determines how long it takes for the fire to reach it — and that’s your answer.

</details>

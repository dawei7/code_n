# Floor and Ceil in a Binary Search Tree

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FLOORANDCEIL |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Binary Trees |
| Official Link | [FLOORANDCEIL](https://www.codechef.com/learn/course/trees/BTREESPRO/problems/FLOORANDCEIL) |

---

## Problem Statement

You are given the root of a **Binary Search Tree (BST)** and an integer value **key**.
Your task is to find:

* **Floor value:** The node value in the BST that is the **largest value less than or equal to** the given key.
* **Ceil value:** The node value in the BST that is the **smallest value greater than or equal to** the given key.

If either the floor or the ceil value does not exist in the tree, return **-1** for that value.

---
### Function Declaration

- **Function Name**
  - $floorAndCeil$

- **Parameters**
  - $root$: The root node of the Binary Search Tree (BST).
  - $key$: An integer value for which the floor and ceil values are to be found.

- **Return Value**
  - Returns a pair (or tuple) of integers:
    - The first value represents the **floor** of the key (largest value ≤ key, or `-1` if it does not exist).
    - The second value represents the **ceil** of the key (smallest value ≥ key, or `-1` if it does not exist).

---
### Constraints
* $ 1 \leq \text{Number of Nodes} \leq 5000 $
* $ 1 \leq \text{Node.val} \leq 10^7 $
* $ 1 \leq \text{key} \leq 10^7 $

---

---

## Input Format

* The first line contains a single integer $T$, denoting the number of test cases.
* Each test case consists of **two lines of input**:

  * The first line contains two space-separated integers:

    * $N$ — the number of nodes in the BST
    * $K$ — the key value for which the floor and ceil must be found
  * The second line contains $N$ space-separated integers representing the **level-order traversal** of the BST.
    Use **`-1`** (or `null`) to denote missing children.

---

---

## Output Format

For each test case, output on a new line two space-separated integers:

* The **floor** value of the key in the BST (or `-1` if it does not exist)
* The **ceil** value of the key in the BST (or `-1` if it does not exist)

---

---

## Examples

**Example 1**

**Input**

```text
3
7 13
10 5 15 2 7 12 20
7 1
10 5 15 2 7 12 20
7 25
10 5 15 2 7 12 20
```

**Output**

```text
12 15
-1 2
20 -1
```

**Explanation**

* For the first test case:
  * The largest value -> 13 is **12** -> floor.
  * The smallest value -> 13 is **15** -> ceil.

* For the second test case:
  * No node has value -> 1, so floor is **-1**.
  * The smallest node -> 1 is **2**, hence ceil is **2**.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
7 13
10 5 15 2 7 12 20
```

**Output for this case**

```text
12 15
```



#### Test case 2

**Input for this case**

```text
7 1
10 5 15 2 7 12 20
```

**Output for this case**

```text
-1 2
```



#### Test case 3

**Input for this case**

```text
7 25
10 5 15 2 7 12 20
```

**Output for this case**

```text
20 -1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## Problem Understanding

You are given a Binary Search Tree (BST) and a key value.
You must determine two specific values in the tree:

* **Floor:** The greatest value in the BST that is less than or equal to the key.
* **Ceil:** The smallest value in the BST that is greater than or equal to the key.

If a valid floor or ceil does not exist, output **-1** for that value.

---

### Example

Consider the following BST:

```
        8
      /   \
     4     12
    / \   /  \
   2  6  10  14
```

| Key | Floor | Ceil |
| --- | ----- | ---- |
| 11  | 10    | 12   |
| 15  | 14    | -1   |
| 1   | -1    | 2    |
| 5   | 4     | 6    |

---

## Properties of a BST

1. **Left Subtree Property:**
   All nodes in the left subtree have values smaller than the root.

2. **Right Subtree Property:**
   All nodes in the right subtree have values larger than the root.

These properties allow efficient navigation. Instead of scanning the entire tree, we can move left or right depending on comparisons.

---

## Approach

We can find both the floor and the ceil using a single pass each through the BST.
The time complexity for each operation is **O(h)**, where **h** is the height of the tree.

---

### Finding the Floor

Start at the root and follow these rules:

1. If the current node’s value is equal to the key,
   then the node’s value is the floor.

2. If the current node’s value is greater than the key,
   move to the **left** subtree, since smaller values might give a valid floor.

3. If the current node’s value is less than the key,
   this node could be a possible floor.
   Record it, and move to the **right** subtree to check for a closer value.

Continue until the traversal ends.
The last recorded candidate is the floor value.

---

### Finding the Ceil

This is symmetric to the floor search:

1. If the current node’s value is equal to the key,
   then the node’s value is the ceil.

2. If the current node’s value is smaller than the key,
   move to the **right** subtree, since larger values may be potential ceils.

3. If the current node’s value is greater than the key,
   this node could be a possible ceil.
   Record it, and move to the **left** subtree to check for a smaller valid value.

Continue until the traversal ends.
The last recorded candidate is the ceil value.

---

## Complexity Analysis

| Operation     | Time Complexity | Space Complexity |
| ------------- | --------------- | ---------------- |
| Finding Floor | O(h)            | O(1)             |
| Finding Ceil  | O(h)            | O(1)             |

* **h** is the height of the BST.
* For a balanced BST, **h ≈ log N**.
* For a skewed BST (worst case), **h ≈ N**.

---

## Edge Cases

1. The key is smaller than the smallest node value → Floor = -1.
2. The key is larger than the largest node value → Ceil = -1.
3. The key matches a node’s value exactly → Floor = Ceil = that node’s value.
4. Tree contains only one node.
5. Duplicate values (if allowed) behave according to BST insertion rules.

---

## Summary of Steps

1. Start from the root node.
2. Traverse left or right depending on comparisons with the key.
3. Keep track of the latest valid floor or ceil during traversal.
4. Return the final recorded values after traversal.

</details>

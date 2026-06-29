# Serialize and deserialize Binary Tree

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SERIALANDDES |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Binary Trees |
| Official Link | [SERIALANDDES](https://www.codechef.com/learn/course/trees/BTREESPRO/problems/SERIALANDDES) |

---

## Problem Statement

Serialization is the technique of converting a binary tree into a sequence of symbols (such as a string or a list of values) so that it can be easily stored, transferred, or reconstructed later in its original structure.

Your task is to **design an algorithm to serialize and deserialize a binary tree**.
In this problem, the serialized representation must be a level-order (breadth-first) traversal stored as an array/list of integers, where -1 represents a null node.

The following operations must be supported:

deserialize(data): Construct a binary tree from the given serialized representation.

serialize(root): Convert the reconstructed binary tree back into the same level-order representation.

After deserializing the input and serializing it again, the output should represent the same tree structure as the original input.

## **Function Declaration**

### **Function Name**
$serialize$ – This function converts a binary tree into its serialized level-order representation.

$deserialize$ – This function reconstructs a binary tree from its serialized level-order representation.

### **Parameters**

For $serialize$
$root$ : The root node of the binary tree to be serialized.

For $deserialize$
$data$ : A list/array of integers representing the serialized binary tree in level-order traversal. A value of $-1$ represents a null node.

### **Return Value**

For $serialize$
Returns a list/array of integers representing the binary tree in level-order traversal, where a value of $-1$ is used to represent a null node.
For $deserialize$
Returns the root node of the reconstructed binary tree.

---

## Input Format

* The first line of input contains a single integer $T$, denoting the number of test cases.
* Each test case consists of multiple lines of input:

  * The first line of each test case contains a single integer $n$ — the number of nodes in the binary tree.
  * The next line contains the level-order traversal of the tree using $n$ space-separated integers.

    * A value of `-1` represents a `null` child (i.e., an absent node).

---

## Output Format

For each test case, output on a new line the **serialized representation** of the tree after performing:

1. **Deserialize** the given level-order input into a binary tree, and
2. **Serialize** the reconstructed tree again.

The output must match the chosen serialization format and must represent the same tree structure as the input.

---

## Constraints

- $\textbf{Number of nodes in the tree:} $
    $0 \leq n \leq 10^{4}$
- $ \textbf{Node values range:} $
    $-1000 \leq \text{Node.val} \leq 1000$
- $\textbf{Node values will never be equal to -1:} $
- $\textbf{-1 is reserved exclusively for representing null nodes.} $

---

## Examples

**Example 1**

**Input**

```text
3
7
10 6 15 3 8 12 20
5
7 -1 9 -1 8
0
```

**Output**

```text
10 6 15 3 8 12 20
7 -1 9 -1 8
```

**Explanation**

* For the first test case after serializing and deserializing the given binary tree, the structure remains the same as the original.
* For second test case an empty left subtree and partial right subtree are handled correctly by the algorithm.
* For third test case an empty tree should serialize and deserialize to an empty structure.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### 1. Overview

Serialization of a binary tree means converting the tree into a sequence (list of integers) in such a way that the tree can later be reconstructed exactly from that sequence. Deserialization is the reverse process.

In this problem:

1. You're given a tree in **level-order form**, where `-1` represents a null child.
2. You must:

   * Deserialize it into an actual binary tree structure.
   * Serialize the tree back into a sequence.
   * Output the serialized sequence.

There is no restriction on the serialization format as long as the tree can be reconstructed exactly and matches the original.

The most natural choice is to use **level-order traversal** (breadth-first order) with `-1` markers for null children because the input already uses this representation.

---

## 2. Key Idea

Both serialization and deserialization rely on **Breadth-First Search (BFS)**.

### Why BFS?

* Level-order uniquely captures parent-child relationships.
* Using `-1` markers allows representing missing children.
* Reconstruction becomes straightforward because nodes are processed in the same order they appear in the serialized list.

---

## 3. Deserialization Logic

Given an array representing the level-order traversal:

1. The first element is the root.
2. Use a queue to keep track of nodes whose children need to be assigned.
3. For each node pulled from the queue:

   * Take the next value as its left child.
   * Take the next value as its right child.
   * Push non-null children into the queue.

This process continues until we exhaust the array.

### Why it works

Level-order combined with a queue ensures children are attached in correct order. The `-1` values ensure missing nodes are preserved correctly.

---

## 4. Serialization Logic

To serialize the tree:

1. Perform a BFS starting from the root.
2. For each node:

   * Append its value if it exists.
   * Append `-1` if it is null.
3. Push children of every non-null node into the queue.

To prevent unnecessarily long output, remove trailing `-1`s because they correspond to the deepest null pointers, which do not contribute to reconstruction.

### Why removing trailing `-1`s is safe

During deserialization:

* Missing trailing nulls do not affect reconstruction.
* Internal `-1`s remain preserved because they represent actual null children.

---

## 5. Complexity Analysis

Let `n` be the number of nodes in the tree.

### Deserialization

* Each element of the array is processed once.
* BFS ensures O(n) time.
* Space used: O(n) for the queue and nodes.

### Serialization

* Each node and its null children are processed exactly once.
* Time: O(n)
* Space: O(n)

Total per test case: O(n)

This is efficient enough for the constraint `n ≤ 10^4`.

---

## 6. Corner Cases

1. **Empty tree** (`n = 0`)
   Output should be an empty sequence.

2. **Tree with only root**
   Serialization simply returns the single value.

3. **Skewed tree**
   BFS still works because null markers preserve structure.

4. **Trees with many missing children**
   Removal of trailing `-1`s avoids unnecessarily long output.

---

## 7. Why the chosen approach guarantees correctness

* The input format is level-order, so reconstructing using level-order is natural and avoids ambiguity.
* Level-order serialization captures complete structure including null positions.
* BFS ensures that children are linked in proper order.
* The serialized format can re-create the original tree exactly, satisfying the problem requirement.

---

## 8. Summary

This problem is essentially about applying breadth-first traversal to both serialization and deserialization:

* Use BFS to rebuild the tree from the given level-order representation.
* Use BFS again to serialize the tree back into a level-order sequence.
* Remove unnecessary trailing null markers for cleaner output.

The method is efficient, simple to implement, and guarantees perfect reconstruction.

</details>

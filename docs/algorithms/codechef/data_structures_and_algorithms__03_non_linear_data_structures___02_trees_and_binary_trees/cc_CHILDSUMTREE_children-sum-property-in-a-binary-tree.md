# Children sum property in a binary tree

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHILDSUMTREE |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Binary Trees |
| Official Link | [CHILDSUMTREE](https://www.codechef.com/learn/course/trees/BTREESPRO/problems/CHILDSUMTREE) |

---

## Problem Statement

Given the root of a binary tree, determine if every node satisfies the **children sum property**: the value of each node must be equal to the sum of the values of its left and right children.

* If a child is missing $null$, consider its value as $0$.
* Leaf nodes automatically satisfy the property since they have no children.

## Function Name

$isChildrenSum$ – This function determines if every node in a binary tree satisfies the children sum property, where a node's value equals the sum of its left and right children's values.

### Parameters

* $root$ : A pointer to the $TreeNode$ representing the root of the binary tree.

### Return Value

* Returns $true$ if the tree satisfies the children sum property at every node.
* Returns $false$ otherwise.

## Constraints

- $1 \leq T \leq 100$
- $1 \leq n \leq 10^4 \quad (number of nodes) $
- $-10^5 \leq \text{Node.val} \leq 10^5$

---

## Input Format

* The first line contains a single integer $T$, denoting the number of test cases.
* Each test case consists of **two lines of input**:

  * The first line contains a single integer $N$ — the number of nodes in the binary tree.
  * The second line contains $N$ space-separated values representing the **level-order traversal** of the tree.
    Use **`null`** to denote missing children.

---

## Output Format

For each test case, output on a new line:

* $true$  — if the binary tree satisfies the children sum property
* $false$ — otherwise

---

## Constraints

- $1 \leq n \leq 10^4 \quad (number of nodes) $
- $-10^5 \leq \text{Node.val} \leq 10^5$

---

---

## Examples

**Example 1**

**Input**

```text
1
3
8 3 5
```

**Output**

```text
true
```

**Explanation**

* Left child = 3, right child = 5 -> 3 + 5 = 8
* Root node value = 8 -> property holds

**Example 2**

**Input**

```text
1
3
10 4 7
```

**Output**

```text
false
```

**Explanation**

* Left child = 4, right child = 7 -> 4 + 7 = 11
* Root node value = 10 -> property violated

**Example 3**

**Input**

```text
1
7
20 8 12 3 5 6 6
```

**Output**

```text
true
```

**Explanation**

* Node 8 -> 3 + 5 = 8
* Node 12 -> 6 + 6 = 12
* Root 20 -> 8 + 12 = 20 -> all nodes satisfy the property

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### Problem Recap

You are given a binary tree and asked to determine whether **every node** satisfies the **Children Sum Property**:

* The value of a node must equal the sum of its left and right children.
* If a child is missing, its value is considered `0`.
* Leaf nodes automatically satisfy the property.

**Input**: Binary tree in level-order (with `null` or `-1` for missing children).
**Output**: `true` if the property holds for all nodes, else `false`.

---

### Understanding the Problem

1. **Leaf nodes** always satisfy the property because they have no children.
2. **Internal nodes** must satisfy:

$\text{node.val} = (\text{left child value}) + (\text{right child value})$

* If one child is missing, treat it as `0`.
* For example, a node with value `5` and only a left child `5` satisfies the property because right child = 0 → 5 = 5 + 0.

---

### Approach

1. **Recursive solution**:

   * Base case:

     * If the node is `null`, return `true`.
     * If the node is a leaf, return `true`.
   * Recursive case:

     1. Compute left and right child values (treat `null` as `0`).
     2. Check if `node.val == left_val + right_val`.
     3. Recursively check left and right subtrees.
     4. Return `true` only if the current node satisfies the property **and** both subtrees satisfy it.

2. **Time Complexity**:

   * Each node is visited exactly once → O(n), where n = number of nodes.
   * Space Complexity:

     * O(h) for recursion stack in a recursive solution, where h = height of the tree.
     * Worst case (skewed tree) → O(n), Best case (balanced tree) → O(log n).

3. **Iterative solution** (optional):

   * Use level-order traversal with a queue.
   * At each node, check if `node.val == left_val + right_val`.
   * Push children into the queue.
   * If any node fails the property, return `false`.

---

### Edge Cases to Consider

1. **Single node tree** → always `true`.
2. **Tree with missing children** → treat missing child as `0`.
3. **Tree with negative values** → negative numbers are valid.
4. **Large trees** → recursion depth may reach n; iterative approach avoids stack overflow.
5. **Violation at different levels** → property must be checked at **all internal nodes**, not just the root.

---

### Example Walkthrough

**Example 1:**

```
      10
     /  \
    4    6
   / \  / \
  1  3 2  4
```

* Check node `4`: 1 + 3 = 4 → OK
* Check node `6`: 2 + 4 = 6 → OK
* Check root `10`: 4 + 6 = 10 → OK
* All nodes satisfy → **true**

**Example 2:**

```
    1
   / \
  4   3
```

* Root `1`: 4 + 3 = 7 → 1 != 7 → property violated → **false**

---

### Summary

1. The problem is essentially a **tree traversal problem**.
2. Recursively check the property for every node, or do a level-order traversal iteratively.
3. Always consider:

   * Leaf nodes automatically satisfy the property.
   * Missing children = 0.
   * Negative values are allowed.

---

### Key Takeaways

* Recursive solution is simple and elegant.
* Iterative solution is safer for very large trees to avoid stack overflow.
* Edge cases like single node, missing children, and negative values must be handled.
* Time complexity is **O(n)**, and space complexity depends on recursion depth or queue size.

</details>

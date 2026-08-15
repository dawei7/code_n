### 1. Description

Given a **multi-dimensional array** of integers, return a generator object which yields integers in the same order as **inorder traversal**.

A **multi-dimensional array** is a recursive data structure that contains both integers and other **multi-dimensional arrays**.

**inorder traversal** iterates over each array from left to right, yielding any integers it encounters or applying **inorder traversal** to any arrays it encounters.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** `arr = [[[6]],[1,3],[]]`
- **Output:** `[6,1,3]`
- **Explanation:** const generator = inorderTraversal(arr);
generator.next().value; // 6
generator.next().value; // 1
generator.next().value; // 3
generator.next().done; // true

#### Example 2

- **Input:** `arr = []`
- **Output:** `[]`
- **Explanation:** There are no integers so the generator doesn't yield anything.

### 4. Constraints

- $0 \le \text{arr.flat}().length \le 10^{5}$

- $0 \le \text{arr.flat}()[i] \le 10^{5}$

- $maxNestingDepth \le 10^{5}$

**Can you solve this without creating a new flattened version of the array?**

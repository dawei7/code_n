# Implement Heap Sort

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | HEAP09 |
| Difficulty Band | Heaps |
| Path | Data Structures and Algorithms |
| Lesson | Learn Heaps |
| Official Link | [HEAP09](https://www.codechef.com/learn/course/heaps/LIHP02/problems/HEAP09) |

---

## Problem Statement

### Task
Given an array of **N** elements. Sort the array using Heap sort.
Functions for inserting and deleting into the heap are already implemented in the code editor.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $M$ — the number of vertices and edges of the graph, respectively.
    - The next $M$ lines describe the edges. The $i$-th of these $M$ lines contains two space-separated integers $u_i$ and $v_i$, denoting an edge between $u_i$ and $v_i$.

---

## Output Format

For each test case

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 100$
- $1 \leq M \leq N\cdot(N-1)/2$
- $1 \leq u_i, v_i \leq N$
- $u_i \neq v_i$ for each $1 \leq i \leq M$.
- The sum of $N$ over all test cases won't exceed $100$.

---

## Examples

**Example 1**

**Input**

```text
10
1 78 29 48 19 2 17 134 93 13
```

**Output**

```text
1 2 13 17 19 29 48 78 93 134
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Implement Heap Sort](https://www.codechef.com/learn/course/heaps/LIHP02/problems/HEAP09)

### [](#problem-statement-1)Problem Statement:

Given an array of **N** elements. Sort the array using Heap sort.

Functions for inserting and deleting into the heap are already implemented in the code editor.

### [](#approach-2)Approach:

The key idea of this solution is to use a **min-heap**, where the smallest element is always at the root of the heap. This allows us to repeatedly extract the smallest value efficiently. The heap operations used are:

-

**Insertion**: Insert a value and maintain the heap property by bubbling up the newly inserted value.

-

**Deletion**: Remove the smallest element (root), replace it with the last element, and maintain the heap property by bubbling down this element.

-

**Heapify**: Used to restore the heap order after deleting the root.

#### [](#step-by-step-explanation-3)Step-by-Step Explanation:

-

**Heap Class**:

- The heap is represented using a **vector** (`v`) to store elements.

-

**insert(int value)**:

- Insert a value at the end of the vector and maintain the **min-heap** property by comparing the newly added value with its parent and swapping if necessary. This process is called **bubbling up**.

-

**Heapify(int index)**:

- After deleting the root, this function ensures the heap property is maintained by comparing the node at `index` with its children and swapping with the smallest child if needed. This process is called **bubbling down**.

-

**delete_from_heap()**:

- Remove the smallest element (root) by swapping it with the last element and removing the last element. Then, call **Heapify** to maintain the heap structure.

-

**Main Function**:

-

We first read `n` values and insert them into the heap.

-

After that, we repeatedly extract the smallest element from the heap using `delete_from_heap()` and store it in a sorted array.

-

Finally, we print the sorted array.

This approach effectively **sorts** the elements by taking advantage of the heap’s ability to repeatedly extract the smallest value.

### [](#time-complexity-4)Time Complexity:

-

**insert**: **O(log n)** for each insertion due to bubbling up.

-

**delete_from_heap**: **O(log n)** for each deletion due to bubbling down.

-

Overall, for `n` elements, the complexity is **O(n log n)**.

### [](#space-complexity-5)Space Complexity:

- **O(n)** because we use a vector to store the heap of size n.

</details>

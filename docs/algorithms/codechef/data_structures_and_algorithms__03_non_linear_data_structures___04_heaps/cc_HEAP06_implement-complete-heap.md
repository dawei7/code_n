# Implement complete heap

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | HEAP06 |
| Difficulty Band | Heaps |
| Path | Data Structures and Algorithms |
| Lesson | Learn Heaps |
| Official Link | [HEAP06](https://www.codechef.com/learn/course/heaps/LIHP01/problems/HEAP06) |

---

## Problem Statement

Complete the functions **insert()**, **delete_from_heap()** and **heapify()** to implement a min-heap in the code editor.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $M$ — the number of vertices and edges of the graph, respectively.
    - The next $M$ lines describe the edges. The $i$-th of these $M$ lines contains two space-separated integers $u_i$ and $v_i$, denoting an edge between $u_i$ and $v_i$.

---

## Output Format

For each test case, output on a new line the number of good subgraphs of $G$, modulo $10^9 + 7$.

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
insert 8
insert 3
insert 4
insert 1
insert 18
print
delete
print
delete
print
```

**Output**

```text
1 3 4 8 18 
3 8 4 18 
4 8 18
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Implement complete heap](https://www.codechef.com/learn/course/heaps/LIHP01/problems/HEAP06)

### [](#problem-statement-1)Problem Statement:

Complete the functions **insert()**, **delete_from_heap()** and **heapify()** to implement a min-heap in the code editor.

### [](#approach-2)Approach:

The code focuses on basic heap operations: **insertion**, **deletion**, and **reordering** using `Heapify`. A **min-heap** ensures that the parent node is smaller than its child nodes.

#### [](#void-insertint-value-3)`void insert(int value)`:

This function inserts a new value by:

-

**Adding the value** to the end of the internal array `v`.

-

**Reordering upwards**: It compares the inserted element with its parent. If the parent is greater, they are swapped, and the process continues until the correct position is found.

#### [](#void-heapifyint-index-4)`void Heapify(int index)`:

This function restores the heap property after deletion by:

-

**Comparing the current node** with its left and right children.

-

**Swapping** the current node with the smallest child if necessary and recursively applying `Heapify` until the heap is properly ordered.

#### [](#void-delete_from_heap-5)`void delete_from_heap()`:

This function removes the `root` (smallest) element by:

-

**Swapping the root** with the last element and removing the last element.

-

**Calling `Heapify`** on the new `root` to maintain the heap structure.

### [](#time-complexity-6)Time Complexity:

-

**Insert**: **O(log n)** since we may need to traverse up to the root in the worst case.

-

**Heapify**: **O(log n)** as it may recursively adjust nodes down to the leaf level.

-

**Delete**: **O(log n)** because it calls Heapify after removing the `root`.

### [](#space-complexity-7)Space Complexity:

- **O(n)** for storing `n` elements in the heap.

</details>

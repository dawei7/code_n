# Find Kth Largest element

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | HEAP11 |
| Difficulty Band | Heaps |
| Path | Data Structures and Algorithms |
| Lesson | Learn Heaps |
| Official Link | [HEAP11](https://www.codechef.com/learn/course/heaps/LIHP02/problems/HEAP11) |

---

## Problem Statement

### Task
Given an array A and an integer k. Print the Kth Largest element from the array.
A Heap has already been implemented for your convenience.

---

## Input Format

- The first line of input contains two integers $N$ and $K$, denoting the number of elements in the array and the integer K.
- Next line contains $N$ integers of the array.

---

## Output Format

In a single line output the Kth Largest element in the array

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
10 4
1 78 29 48 19 2 17 134 93 13
```

**Output**

```text
48
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Find Kth Largest element](https://www.codechef.com/learn/course/heaps/LIHP02/problems/HEAP11)

### [](#problem-statement-1)Problem Statement:

You are given an array `A` of `n` integers and an integer `k`. The task is to find and print the **k-th largest element** in the array using a **Max Heap**. A Max Heap has already been implemented to help you solve this problem.

### [](#approach-2)Approach:

The key idea of this solution is to use a **Max Heap** to efficiently find the **k-th largest element** in the array. A Max Heap always has the largest element at the top, which helps us extract the largest elements in descending order.

Here’s how the approach works:

-

**Heap Insertion**: Insert each element from the array into the heap using the `insert()` function, maintaining the heap property where the parent is greater than its children.

-

**Remove Largest Elements**: Remove the largest element from the heap `k-1` times using the `delete_from_heap()` function. This ensures that the root of the heap now holds the **k-th largest element**.

-

**Heapify**: After removing an element, `Heapify()` restores the heap property by pushing down the swapped element to its correct position.

-

**Final Output**: The root of the heap now holds the **k-th largest element**, which is printed.

This approach leverages heap properties for efficient extraction of the largest elements.

### [](#time-complexity-3)Time Complexity:

-

**Heap Insertion**: Each insertion takes **O(log n)** time due to bubbling up, so inserting `n` elements takes **O(n log n)**.

-

**Deleting from Heap**: Each deletion also takes **O(log n)** due to bubbling down, so deleting `k-1` elements takes **O(k log n)**.

### [](#space-complexity-4)Space Complexity:

- **O(n)** since we use a heap to store all `n` elements from the array.

</details>

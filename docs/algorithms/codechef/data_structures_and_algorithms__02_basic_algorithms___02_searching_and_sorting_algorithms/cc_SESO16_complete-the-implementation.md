# Complete the implementation

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SESO16 |
| Difficulty Band | Searching and Sorting Algorithms |
| Path | Data Structures and Algorithms |
| Lesson | Sorting |
| Official Link | [SESO16](https://www.codechef.com/learn/course/searching-sorting/SORTSEARCH4/problems/SESO16) |

---

## Problem Statement

Given a bubbleSort function that accepts an array as a parameter, sort the array using the **Bubble sort** algorithm.

**Note:** Do not write code to take input or print output, Only complete the implementation of the bubbleSort function.

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
8
6 5 3 1 8 7 2 4
```

**Output**

```text
1 2 3 4 5 6 7 8
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

[Problem Link](https://www.codechef.com/learn/course/searching-sorting/SORTSEARCH4/problems/SESO16)

Bubble Sort works by repeatedly traversing the array and swapping adjacent elements if they are out of order. The algorithm consists of two nested loops:

- **Outer Loop**: The outer loop runs `n-1` times, where `n` is the number of elements in the array. Each iteration of the outer loop ensures that the largest unsorted element “bubbles up” to its correct position at the end of the array.

- **Inner Loop**: The inner loop compares adjacent elements and swaps them if the current element is greater than the next element. After each pass through the inner loop, the largest element in the unsorted portion of the array moves to its correct position.

- **Optimization**: The inner loop decreases in size with each iteration of the outer loop because the last `i` elements are already sorted after `i` passes.

#### [](#code-explanation-1)Code Explanation
``void bubbleSort(int arr[], int n) {
    // Outer loop for each pass through the array
    for (int i = 0; i < n - 1; i++) {
        // Inner loop to compare and swap adjacent elements
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                // Swap arr[j] and arr[j + 1] if they are in the wrong order
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}
``

#### [](#how-it-works-2)How It Works

- **Initial State**: At the beginning, the array is unsorted.

- **First Pass**: The largest element in the array “bubbles up” to the last position after the first pass through the array.

- **Subsequent Passes**: With each subsequent pass, the next largest unsorted element moves to its correct position. As a result, after `i` passes, the last `i` elements of the array are sorted.

- **Termination**: The algorithm stops after `n-1` passes because, at this point, all elements are in their correct positions.

#### [](#complexity-analysis-3)Complexity Analysis

- **Time Complexity**: The time complexity of Bubble Sort in the worst and average cases is O(n^2), where `n` is the number of elements in the array. This is because the algorithm uses two nested loops, each iterating over the array. In the best case, when the array is already sorted, the time complexity can be reduced to O(n) if an optimization is applied to detect no swaps during a pass, allowing for an early termination.

- **Space Complexity**: The space complexity is O(1) because Bubble Sort is an in-place sorting algorithm, meaning it requires only a constant amount of additional space.

</details>

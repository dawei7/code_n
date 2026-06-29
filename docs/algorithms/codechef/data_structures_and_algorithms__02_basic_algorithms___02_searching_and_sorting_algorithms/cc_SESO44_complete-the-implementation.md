# Complete the implementation

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SESO44 |
| Difficulty Band | Searching and Sorting Algorithms |
| Path | Data Structures and Algorithms |
| Lesson | Sorting |
| Official Link | [SESO44](https://www.codechef.com/learn/course/searching-sorting/SORTSEARCH8/problems/SESO44) |

---

## Problem Statement

Given a quickSort function that accepts an array as a parameter, sort the array using the **Quick sort** algorithm.

### Video Explanation

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

[Problem Link](https://www.codechef.com/learn/course/searching-sorting/SORTSEARCH8/problems/SESO44)

Quick Sort is an efficient, in-place, and widely-used sorting algorithm that follows the divide-and-conquer paradigm. The key idea behind Quick Sort is to select a “pivot” element from the array and partition the other elements into two sub-arrays according to whether they are less than or greater than the pivot. The sub-arrays are then recursively sorted. Quick Sort is known for its average-case time complexity of O(n log n) and its ability to sort in-place without requiring additional memory.

Quick Sort works by recursively partitioning the array and sorting the partitions. Here’s a breakdown of the core components of Quick Sort:

-

**Partitioning**:

- The partition function is at the heart of Quick Sort. It selects a pivot element (in this implementation, the last element of the array) and rearranges the array such that all elements less than the pivot are moved to its left, and all elements greater than the pivot are moved to its right.

- The function then returns the index of the pivot element, which is now in its correct position in the sorted array.

-

**Recursive Sorting**:

- After partitioning, the Quick Sort function is called recursively on the sub-arrays to the left and right of the pivot. These recursive calls continue until the base case is reached (i.e., when the sub-array has one or no elements, which is inherently sorted).

-

**Swapping**:

- The `swap` function is used within the partitioning process to exchange elements in the array. This helps in placing elements smaller than the pivot to its left and larger ones to its right.

#### [](#code-explanation-1)Code Explanation
``// Function to swap elements
void swap(vector<int>& arr, int i, int j) {
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}

// Partition function
int partition(vector<int>& arr, int low, int high) {
    int pivot = arr[high];  // Pivot is the last element
    int i = low - 1;  // Index of the smaller element

    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {  // If current element is smaller than the pivot
            i++;
            swap(arr, i, j);  // Swap it with the element at i
        }
    }
    swap(arr, i + 1, high);  // Place the pivot in the correct position
    return i + 1;  // Return the partition index
}

// Quick sort function
void quickSort(vector<int>& arr, int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);  // Partition the array
        quickSort(arr, low, pi - 1);  // Recursively sort the left sub-array
        quickSort(arr, pi + 1, high);  // Recursively sort the right sub-array
    }
}
``

#### [](#how-it-works-2)How It Works

-

**Pivot Selection**: The last element of the array segment is chosen as the pivot. While other pivot selection strategies exist, such as choosing the first element, middle element, or even a random element, the choice of pivot can significantly affect the performance of Quick Sort.

-

**Partitioning Process**: The array is partitioned around the pivot:

- Elements less than the pivot are moved to the left of the pivot.

- Elements greater than the pivot are moved to the right.

- The pivot is then placed in its correct sorted position.

-

**Recursion**: The array is recursively divided into sub-arrays and sorted. The base case for the recursion is when the sub-array has only one or no elements, at which point no further sorting is necessary.

#### [](#complexity-analysis-3)Complexity Analysis

-

**Time Complexity**:

- **Average Case**: O(n log n), where `n` is the number of elements in the array. This occurs when the pivot divides the array into two roughly equal halves.

- **Worst Case**: O(n^2), which can occur if the pivot chosen is the smallest or largest element repeatedly, resulting in highly unbalanced partitions. This is mitigated in practice by choosing better pivot selection strategies (e.g., random pivot).

-

**Space Complexity**: O(log n) for the recursive stack space. Quick Sort is an in-place sorting algorithm, meaning it requires only a small amount of extra memory space for recursion, making it memory efficient.

</details>

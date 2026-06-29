# Complete the implementation

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SESO42 |
| Difficulty Band | Searching and Sorting Algorithms |
| Path | Data Structures and Algorithms |
| Lesson | Sorting |
| Official Link | [SESO42](https://www.codechef.com/learn/course/searching-sorting/SORTSEARCH6/problems/SESO42) |

---

## Problem Statement

Given a insertionSort function that accepts an array as a parameter, sort the array using the **Insertion sort** algorithm.

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

[Problem Link](https://www.codechef.com/learn/course/searching-sorting/SORTSEARCH6/problems/SESO42)

The Insertion Sort algorithm works by iterating through the array and, for each element, inserting it into the correct position relative to the already sorted portion of the array. The process can be described as follows:

-

**Outer Loop**: The algorithm starts with the second element (index 1) because the single element at index 0 is trivially sorted. The outer loop iterates from the second element to the last element in the array.

-

**Key Element**: For each iteration of the outer loop, the current element (`arr[i]`) is considered the “key” element. This key element needs to be placed in the correct position within the sorted portion of the array (i.e., the part of the array before index `i`).

-

**Inner Loop**: The inner loop scans the sorted portion of the array from right to left, comparing each element with the key. If an element is greater than the key, it is shifted one position to the right. This continues until the correct position for the key is found.

-

**Insertion**: Once the correct position is found (i.e., when no more elements in the sorted portion are greater than the key), the key is inserted into its correct position.

-

**Repeat**: The process is repeated for each element in the array, progressively growing the sorted portion until the entire array is sorted.

#### [](#code-explanation-1)Code Explanation
``void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];  // Store the current element as key
        int j = i - 1;

        // Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        // Insert the key at its correct position
        arr[j + 1] = key;
    }
}
``

#### [](#how-it-works-2)How It Works

- **Initial Step**: The algorithm starts by assuming that the first element is sorted by default. It then takes the second element as the key and compares it with the elements in the sorted portion to find its correct position.

- **Shifting**: Elements in the sorted portion that are greater than the key are shifted to the right to make room for the key.

- **Insertion**: The key is inserted into the correct position, extending the sorted portion of the array by one element.

#### [](#complexity-analysis-3)Complexity Analysis

-

**Time Complexity**: The time complexity of Insertion Sort in the worst and average cases is O(n^2), where `n` is the number of elements in the array. This occurs when the array is sorted in reverse order. However, in the best case, when the array is already sorted, the time complexity is O(n) because the inner loop does not perform any shifts.

-

**Space Complexity**: The space complexity is O(1), as Insertion Sort is an in-place sorting algorithm that requires only a constant amount of additional memory beyond the input array.

</details>

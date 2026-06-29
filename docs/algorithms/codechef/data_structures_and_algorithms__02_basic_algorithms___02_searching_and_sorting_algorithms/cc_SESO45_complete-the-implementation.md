# Complete the implementation

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SESO45 |
| Difficulty Band | Searching and Sorting Algorithms |
| Path | Data Structures and Algorithms |
| Lesson | Sorting |
| Official Link | [SESO45](https://www.codechef.com/learn/course/searching-sorting/SORTSEARCH9/problems/SESO45) |

---

## Problem Statement

Given a countSort function that accepts an array as a parameter, sort the array using the **count sort** algorithm.

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

[Problem Link](https://www.codechef.com/learn/course/searching-sorting/SORTSEARCH9/problems/SESO45)

Counting Sort is a non-comparative sorting algorithm that sorts integers in linear time, given a fixed range of integer values. Unlike comparison-based algorithms such as Quick Sort or Merge Sort, Counting Sort leverages the distribution of values within the input array to achieve its efficiency. This makes it particularly useful for sorting arrays with a limited range of integer values.

#### [](#approach-1)Approach

Counting Sort works by counting the occurrences of each unique value in the input array and then using this information to place each value in its correct position in the sorted array. The approach can be broken down into the following steps:

-

**Initialization**:

- First, the algorithm identifies the maximum value (`max_val`) in the array. This value determines the size of the counting array, `count`, which tracks the frequency of each value in the input array.

-

**Counting Occurrences**:

- The algorithm then iterates over the input array and increments the corresponding index in the `count` array for each value encountered. The `count` array essentially records the number of times each value appears in the input array.

-

**Reconstructing the Sorted Array**:

- Finally, the algorithm iterates through the `count` array and reconstructs the sorted array. For each value in the `count` array with a non-zero count, the value is placed in the output array in the correct order based on its frequency.

#### [](#code-explanation-2)Code Explanation
``void countingSort(vector<int>& arr) {
    if (arr.empty()) return;  // Edge case: If the array is empty, there's nothing to sort

    // Find the maximum value in the array
    int max_val = *max_element(arr.begin(), arr.end());

    // Create a count array to store the frequency of each value
    vector<int> count(max_val + 1, 0);

    // Count the occurrences of each value in the array
    for (int num : arr) {
        count[num]++;
    }

    // Reconstruct the sorted array using the count array
    int sorted_index = 0;
    for (int i = 0; i <= max_val; ++i) {
        while (count[i] > 0) {
            arr[sorted_index++] = i;
            count[i]--;
        }
    }
}
``

#### [](#how-it-works-3)How It Works

-

**Counting Occurrences**: The core idea of Counting Sort is to count the number of occurrences of each integer in the input array. This is done using the `count` array, where the index represents the integer value, and the value at each index represents the frequency of that integer in the input array.

-

**Reconstructing the Array**: After counting the occurrences, the algorithm reconstructs the sorted array by iterating through the `count` array. For each index `i` in the `count` array, if `count[i]` is greater than zero, `i` is placed into the sorted array as many times as `count[i]` indicates.

#### [](#complexity-analysis-4)Complexity Analysis

-

**Time Complexity**: The time complexity of Counting Sort is O(n + k), where `n` is the number of elements in the input array, and `k` is the range of the input (i.e., the difference between the maximum and minimum values). This makes Counting Sort highly efficient for cases where `k` is not significantly larger than `n`.

-

**Space Complexity**: The space complexity of Counting Sort is O(k), where `k` is the range of the input values. This space is used to store the `count` array. Additionally, the space for the output array is O(n), but since the sorting is done in-place in this implementation, the extra space required is mainly for the `count` array.

</details>

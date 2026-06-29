# Complete the implementation

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SESO41 |
| Difficulty Band | Searching and Sorting Algorithms |
| Path | Data Structures and Algorithms |
| Lesson | Sorting |
| Official Link | [SESO41](https://www.codechef.com/learn/course/searching-sorting/SORTSEARCH5/problems/SESO41) |

---

## Problem Statement

Given a selectionSort function that accepts an array as a parameter, sort the array using the **Selection sort** algorithm.

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

[Problem Link](https://www.codechef.com/learn/course/searching-sorting/SORTSEARCH5/problems/SESO41)

Selection Sort works by dividing the array into two parts: a sorted section and an unsorted section. Initially, the sorted section is empty, and the unsorted section contains all the elements. The algorithm proceeds as follows:

-

**Outer Loop**: The outer loop iterates over each element of the array, treating the current element as the first unsorted element.

-

**Finding the Minimum**: For each position in the outer loop, an inner loop is used to search through the unsorted portion of the array to find the index of the minimum element (`minIdx`).

-

**Swapping**: After finding the minimum element in the unsorted section, it is swapped with the first unsorted element (the current element of the outer loop). This effectively moves the minimum element into the sorted section of the array.

-

**Progression**: The algorithm continues, reducing the size of the unsorted section by one with each iteration of the outer loop until the entire array is sorted.

#### [](#code-explanation-1)Code Explanation
``void selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;
        // Find the minimum element in the unsorted portion of the array
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIdx]) {
                minIdx = j;
            }
        }
        // Swap the found minimum element with the first unsorted element
        int temp = arr[minIdx];
        arr[minIdx] = arr[i];
        arr[i] = temp;
    }
}
``

#### [](#how-it-works-2)How It Works

- **Initial Step**: The algorithm starts by considering the first element as the minimum and iterates through the rest of the array to find the actual minimum element.

- **Swapping**: Once the minimum element is found, it is swapped with the first unsorted element, effectively moving it to its correct position in the sorted portion.

- **Subsequent Steps**: The process is repeated for the next element in the array until the entire array is sorted.

#### [](#complexity-analysis-3)Complexity Analysis

-

**Time Complexity**: The time complexity of Selection Sort is O(n^2), where `n` is the number of elements in the array. This is because for each element, the algorithm scans the remaining unsorted elements to find the minimum.

-

**Space Complexity**: The space complexity is O(1) since Selection Sort is an in-place sorting algorithm, requiring no additional space beyond the input array and a few auxiliary variables.

</details>

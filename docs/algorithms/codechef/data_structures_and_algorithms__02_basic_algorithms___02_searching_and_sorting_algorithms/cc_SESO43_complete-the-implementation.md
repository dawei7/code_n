# Complete the implementation

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SESO43 |
| Difficulty Band | Searching and Sorting Algorithms |
| Path | Data Structures and Algorithms |
| Lesson | Sorting |
| Official Link | [SESO43](https://www.codechef.com/learn/course/searching-sorting/SORTSEARCH7/problems/SESO43) |

---

## Problem Statement

Given a mergeSort function that accepts an array as a parameter, sort the array using the **Merge sort** algorithm.

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

[Problem Link](https://www.codechef.com/learn/course/searching-sorting/SORTSEARCH7/problems/SESO43)

Merge Sort is a classic, efficient, and stable comparison-based sorting algorithm that follows the divide-and-conquer paradigm. The core idea of Merge Sort is to divide the input array into smaller subarrays, sort these subarrays, and then merge them back together to form a sorted array.

Merge Sort operates by recursively splitting the array into two halves until each subarray contains only one element (which is trivially sorted). After reaching this base case, the algorithm begins to merge the subarrays back together in a sorted order. Here’s how it works step-by-step:

-

**Divide**:

- The array is recursively divided into two halves. This is done by calculating the middle index (`mid`) of the current segment of the array. The left half is from the start index (`left`) to `mid`, and the right half is from `mid + 1` to the end index (`right`).

-

**Conquer (Sort)**:

- Once the array is divided into single-element subarrays, the merge step starts. Each subarray is already sorted (since it contains only one element), so the merge process can begin.

-

**Merge**:

- The `merge` function is responsible for combining two sorted subarrays into a single sorted array. The process involves:

- **Copying Subarrays**: First, the left and right subarrays are copied into temporary vectors `a` and `b`.

- **Merging**: Two pointers (`i` and `j`) are used to traverse the `a` and `b` vectors. The smaller of the two pointed-to elements is appended to the result vector `res`. This continues until all elements from either `a` or `b` have been added to `res`.

- **Appending Remaining Elements**: If one of the vectors still has remaining elements, they are directly appended to `res` since they are already sorted.

- **Copying Back**: Finally, the sorted elements from `res` are copied back into the original array, replacing the original unsorted elements.

#### [](#code-explanation-1)Code Explanation
``void merge(vector<int> &arr, int left, int middle, int right) {
    vector<int> a, b;

    // Copy left half to a
    for (int i = left; i <= middle; i++) {
        a.push_back(arr[i]);
    }

    // Copy right half to b
    for (int i = middle + 1; i <= right; i++) {
        b.push_back(arr[i]);
    }

    int i = 0, j = 0;
    vector<int> res;

    // Merge the two halves back into res
    while (i < a.size() && j < b.size()) {
        if (a[i] < b[j]) {
            res.push_back(a[i]);
            i++;
        } else {
            res.push_back(b[j]);
            j++;
        }
    }

    // Add remaining elements from a
    while (i < a.size()) {
        res.push_back(a[i]);
        i++;
    }

    // Add remaining elements from b
    while (j < b.size()) {
        res.push_back(b[j]);
        j++;
    }

    // Copy the sorted result back into the original array
    for (int k = 0; k < res.size(); k++) {
        arr[left + k] = res[k];
    }
}

void mergeSort(vector<int> &arr, int left, int right) {
    if (left < right) {
        int mid = (left + right) / 2;
        mergeSort(arr, left, mid);       // Sort the left half
        mergeSort(arr, mid + 1, right);  // Sort the right half
        merge(arr, left, mid, right);    // Merge the sorted halves
    }
}
``

#### [](#how-it-works-2)How It Works

- **Recursive Splitting**: The `mergeSort` function splits the array into smaller and smaller subarrays by recursively calling itself until each subarray contains a single element.

- **Merging**: The `merge` function then takes two sorted subarrays and merges them into a single sorted array. This is the critical step where the actual sorting happens.

#### [](#complexity-analysis-3)Complexity Analysis

-

**Time Complexity**: The time complexity of Merge Sort is O(n log n), where `n` is the number of elements in the array. The `n log n` arises because:

- The array is split `log n` times (since each split halves the array).

- Each merge operation takes O(n) time to combine the elements.

-

**Space Complexity**: The space complexity is O(n) due to the additional space used by the temporary vectors `a`, `b`, and `res`. These vectors are necessary for storing the elements during the merging process.

</details>

# Complete the implementation

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SESO46 |
| Difficulty Band | Searching and Sorting Algorithms |
| Path | Data Structures and Algorithms |
| Lesson | Sorting |
| Official Link | [SESO46](https://www.codechef.com/learn/course/searching-sorting/SORTSEARCH10/problems/SESO46) |

---

## Problem Statement

Given a radixSort function that accepts an array as a parameter, sort the array using the **Radix sort** algorithm.

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

[Problem Link](https://www.codechef.com/learn/course/searching-sorting/SORTSEARCH10/problems/SESO46)

Radix Sort is a non-comparative, integer sorting algorithm that sorts numbers by processing individual digits. Unlike other sorting algorithms, such as Quick Sort or Merge Sort, Radix Sort works by sorting numbers digit by digit, starting from the least significant digit (LSD) to the most significant digit (MSD). It leverages Counting Sort as a subroutine to sort numbers based on individual digits.

#### [](#approach-1)Approach

Radix Sort works by sorting the numbers in the array based on each digit, starting from the least significant digit (units place) to the most significant digit. The core of the approach involves the following steps:

-

**Finding the Maximum Number**:

- First, determine the maximum number in the array. The number of digits in this maximum number will determine the number of passes (iterations) the algorithm needs to perform.

-

**Sorting by Each Digit**:

- For each digit place (units, tens, hundreds, etc.), the algorithm uses Counting Sort to sort the array based on that specific digit. Counting Sort is chosen because it is a stable, linear-time sorting algorithm that works efficiently when sorting digits.

- The sorting is performed starting from the least significant digit and moving towards the most significant digit. This ensures that the array remains sorted with respect to the lower-order digits when sorting by higher-order digits.

-

**Iterating for Each Digit**:

- The process of digit-wise sorting is repeated until all digits have been processed. For example, if the maximum number in the array has three digits, the array will be sorted three times—once for each digit.

#### [](#code-explanation-2)Code Explanation
``// Function to get the maximum value in the array
int getMax(vector<int>& arr) {
    return *max_element(arr.begin(), arr.end());
}

// Counting Sort function to sort based on a specific digit (exp)
void countingSort(vector<int>& arr, int exp) {
    int n = arr.size();
    vector<int> output(n);
    int count[10] = {0};  // Since we're dealing with digits (0-9), we use a fixed array of size 10

    // Count the occurrences of each digit in the given place (exp)
    for (int i = 0; i < n; ++i) {
        count[(arr[i] / exp) % 10]++;
    }

    // Compute cumulative count to determine positions
    for (int i = 1; i < 10; ++i) {
        count[i] += count[i - 1];
    }

    // Build the output array using the count array
    for (int i = n - 1; i >= 0; --i) {
        output[count[(arr[i] / exp) % 10] - 1] = arr[i];
        count[(arr[i] / exp) % 10]--;
    }

    // Copy the sorted array back to the original array
    for (int i = 0; i < n; ++i) {
        arr[i] = output[i];
    }
}

// Radix Sort function
void radixSort(vector<int>& arr) {
    // Find the maximum number to determine the number of digits
    int max_val = getMax(arr);

    // Perform counting sort for every digit. exp is 10^i (i.e., 1, 10, 100, ...)
    for (int exp = 1; max_val / exp > 0; exp *= 10) {
        countingSort(arr, exp);
    }
}
``

#### [](#how-it-works-3)How It Works

-

**Digit-by-Digit Sorting**:

- The `countingSort` function is applied to each digit place (`exp`). For example, when `exp = 1`, the function sorts the array by the units place; when `exp = 10`, it sorts by the tens place, and so on.

-

**Stability**:

- Counting Sort, used within Radix Sort, is a stable sorting algorithm. This means that numbers with the same digit in the current place retain their relative order from the previous digit’s sort. This stability is crucial for Radix Sort to function correctly.

-

**Iteration**:

- The loop in the `radixSort` function continues until all digits of the maximum number have been processed. This ensures that the array is fully sorted by the time the loop completes.

#### [](#complexity-analysis-4)Complexity Analysis

-

**Time Complexity**:

- The time complexity of Radix Sort is O(nk), where `n` is the number of elements in the array, and `k` is the number of digits in the maximum number. Since `k` is typically much smaller than `n`, Radix Sort is often considered to have linear time complexity, making it efficient for large datasets.

-

**Space Complexity**:

- The space complexity of Radix Sort is O(n + k), where `n` is for the output array used in Counting Sort, and `k` is the fixed size of the counting array (which is 10 in the case of base-10 numbers).

</details>

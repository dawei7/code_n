# Merge two sorted arrays

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MERGESORTED |
| Difficulty Rating | 1050 |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [MERGESORTED](https://www.codechef.com/practice/course/arrays/ARRAYSPRO/problems/MERGESORTED) |

---

## Problem Statement

You are given two sorted arrays $A$ and $B$ of size $N$ and $M$ respectively. You need to merge these two arrays and keep the final array sorted.

---

## Input Format

- The first line contains two integers $N$ and $M$ — the size of array $A$ and $B$
- The second line contains all the elements of array $A$
- The third line contains all the elements of array $B$

---

## Output Format

Output the merged array elements on a single line.

---

## Constraints

- $1 \leq N, M \leq 10^5$
- $1 \leq A_i, B_i \leq 10^5$

---

## Examples

**Example 1**

**Input**

```text
5 4
1 4 8 9 10
2 3 5 6
```

**Output**

```text
1 2 3 4 5 6 8 9 10
```

**Example 2**

**Input**

```text
1 2
10
1 2
```

**Output**

```text
1 2 10
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites**:- Reccursion

**Problem** :- Given two sorted arrays A and B of sizes N and M respectively, the task is to merge these two arrays while maintaining the final array sorted.

**Approach**:

To solve this problem use the concept of merging two sorted arrays similar to the merge step of Merge Sort.

**Algorithm**:

Initialize an empty array, let’s call it merged_array, to store the merged result.

Initialize two pointers, i and j, to iterate through arrays A and B respectively.

Compare the elements at indices i and j in arrays A and B respectively.

Append the smaller element to the merged_array.

Increment the corresponding pointer (i or j) of the smaller element.

Repeat steps 3-5 until one of the arrays (A or B) is completely traversed.

After reaching the end of one of the arrays, append the remaining elements of the other array to the merged_array.

Return the merged_array.

**Solution** :-

**C++ Solution** : -

``#include <iostream>
#include <vector>
using namespace std;

void mergeArrays(const vector<int>& a, const vector<int>& b) {
    int n = a.size(), m = b.size();
    int i = 0, j = 0;
    while (i < n && j < m) {
        if (a[i] < b[j]) cout << a[i++] << " ";
        else cout << b[j++] << " ";
    }
    while (i < n) cout << a[i++] << " ";
    while (j < m) cout << b[j++] << " ";
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<int> a(n), b(m);
    for (int& ai : a) cin >> ai;
    for (int& bi : b) cin >> bi;

    mergeArrays(a, b);
    return 0;
}

``

</details>

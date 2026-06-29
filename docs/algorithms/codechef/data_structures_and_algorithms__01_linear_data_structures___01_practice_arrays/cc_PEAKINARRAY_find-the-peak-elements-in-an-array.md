# Find the peak elements in an array

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PEAKINARRAY |
| Difficulty Rating | 950 |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [PEAKINARRAY](https://www.codechef.com/practice/course/arrays/ARRAYSPRO/problems/PEAKINARRAY) |

---

## Problem Statement

Given an array `A` of size `N`, your task is to find and print all the peak elements in the array. A peak element is one that is strictly greater than its neighboring elements. For the first and last elements, only consider their single adjacent element.

If no peak element exists in the array, print `-1`.

---

## Input Format

- The first line contains the integer $N$ — the size of array
- The second line contains all the elements of array $A$

---

## Output Format

Output all the peak elements in the array in the order they are present in the original array.

---

## Constraints

- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^5$

---

## Examples

**Example 1**

**Input**

```text
5
1 2 4 3 1
```

**Output**

```text
4
```

**Explanation**

1 is smaller than it's adjacent element 2.\
2 is greater than 1 but smaller than 4.\
4 is greater than both 2 and 3, thus it is a **peak** element.\
Again 3 and 1 are also smaller than their adjacent elements.\
Thus the output is only 4.

**Example 2**

**Input**

```text
5
7 3 5 2 10
```

**Output**

```text
7 5 10
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites**:- None

**Problem** :- Given an array A of size N, find and print all the peak elements in the array. A peak element is one which is strictly greater than any of its adjacent elements.

If there is no peak element in an array, print -1.

**Explanation** :-

Iterate over each element of the array and print it if the element is greater than its left and right adjacent elements. If you don’t find any such element, print -1.

**Solution :-**

**C++ Solution : -**

``#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> A(n);

    // Input array elements
    for(int i = 0; i < n; i++) {
        cin >> A[i];
    }

    bool hasPeak = false;

    for(int i = 0; i < n; i++) {
        if((i == 0 || A[i] > A[i-1]) && (i == n-1 || A[i] > A[i+1])) {
            cout << A[i] << " ";
            hasPeak = true;
        }
    }

    if(!hasPeak) {
        cout << "-1";
    }

    return 0;
}

``

</details>

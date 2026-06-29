# Good subarrays

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREFPRO3 |
| Difficulty Band | Prefix Sum Problems |
| Path | Data Structures and Algorithms |
| Lesson | Prefix and Suffix Sum |
| Official Link | [PREFPRO3](https://www.codechef.com/practice/course/prefix-sums/PREFIXSUMS/problems/PREFPRO3) |

---

## Problem Statement

You are given an array $A_1$, $A_2$, . . ., $A_N$ consisting of $N$ integers.

A subarray $A_l$, $A_{l+1}$, $A_{l+2}$, . . ., $A_{r−1}$, $A_r$ is good if the sum of elements of this subarray is equal to an integer $K$.

Find the number of good subarrays present in the array.

---

## Input Format

- The first line of input will contain two integers $N$ and $K$, $N$ denoting the length of the array and $K$ denoting the sum for a good subarray.
- The second line of input will contain $N$ integers $A_1$, $A_2$, . . . $A_N$.

---

## Output Format

For each test case, output on a new line the number of good subgraphs of $G$, modulo $10^9 + 7$.

---

## Constraints

- $1 \leq N \leq 5000$
- $1 \leq K \leq 5000$
- $1 \leq A_i \leq 10^5$

---

## Examples

**Example 1**

**Input**

```text
3 1
1 1 3
```

**Output**

```text
2
```

**Explanation**

The sum of the elements in all the different sub-arrays are as follows:

- Sum of $[A_1]$ is $1$.
- Sum of $[A_1, A_2]$ is $2$.
- Sum of $[A_1, A_2, A_3]$ is $5$.
- Sum of $[A_2]$ is $1$.
- Sum of $[A_2, A_3]$ is $4$.
- Sum of $[A_3, A_3]$ is $3$.

As we can see, among all the sub-arrays, only the sub-arrays $[A_1]$ and $[A_2]$ have a sum equal to $K$. So the answer is $2$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisite** :- Prefix Sum.

**Explanation** :-

Check over each subarray, whether it is a good subarray or not.

Logic1 :-

A total (N * ( N+1 ) ) / 2 subarrays are possible in an array.

Sum of a subarray can be found by Iterating over a subarray, which will cost us around ~O(N) time.

Iterating over each subarray, make the time complexity ~ O(N3)

Logic2 :-

Finding the sum of a subarray can be optimized from O(N) to O(1) using a prefix array.

Time complexity using prefix sum ~ O(N2)

**C++ Solution** :-

``#include <bits/stdc++.h>
using namespace std;

int main() {
    // your code goes here
    int n, k;
    cin >> n >> k;
    vector < int > v1;
    for (int i = 0; i < n; i++) {
        int n1;
        cin >> n1;
        v1.push_back(n1);
    }
    vector < int > pre(n, 0);
    for (int i = 0; i < n; i++) {
        if (i != 0) {
            pre[i] += pre[i - 1];
        }
        pre[i] += v1[i];
    }
    int fans = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            if (i == j) {
                if (v1[i] == k) fans++;
            }
            else {
                if (i == 0) {
                    if (pre[j] == k) {
                        fans++;
                    }
                }
                else if(pre[j] - pre[i-1] == k){
                    fans++;
                }
            }
        }
    }
    cout << fans << "\n";
}

``

</details>

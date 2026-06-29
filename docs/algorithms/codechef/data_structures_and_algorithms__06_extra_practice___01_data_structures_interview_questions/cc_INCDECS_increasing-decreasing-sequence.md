# Increasing-Decreasing Sequence

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | INCDECS |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Binary Search |
| Official Link | [INCDECS](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_06/problems/INCDECS) |

---

## Problem Statement

You are given a sequence $A_1, A_2, \ldots, A_N$. You need to find the maximum length of a subsequence of $A$ whose elements first strictly increase and then strictly decrease in value. Note that subsequences that are only strictly increasing and subsequences that are only strictly decreasing are considered as well.

A subsequence of a given sequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the order of the remaining elements.

---

## Input Format

- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.

- The first line of each test case contains an integer $N$.

- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

---

## Output Format

- For each test case, print a single line containing one integer ― the maximum length of a subsequence of the sequence $A$ which is first strictly increasing and then strictly increasing.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 2 \cdot 10^{5}$
- the sum of $N$ over all test cases does not exceed $2 \cdot 10^{5}$
- $1 \leq A_i \leq 10^9$ for each valid $i$

---

## Examples

**Example 1**

**Input**

```text
4
9
1 2 3 1 4 1 3 2 1
5
2 4 3 6 3
4
1 2 3 4
5
9 9 9 9 9
```

**Output**

```text
7
4
4
1
```

**Explanation**

**Example case 1:** The longest suitable subsequence is $[1,2,3,4,3,2,1]$.

**Example case 2:** The longest suitable subsequence is $[2,4,6,3]$.

**Example case 3:** Although it is only strictly increasing, the longest suitable subsequence is $[1,2,3,4]$.

**Example case 4:** The longest suitable subsequence is $[9]$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
9
1 2 3 1 4 1 3 2 1
```

**Output for this case**

```text
7
```



#### Test case 2

**Input for this case**

```text
5
2 4 3 6 3
```

**Output for this case**

```text
4
```



#### Test case 3

**Input for this case**

```text
4
1 2 3 4
```

**Output for this case**

```text
4
```



#### Test case 4

**Input for this case**

```text
5
9 9 9 9 9
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this lesson, we address the problem of finding the length of the longest subsequence in an array that first strictly increases and then strictly decreases. Remember that a subsequence can be extracted by deleting zero or more elements without changing the order of the remaining ones. Additionally, note that a subsequence that is entirely increasing or entirely decreasing is also allowed.

A common way to tackle this problem is to decompose it into two parts:
1. Find the length of the longest strictly increasing subsequence ending at each index.
2. Find the length of the longest strictly decreasing subsequence starting at each index.

If we denote these lengths as $dp_{inc}[i]$ and $dp_{dec}[i]$ respectively, then the answer for each index $i$ (when used as the peak element) is:
$$
dp_{inc}[i] + dp_{dec}[i] - 1
$$
We subtract 1 because the peak element is counted twice. The final answer is the maximum value among all indices.

Below, we discuss an efficient $O(N \log N)$ dynamic programming solution using a Fenwick Tree (Binary Indexed Tree). This technique is highly efficient for large inputs.

#### Overview

1. **Coordinate Compression:**
   Since the array values can be as large as $10^9$, we first map them to a smaller range.

2. **DP for Increasing Subsequence:**
   Process the array from left to right. For each element, using its compressed value $idx$, you query the Fenwick Tree for the maximum $dp$ among all indices with a value less than $idx$, then set:
   $$
   dp_{inc}[i] = \text{query}(idx - 1) + 1
   $$
   After computing this, update the Fenwick Tree at index $idx$ with the new $dp$ value.

3. **DP for Decreasing Subsequence:**
   Process the sequence in reverse (from right to left) using a similar approach with a separate Fenwick Tree.

4. **Combine:**
   The final answer is the maximum over all indices of $dp_{inc}[i] + dp_{dec}[i] - 1$.

This method runs in $O(N \log N)$ time and is particularly well-suited for competitive programming and large input sizes.

#### C++ Implementation

```cpp
#include
using namespace std;

struct Fenw {
    int n;
    vector fenw;
    Fenw(int n): n(n), fenw(n + 1, 0) {}
    void update(int i, int val) {
        for (; i <= n; i += i & -i)
            fenw[i] = max(fenw[i], val);
    }
    int query(int i) {
        int res = 0;
        for (; i > 0; i -= i & -i)
            res = max(res, fenw[i]);
        return res;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int N;
        cin >> N;
        vector A(N);
        for (int i = 0; i < N; i++)
            cin >> A[i];

        // Coordinate compression
        vector comp = A;
        sort(comp.begin(), comp.end());
        comp.erase(unique(comp.begin(), comp.end()), comp.end());
        auto getIndex = [&](int x) {
            return (int)(lower_bound(comp.begin(), comp.end(), x) - comp.begin()) + 1;
        };
        int m = comp.size();

        vector dp_inc(N, 0), dp_dec(N, 0);

        // Compute dp_inc using Fenw
        Fenw fenw(m);
        for (int i = 0; i < N; i++) {
            int idx = getIndex(A[i]);
            int best = fenw.query(idx - 1);
            dp_inc[i] = best + 1;
            fenw.update(idx, dp_inc[i]);
        }

        // Compute dp_dec using Fenw (processing in reverse)
        Fenw fenw2(m);
        for (int i = N - 1; i >= 0; i--) {
            int idx = getIndex(A[i]);
            int best = fenw2.query(idx - 1);
            dp_dec[i] = best + 1;
            fenw2.update(idx, dp_dec[i]);
        }

        int ans = 0;
        for (int i = 0; i < N; i++)
            ans = max(ans, dp_inc[i] + dp_dec[i] - 1);

        cout << ans << "\n";
    }
    return 0;
}
```

#### Python Implementation

```python
def solve():
    import sys
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))

        # Coordinate Compression
        comp = sorted(set(A))
        comp_index = {x: i + 1 for i, x in enumerate(comp)}
        m = len(comp)

        # Fenwick Tree for dp_inc
        fenw = [0] * (m+1)
        dp_inc = [0] * N

        def fenw_update(i, val):
            while i <= m:
                fenw[i] = max(fenw[i], val)
                i += i & -i

        def fenw_query(i):
            s = 0
            while i:
                s = max(s, fenw[i])
                i -= i & -i
            return s

        for i in range(N):
            idx = comp_index[A[i]]
            best = fenw_query(idx - 1)
            dp_inc[i] = best + 1
            fenw_update(idx, dp_inc[i])

        # Fenwick Tree for dp_dec using a new tree
        fenw2 = [0] * (m+1)
        dp_dec = [0] * N

        def fenw2_update(i, val):
            while i <= m:
                fenw2[i] = max(fenw2[i], val)
                i += i & -i

        def fenw2_query(i):
            s = 0
            while i:
                s = max(s, fenw2[i])
                i -= i & -i
            return s

        for i in range(N - 1, -1, -1):
            idx = comp_index[A[i]]
            best = fenw2_query(idx - 1)
            dp_dec[i] = best + 1
            fenw2_update(idx, dp_dec[i])

        ans = 0
        for i in range(N):
            ans = max(ans, dp_inc[i] + dp_dec[i] - 1)
        print(ans)

if __name__ == "__main__":
    solve()
```

This approach demonstrates how coordinate compression combined with Fenwick Trees can optimize dynamic programming solutions for subsequence problems.

Happy Coding!

</details>

# Minimize the Absolute Difference

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ABSDIF |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Sorting |
| Official Link | [ABSDIF](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_04/problems/ABSDIF) |

---

## Problem Statement

You are given a sequence $A_1, A_2, \ldots, A_N$ and an integer $K$.

Each subsequence of this sequence has a **beauty** associated with it which is equal to the sum of the absolute differences of every pair of elements in the subsequence. More formally, the **beauty** associated with an arbitrary subsequence $A_{i_1}, A_{i_2}, \ldots, A_{i_l}$ is equal to the following summation:

$$\sum_{a=1}^{l} \sum_{b=a}^{l} |A_{i_a}-A_{i_b}|$$

where $l$ is the number of elements in the subsequence and $i_1, i_2, \ldots i_l$ are the indices of the elements in the original sequence $A$.

You need to find the minimum **beauty** across all the **beauties** that are associated to the subsequences of $A$ which have exactly $K$ elements.

A subsequence of a given sequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the order of the remaining elements.

---

## Input Format

- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.

- The first line of each test case contains two space-separated integers $N$ and $K$.

- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

---

## Output Format

- For each test case, print a single line containing one integer ― the minimum **beauty** associated to a subsequence of $A$ which has exactly $K$ elements.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq K \leq N \leq 2 \cdot 10^{5}$
- the sum of $N$ over all test cases does not exceed $4 \cdot 10^{5}$
- $1 \leq A_i \leq 10^9$ for each valid $i$

---

## Examples

**Example 1**

**Input**

```text
5
5 3
6 2 4 5 1
4 3
1 2 1 1
3 1
8 2 2
6 5
99 12 5 43 7 3
7 7
4 4 4 3 4 4 5
```

**Output**

```text
4
0
0
174
12
```

**Explanation**

**Example case 1:** The subsequence consisting of numbers $6$, $4$ and $5$ has a **beauty** equal to $4$ associated with it. This is the minimum possible **beauty** that is attainable across all subsequences with $3$ elements.

**Example case 2:** The subsequence consisting of numbers $1$, $1$ and $1$ has a **beauty** equal to $0$ associated with it. This is the minimum possible **beauty** that is attainable across all subsequences with $3$ elements.

**Example case 3:** The subsequence containing a single number $8$ has a **beauty** equal to $0$ associated with it. This is the minimum possible **beauty** that is attainable across all subsequences with only one element.

**Example case 4:** The subsequence consisting of numbers $12,5,43,7,3$ has a **beauty** equal to $174$ associated with it. This is the minimum possible **beauty** that is attainable across all subsequences with $5$ elements.

**Example case 5:** The only subsequence we need to consider is the one that is equal to the whole sequence. That subsequence has a **beauty** of $12$ associated with it.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 3
6 2 4 5 1
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
4 3
1 2 1 1
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
3 1
8 2 2
```

**Output for this case**

```text
0
```



#### Test case 4

**Input for this case**

```text
6 5
99 12 5 43 7 3
```

**Output for this case**

```text
174
```



#### Test case 5

**Input for this case**

```text
7 7
4 4 4 3 4 4 5
```

**Output for this case**

```text
12
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this lesson, we discuss an efficient solution for the “Minimum Beauty of a K-Subsequence” problem. In this problem, you are given an array $A$ and an integer $K$, and you need to choose a subsequence of exactly $K$ elements. The “beauty” of a subsequence is defined as the sum of the absolute differences of every pair of elements within the subsequence, i.e.,
$$\text{beauty} = \sum_{0 \le i < j < K} |a_i - a_j|.$$

A key observation is that the minimum beauty is achieved when the chosen $K$ elements are as close as possible in value. In a sorted array, this corresponds to selecting $K$ consecutive elements.

After evaluating several ideas, the **Optimized Prefix Sum Method** stands out as the correct and optimal approach for this problem. This method leverages sorting and precomputation to efficiently compute the beauty of every contiguous block of $K$ elements.

---

### Optimized Prefix Sum Method (Sliding Window with Precomputation)

**Idea:**
Once the array is sorted, the beauty of any block of $K$ consecutive elements
$$[b_0, b_1, \ldots, b_{K-1}]$$
can be efficiently computed using the formula:
$$\text{beauty} = \sum_{j=0}^{K-1} (2j - K + 1)\cdot b_j.$$
By precomputing:
- A prefix sum array: $$\text{prefix}[i] = \sum_{j=0}^{i-1} arr[j],$$
- And a weighted prefix sum array: $$\text{prefixWeighted}[i] = \sum_{j=0}^{i-1} j\cdot arr[j],$$

we can calculate the beauty for any block starting at index $i$ in $O(1)$ time using:
$$
\text{beauty} = 2\left[(\text{prefixWeighted}[i+K] - \text{prefixWeighted}[i]) - i\cdot(\text{prefix}[i+K] - \text{prefix}[i])\right] - (K-1)\cdot(\text{prefix}[i+K]-\text{prefix}[i]).
$$

**How It Works:**
- **Step 1:** Sort the array.
- **Step 2:** Precompute the prefix sum and weighted prefix sum arrays.
- **Step 3:** For each contiguous block of $K$ elements, compute its beauty using the above formula.
- **Step 4:** Track and report the minimum beauty among all possible blocks.

**C++ Code for the Optimized Prefix Sum Method:**
```cpp
#include
#include
#include
#include
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while(t--){
        int n, k;
        cin >> n >> k;
        vector arr(n);
        for (int i = 0; i < n; i++){
            cin >> arr[i];
        }
        sort(arr.begin(), arr.end());

        // Special case: when k == 1, beauty is 0.
        if(k == 1){
            cout << 0 << "\n";
            continue;
        }

        // Precompute prefix sums and weighted prefix sums.
        vector prefix(n + 1, 0), prefixWeighted(n + 1, 0);
        for (int i = 0; i < n; i++){
            prefix[i + 1] = prefix[i] + arr[i];
            prefixWeighted[i + 1] = prefixWeighted[i] + arr[i] * i;
        }

        long long best = numeric_limits::max();
        // Iterate over all contiguous blocks of k elements.
        for (int i = 0; i <= n - k; i++){
            int L = i, R = i + k;
            long long sumBlock = prefix[R] - prefix[L];
            long long weighted = (prefixWeighted[R] - prefixWeighted[L]) - (long long)i * sumBlock;
            long long beauty = 2LL * weighted - (long long)(k - 1) * sumBlock;
            best = min(best, beauty);
        }

        cout << best << "\n";
    }
    return 0;
}
```

**Python Code for the Optimized Prefix Sum Method:**
```python
import sys

def approach3(n, k, arr):
    arr.sort()
    if k == 1:
        return 0
    prefix = [0] * (n + 1)
    prefixWeighted = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + arr[i]
        prefixWeighted[i+1] = prefixWeighted[i] + arr[i] * i
    best = float('inf')
    for i in range(n - k + 1):
        L = i
        R = i + k
        sumBlock = prefix[R] - prefix[L]
        weighted = (prefixWeighted[R] - prefixWeighted[L]) - i * sumBlock
        beauty = 2 * weighted - (k - 1) * sumBlock
        best = min(best, beauty)
    return best

if __name__ == "__main__":
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    idx = 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx + 1])
        idx += 2
        arr = list(map(int, data[idx:idx+n]))
        idx += n
        results.append(approach3(n, k, arr))
    sys.stdout.write("\n".join(map(str,results)))
```

---

### Summary & Insights

The **Optimized Prefix Sum Method** is the most efficient solution for the “Minimum Beauty of a K-Subsequence” problem. By leveraging sorting and precomputed prefix sums, the beauty for each contiguous block of $K$ elements is computed in $O(1)$ time, resulting in an overall complexity of $O(N \log N)$ (due to the sorting step). This approach is well-suited for larger inputs, ensuring that the solution is both correct and efficient.

Happy coding and best of luck with your DSA interviews!

</details>

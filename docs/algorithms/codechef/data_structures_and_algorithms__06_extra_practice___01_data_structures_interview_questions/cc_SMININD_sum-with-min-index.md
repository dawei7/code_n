# Sum with min index

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SMININD |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Binary Search |
| Official Link | [SMININD](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_06/problems/SMININD) |

---

## Problem Statement

Given an array $A$  in sorted order, and $Q$ queries that contain $i$ and $x$ for each query you have to find smallest j such that $j \geq i$ and $\sum_{k=i}^j A_k \geq x$. If the answer doesn’t exist, report $-1$ as the value of $j$.

---

## Input Format

- The first line of input contains 2 integers $N$ - size of array $A$ and $Q$ - number of queries
- The second line contains $N$ space-separated integers $A_1, A_2,……, A_N$
- Each of the next $Q$ lines contains a 2 integer $i$ and $x$ for each query.

---

## Output Format

- Output $Q$ space-separated integers with $m^{th}$ integer as $j$ value for $m^{th}$ query.

---

## Constraints

- $1 \leq N \leq 10^5$
- $1 \leq Q \leq 10^5$
- $1 \leq x \leq 10^{11}$
- $1 \leq i \leq N$
- $1 \leq A_i \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
5 4
10 20 30 40 50
1 5
2 60
1 149
1 151
```

**Output**

```text
1 4 5 -1
```

**Explanation**

Query 1 : $i = 1$ and $x = 5$
$A_1 = 10$ is greater than $5$, so $j = 1$

Query 2 :  $i = 2$ and $x = 60$
$A_2 + A_3 = 20 + 30 = 50$ is less than $60$, so $j  \nleq 3$.
$A_2 + A_3 + A_4 = 20 + 30 + 40 = 90$ is greater than $60$, so $j = 4$

Query 3 :  $i = 1$ and $x = 149$
$A_1 + A_2 + A_3 + A_4 = 100$ is less than $149$, so $j \nleq 4$.
$A_1 + A_2 + A_3 + A_4 + A_5 = 150$ is greater than $149$, so $j = 5$

Query 4 :  $i = 1$ and $x = 151$
Sum of entire array $A$ is $150$, so it is not possible to find any value of $j$, so $j = -1$

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this lesson, we explore the problem of finding a subarray with a sum constraint from a sorted array. Specifically, you are given an array $A$ (sorted in non-decreasing order) and $Q$ queries. Each query provides an index $i$ and a value $x$, and you must determine the smallest index $j$ (with $j \geq i$) such that

$$
\sum_{k=i}^{j} A_k \geq x.
$$

If no such index exists, you should output $-1$.

This problem can be solved using efficient techniques that leverage prefix sums and binary search. We will discuss two methods: a prefix sum with manual binary search and a prefix sum with built-in binary search functions. Each approach builds your understanding of how to efficiently process range queries.

---

### Approach 1: Prefix Sum with Manual Binary Search

#### Explanation:
A more efficient method involves precomputing a prefix sum array $P$, where

$$
P[j] = \sum_{k=1}^{j} A_k.
$$

For a query $(i, x)$, the sum of the subarray from $i$ to $j$ is given by

$$
P[j] - P[i-1].
$$

We need to find the smallest $j$ such that

$$
P[j] - P[i-1] \geq x \quad \Longleftrightarrow \quad P[j] \geq x + P[i-1].
$$

Because the array $A$ contains only positive integers, $P$ is strictly increasing, which allows us to apply binary search to quickly find the smallest index $j$ that satisfies the condition.

#### C++ Implementation:
```cpp
#include
#include
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, Q;
    cin >> N >> Q;
    vector A(N + 1);
    for (int i = 1; i <= N; i++){
        cin >> A[i];
    }

    vector prefixSum(N + 1, 0);
    for (int i = 1; i <= N; i++){
        prefixSum[i] = prefixSum[i - 1] + A[i];
    }

    for (int qi = 0; qi < Q; qi++){
        int i;
        long long x;
        cin >> i >> x;
        long long target = x + prefixSum[i - 1];
        int left = i, right = N, answer = -1;
        while(left <= right){
            int mid = left + (right - left) / 2;
            if(prefixSum[mid] >= target){
                answer = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        cout << answer << (qi == Q - 1 ? "\n" : " ");
    }

    return 0;
}
```

#### Python Implementation:
```python
N, Q = map(int, input().split())
A = [0] + list(map(int, input().split()))
prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + A[i]

for _ in range(Q):
    i, x = map(int, input().split())
    target = x + prefix_sum[i - 1]
    left, right = i, N
    answer = -1
    while left <= right:
        mid = left + (right - left) // 2
        if prefix_sum[mid] >= target:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    print(answer, end=" ")
print()
```

---

### Approach 2: Prefix Sum with Built-in Binary Search Functions

#### Explanation:
This approach builds on the previous technique by leveraging built-in binary search routines. In C++, we use `std::lower_bound` and in Python, we use the `bisect_left` function from the `bisect` module. After forming the prefix sum array $P$, we set a target value as follows:

$$
target = x + P[i-1],
$$

and use the built-in binary search functions to directly locate the smallest index $j$ such that $P[j] \geq target$. This method simplifies the code and is less error-prone while maintaining efficiency.

#### C++ Implementation:
```cpp
#include
#include
#include
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, Q;
    cin >> N >> Q;
    vector A(N + 1);
    for (int i = 1; i <= N; i++){
        cin >> A[i];
    }

    vector prefixSum(N + 1, 0);
    for (int i = 1; i <= N; i++){
        prefixSum[i] = prefixSum[i - 1] + A[i];
    }

    for (int qi = 0; qi < Q; qi++){
        int i;
        long long x;
        cin >> i >> x;
        long long target = x + prefixSum[i - 1];
        auto it = lower_bound(prefixSum.begin() + i, prefixSum.end(), target);
        if(it == prefixSum.end()){
            cout << -1;
        } else {
            cout << (it - prefixSum.begin());
        }
        cout << (qi == Q - 1 ? "\n" : " ");
    }

    return 0;
}
```

#### Python Implementation:
```python
import bisect
N, Q = map(int, input().split())
A = [0] + list(map(int, input().split()))
prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + A[i]

for _ in range(Q):
    i, x = map(int, input().split())
    target = x + prefix_sum[i - 1]
    pos = bisect.bisect_left(prefix_sum, target, lo=i, hi=N+1)
    if pos > N:
        print(-1, end=" ")
    else:
        print(pos, end=" ")
print()
```

---

### Summary

- **Prefix Sum with Manual Binary Search:** Uses precomputation of the prefix sum array and a custom binary search algorithm to obtain the answer in $O(N + Q \log N)$ time.
- **Prefix Sum with Built-in Binary Search:** Leverages standard library functions (`std::lower_bound` in C++ and `bisect_left` in Python) for cleaner, concise, and efficient code.

Each of these approaches highlights key techniques in algorithm design—namely, preprocessing data via prefix sums and using binary search to efficiently query them. Mastering these methods will greatly enhance your toolkit for tackling range query problems in DSA interviews.

</details>

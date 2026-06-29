# Least pair sum k elements

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LSTKELE |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Sorting |
| Official Link | [LSTKELE](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_04/problems/LSTKELE) |

---

## Problem Statement

Given an array $A$ of $N$ positive integers, you have to print $K$ elements such that summation of product between in each pair is minimised i.e $\sum_{i=1}^K \sum_{j=i+1}^K A_i \times A_j$ is minimum

---

## Input Format

- First line will contain $T$, number of testcases. Then the testcases follow.
- First line of each testcase contains 2 integer $N$ - size of array $A$ and $K$
- Second line contains $N$ space separated integers $A_1, A_2, ....., A_N$

Sum of $N$ over all test cases will not exceed $10^5$

---

## Output Format

- For each testcase, output $K$ space-separated integers in non-decreasing order.

---

## Constraints

- $1 \leq T \leq 10^3$
- $1 \leq N \leq 10^5$
- $1 \leq K \leq N$
- $1 \leq A[i] \leq 10^9$

Sum of $N$ over all test cases will not exceed 10^5

---

## Examples

**Example 1**

**Input**

```text
3
3 2
1 2 4
1 1
987
4 3
2 1 1 1000000000
```

**Output**

```text
1 2
987
1 1 2
```

**Explanation**

**Testcase 1** : We have 3 possible sets
$\{\{1,2\} , \{2,4\} , \{1,4\}\}$

For set - $\{1,2\}$

$\sum_{i=1}^2 \sum_{j=i+1}^2 A_i \times A_j = 2$

For set - $\{2,4\}$

$\sum_{i=1}^2 \sum_{j=i+1}^2 A_i \times A_j = 8$

For set - $\{1,4\}$

$\sum_{i=1}^2 \sum_{j=i+1}^2 A_i \times A_j = 4$

So set $\{1,2\}$ is the correct answer

**Testcase 2** :  We have only 1 possible set i.e $\{\{987\}\}$

**Testcase 3** : We have 3 possible sets
$\{\{1,1,2\} , \{1,2,1000000000\}, \{1,1,1000000000\}\}$

For set - $\{1,1,2\}$

$\sum_{i=1}^3 \sum_{j=i+1}^3 A_i \times A_j = 1*1 + 1*2 + 1*2 = 5$

For set - $\{1,1,1000000000\}$

$\sum_{i=1}^3 \sum_{j=i+1}^3 A_i \times A_j = 1*1 + 1*1000000000 + 1*1000000000 = 2000000002$

For set - $\{1,2,1000000000\}$

$\sum_{i=1}^3 \sum_{j=i+1}^3 A_i \times A_j = 1*2 + 1*1000000000 + 2*1000000000 = 3000000002$

So set $\{1,1,2\}$ is the correct answer

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 2
1 2 4
```

**Output for this case**

```text
1 2
```



#### Test case 2

**Input for this case**

```text
1 1
987
```

**Output for this case**

```text
987
```



#### Test case 3

**Input for this case**

```text
4 3
2 1 1 1000000000
```

**Output for this case**

```text
1 1 2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial

In this lesson, we focused on solving a problem where we need to select $K$ elements from an array of $N$ positive integers such that the sum of the products of every pair is minimized. The objective function is given by

$$
f = \sum_{i=1}^{K} \sum_{j=i+1}^{K} A_i \times A_j.
$$

Since all numbers are positive, increasing any of the selected numbers increases $f$. Hence, intuitively, choosing the $K$ smallest numbers from the array minimizes the expression. Below, we discuss three different approaches to achieve this.

## Approach 1: Full Sorting

The most straightforward method is to sort the entire array in non-decreasing order and then simply select the first $K$ elements. Given that sorting arranges the smallest numbers first, this approach guarantees that the resulting selection minimizes the sum of products.

### C++ Implementation

```cpp
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
        vector a(n);
        for (int i = 0; i < n; i++){
            cin >> a[i];
        }
        sort(a.begin(), a.end());
        for (int i = 0; i < k; i++){
            cout << a[i] << " ";
        }
        cout << "\n";
    }
    return 0;
}
```

### Python Implementation

```python
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    print(" ".join(map(str, arr[:k])))
```

## Approach 2: Using a Min-Heap

An alternative strategy is to use a min-heap (or priority queue) to retrieve the $K$ smallest elements without sorting the entire array. In this approach, we insert all elements into the min-heap and then extract the top $K$ elements. Finally, we sort the extracted $K$ numbers to meet the output requirement of non-decreasing order.

### C++ Implementation

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
        priority_queue, greater> minHeap;
        for (int i = 0; i < n; i++){
            int x;
            cin >> x;
            minHeap.push(x);
        }
        vector result;
        for (int i = 0; i < k; i++){
            result.push_back(minHeap.top());
            minHeap.pop();
        }
        sort(result.begin(), result.end());
        for(auto x : result)
            cout << x << " ";
        cout << "\n";
    }
    return 0;
}
```

### Python Implementation

```python
import heapq
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    smallest = heapq.nsmallest(k, arr)
    smallest.sort()
    print(" ".join(map(str, smallest)))
```

## Approach 3: Quickselect Algorithm

A more advanced method is to use the Quickselect algorithm. Quickselect partitions the array to place the $K$ smallest elements in the first $K$ positions with an average time complexity of $O(N)$. After partitioning, we sort the selected subset to output the numbers in non-decreasing order.

### C++ Implementation

```cpp
#include
#include
#include
using namespace std;

int partition(vector& v, int low, int high) {
    int pivot = v[high];
    int i = low;
    for (int j = low; j < high; j++) {
        if (v[j] <= pivot) {
            swap(v[i], v[j]);
            i++;
        }
    }
    swap(v[i], v[high]);
    return i;
}

void quickselect(vector& v, int low, int high, int k) {
    if (low < high) {
        int pi = partition(v, low, high);
        if (pi == k) {
            return;
        } else if (pi < k) {
            quickselect(v, pi + 1, high, k);
        } else {
            quickselect(v, low, pi - 1, k);
        }
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while(t--){
        int n, k;
        cin >> n >> k;
        vector a(n);
        for(int i = 0; i < n; i++){
            cin >> a[i];
        }
        quickselect(a, 0, n-1, k);
        vector result(a.begin(), a.begin() + k);
        sort(result.begin(), result.end());
        for(auto x : result){
            cout << x << " ";
        }
        cout << "\n";
    }
    return 0;
}
```

### Python Implementation

```python
def quickselect(arr, k):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    if k <= len(left):
        return quickselect(left, k)
    elif k <= len(left) + len(mid):
        return left + mid[:(k - len(left))]
    else:
        return left + mid + quickselect(right, k - len(left) - len(mid))

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    result = quickselect(arr, k)
    result.sort()
    print(" ".join(map(str, result)))
```

## Conclusion

All three approaches rely on the key observation that selecting the $K$ smallest elements minimizes the sum of products when all numbers are positive. The sort-based method is simplest and most intuitive, while the min-heap and Quickselect methods provide alternative techniques that may offer performance benefits in different scenarios.

Choose the approach based on your familiarity and the specific constraints of the problem at hand.

</details>

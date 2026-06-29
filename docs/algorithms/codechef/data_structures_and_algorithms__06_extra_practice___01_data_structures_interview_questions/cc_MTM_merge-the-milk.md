# Merge The Milk

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MTM |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Strings |
| Official Link | [MTM](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_05/problems/MTM) |

---

## Problem Statement

Neca is a farmer in a village called Red River and he has $N$ cows. $i$-th cow produces $a_i$ liters of milk and Neca collects the milk in $n$ buckets of infinite size (one bucket for one cow). At the end of the day he wants to merge all the milk into one bucket. However, he wants to do it as fast as possible!

Since the buckets are infinite, they are magic as well - in order to merge two buckets with $A$ and $B$ liters of milk he needs $A+B$ units of time.

Help Neca calculate the minimum amount of time he needs in order to merge the milk.

---

## Input Format

- First line will contain $T$, the number of test cases. Then the test cases follow.
- The first line of input of every test case contains a single integer $N$
- The second line of input of every test case contains $N$ integers - $a_1, a_2, ..., a_n$

---

## Output Format

For each test case, output in a single line minimal amount of time that Neca needs in order to merge all the milk into one bucket.

---

## Constraints

- $1 \leq T \leq 20$
- $1 \leq N \leq 10^5$
- Sum of $N$ over all test cases does not exceed $2\cdot10^5$
- $0 \leq a_i \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
2
4
1 2 1 1000
3
1 1 1
```

**Output**

```text
1010
5
```

**Explanation**

In the first test case it is optimal to first merge buckets with $1$ and $1$ liter of milk, then the "new" bucket with the $2$ liter bucket. In the end we merge the remaining two buckets.

In the second test case one of the optimal solutions is to first merge the first and the third bucket. Then, merge the second bucket with the remaining.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
1 2 1 1000
```

**Output for this case**

```text
1010
```



#### Test case 2

**Input for this case**

```text
3
1 1 1
```

**Output for this case**

```text
5
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial: Minimizing the Time to Merge Milk Buckets

In this lesson, we will discuss a strategy to solve the problem of merging milk from $N$ buckets such that the total merge time is minimized. Each bucket has a certain amount of milk and merging two buckets with amounts $A$ and $B$ incurs a cost of $A+B$. Our goal is to merge all the buckets into one bucket while minimizing this total merge time.

Among the various methods one might consider, the most efficient and correct approach is the Greedy Strategy using a Min-Heap. This approach is inspired by techniques used in Huffman coding and guarantees optimality by always merging the two buckets with the smallest amounts first.

---

## Greedy Strategy via Min-Heap (Optimal Merge Pattern)

### Explanation:
The idea behind this strategy is to minimize the merge cost incrementally by always merging the two smallest available buckets.

**Steps:**
1. **Initialize a Min-Heap:**
   Insert all bucket milk amounts into a min-heap (or priority queue) to efficiently access the smallest elements.

2. **Merge the Two Smallest Buckets:**
   Remove the two smallest elements from the heap. The cost to merge these two buckets is the sum of their values. Add this cost to a cumulative total.

3. **Insert the Merged Bucket Back:**
   Push the merged bucket amount (i.e., the sum of the two smallest values) back into the heap.

4. **Repeat:**
   Continue the above process until only one bucket remains. That final bucket represents the fully merged bucket with the minimum possible total merge cost.

**Key Points:**
- **Efficiency:** The algorithm utilizes a min-heap, leading to a time complexity of $O(n \log n)$, which makes it suitable for large input sizes.
- **Optimality:** Merging the smallest buckets first ensures that the additional cost introduced in each merge is minimized, thereby minimizing the overall total merge time.

### Code Implementation:

#### C++ Code:
```cpp
#include
#include
#include
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while(T--){
        int N;
        cin >> N;
        priority_queue, greater> min_heap;
        for(int i = 0; i < N; i++){
            long long milk;
            cin >> milk;
            min_heap.push(milk);
        }

        long long total = 0;
        while(min_heap.size() > 1) {
            long long first = min_heap.top();
            min_heap.pop();
            long long second = min_heap.top();
            min_heap.pop();

            long long merged = first + second;
            total += merged;
            min_heap.push(merged);
        }

        cout << total << "\n";
    }

    return 0;
}
```

#### Python Code:
```python
import heapq
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    buckets = list(map(int, input().split()))
    heapq.heapify(buckets)

    total = 0
    while len(buckets) > 1:
        first = heapq.heappop(buckets)
        second = heapq.heappop(buckets)
        merged = first + second
        total += merged
        heapq.heappush(buckets, merged)

    print(total)
```

---

**Summary:**

The Greedy Strategy via Min-Heap is the optimal solution for merging milk buckets with minimal total cost. By always merging the two smallest buckets first, the method ensures that each merge step is as cost-effective as possible, resulting in an overall merge process that is both efficient and optimal.

</details>

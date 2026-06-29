# Alice and Bob

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TOYDESIRE |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Sorting |
| Official Link | [TOYDESIRE](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_04/problems/TOYDESIRE) |

---

## Problem Statement

Alice has $N$ coins. The value of $i^{th}$ coin is $C_i$. Bob wants to buy a toy whose value is $X$. Alice, being a good friend of Bob, agrees to lend enough money to Bob so that he can buy the toy. However, Alice wants to lend as few coins as possible to Bob. Determine the minimum number of coins Alice can lend to Bob such that Bob can buy his desired toy. Bob can buy his desired toy if he can get coins whose combined worth is greater than or equal to $X$.

If there exists no way for Alice to lend Bob coins such that Bob can buy his desired toys, print "-1".

---

## Input Format

- First line will contain a single integer $T$, the number of test cases. Then $T$ test cases follow.
- Each test case will contain two lines of input.
- The first line of each test case contains two integers $N$ and $X$.
- The second line of each test case contains $N$ integers, $A_1, A_2 . . . A_N$.

---

## Output Format

- Print a single integer denoting the minimum number of coins which Alice must lend to Bob so that he can buy his desired toy. If there exists no way for Alice to lend Bob coins such that Bob can buy his desired toys, print "-1" (without quotes).

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 2*10^5$
- $1 \leq X \leq 10^{12}$
- $ \leq A_i \leq 10^9$
- It is guaranteed that the sum of $N$ over all test cases is less than or equal to $3*10^5$.

---

## Examples

**Example 1**

**Input**

```text
2
5 7
1 3 4 7 8
5 7
1 2 3 4 5
```

**Output**

```text
1
2
```

**Explanation**

- **Test-Case 1:** We can choose the coin with value “7” or the coin with value “8”.
- **Test-Case 2:** The minimum number of coins Alice will have to lend to Bob from her collection so that Bob can buy his desired toy is “2”.  She can lend the coins whose values are “2” and “5” respectively OR She can lend the coins whose values are “3” and “4” respectively.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 7
1 3 4 7 8
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
5 7
1 2 3 4 5
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this lesson, we will discuss different methods to solve the problem where we need to determine the minimum number of coins that sum up to at least a given value $X$. Alice has $N$ coins with values ${C_1, C_2, \dots, C_N}$, and our goal is to lend the minimum number of coins so that their total value is at least $X$. If it is not possible, we return \(-1\).

Below are three important approaches to solving this problem.

---

### **Approach 1: Greedy Algorithm by Sorting and Iteration**

**Idea:**
Since we need the fewest coins possible, it is optimal to pick the coins with the highest values first. We can achieve this by sorting the coins in descending order and then iteratively adding their values until the total reaches or exceeds $X$.

**Algorithm Steps:**
1. **Sort:** Arrange the array of coin values in descending order.
2. **Iterate:** Initialize a running sum and a counter. Traverse the sorted list and keep adding coin values until the sum reaches or exceeds $X$.
3. **Check:** If at any point the sum is greater than or equal to $X$, the counter will be our answer. Otherwise, print \(-1\).

**Complexity:**
- Sorting takes $O(N\log N)$ time.
- The iteration takes $O(N)$ time.
- Overall, the approach runs in $O(N\log N)$ time, which is efficient given the constraints.

**C++ Implementation:**
```cpp
#include
#include
#include
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        int n;
        long long x;
        cin >> n >> x;
        vector coins(n);
        for (int i = 0; i < n; i++) {
            cin >> coins[i];
        }
        // Sort coins in descending order
        sort(coins.begin(), coins.end(), greater());

        long long sum = 0;
        int count = 0;
        for (int i = 0; i < n; i++) {
            sum += coins[i];
            count++;
            if (sum >= x)
                break;
        }
        cout << (sum >= x ? count : -1) << "\n";
    }
    return 0;
}
```

**Python Implementation:**
```python
import sys
input = sys.stdin.readline

def main():
    t = int(input().strip())
    for _ in range(t):
        n, x = map(int, input().split())
        coins = list(map(int, input().split()))
        # Sort coins in descending order
        coins.sort(reverse=True)

        total = 0
        count = 0
        for coin in coins:
            total += coin
            count += 1
            if total >= x:
                print(count)
                break
        else:
            print(-1)

if __name__ == "__main__":
    main()
```

---

### **Approach 2: Greedy with Prefix Sum and Binary Search**

**Idea:**
After sorting the coins in descending order, we can compute a prefix sum array where the $i^{th}$ element represents the sum of the first $i+1$ coins. Once this prefix sum array is built, we can quickly find the smallest index \( i \) such that
$$
\text{prefix}[i] \geq X
$$
using binary search.

**Algorithm Steps:**
1. **Sort:** Arrange the coins in descending order.
2. **Prefix Sum:** Build an array where each element is the cumulative sum of coins.
3. **Binary Search:** Use binary search to find the smallest index where the prefix sum is at least $X$.
4. **Determine Answer:** If such an index is found, the result is the index value plus one; otherwise, print \(-1\).

**Complexity:**
- Sorting takes $O(N\log N)$.
- Building the prefix array takes $O(N)$.
- Binary search takes $O(\log N)$.
- Overall, this approach is also efficient.

**C++ Implementation:**
```cpp
#include
#include
#include
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        int n;
        long long x;
        cin >> n >> x;
        vector coins(n);
        for (int i = 0; i < n; i++) {
            cin >> coins[i];
        }
        // Sort coins in descending order
        sort(coins.begin(), coins.end(), greater());

        // Build the prefix sum array
        vector prefix(n);
        prefix[0] = coins[0];
        for (int i = 1; i < n; i++) {
            prefix[i] = prefix[i - 1] + coins[i];
        }

        // Binary search for the smallest index with prefix sum >= x
        int ans = -1;
        int low = 0, high = n - 1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (prefix[mid] >= x) {
                ans = mid + 1;  // Convert 0-index to count
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        cout << ans << "\n";
    }
    return 0;
}
```

**Python Implementation:**
```python
import sys
from bisect import bisect_left

def main():
    input = sys.stdin.readline
    t = int(input().strip())
    for _ in range(t):
        n, x = map(int, input().split())
        coins = list(map(int, input().split()))
        coins.sort(reverse=True)

        prefix = []
        total = 0
        for coin in coins:
            total += coin
            prefix.append(total)

        # Binary search for the leftmost index where prefix sum >= x
        index = bisect_left(prefix, x)
        if index < len(prefix):
            print(index + 1)
        else:
            print(-1)

if __name__ == '__main__':
    main()
```

---

### **Approach 3: Using a Max-Heap**

**Idea:**
Instead of sorting, we can use a max-heap to repeatedly extract the largest coin. This method mimics the greedy approach by always selecting the coin with the highest value first.

**Algorithm Steps:**
1. **Construct Heap:** Insert all coin values into a max-heap.
2. **Extract Maximums:** Repeatedly extract the top element (largest coin), add it to a running sum, and count each extraction.
3. **Check:** Stop when the running sum is greater than or equal to $X$. If the max-heap is exhausted and the sum is still less than $X$, print \(-1\).

**Complexity:**
- Building a heap in C++ takes $O(N)$ and each extraction takes $O(\log N)$.
- In Python, we simulate a max-heap using negative values.
- This approach runs in $O(N \log N)$ in the worst case.

**C++ Implementation:**
```cpp
#include
#include
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        int n;
        long long x;
        cin >> n >> x;
        priority_queue pq;
        for (int i = 0; i < n; i++) {
            long long coin;
            cin >> coin;
            pq.push(coin);
        }

        long long sum = 0;
        int count = 0;
        while (!pq.empty() && sum < x) {
            sum += pq.top();
            pq.pop();
            count++;
        }
        cout << (sum >= x ? count : -1) << "\n";
    }
    return 0;
}
```

**Python Implementation:**
```python
import sys
import heapq

def main():
    input = sys.stdin.readline
    t = int(input().strip())
    for _ in range(t):
        n, x = map(int, input().split())
        coins = list(map(int, input().split()))
        # Simulate a max-heap by pushing negative values
        max_heap = [-coin for coin in coins]
        heapq.heapify(max_heap)

        total = 0
        count = 0
        while max_heap and total < x:
            largest = -heapq.heappop(max_heap)
            total += largest
            count += 1
        print(count if total >= x else -1)

if __name__ == '__main__':
    main()
```

---

### **Summary and Insights**

1. **Greedy Approach (Approach 1)** is straightforward and works efficiently by leveraging the natural ordering of coin values.
2. **Prefix Sum with Binary Search (Approach 2)** provides a neat alternative especially if you wish to separate the process of sum computation from searching, which might be useful in extended problems.
3. **Max-Heap (Approach 3)** is another way to implement the greedy algorithm when dynamic extraction of maximum is preferred.

Each of these methods correctly identifies the minimal set of coins needed to reach the target value $X$. The greedy strategy is optimal here because, with positive coin values, always choosing the highest available value minimizes the number of coins required.

We hope this detailed explanation helps you understand the rationale and methods behind solving this problem!

</details>

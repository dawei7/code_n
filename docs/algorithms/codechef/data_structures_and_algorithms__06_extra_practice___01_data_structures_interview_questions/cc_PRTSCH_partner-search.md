# Partner Search

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PRTSCH |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Binary Search |
| Official Link | [PRTSCH](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_06/problems/PRTSCH) |

---

## Problem Statement

Chef lives in a world where every woman has a unique height. Chef has $M$ female friends and is searching for all of them.
Chef is smart and knows the height of all the friends such that $H_i$ is the height the $i^{th}$ friend.

There is a queue of $N$ women with their heights $Q_i$ in strictly increasing order. By the time Chef reaches near this queue, some women (possibly 0) from the front go to the back of the queue, without changing their relative order in the queue.

Now, since Chef is really missing his friends, help him to quickly find whether his friends are present in the queue or not.

---

## Input Format

- First line will contain $T$, the number of testcases. Then the testcases follow.
- First line of each testcase contains 2 integers $N$ - number of women in queue and $M$ - number of female friends.
- Second line contains $N$ space separated integers $Q_1, Q_2, ....., Q_N$
- Third line contains $M$ space separated integers $H_1, H_2, ....., H_M$

It is guaranteed that the initial queue has heights in strictly increasing order.

---

## Output Format

- For each test case, output a single line containing $M$ strings where $i^{th}$ string is either "Yes" if the $i^{th}$friend is present in the queue or "No" otherwise.
- You may print each character of the string in uppercase or lowercase (for example: the strings "yes", "YeS", "YES" will be treated as the same strings).

---

## Constraints

- $1 \leq T \leq 10^3$
- $1 \leq N \leq 10^5$
- $1 \leq M \leq N$
- $10^5 \leq Q_i \leq 2*10^5$
- $10^5 \leq H_i \leq 2*10^5$

Sum of $N$ over all test cases will not exceed 10^5

---

## Examples

**Example 1**

**Input**

```text
2
5 3
10002 10003 10004 10000 10001
10004 19000 18000
8 2
13000 10002 10012 10098 11008 11230 12032 12321 
11008 12321
```

**Output**

```text
Yes No No
Yes Yes
```

**Explanation**

Testcase 1 : Original queue was : [10000 10001 10002 10003 10004]
and last 3 women moved to the front

Testcase 2 : Original queue was : [10002 10012 10098 11008 11230 12032 12321 13000]  and last women moved to the front

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 3
10002 10003 10004 10000 10001
10004 19000 18000
```

**Output for this case**

```text
Yes No No
```



#### Test case 2

**Input for this case**

```text
8 2
13000 10002 10012 10098 11008 11230 12032 12321
11008 12321
```

**Output for this case**

```text
Yes Yes
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this lesson, we discuss several viable approaches to determine whether each of Chef's friends (represented by their unique heights) is present in a rotated queue of women. Although the queue was originally sorted in strictly increasing order, a rotation may make it appear unsorted. We will explore three important approaches for solving this problem.

---

### **Approach 1: Using a Hash Set**

**Idea:**
Since we only need to check membership (i.e. whether a given friend’s height exists in the queue), we can store all the heights from the queue into a hash set (or unordered set in C++) and then perform membership queries for each friend’s height. A set supports average‑case constant time $(O(1))$ lookups and thus solves the problem in $O(N+M)$ time where $N$ is the number of women in the queue and $M$ is the number of friends.

**When to Use:**
- This approach is straightforward and leverages hash table properties.
- It works regardless of whether the list is rotated or not.

**Implementations:**

**C++ Code:**
```cpp
#include
#include
#include
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--) {
        int N, M;
        cin >> N >> M;
        vector queueHeights(N);
        for (int i = 0; i < N; i++) {
            cin >> queueHeights[i];
        }

        // Create a hash set for O(1) average lookups
        unordered_set heightSet(queueHeights.begin(), queueHeights.end());

        // Process each friend’s height
        for (int i = 0; i < M; i++) {
            int friendHeight;
            cin >> friendHeight;
            if (heightSet.count(friendHeight))
                cout << "Yes ";
            else
                cout << "No ";
        }
        cout << "\n";
    }

    return 0;
}
```

**Python Code:**
```python
def solve():
    import sys
    input = sys.stdin.readline

    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        # Read the queue, then create a set of heights
        queue_heights = list(map(int, input().split()))
        height_set = set(queue_heights)
        # Process each friend’s height
        friends = list(map(int, input().split()))
        result = []
        for friend_height in friends:
            result.append("Yes" if friend_height in height_set else "No")
        print(" ".join(result))

if __name__ == '__main__':
    solve()
```

---

### **Approach 2: Modified Binary Search on a Rotated Sorted Array**

**Idea:**
The queue is initially sorted, but a rotation splits it into two sorted segments. We can adapt the standard binary search to account for this by checking which side of the array (left or right) is monotonically increasing. The algorithm works as follows for a given target height:

1. Set two pointers, with $L = 0$ and $R = N - 1$.
2. Compute the middle index $mid = \lfloor \frac{L + R}{2} \rfloor$.
3. If the element at index $mid$ equals the target, return "Yes".
4. Otherwise, determine whether the subarray $[L, mid]$ is sorted:
   - If $Q_L \leq Q_{mid}$ and the target lies in the interval $$\left[ Q_L, Q_{mid} \right],$$
     then restrict the search to the left half by updating $R = mid - 1$.
   - Otherwise, search the other half by setting $L = mid + 1$.
5. Continue until $L > R$; if no match is found, return "No".

**Time Complexity:**
Each query takes $O(\log N)$ time, leading to an overall complexity of $O(M\log N)$ for $M$ queries.

**C++ Code:**
```cpp
#include
#include
using namespace std;

// Function to search for target in rotated sorted array using modified binary search
bool rotatedBinarySearch(const vector& arr, int target) {
    int L = 0, R = arr.size() - 1;
    while (L <= R) {
        int mid = L + (R - L) / 2;
        if (arr[mid] == target) return true;

        // If left half is sorted
        if (arr[L] <= arr[mid]) {
            if (target >= arr[L] && target <= arr[mid])
                R = mid - 1;
            else
                L = mid + 1;
        }
        // Else, right half is sorted
        else {
            if (target >= arr[mid] && target <= arr[R])
                L = mid + 1;
            else
                R = mid - 1;
        }
    }
    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int N, M;
        cin >> N >> M;
        vector Q(N);
        for (int i = 0; i < N; i++) {
            cin >> Q[i];
        }
        for (int i = 0; i < M; i++) {
            int friendHeight;
            cin >> friendHeight;
            cout << (rotatedBinarySearch(Q, friendHeight) ? "Yes" : "No") << " ";
        }
        cout << "\n";
    }
    return 0;
}
```

**Python Code:**
```python
def rotated_binary_search(arr, target):
    L, R = 0, len(arr) - 1
    while L <= R:
        mid = L + (R - L) // 2
        if arr[mid] == target:
            return True
        # Check if left half is sorted
        if arr[L] <= arr[mid]:
            if arr[L] <= target <= arr[mid]:
                R = mid - 1
            else:
                L = mid + 1
        else:
            if arr[mid] <= target <= arr[R]:
                L = mid + 1
            else:
                R = mid - 1
    return False

def solve():
    import sys
    input = sys.stdin.readline

    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        Q = list(map(int, input().split()))
        friends = list(map(int, input().split()))
        result = []
        for friend in friends:
            result.append("Yes" if rotated_binary_search(Q, friend) else "No")
        print(" ".join(result))

if __name__ == '__main__':
    solve()
```

---

### **Approach 3: Reconstructing the Original Sorted Order**

**Idea:**
Since the initial queue is in strictly increasing order, we can restore the original order by identifying the pivot point—the index of the smallest element. Once identified, we can reassemble the sorted array by concatenating the segment from the pivot to the end with the segment from the beginning to the pivot:
$$ \text{sorted\_queue} = Q_{pivot}, Q_{pivot + 1}, ..., Q_{N - 1}, Q_0, Q_1, ..., Q_{pivot - 1}. $$
After reconstructing the sorted array, we can use standard binary search for each friend’s height.

**Finding the Pivot:**
- We perform a binary search to locate the smallest element. The condition is to check if $Q[mid] > Q[right]$, then the pivot is to the right of $mid$, otherwise, it is to the left or at $mid$.

**Time Complexity:**
- Finding the pivot is $O(\log N)$.
- Reconstructing the sorted order takes $O(N)$.
- Each query takes $O(\log N)$, hence the overall complexity is acceptable given the constraints.

**C++ Code:**
```cpp
#include
#include
#include
using namespace std;

// Function to find the pivot point (index of the smallest element)
int findPivot(const vector& arr) {
    int L = 0, R = arr.size() - 1;
    while (L < R) {
        int mid = L + (R - L) / 2;
        if (arr[mid] > arr[R])
            L = mid + 1;
        else
            R = mid;
    }
    return L;
}

// Standard binary search function
bool binarySearch(const vector& arr, int target) {
    int L = 0, R = arr.size() - 1;
    while(L <= R) {
        int mid = L + (R - L) / 2;
        if(arr[mid] == target)
            return true;
        else if(arr[mid] < target)
            L = mid + 1;
        else
            R = mid - 1;
    }
    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while(T--) {
        int N, M;
        cin >> N >> M;
        vector Q(N);
        for (int i = 0; i < N; i++) {
            cin >> Q[i];
        }

        // Find pivot and reconstruct the sorted order.
        int pivot = findPivot(Q);
        vector sortedQueue;
        sortedQueue.insert(sortedQueue.end(), Q.begin() + pivot, Q.end());
        sortedQueue.insert(sortedQueue.end(), Q.begin(), Q.begin() + pivot);

        for (int i = 0; i < M; i++) {
            int friendHeight;
            cin >> friendHeight;
            cout << (binarySearch(sortedQueue, friendHeight) ? "Yes" : "No") << " ";
        }
        cout << "\n";
    }
    return 0;
}
```

**Python Code:**
```python
def find_pivot(arr):
    L, R = 0, len(arr) - 1
    while L < R:
        mid = L + (R - L) // 2
        if arr[mid] > arr[R]:
            L = mid + 1
        else:
            R = mid
    return L

def binary_search(arr, target):
    L, R = 0, len(arr) - 1
    while L <= R:
        mid = L + (R - L) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            L = mid + 1
        else:
            R = mid - 1
    return False

def solve():
    import sys
    input = sys.stdin.readline

    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        Q = list(map(int, input().split()))
        friends = list(map(int, input().split()))

        # Find pivot to restore original sorted order of the queue
        pivot = find_pivot(Q)
        sorted_queue = Q[pivot:] + Q[:pivot]

        result = []
        for friend in friends:
            result.append("Yes" if binary_search(sorted_queue, friend) else "No")
        print(" ".join(result))

if __name__ == '__main__':
    solve()
```

---

### **Summary**

- **Approach 1 (Hash Set):** Best for simplicity and constant time membership checks.
- **Approach 2 (Modified Binary Search):** Exploits the rotated sorted property for efficient search.
- **Approach 3 (Reconstruct & Binary Search):** Demonstrates a two-step method by restoring the original order and then applying binary search.

These approaches illustrate different paradigms to solve the problem, and understanding each can deepen your grasp of problem-solving techniques in data structures and algorithms.

</details>

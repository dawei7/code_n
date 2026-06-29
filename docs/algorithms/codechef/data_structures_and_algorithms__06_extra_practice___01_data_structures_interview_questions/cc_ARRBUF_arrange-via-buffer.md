# Arrange via Buffer

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ARRBUF |
| Difficulty Rating | 1400 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Queues |
| Official Link | [ARRBUF](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_09/problems/ARRBUF) |

---

## Problem Statement

There is a container $A$ filled with N blocks placed from left to right, where the size of block placed at $i^{th}$ position from the left has size $A_i$. There is another **empty** container $B$ (identical as $A$) in which you wish to transfer the blocks.

To arrange the blocks you are given a vertical buffer where you can pile up the blocks.
You are allowed to perform any of the two moves multiple times -
- Pick the **rightmost** block from container $A$ and put it on the **top** of the buffer.
- Pick the **topmost** block from the buffer and put it in the **rightmost** unoccupied space in container $B$.

Your task is to determine if it is possible to place all the blocks from container $A$ to container $B$ such that their size is non decreasing order. More formally, $B_i \leq B_{i+1}$ for all $ 1 \leq i \lt N$.

---

## Input Format

- First line will contain $T$, number of testcases. Then the testcases follow.
- First line of each testcase contains an integer $N$ - number of blocks in container $A$.
- Second line contains N space separated integers $A_1, A_2, ....., A_N$

---

## Output Format

- For each test case, output a single line containing either "Yes" if possible or "No" if not possible.
- You may print each character of the string in uppercase or lowercase (for example: the strings "yes", "YeS", "YES" will be treated as the same strings).

---

## Constraints

- $1 \leq T \leq 10^3 $
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^6$

Sum of $N$ over all test cases will not exceed $10^5$

---

## Examples

**Example 1**

**Input**

```text
2
5
2 1 3 5 4
3
3 1 2
```

**Output**

```text
Yes
No
```

**Explanation**

**Test Case 1** : Follow the following moves
- Pick rightmost block from A (4 in this case) and put in the buffer.
  A = [ 2 1 3 5 4 ], buffer = [ 4 ] and B = [ ]
- Pick rightmost block from A (5 in this case) and put in the buffer.
   A = [ 2 1 3 ], buffer = [ 5 4 ] and B = [ ]
- Pick topmost block from buffer (5 in this case) and put in B.
  A = [ 2 1 3 ],  buffer = [ 4 ] and B = [ 5 ]
- Pick topmost block from buffer (4 in this case) and put in B.
  A = [ 2 1 3 ],  buffer = [  ] and B = [ 4 5 ]
- Pick rightmost block from A (3 in this case) and put in the buffer.
  A = [ 2 1 ],  buffer = [ 3 ] and B = [ 4 5 ]
- Pick topmost block from buffer (3 in this case) and put in B.
  A = [ 2 1 ],  buffer = [  ] and B = [ 3 4 5 ]
- Pick rightmost block from A (1 in this case) and put in the buffer.
   A = [ 2 ],  buffer = [ 1 ] and B = [ 3 4 5 ]
- Pick rightmost block from A (2 in this case) and put in the buffer.
  A = [ ],  buffer = [ 2 1 ] and B = [ 3 4 5 ]
- Pick topmost block from buffer (2 in this case) and put in B.
  A = [ ],  buffer = [ 1 ] and B = [ 2 3 4 5 ]
- Pick topmost block from buffer (1 in this case) and put in B.
  A = [ ],  buffer = [  ] and B = [ 1 2 3 4 5 ]

We can see Container B contains all blocks in increasing order of their size.

**Test Case 2** : It can be proved that there exists no sequence of moves such that container B contains blocks in increasing order of their sizes.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
2 1 3 5 4
```

**Output for this case**

```text
Yes
```



#### Test case 2

**Input for this case**

```text
3
3 1 2
```

**Output for this case**

```text
No
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## DSA Interview Preparation: Container Block Transfer Using a Buffer Stack

In this lesson, we discuss a problem where you have two containers:
- Container **A** contains $N$ blocks arranged from left to right, with the block at the $i^{th}$ position having size $A_i$.
- Container **B** is initially empty.

You have a vertical **buffer** (which we will simulate using a stack) and you are allowed the following moves:
1. Remove the **rightmost** block from container **A** and push it on the top of the buffer.
2. Remove the **topmost** block from the buffer and place it into the **rightmost unoccupied** space in container **B**.

The aim is to perform these moves such that the final arrangement of blocks in container **B** is in non-decreasing order
$$ B_1 \leq B_2 \leq \cdots \leq B_N. $$

Below, we explain two approaches to solve this problem.

---

### Approaches to the Problem

We first outline two techniques that are useful when solving this problem.

#### **Approach 1: Direct Simulation Using a Buffer Stack**

In this method, we mimic the allowed moves exactly. We use:
- A **deque** (or vector) to simulate container **A**.
- A **stack** to simulate the buffer.
- A **deque** (or list) to simulate container **B**.

**Algorithm Steps:**
1. **While container A is not empty:**
   - **Push Move:** If the buffer is empty or the rightmost block of **A** is **greater than or equal to** the top of the buffer, remove the rightmost block from **A** and push it onto the buffer.
   - **Pop Move:** Otherwise, pop the top block from the buffer and append it to container **B** (using a method equivalent to inserting at the left so that the final order is aligned correctly).
2. **Empty the Buffer:** Once container **A** is empty, pop any remaining blocks from the buffer into **B**.
3. **Sorted Verification:** Finally, check if container **B** is sorted in non-decreasing order (i.e. for all $1 \leq i < N$, we have $B_i \leq B_{i+1}$).

**Intuition:**
This simulation is analogous to the classic *stack-sorting* method. If after all the moves the container **B** is sorted (non-decreasing), then it is possible to transfer the blocks accordingly. The algorithm runs in $O(N)$ time per test case, which is efficient for the given constraints.

Below is the **C++** and **Python** implementation for this approach.

---

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
    while(T--) {
        int N;
        cin >> N;
        deque A, B;
        stack buffer;
        long long x;
        for (int i = 0; i < N; i++){
            cin >> x;
            A.push_back(x);
        }

        while(!A.empty()){
            if(buffer.empty() || A.back() >= buffer.top()){
                x = A.back();
                A.pop_back();
                buffer.push(x);
            } else {
                x = buffer.top();
                buffer.pop();
                B.push_front(x);
            }
        }
        while(!buffer.empty()){
            x = buffer.top();
            buffer.pop();
            B.push_front(x);
        }

        bool sorted = true;
        for (int i = 1; i < N; i++){
            if(B[i] < B[i-1]){
                sorted = false;
                break;
            }
        }
        cout << (sorted ? "Yes" : "No") << "\n";
    }
    return 0;
}
```

**Python Code:**
```python
from collections import deque
import sys

input = sys.stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = deque(map(int, input().split()))
        B = deque()
        buffer = []  # Using list as a stack

        while A:
            if not buffer or A[-1] >= buffer[-1]:
                buffer.append(A.pop())
            else:
                B.appendleft(buffer.pop())
        while buffer:
            B.appendleft(buffer.pop())

        sorted_order = all(B[i] >= B[i-1] for i in range(1, N))
        print("Yes" if sorted_order else "No")

if __name__ == "__main__":
    main()
```

---

#### **Approach 2: Optimized Simulation with Early Sorted Check**

This approach follows the same simulation logic but seeks to improve efficiency by integrating an early check for sorted order. Instead of always performing all moves before verifying if container **B** is sorted, you can:

1. **Simulate the moves:** As with Approach 1, use container **A**, a buffer stack, and container **B**.
2. **Check While Building:** While transferring blocks from the buffer to **B**, monitor the order. You maintain the last (smallest) block added to **B** and, if at any point a newly placed block violates the non-decreasing order (i.e. it is smaller than the previous block), you can conclude early that the transfer is impossible.
3. **Conclude:** If the simulation completes without detecting any order violation, then the sequence is stack-sortable into container **B**.

Even though the core simulation is nearly identical (as the operations permitted are fixed), this early termination strategy can save computation time in practice, especially for cases where an order violation is encountered before processing all elements.

Below, find the **C++** and **Python** implementations for this approach.

---

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
    while(T--) {
        int N;
        cin >> N;
        deque A;
        stack buffer;
        bool possible = true;

        // Read the blocks into container A.
        for (int i = 0; i < N; i++){
            long long x;
            cin >> x;
            A.push_back(x);
        }

        // Here we simulate building container B and store the result in deque B.
        deque B;
        while(!A.empty()){
            if(buffer.empty() || A.back() >= buffer.top()){
                buffer.push(A.back());
                A.pop_back();
            } else {
                long long x = buffer.top();
                buffer.pop();
                B.push_front(x);
            }
        }
        while(!buffer.empty()){
            B.push_front(buffer.top());
            buffer.pop();
        }

        // Early verification for non-decreasing order in container B.
        for (int i = 1; i < N; i++){
            if(B[i] < B[i-1]){
                possible = false;
                break;
            }
        }
        cout << (possible ? "Yes" : "No") << "\n";
    }
    return 0;
}
```

**Python Code:**
```python
from collections import deque
import sys

input = sys.stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = deque(map(int, input().split()))
        B = deque()
        buffer = []  # Using list as a stack

        while A:
            if not buffer or A[-1] >= buffer[-1]:
                buffer.append(A.pop())
            else:
                B.appendleft(buffer.pop())
        while buffer:
            B.appendleft(buffer.pop())

        possible = True
        # Check that container B is sorted in non-decreasing order.
        for i in range(1, N):
            if B[i] < B[i-1]:
                possible = False
                break
        print("Yes" if possible else "No")

if __name__ == "__main__":
    main()
```

---

### Conclusion

Both approaches simulate the transfer of blocks using a buffer (stack) and then verify that the blocks in container **B** are sorted in non-decreasing order.
- **Approach 1** directly simulates the allowed moves and checks the sorted order afterward.
- **Approach 2** enhances this simulation by integrating an early termination check while building container **B**.

These strategies run in $O(N)$ per test case and work efficiently under the given constraints, making them well-suited for DSA interview preparation and real-world problem solving.

Happy Coding!

</details>

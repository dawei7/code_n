# Jump To The End

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | JUMPEND |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [JUMPEND](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_03/problems/JUMPEND) |

---

## Problem Statement

You are given a sequence of **nonnegative** integers $A_1, A_2, \ldots, A_{N}$.

There is a pawn placed on the first element of the sequence, i.e. at position $1$. When the pawn is on the position numbered with $x$, it can jump at most $A_x$ places to the right. In other words, if $A_x > 0$, the pawn can jump to any position from $x+1$ to $x+A_x$. If $A_x=0$, the pawn can not move from the position numbered with $x$ at all.

Find the maximum possible number of jumps using which it is possible to place the pawn on the last position, i.e. the position numbered with $N$, or determine that it is impossible to reach it.

---

## Input Format

- The first line of the input contains a single integer $T$ - the number of test cases. The description of $T$ test cases follows.

- The first line of each test case contains an integer $N$.

- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

---

## Output Format

- For each test case, print a single line containing one integer. In case it is possible to reach the last position, this integer should be the maximum possible number of jumps in which the pawn can be placed on the last position. Otherwise, this integer should be $-1$.

---

## Constraints

- $1 \leq T \leq 100$
- $2 \leq N \leq 2 \cdot 10^{5}$
- the sum of $N$ over all test cases does not exceed $4 \cdot 10^{5}$
- $0 \leq A_i \leq N-i$ for each valid $i$

---

## Examples

**Example 1**

**Input**

```text
4
2
1 0
3
0 1 0
5 
2 0 1 1 0
6
2 2 2 2 1 0
```

**Output**

```text
1
-1
3
5
```

**Explanation**

**Example case 1:** The maximum number of jumps in a path from the position $1$ to the position $N$ is $1$.

**Example case 2:** It is impossible to reach the position $N$ because $A_1=0$.

**Example case 3:** It is possible to reach the position $N$ using $3$ jumps if we follow the path $1 \rightarrow 3 \rightarrow 4 \rightarrow 5$.

**Example case 4:** It is possible to reach the position $N$ using $5$ jumps if we follow the path $1 \rightarrow 2 \rightarrow 3 \rightarrow 4 \rightarrow 5 \rightarrow 6$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
1 0
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
3
0 1 0
```

**Output for this case**

```text
-1
```



#### Test case 3

**Input for this case**

```text
5
2 0 1 1 0
```

**Output for this case**

```text
3
```



#### Test case 4

**Input for this case**

```text
6
2 2 2 2 1 0
```

**Output for this case**

```text
5
```



**Example 2**

**Input**

```text
3
7
4 0 1 0 2 0 0
4
3 1 0 0
6
3 0 0 1 0 0
```

**Output**

```text
2
1
-1
```

**Explanation**

**Example case 1:** It is possible to reach the position $N$ using $2$ jumps if we follow the path $1 \rightarrow 5 \rightarrow 7$. It is impossible to reach it using $3$ jumps because when the pawn is located at the position $3$ it can not move anywhere.

**Example case 2:** It is possible to reach the position $N$ using $1$ jump if the pawn jumps straight to the position $N$ from the position $1$. Note that it must not jump to the position $2$ because it can not jump anywhere from that position.

**Example case 3:** It is impossible to reach the position $N$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
7
4 0 1 0 2 0 0
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
4
3 1 0 0
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
6
3 0 0 1 0 0
```

**Output for this case**

```text
-1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this lesson we will discuss how to solve the problem of finding the maximum possible number of jumps to reach the last element in a sequence. In the problem, we are given an array
$$
A_1, A_2, \ldots, A_N
$$
where each $A_i$ tells you how far you can jump from the current position $i$. The twist is that instead of minimizing the number of jumps (as in the classic “Jump Game” problem), we need to maximize the number of jumps (i.e. take as many short jumps as possible) while still reaching the last position. If the last position cannot be reached, we return $-1$.

Below, we describe the correct approach to solve this problem.

---

### Approach: Dynamic Programming with a Priority Queue

#### **Idea**

We use a dynamic programming (DP) formulation where we define:
$$
dp[i] = \text{maximum number of jumps needed to reach index } i.
$$
- We initialize $dp[0] = 0$ (starting position; no jump needed).
- For each subsequent position $j$ (from $1$ to $N-1$), we need to choose a previous index $i$ (with $0 \le i < j$) such that the pawn can jump from $i$ to $j$ (i.e., $i + A_i \ge j$) and that gives the maximum $dp[i]$. Then, we set:
$$
dp[j] = \max_{\text{all } i \text{ with } i+A_i \ge j}\{dp[i]\} + 1.
$$

Since directly scanning all possible $i$ for every $j$ would be too slow, we use a max-heap (priority queue) to keep track of “candidate” indices. Each candidate is stored as a pair containing its current $dp$ value and its “expiry” value, which is $i+A_i$ (the farthest index this candidate can reach). As we iterate through $j$, we remove candidates that have expired (i.e. whose expiry is less than $j$) and then use the candidate at the top of the queue (the one with the highest $dp$ among the active candidates) to update $dp[j]$. Finally, we add $j$ as a new candidate with an expiry of $j+A_j$.

This approach works in $O(n \log n)$ time per test case, which is efficient given the problem constraints.

#### **C++ Implementation**
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
        int n;
        cin >> n;
        vector A(n);
        for (int i = 0; i < n; i++){
            cin >> A[i];
        }

        // dp[i] holds the maximum number of jumps required to reach index i (0-indexed)
        vector dp(n, -1);
        dp[0] = 0;

        // Priority queue stores pairs {dp[i], expiry} where expiry = i + A[i]
        // We use this to quickly retrieve the candidate with the highest dp value that can reach the current j.
        priority_queue> pq;
        pq.push({dp[0], 0 + A[0]});

        for (int j = 1; j < n; j++){
            // Remove candidates that are no longer able to jump to position j.
            while (!pq.empty() && pq.top().second < j)
                pq.pop();

            // If no candidate can reach index j, then it is unreachable.
            if (pq.empty()){
                dp[j] = -1;
                break;
            }

            dp[j] = pq.top().first + 1;
            pq.push({dp[j], j + A[j]});
        }

        cout << dp[n-1] << "\n";
    }
    return 0;
}
```

#### **Python Implementation**
```python
import heapq
import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        n = int(input())
        A = list(map(int, input().split()))
        dp = [-1] * n
        dp[0] = 0

        # Python's heapq implements a min-heap.
        # To simulate a max-heap, store (-dp_value, expiry).
        pq = []
        heapq.heappush(pq, (-dp[0], 0 + A[0]))

        for j in range(1, n):
            # Remove all candidates that have expired.
            while pq and pq[0][1] < j:
                heapq.heappop(pq)
            if not pq:
                dp[j] = -1
                break
            dp[j] = (-pq[0][0]) + 1
            heapq.heappush(pq, (-dp[j], j + A[j]))
        print(dp[n-1])

if __name__ == "__main__":
    solve()
```

---

### Summary and Insights

In this lesson, we focused on a dynamic programming approach enhanced with a priority queue to maximize the number of jumps required to reach the end of the sequence. By efficiently tracking candidate positions and only considering relevant indices, this method achieves an $O(n \log n)$ performance per test case. This approach is both efficient and effective for large inputs, making it highly suitable for competitive programming and interview scenarios.

Happy coding and good luck with your DSA interviews!

</details>

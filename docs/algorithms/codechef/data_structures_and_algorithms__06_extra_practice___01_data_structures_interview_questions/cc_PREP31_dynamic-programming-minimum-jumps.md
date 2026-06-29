# Dynamic Programming - Minimum Jumps

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP31 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Dynamic Programming |
| Official Link | [PREP31](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_14/problems/PREP31) |

---

## Problem Statement

Chef has an array $A$ of size $N$.
On standing at the $i^{th}$ index of the array $(1\le i \le N)$, Chef can make a jump of length **less than or equal to** $A_i$.

If Chef starts from the **first** index of the array, find the **minimum** number of jumps required by Chef to reach the **last** index of the array.

If it is impossible to reach the last index, print $-1$ instead.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains a single integer $N$ — the number elements in the array.
    - The next line contains $N$ space-separated integers - the elements of the array $A$.

---

## Output Format

For each test case, output on a new line, the **minimum** number of jumps required by Chef to reach the **last** element of the array.

If it is impossible to reach the last index, print $-1$ instead.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 10^5$
- $0 \leq A_i \lt N$
- The sum of $N$ over all test cases won't exceed $2\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
4
1 1 2 2
4
1 2 0 2
4
2 1 0 2
4
0 2 0 2
```

**Output**

```text
3
2
-1
-1
```

**Explanation**

**Test case $1$:** Minimum number of moves required to reach the last index is $3$:
- Move $1$: Make a jump of length $1 \le A_1$. Thus, Chef moves from index $1$ to index $2$.
- Move $2$: Make a jump of length $1 \le A_2$. Thus, Chef moves from index $2$ to index $3$.
- Move $3$: Make a jump of length $1 \le A_3$. Thus, Chef moves from index $3$ to index $4$.

**Test case $2$:** Minimum number of moves required to reach the last index is $2$:
- Move $1$: Make a jump of length $1 \le A_1$. Thus, Chef moves from index $1$ to index $2$.
- Move $2$: Make a jump of length $2 \le A_2$. Thus, Chef moves from index $2$ to index $4$.

**Test case $3$:** It is not possible to reach the last index using any number of moves.

**Test case $4$:** It is not possible to reach the last index using any number of moves.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
1 1 2 2
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
4
1 2 0 2
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
4
2 1 0 2
```

**Output for this case**

```text
-1
```



#### Test case 4

**Input for this case**

```text
4
0 2 0 2
```

**Output for this case**

```text
-1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial: Minimum Jumps to Reach the End

In this lesson, we explore multiple approaches for solving the problem of finding the minimum number of jumps needed to reach the last index of an array. Given an array $A$ of size $N$, where at index $i$ you can jump up to $A_i$ steps forward, our goal is to compute the minimum number of moves needed to reach index $N-1$ (if possible). We now discuss two approaches: Greedy and Breadth-First Search (BFS).

---

## Approach 1: Greedy Algorithm

### Intuition and Explanation:
The greedy method is the most efficient for this problem, offering an optimal $O(N)$ solution. The main idea is to maintain:
- **$maxReach$:** The farthest index reachable from the current position.
- **$steps$:** The number of steps we can still take in the current jump.
- **$jumps$:** The count of jumps we have made so far.

**Algorithm steps:**
1. **Initialization:**
   Start from index $0$. Initialize $maxReach = A[0]$, $steps = A[0]$, and $jumps = 1$ (if $N > 1$).

2. **Iterate over the array:**
   For each index $i$ from $1$ to $N-1$, update $maxReach$ as the maximum of the current $maxReach$ and $i + A[i]$.

3. **Use up steps:**
   Decrement $steps$. When $steps$ becomes $0$, it means you have reached the limit of the current jump. At that point, increase the $jumps$ count and recalculate $steps$ as $maxReach - i$.

4. **Check for impossible cases:**
   If at any index you find that $i \geq maxReach$, then it is impossible to proceed, and the answer is $-1$.

5. **Return the answer:**
   The moment you reach the last index, return the number of jumps.

This approach effectively chooses the farthest you can reach at each step, which helps minimize the number of jumps.

### C++ Code:
```cpp
#include
#include
#include
using namespace std;

int minJumps(vector& arr) {
    int n = arr.size();
    if(n <= 1) return 0;
    if(arr[0] == 0) return -1;

    int maxReach = arr[0];
    int steps = arr[0];
    int jumps = 1;

    for(int i = 1; i < n; i++) {
        if(i == n - 1)
            return jumps;

        maxReach = max(maxReach, i + arr[i]);
        steps--;

        if(steps == 0) {
            jumps++;
            if(i >= maxReach)
                return -1;
            steps = maxReach - i;
        }
    }

    return -1;
}

int main() {
    int t;
    cin >> t;
    while(t--) {
        int n;
        cin >> n;
        vector arr(n);
        for(int i = 0; i < n; i++)
            cin >> arr[i];
        cout << minJumps(arr) << endl;
    }
    return 0;
}
```

### Python Code:
```python
def min_jumps(arr):
    n = len(arr)
    if n <= 1:
        return 0
    if arr[0] == 0:
        return -1

    max_reach = arr[0]
    steps = arr[0]
    jumps = 1

    for i in range(1, n):
        if i == n - 1:
            return jumps

        max_reach = max(max_reach, i + arr[i])
        steps -= 1

        if steps == 0:
            jumps += 1
            if i >= max_reach:
                return -1
            steps = max_reach - i

    return -1

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(min_jumps(arr))
```

---

## Approach 2: Breadth-First Search (BFS)

### Intuition and Explanation:
We can interpret the problem as finding the shortest path in an unweighted graph where each index represents a node. From the node at index $i$, there is an edge to every node $j$ such that $i+1 \leq j \leq i+A[i]$.

**Algorithm steps:**
1. **Initialization:**
   Use a queue to perform BFS from index $0$. Keep an array `visited` to record nodes that have been visited while tracking the number of jumps taken to reach each node.

2. **BFS Traversal:**
   For every node dequeued, explore all possible reachable indices. Once the last index is reached, return the level (number of jumps).

3. **Result:**
   If BFS completes without reaching the last index, return $-1$.

### C++ Code:
```cpp
#include
#include
#include
using namespace std;

int minJumpsBFS(vector& arr) {
    int n = arr.size();
    if(n <= 1) return 0;
    if(arr[0] == 0) return -1;

    vector visited(n, false);
    queue> q; // {index, jumps}

    q.push({0, 0});
    visited[0] = true;

    while(!q.empty()){
        auto [index, jumps] = q.front();
        q.pop();

        for (int i = index + 1; i < n && i <= index + arr[index]; i++){
            if (!visited[i]){
                if(i == n - 1)
                    return jumps + 1;
                q.push({i, jumps + 1});
                visited[i] = true;
            }
        }
    }

    return -1;
}

int main(){
    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        vector arr(n);
        for(int i = 0; i < n; i++){
            cin >> arr[i];
        }
        cout << minJumpsBFS(arr) << endl;
    }
    return 0;
}
```

### Python Code:
```python
from collections import deque

def min_jumps_bfs(arr):
    n = len(arr)
    if n <= 1:
        return 0
    if arr[0] == 0:
        return -1

    visited = [False] * n
    q = deque([(0, 0)])  # (index, jumps)
    visited[0] = True

    while q:
        index, jumps = q.popleft()

        for i in range(index + 1, min(n, index + arr[index] + 1)):
            if not visited[i]:
                if i == n - 1:
                    return jumps + 1
                q.append((i, jumps + 1))
                visited[i] = True

    return -1

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(min_jumps_bfs(arr))
```

---

### Conclusion

- The **Greedy approach** is optimal with a time complexity of $O(N)$ and is recommended for large inputs.
- The **BFS approach** offers an alternative view by treating the problem as a shortest path search in an unweighted graph, though its worst-case complexity may be higher.

Choose the method that best fits your needs based on the problem constraints and input size.

</details>

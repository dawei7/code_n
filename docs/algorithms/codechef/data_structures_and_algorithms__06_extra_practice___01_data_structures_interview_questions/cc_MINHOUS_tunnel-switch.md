# Tunnel Switch

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MINHOUS |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [MINHOUS](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_03/problems/MINHOUS) |

---

## Problem Statement

You live on a street with $N$ houses. The houses are labelled as $1$ $2$ . . . $N$, from left to right. You live in the house labelled $1$, i.e the left-most house. and you wish to reach the house labelled $N$ i.e. the right-most house.

There is a tunnel present in each house. The tunnel present in the housel labelled $i$ can be used to reach any house labelled $j$, such that $j - i \leq A_{i}$.

Determine the minimum number of houses you can visit in order to reach the right-most house.

---

## Input Format

- First line will contain $T$, number of testcases. Then the testcases follow.
- The first line of each testcase contains a single integer $N$.
- The second line of each testcase contains $N$ integers : $A_1, A_2 . . . A_N$.

It is guaranteed that the sum of the values of $N$ over all the testcases doesn't exceed $3*10^6$.

---

## Output Format

For each testcase, output in a single integer equal to the minimum number of houses you can visit in order to reach the right-most house.

---

## Constraints

- $1 \leq T \leq 50$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^5$

---

## Examples

**Example 1**

**Input**

```text
2
3
2 1 1
8
3 4 2 1 1 2 1 8
```

**Output**

```text
2
4
```

**Explanation**

**Test-case 1:**
You use the tunnel present in the house labelled $1$ to reach the house labelled $3$. Thus, you visited $2$ houses in total, the house labelled $1$ and the house labelled $3$.

**Test-case 2:**
One of the ways to reach the house labelled $N$ is to
- Use the tunnel in house labelled $1$ to reach house labelled $2$.
- Use the tunnel in house labelled $2$ to reach house labelled $6$.
- Use the tunnel in house labelled $6$ to reach house labelled $8$.

Thus we visit $4$ houses in total. There exists no way to reach house labelled $N$ by visiting less than $4$ houses.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
2 1 1
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
8
3 4 2 1 1 2 1 8
```

**Output for this case**

```text
4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial: Minimum Houses Visited Problem

In this problem, you are given a street with $N$ houses labelled from $1$ to $N$. At each house $i$, you can jump to any house $j$ such that $j - i \leq A_i$. You start from the first house and aim to reach the last house while minimizing the number of houses visited. This problem is a variant of the classic "Jump Game II".

In this updated editorial, we present the **Greedy Approach**, which is both correct and optimal for solving the problem.

---

## Greedy Approach (Optimal)

### Idea:
The Greedy algorithm efficiently finds the minimum number of houses to visit by keeping track of:
- **farthest:** The farthest house reachable from the current range of houses.
- **currentEnd:** The current boundary of the jump range.
- **jumps:** The count of jumps made.

### Explanation:
1. **Initialization:** Set `jumps = 0`, `currentEnd = 0`, and `farthest = 0`.
2. **Iteration:** Loop through each house index $i$ from $0$ to $N-2$.
   - Update the farthest reachable house:
     $$ farthest = \max(farthest, i + A[i]) $$
   - When you reach the end of the current jump range (i.e. $i == currentEnd$), increment the jump count and update `currentEnd` to the current `farthest`.
3. **Termination:** The loop terminates if `currentEnd` reaches or exceeds the last house index ($N - 1$).
4. **Final Answer:** The total number of houses visited is `jumps + 1` (including the starting house).

### Code Implementation:

#### C++ Code:
```cpp
#include
#include
#include
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int N;
        cin >> N;
        vector A(N);
        for (int i = 0; i < N; i++) {
            cin >> A[i];
        }
        if (N == 1) {
            cout << 1 << "\n";
            continue;
        }

        int jumps = 0, currentEnd = 0, farthest = 0;
        for (int i = 0; i < N - 1; i++) {
            farthest = max(farthest, i + A[i]);
            if (i == currentEnd) {
                jumps++;
                currentEnd = farthest;
            }
            if (currentEnd >= N - 1)
                break;
        }
        cout << jumps + 1 << "\n";
    }
    return 0;
}
```

#### Python Code:
```python
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    if N == 1:
        print(1)
        continue
    jumps = 0
    currentEnd = 0
    farthest = 0
    for i in range(N - 1):
        farthest = max(farthest, i + A[i])
        if i == currentEnd:
            jumps += 1
            currentEnd = farthest
        if currentEnd >= N - 1:
            break
    print(jumps + 1)
```

---

## Conclusion

The **Greedy Approach** offers an optimal solution to the Minimum Houses Visited Problem with a linear time complexity of $O(N)$. By dynamically maintaining the farthest reachable index and the current jump boundary, we can quickly determine the minimum number of jumps needed to reach the final house.

Happy coding and best of luck with your DSA interviews!

</details>

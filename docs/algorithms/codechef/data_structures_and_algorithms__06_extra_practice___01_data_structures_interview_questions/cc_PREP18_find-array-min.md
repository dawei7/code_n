# Find Array Min

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP18 |
| Difficulty Rating | 1500 |
| Difficulty Band | Two Pointers and Sliding Window Technique |
| Path | Data Structures and Algorithms |
| Lesson | Two-Pointer |
| Official Link | [PREP18](https://www.codechef.com/practice/course/two-pointers/POINTERP/problems/PREP18) |

---

## Problem Statement

You're given three non-decreasing arrays $A$, $B$, $C$ of length $N_A$, $N_B$, $N_C$. We define,

$f(i, j, k) = \max{(|A_i - B_j|, |B_j - C_k|, |A_i - C_k|)}$ where $1 \leq i \leq N_A, 1 \leq j \leq N_B, 1 \leq k \leq N_C$

Find the **minimum** possible value of $f(i, j, k)$ over all possible value of $i$, $j$, $k$.

Note: Array $A$ being non-decreasing means that $A_1 \leq A_2 \leq \dots \leq A_N$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first line of each test case contains three space-separated integers $N_A$, $N_B$, $N_C$ — the number of elements in the array $A$, $B$, $C$.
- The second line of each test case contains $N_A$ space-separated integers $A_1,A_2,\ldots,A_{N_A}$ — the elements of array $A$.
- The third line of each test case contains $N_B$ space-separated integers $B_1,B_2,\ldots,B_{N_B}$ — the elements of array $B$.
- The fourth line of each test case contains $N_C$ space-separated integers $C_1,C_2,\ldots,C_{N_C}$ — the elements of array $C$.

---

## Output Format

For each test case, output on a new line the **minimum** possible value of $f(i, j, k)$.

---

## Constraints

- $1 \leq T \leq 10$
- $1 \leq N_A, N_B, N_C \leq 10^5$
- $1 \leq A_i, B_i, C_i \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
3
4 2 2
2 5 10 15
4 4
10 15
1 1 1
5 
10
25
6 6 2
4 8 10 15 15 20
6 15 25 28 28 45 
10 15
```

**Output**

```text
6
20
0
```

**Explanation**

**Test case $1$**: Minimum value will be $f(3, 1, 1) = \max{(|10 - 4|, |4 - 10|, |10 - 10|)} = 6$.

**Test case $2$**: Minimum value will be $f(1, 1, 1) = \max{(|5 - 10|, |10 - 25|, |25 - 5|)} = 20$.

**Test case $3$**: Minimum value will be $f(4, 2, 2) = \max{(|15 - 15|, |15 - 15|, |15 - 15|)} = 0$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 2 2
2 5 10 15
4 4
10 15
```

**Output for this case**

```text
6
```



#### Test case 2

**Input for this case**

```text
1 1 1
5
10
25
```

**Output for this case**

```text
20
```



#### Test case 3

**Input for this case**

```text
6 6 2
4 8 10 15 15 20
6 15 25 28 28 45
10 15
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this lesson, we explore an efficient approach to solve the problem of finding the minimum possible value of
$$ f(i,j,k) = \max(|A[i]-B[j]|,\; |B[j]-C[k]|,\; |A[i]-C[k]|) $$
for three non-decreasing arrays $A$, $B$, and $C$. Instead of using less efficient methods, we focus on the optimal solution using the **Three Pointer (Optimal Merging)** technique.

---

### Approach: Three Pointer (Optimal Merging)

**Idea:**
This method employs three pointers (one for each array) to traverse the arrays concurrently. At each step, the algorithm computes the minimum and maximum among the three current elements and updates the answer with their difference. The pointer corresponding to the minimum element is then incremented, with the goal of reducing the range and possibly finding a tighter grouping of values.

**Explanation:**
- Initialize pointers $i$, $j$, and $k$ to $0$ for arrays $A$, $B$, and $C$ respectively.
- At each iteration:
  - Compute:
    $$ \text{minVal} = \min(A[i],\;B[j],\;C[k]) $$
    $$ \text{maxVal} = \max(A[i],\;B[j],\;C[k]) $$
  - Update the answer with the difference $(\text{maxVal} - \text{minVal})$.
  - Increment the pointer corresponding to the smallest current element.
- The overall time complexity is
$$ O(N_A + N_B + N_C), $$
which is optimal for large input sizes.

**C++ Code:**
```cpp
#include
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
        int NA, NB, NC;
        cin >> NA >> NB >> NC;
        vector A(NA), B(NB), C(NC);
        for (int i = 0; i < NA; i++)
            cin >> A[i];
        for (int i = 0; i < NB; i++)
            cin >> B[i];
        for (int i = 0; i < NC; i++)
            cin >> C[i];

        int i = 0, j = 0, k = 0;
        int ans = INT_MAX;
        while(i < NA && j < NB && k < NC){
            int a = A[i], b = B[j], c = C[k];
            int currMin = min({a, b, c});
            int currMax = max({a, b, c});
            ans = min(ans, currMax - currMin);

            if(currMin == a)
                i++;
            else if(currMin == b)
                j++;
            else
                k++;
        }
        cout << ans << "\n";
    }
    return 0;
}
```

**Python Code:**
```python
import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    NA, NB, NC = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    i = j = k = 0
    ans = float("inf")
    while i < NA and j < NB and k < NC:
        a, b, c = A[i], B[j], C[k]
        curr_min = min(a, b, c)
        curr_max = max(a, b, c)
        ans = min(ans, curr_max - curr_min)

        if curr_min == a:
            i += 1
        elif curr_min == b:
            j += 1
        else:
            k += 1
    print(ans)
```

---

**Conclusion:**
The **Three Pointer** technique is the optimal solution for this problem, offering an efficient linear time approach relative to the total number of elements. It not only simplifies the logic compared to exhaustive methods but also proves invaluable in interviews where demonstrating optimal strategies is key.

Happy coding and keep practicing!

</details>

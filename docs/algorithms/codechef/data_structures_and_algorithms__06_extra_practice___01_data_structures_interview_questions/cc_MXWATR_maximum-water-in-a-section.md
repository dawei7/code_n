# Maximum water in a section

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MXWATR |
| Difficulty Rating | 1700 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Stacks |
| Official Link | [MXWATR](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_10/problems/MXWATR) |

---

## Problem Statement

Chef owns a swimming pool with width $N$ meters which contains $N$ continuous walls with height $h_i$ (possible zero) and width $1$ meter each.

When it rains heavily, water is stored in the swimming pool in the form of sections (check Figure 1). Chef is busy calling his friends for a party. So, you need to determine the maximum water stored in **a section** among all the sections after a heavy rain.

Figure 1 :

![figure 1](https://s3.amazonaws.com/codechef_shared/download/Images/Aman/Copy+of+Figure+1.png)

This swimming pool has 3 sections :
- Section 2 has the maximum water i.e 10 units.
- Section 1 has 9 units of water.
- Section 3 contains 2 units of water.

So, the answer would be 10 units (maximum of all the sections)

---

## Input Format

- First line will contain $T$, number of testcases. Then the testcases follow.
- First line of each testcase contains an integer $N$ - number of walls $A$.
- Second line contains N space separated integers $h_1, h_2, ....., h_N$

---

## Output Format

For each testcase, output one integer in a single line - Maximum water stored among all sections.

---

## Constraints

- $ 1 \leq T \leq 10^3$
- $ 2 \leq N \leq 10^5$
- $0 \leq h_i \leq 10^6 $

Sum of $N$ over all test cases will not exceed $10^5$

---

## Examples

**Example 1**

**Input**

```text
2
4
5 0 2 6
6
3 1 4 0 3 5
```

**Output**

```text
8
5
```

**Explanation**

**Test Case 1** :
![Test Case 1](https://s3.amazonaws.com/codechef_shared/download/Images/Aman/Copy+of+Test+Case+1.png =200x300)

This swimming pool has only 1 section with 8 units of water.

**Test Case 2** :
![Test Case 2](https://s3.amazonaws.com/codechef_shared/download/Images/Aman/Copy+of+Test+Case+2.png =300x300)

This swimming pool has 2 sections :
- Section 1 has 2 units of water.
- Section 2 has maximum water i.e 5 units.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
5 0 2 6
```

**Output for this case**

```text
8
```



#### Test case 2

**Input for this case**

```text
6
3 1 4 0 3 5
```

**Output for this case**

```text
5
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial: Maximum Water Stored in a Section

In this problem, you are given a swimming pool formed by $N$ walls of width 1 meter each and various heights given by the array $h$. When it rains, water gets trapped between the walls. Our goal is to determine the maximum amount of water stored in **any contiguous section** of the pool. A "section" is defined as a continuous group of indices where water is trapped; these sections are separated by indices that do not contain any water.

Below, we explain two different approaches to solving this problem.

---

## Approach 1: Pre-computation of Left and Right Maximums

### Idea

For every index $i$, the water that can be trapped above it depends on the maximum height to its left and the maximum height to its right. Formally, we define:
$$
\text{leftMax}[i] = \max \{ h_0, h_1, \ldots, h_i \}
$$
$$
\text{rightMax}[i] = \max \{ h_i, h_{i+1}, \ldots, h_{N-1} \}
$$

Then, the water trapped at index $i$ is:
$$
\text{water}[i] = \max \Big( \min \big( \text{leftMax}[i],\, \text{rightMax}[i] \big) - h[i],\ 0 \Big)
$$

Once the water for each index is computed, we group these values into contiguous sections—sections being segments of consecutive indices where the water value is greater than zero—and then we take the maximum sum among all these sections.

### Code Implementation

Below are the implementations in both **C++** and **Python**.

#### C++ Code for Approach 1

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
        vector h(N);
        for (int i = 0; i < N; i++){
            cin >> h[i];
        }

        vector leftMax(N), rightMax(N);
        leftMax[0] = h[0];
        for (int i = 1; i < N; i++){
            leftMax[i] = max(leftMax[i-1], h[i]);
        }
        rightMax[N-1] = h[N-1];
        for (int i = N-2; i >= 0; i--){
            rightMax[i] = max(rightMax[i+1], h[i]);
        }

        vector water(N, 0);
        for (int i = 0; i < N; i++){
            long long minHeight = min(leftMax[i], rightMax[i]);
            if(minHeight > h[i])
                water[i] = minHeight - h[i];
        }

        long long maxSection = 0, currentSection = 0;
        for (int i = 0; i < N; i++){
            if(water[i] > 0)
                currentSection += water[i];
            else{
                maxSection = max(maxSection, currentSection);
                currentSection = 0;
            }
        }
        maxSection = max(maxSection, currentSection);

        cout << maxSection << "\n";
    }
    return 0;
}
```

#### Python Code for Approach 1

```python
import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    h = list(map(int, input().split()))

    leftMax = [0] * N
    rightMax = [0] * N

    leftMax[0] = h[0]
    for i in range(1, N):
        leftMax[i] = max(leftMax[i-1], h[i])

    rightMax[N-1] = h[N-1]
    for i in range(N-2, -1, -1):
        rightMax[i] = max(rightMax[i+1], h[i])

    water = [0] * N
    for i in range(N):
        minHeight = min(leftMax[i], rightMax[i])
        if minHeight > h[i]:
            water[i] = minHeight - h[i]

    maxSection = 0
    currentSection = 0
    for w in water:
        if w > 0:
            currentSection += w
        else:
            maxSection = max(maxSection, currentSection)
            currentSection = 0
    maxSection = max(maxSection, currentSection)
    print(maxSection)
```

---

## Approach 2: Two-Pointer Technique

### Idea

The two-pointer technique reduces the need for additional arrays by maintaining two pointers: one at the beginning (`left`) and one at the end (`right`) of the array. We also keep track of `left_max` (the highest wall seen so far from the left) and `right_max` (the highest wall seen so far from the right).

At every step, we compare $h[left]$ and $h[right]$:
- If $h[left] \leq h[right]$, we update or use `left_max` to compute the water stored at index `left` and then move the `left` pointer to the right.
- Otherwise, we update or use `right_max` to compute the water stored at index `right` and then move the `right` pointer to the left.

After computing the water for every index (stored in a `water` array), we group the contiguous indices with nonzero water values to determine sections, picking the maximum section sum.

### Code Implementation

Below are the implementations in both **C++** and **Python**.

#### C++ Code for Approach 2

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
        vector h(N);
        for(int i = 0; i < N; i++){
            cin >> h[i];
        }

        vector water(N, 0);
        int left = 0, right = N - 1;
        long long left_max = 0, right_max = 0;
        while(left <= right){
            if(h[left] <= h[right]){
                if(h[left] >= left_max)
                    left_max = h[left];
                else
                    water[left] = left_max - h[left];
                left++;
            } else {
                if(h[right] >= right_max)
                    right_max = h[right];
                else
                    water[right] = right_max - h[right];
                right--;
            }
        }

        long long maxSection = 0, currentSection = 0;
        for(int i = 0; i < N; i++){
            if(water[i] > 0)
                currentSection += water[i];
            else{
                maxSection = max(maxSection, currentSection);
                currentSection = 0;
            }
        }
        maxSection = max(maxSection, currentSection);
        cout << maxSection << "\n";
    }
    return 0;
}
```

#### Python Code for Approach 2

```python
import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    h = list(map(int, input().split()))

    water = [0] * N
    left, right = 0, N - 1
    left_max, right_max = 0, 0
    while left <= right:
        if h[left] <= h[right]:
            if h[left] >= left_max:
                left_max = h[left]
            else:
                water[left] = left_max - h[left]
            left += 1
        else:
            if h[right] >= right_max:
                right_max = h[right]
            else:
                water[right] = right_max - h[right]
            right -= 1

    maxSection = 0
    currentSection = 0
    for w in water:
        if w > 0:
            currentSection += w
        else:
            maxSection = max(maxSection, currentSection)
            currentSection = 0
    maxSection = max(maxSection, currentSection)
    print(maxSection)
```

---

## Final Thoughts

Both approaches work in $O(N)$ time and require $O(N)$ space.

- **Approach 1** is very intuitive: it precomputes the maximum height to the left and right for every index to determine the trapped water.
- **Approach 2** makes use of the two-pointer technique to optimize the computation by reducing redundant traversals.

Choose the approach that you find most clear and intuitive. Both methods help you understand the underlying concept of "trapping rain water" and how to group the water values into contiguous sections to solve the problem.

Happy Coding!

</details>

# Trapping Rainwater

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP19 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Two pointers |
| Official Link | [PREP19](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_11/problems/PREP19) |

---

## Problem Statement

You are given an array $A$ with $N$ non-negative integers. There are $N$ bars arranged adjacent to each other, such that the height of the $i^{th}$ bar is $A_i$ units and the width of each bar is $1$ unit.

Find out the total amount of water the bars can trap after raining.

**Note**: Use 64 bit integers.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains a single integer $N$ — the size of the array.
    - The next line contains $N$ space-separated integers - the elements of the array $A$.

---

## Output Format

For each test case, output on a new line, the total amount of water the bars can trap after raining.

---

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq N \leq 10^5$
- $0 \leq A_i \leq 10^9$
- The sum of $N$ over all test cases does not exceed $2\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
4
2 1 1 3
4
4 1 1 1
2
2 2
5
3 0 2 0 4
```

**Output**

```text
2
0
0
7
```

**Explanation**

**Test case $1$:** The arrangement of the bars looks like:

Thus, $2$ units of water is trapped with the bars.

**Test case $2$:** The arrangement of the bars looks like:

No water can be trapped with the bars.

**Test case $3$:** The arrangement of the bars looks like:

No water can be trapped with the bars.

**Test case $4$:** The arrangement of the bars looks like:

Thus, $7$ units of water is trapped with the bars.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
2 1 1 3
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
4
4 1 1 1
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
2
2 2
```

**Output for this case**

```text
0
```



#### Test case 4

**Input for this case**

```text
5
3 0 2 0 4
```

**Output for this case**

```text
7
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Trapping Rain Water Problem Editorial

In this lesson, we will learn how to determine the amount of water trapped between the bars after raining. The height of each bar is given in an array, and our goal is to calculate the total water that can be held by the configuration of the bars.

Given an array $A$ of size $N$, where each $A_i$ represents the height of the bar, the water that can be trapped at each index $i$ depends on the highest bar to the left and right of $i$. In particular, the water trapped at position $i$ is given by:

$$
water_i = \min(left_{max}(i),\, right_{max}(i)) - A_i,
$$

where $left_{max}(i)$ is the maximum height from the beginning of the array up to index $i$, and $right_{max}(i)$ is the maximum height from index $i$ to the end of the array. The total trapped water is the sum of all $water_i$ for indices where this is positive.

Below, we discuss three approaches to solve the problem.

---

## Approach 1: Precomputed Maximum Arrays (Dynamic Programming)

### Explanation
In this method, we precompute two arrays:
- **leftMax:** For each index $i$, it stores the maximum height from the start up to $i$.
- **rightMax:** For each index $i$, it stores the maximum height from index $i$ to the end.

Once these arrays are constructed, for each index $i$, we compute the water trapped as:
$$
water_i = \min(leftMax[i],\, rightMax[i]) - A_i.
$$
Summing this over all indices gives the total water.

**Time Complexity:** $O(N)$
**Space Complexity:** $O(N)$

### Code Implementation

#### C++
```cpp
#include
#include
#include
using namespace std;

long long trapRainWater(const vector& height) {
    int n = height.size();
    if (n == 0) return 0;

    vector leftMax(n), rightMax(n);
    leftMax[0] = height[0];
    for (int i = 1; i < n; i++) {
        leftMax[i] = max(leftMax[i - 1], height[i]);
    }

    rightMax[n - 1] = height[n - 1];
    for (int i = n - 2; i >= 0; i--) {
        rightMax[i] = max(rightMax[i + 1], height[i]);
    }

    long long water = 0;
    for (int i = 0; i < n; i++) {
        water += min(leftMax[i], rightMax[i]) - height[i];
    }

    return water;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector heights(n);
        for (int i = 0; i < n; i++) {
            cin >> heights[i];
        }
        cout << trapRainWater(heights) << "\n";
    }

    return 0;
}
```

#### Python
```python
def trapRainWater(heights):
    n = len(heights)
    if n == 0:
        return 0
    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = heights[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], heights[i])

    right_max[n - 1] = heights[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], heights[i])

    water = 0
    for i in range(n):
        water += min(left_max[i], right_max[i]) - heights[i]
    return water

t = int(input())
for _ in range(t):
    n = int(input())
    heights = list(map(int, input().split()))
    print(trapRainWater(heights))
```

---

## Approach 2: Two Pointers

### Explanation
The two pointers approach optimizes space by eliminating the need for extra arrays. We maintain two pointers, `left` and `right`, and two variables, `left_max` and `right_max`, to keep track of the maximum height encountered so far from the left and right respectively.

The idea is as follows:
- If $A[left] < A[right]$, then the water at `left` is determined by `left_max`. Update `left_max` if $A[left]$ is greater; otherwise, add $left\_max - A[left]$ to the water.
- Otherwise, the water at `right` is determined by `right_max`. Update `right_max` if $A[right]$ is greater; otherwise, add $right\_max - A[right]$ to the water.

We then move the pointer that has the smaller bar.

**Time Complexity:** $O(N)$
**Space Complexity:** $O(1)$

### Code Implementation

#### C++
```cpp
#include
#include
#include
using namespace std;

long long trapRainWaterTwoPointers(const vector& height) {
    int left = 0, right = height.size() - 1;
    long long water = 0;
    int left_max = 0, right_max = 0;

    while (left <= right) {
        if (height[left] < height[right]) {
            if (height[left] >= left_max)
                left_max = height[left];
            else
                water += left_max - height[left];
            left++;
        } else {
            if (height[right] >= right_max)
                right_max = height[right];
            else
                water += right_max - height[right];
            right--;
        }
    }
    return water;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector heights(n);
        for (int i = 0; i < n; i++) {
            cin >> heights[i];
        }
        cout << trapRainWaterTwoPointers(heights) << "\n";
    }

    return 0;
}
```

#### Python
```python
def trapRainWaterTwoPointers(heights):
    left, right = 0, len(heights) - 1
    left_max, right_max = 0, 0
    water = 0

    while left <= right:
        if heights[left] < heights[right]:
            if heights[left] >= left_max:
                left_max = heights[left]
            else:
                water += left_max - heights[left]
            left += 1
        else:
            if heights[right] >= right_max:
                right_max = heights[right]
            else:
                water += right_max - heights[right]
            right -= 1
    return water

t = int(input())
for _ in range(t):
    n = int(input())
    heights = list(map(int, input().split()))
    print(trapRainWaterTwoPointers(heights))
```

---

## Approach 3: Stack Based Approach

### Explanation
The stack-based approach uses a stack to keep track of indices whose water trapping capacity is not yet calculated. We iterate over each bar and perform the following:
- While the current bar is higher than the bar at the top of the stack, it means we have found a right boundary that can trap water.
- Pop the top of the stack and calculate the distance between the current index and the new top of the stack.
- The water trapped over the popped bar is determined by the distance multiplied by the minimum of the two boundaries minus the height of the popped bar.

**Time Complexity:** $O(N)$ on average
**Space Complexity:** $O(N)$

### Code Implementation

#### C++
```cpp
#include
#include
#include
#include
using namespace std;

long long trapRainWaterStack(const vector& height) {
    int n = height.size();
    long long water = 0;
    stack st;

    for (int i = 0; i < n; i++) {
        while (!st.empty() && height[i] > height[st.top()]) {
            int top = st.top();
            st.pop();
            if (st.empty())
                break;
            int distance = i - st.top() - 1;
            int bounded_height = min(height[i], height[st.top()]) - height[top];
            water += (long long)distance * bounded_height;
        }
        st.push(i);
    }
    return water;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector heights(n);
        for (int i = 0; i < n; i++) {
            cin >> heights[i];
        }
        cout << trapRainWaterStack(heights) << "\n";
    }

    return 0;
}
```

#### Python
```python
def trapRainWaterStack(heights):
    water = 0
    stack = []

    for i, h in enumerate(heights):
        while stack and h > heights[stack[-1]]:
            top = stack.pop()
            if not stack:
                break
            distance = i - stack[-1] - 1
            bounded_height = min(h, heights[stack[-1]]) - heights[top]
            water += distance * bounded_height
        stack.append(i)
    return water

t = int(input())
for _ in range(t):
    n = int(input())
    heights = list(map(int, input().split()))
    print(trapRainWaterStack(heights))
```

---

## Conclusion
We have explored three distinct approaches to solve the Trapping Rain Water problem:
1. **Precomputed Maximum Arrays:** Easy to understand and implement, but uses extra space.
2. **Two Pointers:** Space-optimized solution that efficiently calculates the trapped water using two indices.
3. **Stack Based Approach:** A more advanced technique that uses a stack to handle variable boundaries dynamically.

Each method has its own advantages. Beginners are encouraged to start with the precomputed arrays approach and then explore the two pointers method to optimize space. The stack approach offers additional insights into handling problems with variable boundaries using data structures.

Happy Coding!

</details>

# Largest Rectangle in Histogram

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP22 |
| Difficulty Rating | 1700 |
| Difficulty Band | Stacks and Queues |
| Path | Data Structures and Algorithms |
| Lesson | Stacks |
| Official Link | [PREP22](https://www.codechef.com/learn/course/stacks-and-queues/LSTACKS02/problems/PREP22) |

---

## Problem Statement

You are given an array $A_1, A_2, \dots, A_N$ of length $N$. $A$ represents a histogram which means the height of the $i^{th}$ bar will be $A_i$ units and the width of each bar is $1$ unit.

Find the area of the largest rectangle in the histogram.

---

## Function Declaration

### Function Name
$largestRectangleArea$ – This function calculates the maximum rectangular area possible within the given histogram.

### Parameters

$N$ : An integer representing the number of bars in the histogram.
$A$ : An array of integers representing the heights of the histogram bars.

### Return Value

Returns an integer: the area of the largest rectangle that can be formed in the histogram.

---

### Constraints:
$1 \leq T \leq 10$
$1 \le N \le 10^5$
$0 \le A_i \le 10^9$

*The input and output formats provided below are only for testing with custom inputs. You only need to return the value. Printing is handled automatically.*

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first line of each test case contains an integer $N$ - the length of the array $A$.
- The second line of each test case contains $N$ space-separated integers $A_1,A_2,\ldots,A_N$.

---

## Output Format

For each test case, output on a new line the area of the largest rectangle in the histogram.

---

## Constraints

- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- The sum of $N$ over all test cases won't exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
4
2 6 8 4
4
5 10 5 2
2
5 5
```

**Output**

```text
12
15
10
```

**Explanation**

**Test case $1$**: Largest rectangle will create using $A_2$, $A_3$. So height will be $\min(6, 8) = 6$, width will be $2$. So area will be $12$.

**Test case $2$**: Largest rectangle will create using $A_1$, $A_2$, $A_3$. So height will be $\min(5, 10, 5) = 5$, width will be $3$. So area will be $15$.

**Test case $3$**: Largest rectangle will create using $A_1$, $A_2$. So height will be $\min(5, 5) = 5$, width will be $2$. So area will be $10$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
2 6 8 4
```

**Output for this case**

```text
12
```



#### Test case 2

**Input for this case**

```text
4
5 10 5 2
```

**Output for this case**

```text
15
```



#### Test case 3

**Input for this case**

```text
2
5 5
```

**Output for this case**

```text
10
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this lesson, we will discuss how to solve the "Largest Rectangle in Histogram" problem. You are given an array $A_1, A_2, \dots, A_N$ where each $A_i$ represents the height of a histogram bar of width $1$. The goal is to compute the area of the largest rectangle that can be formed within this histogram.

Below, we present the **optimal approach** that leverages a stack to achieve an overall time complexity of $O(N)$. This method is both efficient and scalable, making it ideal for handling large inputs.

---

## Optimal Approach: Stack Based

### Idea
The optimal method uses a stack to maintain the indices of histogram bars in increasing order. Here is the general strategy:
- **Iteration:** Traverse through each bar in the histogram.
- **Stack Maintenance:** For each bar, if its height is less than the bar referenced by the index at the top of the stack, pop the stack and calculate the area with the popped bar as the smallest (limiting) height.
- **Area Calculation:** The width for the rectangle is computed as the difference between the current index and the new top of the stack (or the current index itself if the stack is empty).
- **Final Sweep:** After iterating through all bars, perform an extra iteration (by considering a bar of height $0$) to ensure that all bars are processed.
- **Maximization:** Update the maximum area encountered during these steps.

### Complexity
Each bar is pushed and popped from the stack at most once, resulting in a time complexity of $O(N)$, which is optimal for this problem.

### Code Implementation

#### C++ Code
```cpp
#include
#include
#include
#include
using namespace std;

long long largestRectangleArea(vector& heights) {
    int n = heights.size();
    stack s;
    long long maxArea = 0;

    for (int i = 0; i <= n; i++) {
        int currentHeight = (i == n ? 0 : heights[i]);

        while (!s.empty() && currentHeight < heights[s.top()]) {
            int height = heights[s.top()];
            s.pop();

            int width = s.empty() ? i : i - s.top() - 1;
            maxArea = max(maxArea, (long long)height * width);
        }

        s.push(i);
    }

    return maxArea;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector heights(n);
        for (int i = 0; i < n; i++) {
            cin >> heights[i];
        }
        cout << largestRectangleArea(heights) << "\n";
    }

    return 0;
}
```

#### Python Code
```python
def largest_rectangle_stack(heights):
    stack = []
    max_area = 0
    n = len(heights)

    for i in range(n + 1):
        current_height = 0 if i == n else heights[i]
        while stack and current_height < heights[stack[-1]]:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    return max_area

if __name__ == "__main__":
    import sys
    input_data = sys.stdin.read().split()
    t = int(input_data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(input_data[index])
        index += 1
        heights = list(map(int, input_data[index:index+n]))
        index += n
        results.append(largest_rectangle_stack(heights))
    print("\n".join(map(str, results)))
```

---

## Conclusion

The **Stack Based** approach is an optimal solution for the "Largest Rectangle in Histogram" problem with a time complexity of $O(N)$. This strategy efficiently computes the maximum rectangle area by capitalizing on the properties of a stack, making it highly effective for large-scale histograms. Mastering this technique not only equips you to solve this specific problem but also enhances your understanding of how stacks can be utilized to optimize other algorithmic challenges.

</details>

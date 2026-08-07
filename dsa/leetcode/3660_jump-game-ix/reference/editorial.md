### Approach 1: Interval Divide and Conquer

#### Intuition

Let us simulate the process of element transfer. Let the length of $\textit{nums}$ be $n$, and first consider the global maximum, denoted as $r_{\textit{max}1}$, located at index $i_1$.

This maximum value splits the entire interval into two parts. It is easy to see that all elements to the right of $i_1$ can jump to $r_{\textit{max}1}$, and this is clearly the globally optimal solution for these elements.

Now consider the elements to the left of $i_1$. Let the prefix maximum in the interval $[0, i_1 - 1]$ be $r_{\textit{max}2}$, located at index $i_2$. This value further divides the interval $[0, i_1 - 1]$ into two parts. We first consider the elements on the right side of this maximum, that is, the elements in the interval $[i_2, i_1 - 1]$.

Let the minimum value in the previously processed right interval $[i_1, n - 1]$ be $r_{\textit{min}}$. Then we have the following two cases:

- If $r_{\textit{max}2} \le r_{\textit{min}}$, it means that none of the elements in the current interval can transfer to the right interval $[i_1, n - 1]$. Therefore, the elements in $[i_2, i_1 - 1]$ can only transfer to $r_{\textit{max}2}$, which is the optimal solution for them.

- If $r_{\textit{max}2} > r_{\textit{min}}$, then all elements in the current interval $[i_2, i_1 - 1]$ can first reach $r_{\textit{max}2}$, then transfer through the element corresponding to $r_{\textit{min}}$, and finally reach the maximum value in the right interval. Hence, the optimal solution for these elements becomes $r_{\textit{max}1}$.

Applying the same reasoning, we observe that the subproblem on the interval $[0, i_2 - 1]$ has exactly the same structure. It again involves selecting the prefix maximum, splitting the interval, and deciding whether the current right part can transfer to the previously processed right interval.

This repeating structure suggests an interval divide-and-conquer approach. We dynamically maintain the maximum and minimum values of the right interval while processing smaller prefixes.

We first preprocess the prefix maximum values. Then we apply divide and conquer as described above. What remains is to clearly define $r_{\textit{min}}$ and $r_{\textit{max}}$, and how to update them during transitions.

Let the current interval be $[0, i]$, and let the prefix maximum be at index $i'$. Based on whether the interval $[i', i]$ can transfer to the previously processed right interval, we have the following transitions:

- $r_{\textit{max}}$ represents the final target value for the current interval. If transfer is possible, it inherits the previous $r_{\textit{max}}$, since that value is guaranteed to be greater than or equal to the current prefix maximum. Otherwise, $r_{\textit{max}}$ is updated to the current prefix maximum.

- $r_{\textit{min}}$ represents the minimum value among elements that can reach $r_{\textit{max}}$. If the current prefix maximum is greater than $r_{\textit{min}}$, then the interval $[i', i]$ can transfer to the right side. In this case, we update
  $r_{\textit{min}} = \min\left(r_{\textit{min}}, \min_{i' \le k \le i} (\textit{nums}[k])\right)$
  thereby incorporating values from the current interval.

- Even when transfer is not possible, we still apply the same update rule. At first, this may seem incorrect, because the previous $r_{\textit{min}}$ corresponds to an unreachable interval. However, in this case, the previous $r_{\textit{min}}$ must be greater than or equal to the current prefix maximum. Therefore, the new minimum will necessarily come from the current interval $[i', i]$, effectively discarding the old value. Hence, using the same update formula remains valid.

#### Implementation

```python
class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)

        ans = [0] * n
        # [value, index]
        prev_max = [(0, 0)] * n

        prev = (-math.inf, -1)
        for i, value in enumerate(nums):
            if value > prev[0]:
                prev = (value, i)
            prev_max[i] = prev

        def process(r: int, right_min: float, right_max: float) -> None:
            p_max, pivot_index = prev_max[r]
            curr_max = p_max if p_max <= right_min else right_max

            next_right_min = min(p_max, right_min)
            for i in range(pivot_index, r + 1):
                ans[i] = curr_max
                next_right_min = min(next_right_min, nums[i])

            if pivot_index == 0:
                return

            process(pivot_index - 1, next_right_min, curr_max)

        process(n - 1, math.inf, 0)

        return ans
```

#### Complexity Analysis

Let $n$ be the length of $\textit{nums}$.

- Time complexity: $O(n)$.

  Preprocessing the prefix maximum values takes $O(n)$. The intervals formed during the divide-and-conquer process partition the entire array without overlap, so the total time spent on interval processing is also $O(n)$.

- Space complexity: $O(n)$.

  Storing the prefix maximum values requires $O(n)$ space.

---

### Approach 2: Monotonic Stack

#### Intuition

Let us analyze the problem from another perspective. The condition in the problem can be interpreted as follows: if two elements in $\textit{nums}$ form an **inversion pair**, then they can **reach each other**. This naturally leads to viewing the problem as maintaining **connected components** in an undirected graph.

From this perspective, we can observe an important property. For the current element $\textit{nums}[i]$ and any connected component to its left, if $\textit{nums}[i]$ is smaller than the maximum value in that component, then it can merge with that component. Moreover, due to bidirectional connectivity, multiple components can merge together through $\textit{nums}[i]$, forming a larger connected component.

Now consider two adjacent connected components $A$ and $B$ from left to right. Let their maximum values be $a_{\textit{max}}$ and $b_{\textit{max}}$, respectively. Then we must have $a_{\textit{max}} \le b_{\textit{max}}$. If the current element satisfies $\textit{nums}[i] < a_{\textit{max}}$, then it will also satisfy $\textit{nums}[i] < b_{\textit{max}}$, meaning it can merge with both components. As a result, $A$, $B$, and $\textit{nums}[i]$ form a single larger connected component.

This implies that connected components are **continuous segments** in the array, and their maximum values follow a **monotonic order**. Connectivity depends only on adjacent components, not on distant ones.

Based on this observation, we do not need to explicitly simulate paths. Instead, we can maintain these connected components using a **monotonic stack**, where each component is represented as $(\textit{value}, \textit{left}, \textit{right})$.

We iterate through $\textit{nums}$ from left to right. For each element, we repeatedly merge it with components on the stack while the merging condition holds. After merging, we push the resulting component back onto the stack.

Finally, for each connected component, all its elements will have the same answer, which is the maximum value of that component.

#### Implementation

```python
class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        # [value, left, right]
        stack = []

        for i in range(n):
            curr_val = nums[i]
            curr_left = i
            curr_right = i

            while stack and stack[-1][0] > nums[i]:
                top_val, top_left, top_right = stack.pop()
                curr_val = max(curr_val, top_val)
                curr_left = top_left

            stack.append((curr_val, curr_left, curr_right))

        for i in range(len(stack)):
            for j in range(stack[i][1], stack[i][2] + 1):
                ans[j] = stack[i][0]

        return ans
```

#### Complexity Analysis

Let $n$ be the length of $\textit{nums}$.

- Time complexity: $O(n)$.

  Each element is pushed to and popped from the monotonic stack at most once, resulting in at most $2n$ operations. Therefore, stack operations take $O(n)$ time. Additionally, constructing the final answer from the connected components also takes $O(n)$ time, giving an overall time complexity of $O(n)$.

- Space complexity: $O(n)$.

  The monotonic stack requires $O(n)$ space.

---
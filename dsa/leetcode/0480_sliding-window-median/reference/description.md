### 1. Description

The **median** is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.

- For examples, if `arr = [2,<u>3</u>,4]`, the median is `3`.

- For examples, if `arr = [1,<u>2,3</u>,4]`, the median is $(2 + 3) / 2 = 2.5$.

You are given an integer array `nums` and an integer `k`. There is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

Return *the median array for each window in the original array*. Answers within $10^{-5}$ of the actual value will be accepted.

### 2. Function Contract

**Inputs**

- `nums`: the integer array traversed by the window.
- `k`: the number of consecutive elements in every window.

Let $n = \lvert\texttt{nums}\rvert$. The contract guarantees that `k` is at least one and at most `n`, so every
window is nonempty and there are exactly $n-k+1$ window positions.

**Return value**

Return a floating-point list of length $n-k+1$. Entry $i$ is the median of $nums[i:i + k]$: the central ordered value
when `k` is odd, or the mean of the two central ordered values when `k` is even.

### 3. Examples

#### Example 1

- **Input:** `nums = [1,3,-1,-3,5,3,6,7], k = 3`
- **Output:** `[1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]`
- **Explanation:** Window position                Median
---------------                -----
[**1  3  -1**] -3  5  3  6  7        1
1 [**3  -1  -3**] 5  3  6  7       -1
1  3 [**-1  -3  5**] 3  6  7       -1
1  3  -1 [**-3  5  3**] 6  7        3
1  3  -1  -3 [**5  3  6**] 7        5
1  3  -1  -3  5 [**3  6  7**]       6

#### Example 2

- **Input:** `nums = [1,2,3,4,2,3,1,4,2], k = 3`
- **Output:** `[2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]`

### 4. Constraints

- $1 \le k \le \text{nums.length} \le 10^{5}$

- $-2^{31} \le \text{nums}[i] \le 2^{31} - 1$

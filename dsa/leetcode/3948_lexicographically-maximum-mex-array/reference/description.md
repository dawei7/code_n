### 1. Description

You are given an integer array `nums`.

You want to construct an array `result` by repeatedly performing the following operation until `nums` becomes empty:

- Choose an integer `k` such that $1 \le k \le len(nums)$.

- Compute the **MEX** of the first `k` elements of `nums`.

- Append this **MEX** to `result`.

- Remove the first `k` elements from `nums`.

Return the **lexicographically maximum** array `result` that can be obtained after performing the operations.

The **MEX** of an array is the **smallest non-negative** integer not present in the array.

An array `a` is **lexicographically greater** than an array `b` if in the first position where `a` and `b` differ, array `a` has an element that is greater than the corresponding element in `b`. If the first `min(a.length, b.length)` elements do not differ, then the longer array is the **lexicographically greater** one.

### 2. Function Contract

**Inputs**

- `nums`: A nonempty integer array whose entries are non-negative.

Let $n=\lvert\texttt{nums}\rvert$.

**Return value**

Return the lexicographically maximum array of prefix MEX values obtainable by removing one nonempty prefix after another until `nums` is empty.

### 3. Examples

#### Example 1

- **Input:** nums = [0,1,0]

- **Output:** [2,1]

- **Explanation:** 

- Take the first $k = 2$ elements `[0, 1]` which has MEX = 2. Current $result = [2]$.

- Remaining array `[0]` has MEX = 1. Thus, the final $result = [2, 1]$.

#### Example 2

- **Input:** nums = [1,0,2]

- **Output:** [3]

- **Explanation:** 

- Take the first $k = 3$ elements `[1, 0, 2]` which has MEX = 3.

- `nums` is now empty. Thus, the final $result = [3]$.

#### Example 3

- **Input:** nums = [3,1]

- **Output:** [0,0]

- **Explanation:** 

- Take $k = 1$, first element `[3]` has MEX = 0. Current $result = [0]$.

- Remaining array `[1]` has MEX = 0. Thus, the final $result = [0, 0]$.

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $0 \le \text{nums}[i] \le 10^{5}$

## Description

You are given an integer array `nums`.

A **subarray** of `nums` is called **stable** if it contains **no inversions**, i.e., there is no pair of indices `i < j` such that $\text{nums}[i] > \text{nums}[j]$.

You are also given a **2D integer array** `queries` of length `q`, where each $\text{queries}[i] = [l_{i}, r_{i}]$ represents a query. For each query $[l_{i}, r_{i}]$, compute the number of **stable subarrays** that lie entirely within the segment $nums[l_{i}..r_{i}]$.

Return an integer array `ans` of length `q`, where $\text{ans}[i]$ is the answer to the $$i^{\text{th}}$$ query.​​​​​​​​​​​​​​

**Note**:

- A single element subarray is considered stable.
### Function Contract

**Inputs**

- `nums`: The integer array whose contiguous subarrays are classified.
- `queries`: A list of inclusive index pairs $[l_{i},r_{i}]$ into `nums`.

Let $n=\texttt{nums.length}$ and $q=\texttt{queries.length}$. Each result counts subarrays by their index ranges, so equal-valued subarrays at different positions count separately.

**Return value**

Return $q$ integers, one per query, giving the number of nonempty, non-decreasing subarrays wholly contained in its requested segment.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums = [3,1,2], queries = [[0,1],[1,2],[0,2]]

**Output:** [2,3,4]

**Explanation:**​​​​​

- For $\text{queries}[0] = [0, 1]$, the subarray is `[nums[0], nums[1]] = [3, 1]`.

		<li>The stable subarrays are `[3]` and `[1]`. The total number of stable subarrays is 2.

	</li>
- For $\text{queries}[1] = [1, 2]$, the subarray is `[nums[1], nums[2]] = [1, 2]`.

		<li>The stable subarrays are `[1]`, `[2]`, and `[1, 2]`. The total number of stable subarrays is 3.

	</li>
- For $\text{queries}[2] = [0, 2]$, the subarray is `[nums[0], nums[1], nums[2]] = [3, 1, 2]`.

		<li>The stable subarrays are `[3]`, `[1]`, `[2]`, and `[1, 2]`. The total number of stable subarrays is 4.

	</li>

Thus, $ans = [2, 3, 4]$.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [2,2], queries = [[0,1],[0,0]]

**Output:** [3,1]

**Explanation:**

- For $\text{queries}[0] = [0, 1]$, the subarray is `[nums[0], nums[1]] = [2, 2]`.

		<li>The stable subarrays are `[2]`, `[2]`, and `[2, 2]`. The total number of stable subarrays is 3.

	</li>
- For $\text{queries}[1] = [0, 0]$, the subarray is `[nums[0]] = [2]`.

		<li>The stable subarray is `[2]`. The total number of stable subarrays is 1.

	</li>

Thus, $ans = [3, 1]$.

</div>
### Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{5}$

- $1 \le \text{queries.length} \le 10^{5}$

- $\text{queries}[i] = [l_{i}, r_{i}]$

- $0 \le l_{i} \le r_{i} \le \text{nums.length} - 1$
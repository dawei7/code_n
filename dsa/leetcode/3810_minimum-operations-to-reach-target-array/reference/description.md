## Description

You are given two integer arrays `nums` and `target`, each of length `n`, where $\text{nums}[i]$ is the current value at index `i` and $\text{target}[i]$ is the desired value at index `i`.

You may perform the following operation any number of times (including zero):

- Choose an integer value `x`

- Find all **maximal contiguous segments** where $\text{nums}[i] = x$ (a segment is **maximal** if it cannot be extended to the left or right while keeping all values equal to `x`)

- For each such segment `[l, r]`, update **simultaneously**:

		<li>$\text{nums}[l] = \text{target}[l], nums[l + 1] = target[l + 1], ..., \text{nums}[r] = \text{target}[r]$

	</li>

Return the **minimum** number of operations required to make `nums` equal to `target`.
### Function Contract

**Inputs**

- `nums`: A non-empty integer array representing the current values.
- `target`: An integer array of the same length representing the required values.

Let $N=\lvert\texttt{nums}\rvert=\lvert\texttt{target}\rvert$. One operation chooses a value from the current `nums` and simultaneously replaces every element in every maximal segment of that value with the corresponding element of `target`.

**Return value**

Return the fewest operations required to transform `nums` into `target` exactly.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [1,2,3], target = [2,1,3]

**Output:** 2

**Explanation:**​​​​​​​

- Choose $x = 1$: maximal segment `[0, 0]` updated -> nums becomes `[2, 2, 3]`

- Choose $x = 2$: maximal segment `[0, 1]` updated ($\text{nums}[0]$ stays 2, $\text{nums}[1]$ becomes 1) -> `nums` becomes `[2, 1, 3]`

- Thus, 2 operations are required to convert `nums` to `target`.​​​​​​​​​​​​​​

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [4,1,4], target = [5,1,4]

**Output:** 1

**Explanation:**

- Choose $x = 4$: maximal segments `[0, 0]` and `[2, 2]` updated ($\text{nums}[2]$ stays 4) -> `nums` becomes `[5, 1, 4]`

- Thus, 1 operation is required to convert `nums` to `target`.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [7,3,7], target = [5,5,9]

**Output:** 2

**Explanation:**

- Choose $x = 7$: maximal segments `[0, 0]` and `[2, 2]` updated -> `nums` becomes `[5, 3, 9]`

- Choose $x = 3$: maximal segment `[1, 1]` updated -> `nums` becomes `[5, 5, 9]`

- Thus, 2 operations are required to convert `nums` to `target`.

</div>
### Constraints

- $1 \le n = \text{nums.length} = \text{target.length} \le 10^{5}$

- $1 \le \text{nums}[i], \text{target}[i] \le 10^{5}$
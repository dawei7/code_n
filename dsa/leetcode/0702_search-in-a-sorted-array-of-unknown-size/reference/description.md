### 1. Description

This is an ***interactive problem***.

You have a sorted array of **unique** elements and an **unknown size**. You do not have an access to the array but you can use the `ArrayReader` interface to access it. You can call `ArrayReader.get(i)` that:

- returns the value at the $i^{\text{th}}$ index (**0-indexed**) of the secret array (i.e., $\text{secret}[i]$), or

- returns $2^{31} - 1$ if the `i` is out of the boundary of the array.

You are also given an integer `target`.

Return the index `k` of the hidden array where $\text{secret}[k] = target$ or return `-1` otherwise.

You must write an algorithm with `O(log n)` runtime complexity.

### 2. Function Contract

$solve(reader: \text{list}[int], target: int) -> int$

The source-native method is `Solution.search(reader: ArrayReader, target: int) -> int`. The standalone app receives the hidden values as the list `reader` and wraps them in a local equivalent of LeetCode's `ArrayReader`; callers of the search logic still access values only through `get`.

**Inputs**

- `reader`: the strictly increasing secret values used by the app-local reader adapter.
- `target`: the integer to locate.

**Return value**

Return the target's unique zero-based index, or `-1` if it does not occur. An out-of-bound reader access yields $2^{31} - 1$, which is greater than every legal value and target.

### 3. Examples

#### Example 1

- **Input:** $secret = [-1,0,3,5,9,12], target = 9$
- **Output:** `4`
- **Explanation:** 9 exists in secret and its index is 4.

#### Example 2

- **Input:** $secret = [-1,0,3,5,9,12], target = 2$
- **Output:** `-1`
- **Explanation:** 2 does not exist in secret so return -1.

### 4. Constraints

- $1 \le \text{secret.length} \le 10^{4}$

- $-10^{4} \le \text{secret}[i], target \le 10^{4}$

- `secret` is sorted in a strictly increasing order.

### 1. Description

Given a binary array `nums`, return *the maximum number of consecutive *`1`*'s in the array if you can flip at most one* `0`.

### 2. Function Contract

**Inputs**

- `nums`: a nonempty array containing only `0` and `1`

**Return value**

- Return the greatest length of a contiguous run that can consist entirely of `1` after flipping at most one `0`.

The flip is optional, so an existing all-`1` run is a valid choice without modifying the array.

### 3. Examples

#### Example 1

- **Input:** `nums = [1,0,1,1,0]`
- **Output:** `4`
- **Explanation:** 
- If we flip the first zero, nums becomes [1,1,1,1,0] and we have 4 consecutive ones.
- If we flip the second zero, nums becomes [1,0,1,1,1] and we have 3 consecutive ones.
The max number of consecutive ones is 4.

#### Example 2

- **Input:** `nums = [1,0,1,1,0,1]`
- **Output:** `4`
- **Explanation:** 
- If we flip the first zero, nums becomes [1,1,1,1,0,1] and we have 4 consecutive ones.
- If we flip the second zero, nums becomes [1,0,1,1,1,1] and we have 4 consecutive ones.
The max number of consecutive ones is 4.

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $\text{nums}[i]$ is either `0` or `1`.

**Follow up:** What if the input numbers come in one by one as an infinite stream? In other words, you can't store all numbers coming from the stream as it's too large to hold in memory. Could you solve it efficiently?

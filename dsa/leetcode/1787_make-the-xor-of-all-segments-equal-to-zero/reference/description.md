### 1. Description

You are given an array `nums`​​​ and an integer `k`​​​​​. The XOR of a segment `[left, right]` where $left \le right$ is the `XOR` of all the elements with indices between `left` and `right`, inclusive: $\text{nums}[left] XOR nums[left+1] XOR ... XOR \text{nums}[right]$.

Return *the minimum number of elements to change in the array *such that the `XOR` of all segments of size `k`​​​​​​ is equal to zero.

### 2. Function Contract

**Inputs**

- `nums`: Input parameter (`List[int]`).
- `k`: Input parameter (`int`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** `nums = [1,2,0,3,0], k = 1`
- **Output:** `3`
- **Explanation:** Modify the array from [<u>**1**</u>,<u>**2**</u>,0,<u>**3**</u>,0] to from [<u>**0**</u>,<u>**0**</u>,0,<u>**0**</u>,0].

#### Example 2

- **Input:** `nums = [3,4,5,2,1,7,3,4,7], k = 3`
- **Output:** `3`
- **Explanation:** Modify the array from [3,4,**<u>5</u>**,**<u>2</u>**,**<u>1</u>**,7,3,4,7] to [3,4,**<u>7</u>**,**<u>3</u>**,**<u>4</u>**,7,3,4,7].

#### Example 3

- **Input:** `nums = [1,2,4,1,2,5,1,2,6], k = 3`
- **Output:** `3`
- **Explanation:** Modify the array from [1,2,**<u>4,</u>**1,2,**<u>5</u>**,1,2,**<u>6</u>**] to [1,2,**<u>3</u>**,1,2,**<u>3</u>**,1,2,**<u>3</u>**].

### 4. Constraints

- $1 \le k \le \text{nums.length} \le 2000$

- $​​​​​​0 \le \text{nums}[i] < 2^{10}$

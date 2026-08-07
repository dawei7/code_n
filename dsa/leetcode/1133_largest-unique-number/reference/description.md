### 1. Description

Given an integer array `nums`, return *the largest integer that only occurs once*. If no integer occurs once, return `-1`.

### 2. Function Contract

**Inputs**

- `nums`: a nonempty integer array. A value is eligible exactly when its total frequency in `nums` is one.

**Return value**

- The greatest eligible value, or `-1` when no value occurs exactly once.

The sentinel `-1` lies outside the legal value domain, so it cannot be confused with an input value. In particular, `0` is a valid answer.

### 3. Examples

#### Example 1

- **Input:** `nums = [5,7,3,9,4,9,8,3,1]`
- **Output:** `8`
- **Explanation:** The maximum integer in the array is 9 but it is repeated. The number 8 occurs only once, so it is the answer.
#### Example 2

- **Input:** `nums = [9,9,8,8]`
- **Output:** `-1`
- **Explanation:** There is no number that occurs only once.

### 4. Constraints

- $1 \le \text{nums.length} \le 2000$

- $0 \le \text{nums}[i] \le 1000$
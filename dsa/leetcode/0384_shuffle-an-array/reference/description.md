## Description

Given an integer array `nums`, design an algorithm to randomly shuffle the array. All permutations of the array should be **equally likely** as a result of the shuffling.

Implement the `Solution` class:

- `Solution(int[] nums)` Initializes the object with the integer array `nums`.

- `int[] reset()` Resets the array to its original configuration and returns it.

- `int[] shuffle()` Returns a random shuffling of the array.
### Function Contract

**Inputs**

- `nums`: The original array of distinct integers.
- `operations`: In cOde(n), an ordered list containing `"shuffle"` and `"reset"` calls.

**Return value**

The app adapter returns one array per operation. On LeetCode, construct `Solution(nums)` and call `reset()` or `shuffle()` directly; each possible shuffled ordering must have equal probability.

### Examples
#### Example 1

```
**Input**
["Solution", "shuffle", "reset", "shuffle"]
[[[1, 2, 3]], [], [], []]
**Output**
[null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

**Explanation**
Solution solution = new Solution([1, 2, 3]);
solution.shuffle();    // Shuffle the array [1,2,3] and return its result.
                       // Any permutation of [1,2,3] must be equally likely to be returned.
                       // Example: return [3, 1, 2]
solution.reset();      // Resets the array back to its original configuration [1,2,3]. Return [1, 2, 3]
solution.shuffle();    // Returns the random shuffling of array [1,2,3]. Example: return [1, 3, 2]
```
### Constraints

- $1 \le \text{nums.length} \le 50$

- $-10^{6} \le \text{nums}[i] \le 10^{6}$

- All the elements of `nums` are **unique**.

- At most $10^{4}$ calls **in total** will be made to `reset` and `shuffle`.
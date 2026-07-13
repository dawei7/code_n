# Number of Unique XOR Triplets II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3514 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Bit Manipulation, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [number-of-unique-xor-triplets-ii](https://leetcode.com/problems/number-of-unique-xor-triplets-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/number-of-unique-xor-triplets-ii/).

### Goal
Given an array of integers, identify the number of triplets $(i, j, k)$ such that $0 \le i < j \le k < n$ and the XOR sum of the elements in the range $[i, j-1]$ is equal to the XOR sum of the elements in the range $[j, k]$.

### Function Contract
**Inputs**

- `nums`: A list of integers where $1 \le \text{nums.length} \le 10^5$ and $0 \le \text{nums}[i] \le 10^6$.

**Return value**

- An integer representing the total count of valid triplets $(i, j, k)$ satisfying the XOR condition.

### Examples
**Example 1**

- Input: `nums = [0, 1, 1, 0]`
- Output: `7`

**Example 2**

- Input: `nums = [1, 2, 3]`
- Output: `0`

**Example 3**

- Input: `nums = [1, 2, 2, 1]`
- Output: `4`

---

## Solution
### Approach
The problem relies on the property of the XOR operation where $A \oplus B = C$ is equivalent to $A \oplus C = B$ or $A \oplus B \oplus C = 0$. Let $P[i]$ be the prefix XOR sum of the array up to index $i-1$. The XOR sum of range $[i, j-1]$ is $P[j] \oplus P[i]$, and the XOR sum of range $[j, k]$ is $P[k+1] \oplus P[j]$. The condition $P[j] \oplus P[i] = P[k+1] \oplus P[j]$ simplifies to $P[i] = P[k+1]$. We count pairs $(i, k+1)$ such that $P[i] = P[k+1]$ and then account for the possible positions of $j$ between $i$ and $k+1$.

### Complexity Analysis
- **Time Complexity**: $O(n)$, where $n$ is the length of the array, as we iterate through the array once to compute prefix XORs and once to count occurrences.
- **Space Complexity**: $O(n)$ to store the frequency map of prefix XOR values.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import defaultdict

def solve(nums: list[int]) -> int:
    """
    The condition XOR(nums[i...j-1]) == XOR(nums[j...k])
    Let P[x] be the prefix XOR sum: P[x] = nums[0] ^ ... ^ nums[x-1]
    The condition is: (P[j] ^ P[i]) == (P[k+1] ^ P[j])
    This simplifies to: P[i] == P[k+1]

    For a fixed pair (i, m) where m = k+1 and P[i] == P[m],
    any j such that i < j < m is a valid split point.
    The number of such j's is (m - i - 1).

    We need to sum (m - i - 1) for all pairs (i, m) with i < m and P[i] == P[m].
    Sum = sum(m - i - 1) = sum(m) - sum(i) - count
    """
    n = len(nums)
    prefix_xor = [0] * (n + 1)
    for i in range(n):
        prefix_xor[i + 1] = prefix_xor[i] ^ nums[i]

    # Store indices for each prefix XOR value
    val_to_indices = defaultdict(list)
    for idx, val in enumerate(prefix_xor):
        val_to_indices[val].append(idx)

    total_triplets = 0
    for val in val_to_indices:
        indices = val_to_indices[val]
        # For a list of indices [i1, i2, ..., im] where P[ix] are equal:
        # We want sum_{a < b} (indices[b] - indices[a] - 1)
        # = sum_{a < b} (indices[b] - indices[a]) - (number of pairs)
        # Let count = k. Number of pairs is k*(k-1)/2.
        # sum_{a < b} (indices[b] - indices[a]) = sum_{b=0 to k-1} (b * indices[b] - (k-1-b) * indices[b])
        # = sum_{b=0 to k-1} (2*b - k + 1) * indices[b]

        k = len(indices)
        if k < 2:
            continue

        sum_diff = 0
        for b in range(k):
            sum_diff += (2 * b - k + 1) * indices[b]

        num_pairs = k * (k - 1) // 2
        total_triplets += (sum_diff - num_pairs)

    return total_triplets
```
</details>

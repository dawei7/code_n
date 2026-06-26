# Single Number (XOR)

| | |
|---|---|
| **ID** | `bit_03` |
| **Category** | bit_manipulation |
| **Complexity (required)** | $O(N)$ Time, $O(1)$ Space |
| **Difficulty** | 2/10 |
| **Interview relevance** | 9/10 |
| **LeetCode Equivalent** | [Single Number](https://leetcode.com/problems/single-number/) |

## Problem statement

Given a non-empty array of integers `nums`, every element appears *twice* except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

**Input:** An integer array `nums`.
**Output:** An integer representing the single number.

## When to use it

- To showcase the magical, commutative properties of the Bitwise XOR (`^`) operator.
- The fundamental "cancellation" trick used to solve an entire family of paired array problems.

## Approach

**1. The Flaw of Standard Approaches:**
- **Hash Map:** Count the frequencies of every number, then iterate through the map to find the count of 1. This takes $O(N)$ time but $O(N)$ space, violating the problem constraint!
- **Sorting:** Sort the array, then iterate through it jumping by 2. If `nums[i] != nums[i+1]`, you found the target. This uses $O(1)$ space, but sorting takes $O(N \log N)$ time, violating the linear time constraint!

**2. The Magic of XOR:**
The bitwise XOR operator (`^`) compares two binary numbers bit by bit. If the bits are the same, it outputs `0`. If they are different, it outputs `1`.
This leads to two incredible mathematical axioms:
1. **Self-Cancellation:** Any number XOR'd with itself is 0! `A ^ A = 0`.
2. **Identity:** Any number XOR'd with 0 is itself! `A ^ 0 = A`.

**3. The Commutative Property:**
XOR is commutative and associative. This means `A ^ B ^ A` is mathematically identical to `(A ^ A) ^ B`.
Because `A ^ A = 0`, the equation simplifies to `0 ^ B`, which equals `B`!
Notice that the order of the numbers in the array does NOT matter.
If we initialize a variable `result = 0` and XOR it with every single number in the array, all the numbers that appear twice will completely obliterate each other (canceling out to `0`), no matter how far apart they are!
The only number left standing in `result` will be the single number!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for bit_03: Single Number (XOR).

Every element in the input array appears exactly
"""


def solve(arr):
    """Return the element that appears exactly once (others appear twice)."""
    result = 0
    for v in arr:
        result ^= v
    return result
```

</details>

## Walk-through

`nums = [4, 1, 2, 1, 2]`. `result = 0`.

1. **num = 4:**
   - `result = 0 ^ 4 = 4` (`000 ^ 100 = 100`)
2. **num = 1:**
   - `result = 4 ^ 1 = 5` (`100 ^ 001 = 101`)
3. **num = 2:**
   - `result = 5 ^ 2 = 7` (`101 ^ 010 = 111`)
4. **num = 1:**
   - `result = 7 ^ 1 = 6` (`111 ^ 001 = 110`)
   - *(Notice that the '1' bit from the first `1` has been canceled out!)*
5. **num = 2:**
   - `result = 6 ^ 2 = 4` (`110 ^ 010 = 100`)
   - *(Notice that the '1' bit from the first `2` has been canceled out!)*

Final `result` is 4. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(1)$ |
| **Average** | $O(N)$ | $O(1)$ |
| **Worst** | $O(N)$ | $O(1)$ |

The array is traversed exactly once, performing a single $O(1)$ XOR operation at each step. Time complexity is strictly $O(N)$.
We only use a single integer variable `result`, making the space complexity strictly $O(1)$.

## Variants & optimizations

- **Missing Number (1 to N):** Given an array of N distinct numbers taken from the range 0 to N. One number is missing. Find it.
  You can solve this with XOR! The array is missing exactly ONE paired number. If you XOR all the indices `0...N`, and then XOR all the values in the array `nums`, every number will pair up and cancel out *except* the missing index!
- **Single Number II (Every element appears 3 times):** The XOR trick fails because `A ^ A ^ A = A`, not `0`. You must use a state machine with two variables (`ones`, `twos`) to track the bits modulo 3.
- **Single Number III (Two elements appear once):** If two numbers are unique, the final XOR result will be `A ^ B`. You must use Brian Kernighan's trick (`result & -result`) to isolate a distinguishing bit, then split the array into two buckets and run the XOR trick again on both buckets! (`bit_05`)

## Real-world applications

- **RAID Storage Systems:** RAID 4 and RAID 5 arrays distribute data across multiple hard drives and use an extra "parity" drive. The parity drive is literally just the bitwise XOR of all the other drives! If any single drive fails, the exact data of the missing drive can be recovered by XORing the surviving drives with the parity drive.

## Related algorithms in cOde(n)

- **[bit_05 - Single Number III](bit_05_single-number-iii.md)** — The much harder variant where exactly TWO numbers appear once.
- **[bit_10 - Missing Number](bit_10_missing-number.md)** — The variant where you must XOR against a known expected sequence.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*

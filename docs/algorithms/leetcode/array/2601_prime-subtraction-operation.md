# Prime Subtraction Operation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2601 |
| Difficulty | Medium |
| Topics | Array, Math, Binary Search, Greedy, Number Theory |
| Official Link | [prime-subtraction-operation](https://leetcode.com/problems/prime-subtraction-operation/) |

## Problem Description & Examples
### Goal
Determine if it is possible to make an array strictly increasing by subtracting a prime number less than the current element from each element at most once. Each element can be modified independently, provided the resulting sequence maintains a strictly increasing order.

### Function Contract
**Inputs**

- `nums`: A list of positive integers.

**Return value**

- `bool`: Returns `True` if the array can be transformed into a strictly increasing sequence, otherwise `False`.

### Examples
**Example 1**

- Input: `nums = [4, 9, 6, 10]`
- Output: `True`
- Explanation: Subtract 3 from 4 (1), 0 from 9 (9), 2 from 6 (4), 0 from 10 (10). Result: [1, 9, 4, 10] is not correct; rather, subtract 3 from 4 (1), 7 from 9 (2), 2 from 6 (4), 0 from 10 (10). Result: [1, 2, 4, 10], which is strictly increasing.

**Example 2**

- Input: `nums = [6, 8, 11, 12]`
- Output: `True`
- Explanation: The array is already strictly increasing.

**Example 3**

- Input: `nums = [5, 8, 3]`
- Output: `False`
- Explanation: It is impossible to make the array strictly increasing.

---

## Underlying Base Algorithm(s)
The solution utilizes the **Sieve of Eratosthenes** to precompute prime numbers up to the maximum possible value in the input array. It then employs a **Greedy approach** combined with **Binary Search** (`bisect_left`) to find the largest prime $p$ such that `nums[i] - p` is greater than the previous element in the modified array.

---

## Complexity Analysis
- **Time Complexity**: $O(N \log(\log M) + N \log P)$, where $N$ is the length of the array, $M$ is the maximum value in the array, and $P$ is the number of primes up to $M$. The sieve takes $O(M \log(\log M))$ and the greedy pass takes $O(N \log P)$.
- **Space Complexity**: $O(M)$ to store the sieve of primes up to the maximum element.

# Number of Unique XOR Triplets II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3514 |
| Difficulty | Medium |
| Topics | Array, Math, Bit Manipulation, Enumeration |
| Official Link | [number-of-unique-xor-triplets-ii](https://leetcode.com/problems/number-of-unique-xor-triplets-ii/) |

## Problem Description & Examples
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

## Underlying Base Algorithm(s)
The problem relies on the property of the XOR operation where $A \oplus B = C$ is equivalent to $A \oplus C = B$ or $A \oplus B \oplus C = 0$. Let $P[i]$ be the prefix XOR sum of the array up to index $i-1$. The XOR sum of range $[i, j-1]$ is $P[j] \oplus P[i]$, and the XOR sum of range $[j, k]$ is $P[k+1] \oplus P[j]$. The condition $P[j] \oplus P[i] = P[k+1] \oplus P[j]$ simplifies to $P[i] = P[k+1]$. We count pairs $(i, k+1)$ such that $P[i] = P[k+1]$ and then account for the possible positions of $j$ between $i$ and $k+1$.

---

## Complexity Analysis
- **Time Complexity**: $O(n)$, where $n$ is the length of the array, as we iterate through the array once to compute prefix XORs and once to count occurrences.
- **Space Complexity**: $O(n)$ to store the frequency map of prefix XOR values.

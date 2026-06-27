# Maximum Palindromes After Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3035 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String, Greedy, Sorting, Counting |
| Official Link | [maximum-palindromes-after-operations](https://leetcode.com/problems/maximum-palindromes-after-operations/) |

## Problem Description & Examples
### Goal
Given a list of strings, you are permitted to rearrange the characters of all strings arbitrarily. The objective is to maximize the total number of palindromic strings you can form by redistributing these characters across the original string lengths.

### Function Contract
**Inputs**

- `words`: A list of strings representing the available characters and the target lengths for the resulting palindromes.

**Return value**

- An integer representing the maximum number of palindromes that can be formed.

### Examples
**Example 1**

- Input: `words = ["abbb","ba","aa"]`
- Output: `3`

**Example 2**

- Input: `words = ["abc","ab"]`
- Output: `2`

**Example 3**

- Input: `words = ["cdl","abc","ab"]`
- Output: `1`

---

## Underlying Base Algorithm(s)
The problem is solved using a **Greedy** approach combined with **Frequency Counting**. 
1. Count the total occurrences of every character across all strings.
2. Determine the number of "pairs" (two identical characters) available.
3. Sort the input strings by length.
4. Iterate through the sorted strings, attempting to fill each palindrome by using as many pairs as possible. If a string has an odd length, it will require one "center" character (which can be any remaining character).
5. Keep track of the number of pairs used and the number of leftover characters to satisfy the odd-length requirements.

---

## Complexity Analysis
- **Time Complexity**: $O(N \log N + \sum L_i)$, where $N$ is the number of words and $L_i$ is the length of each word. Sorting the words takes $O(N \log N)$, and counting characters takes $O(\sum L_i)$.
- **Space Complexity**: $O(1)$ (or $O(\Sigma)$ where $\Sigma$ is the alphabet size, which is constant at 26).

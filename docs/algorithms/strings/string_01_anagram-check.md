# Anagram Check

| | |
|---|---|
| **ID** | `string_01` |
| **Category** | strings |
| **Complexity (required)** | $O(N)$ |
| **Difficulty** | 1/10 |
| **Interview relevance** | 9/10 |
| **LeetCode Equivalent** | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) |

## Problem statement

Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`, and `False` otherwise.
An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

**Input:** Two strings `s` and `t`.
**Output:** A boolean indicating if they are anagrams.

**Example 1:**
`s = "anagram"`, `t = "nagaram"`
Output: `True`.

**Example 2:**
`s = "rat"`, `t = "car"`
Output: `False`.

## When to use it

- To determine if two strings share the exact same character frequencies.
- It is the most fundamental introductory problem for understanding **Hash Maps** or **Frequency Arrays** in string processing.

## Approach

The naive approach is to sort both strings and compare them: `return sort(s) == sort(t)`. This takes $O(N \log N)$ time. We can do better!

Since an anagram merely means both strings have the exact same count of each letter, we can count the frequencies of characters in $O(N)$ time.

1. **Length Check:** If `length(s) != length(t)`, they cannot be anagrams. Return `False`.
2. **Frequency Array:** Create an array (or Hash Map) of size 26 (if the strings only contain lowercase English letters).
3. Iterate through both strings simultaneously using an index `i`.
   - Increment the count for the character `s[i]`.
   - Decrement the count for the character `t[i]`.
4. After the loop, iterate through the frequency array. If any count is not exactly `0`, the strings have a mismatch in character frequency. Return `False`.
5. If all counts are `0`, return `True`.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for string_01: Anagram Check.

Check whether two strings are anagrams (same character counts).
"""


def solve(s, t):
    return sorted(s) == sorted(t)
```

</details>

## Walk-through

`s = "cat"`, `t = "act"`.
`counts = [0, 0, 0, ..., 0]` (size 26).

**i = 0:**
`s[0] = 'c'` (index 2). `counts[2] += 1`.
`t[0] = 'a'` (index 0). `counts[0] -= 1`.
Array state: `[-1, 0, 1, ...]`

**i = 1:**
`s[1] = 'a'` (index 0). `counts[0] += 1`. (Becomes 0).
`t[1] = 'c'` (index 2). `counts[2] -= 1`. (Becomes 0).
Array state: `[0, 0, 0, ...]`

**i = 2:**
`s[2] = 't'` (index 19). `counts[19] += 1`.
`t[2] = 't'` (index 19). `counts[19] -= 1`. (Becomes 0).
Array state: `[0, 0, 0, ...]`

Loop ends. All values in `counts` are 0. Return `True`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(1)$ | $O(1)$ |
| **Average** | $O(N)$ | $O(1)$ |
| **Worst** | $O(N)$ | $O(1)$ |

The time complexity is $O(N)$ where N is the length of the string. We loop through the strings once, and loop through the fixed 26-element array once. (Best case is $O(1)$ if the lengths differ).
Space complexity is $O(1)$ because the size of the `char_counts` array is always 26, regardless of how large N gets. *(If the strings contain arbitrary Unicode characters, a Hash Map would take $O(K)$ space where K is the number of unique characters).*

## Variants & optimizations

- **Group Anagrams:** Given an array of strings, group the anagrams together. Instead of an array of 26 integers, you convert the frequency array into a string or tuple (e.g., `(1, 0, 1, 0...)`) and use it as the key in a Hash Map mapping to a list of strings!
- **Find All Anagrams in a String:** Find all starting indices of `p`'s anagrams in `s`. This requires combining the frequency array with a **Sliding Window** of size `length(p)`.

## Real-world applications

- **Cryptography (Permutation Ciphers):** Checking if a ciphertext could potentially be a simple permutation (anagram) of a known plaintext by comparing their frequency histograms.

## Related algorithms in cOde(n)

- **[string_08 - Smallest Window](string_08_smallest-window.md)** — Relies heavily on maintaining and comparing character frequency arrays.
- **[hashing_01 - Hash Map](../hashing/hashing_01_hash-map-chaining.md)** — The data structure used when characters are not restricted to the English alphabet.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*

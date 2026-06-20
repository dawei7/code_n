# Group Anagrams

| | |
|---|---|
| **ID** | `hash_04` |
| **Category** | hashing |
| **Complexity (required)** | $O(N * K)$ Time, $O(N * K)$ Space |
| **Difficulty** | 4/10 |
| **Interview relevance** | 8/10 |
| **LeetCode Equivalent** | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) |

## Problem statement

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

**Input:** An array of strings `strs`.
**Output:** A 2D array of strings, where each inner array contains strings that are anagrams of each other.

## When to use it

- To group elements based on a defining, permutation-invariant characteristic.
- When sorting strings takes too long ($O(K log K)$ per string) and you need a linear $O(K)$ way to generate a unique signature.

## Approach

**1. The Canonical Key:**
A Hash Map is perfect for grouping items. The tricky part is figuring out what the `key` should be!
For anagrams, `"eat"`, `"tea"`, and `"ate"` must all map to the exact same key.
- *Method 1 (Sorting):* If we alphabetically sort all three strings, they all become `"aet"`. We can use `"aet"` as the dictionary key! But sorting a string of length K takes $O(K log K)$ time.
- *Method 2 (Character Count):* Instead of sorting, we can just count the frequencies of the 26 lowercase English letters. `"eat"` has 1 'a', 1 'e', and 1 't'. We can represent this as a tuple of 26 integers: `(1, 0, 0, 0, 1, 0..., 1, 0)`.

**2. The Hash Map Grouping:**
We initialize a Hash Map mapping a `Tuple` to a `List of Strings`.
We iterate through every string in the array.
We generate its Character Count Tuple in $O(K)$ time.
We use that Tuple as the key in the Hash Map, and append the original string to the corresponding list.
Finally, we just return all the `values` from the Hash Map!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for hash_04: Group Anagrams.

Two strings are anagrams iff their sorted characters are equal.
Use a dict keyed on the sorted-tuple; collect the original
strings into per-key lists. Sort each group's inner list and
the outer list of group keys so the verify can compare
directly. O(n * k log k) where k is the string length.
"""


def solve(strs, n):
    groups = {}
    for s in strs:
        key = tuple(sorted(s))
        groups.setdefault(key, []).append(s)
    out = []
    for key in groups:
        out.append(sorted(groups[key]))
    out.sort(key=lambda g: g[0])
    return out
```

</details>

## Walk-through

`strs = ["eat", "tea", "tan", "ate", "nat", "bat"]`

1. `s = "eat"`:
   - Count array: `a:1, e:1, t:1`. (All others 0).
   - `key = (1, 0, 0, 0, 1, ..., 1, 0)`.
   - `map[key] = ["eat"]`.
2. `s = "tea"`:
   - Count array: `a:1, e:1, t:1`.
   - `key = (1, 0, 0, 0, 1, ..., 1, 0)`. Matches exactly!
   - `map[key] = ["eat", "tea"]`.
3. `s = "tan"`:
   - Count array: `a:1, n:1, t:1`.
   - `key_2 = (1, 0, 0, ..., 1, ..., 1, 0)`.
   - `map[key_2] = ["tan"]`.
4. `s = "ate"`:
   - Matches `key`. `map[key] = ["eat", "tea", "ate"]`.
5. `s = "nat"`:
   - Matches `key_2`. `map[key_2] = ["tan", "nat"]`.
6. `s = "bat"`:
   - Count array: `a:1, b:1, t:1`.
   - `key_3 = (1, 1, 0, ..., 1, 0)`.
   - `map[key_3] = ["bat"]`.

Return `values`: `[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N * K)$ | $O(N * K)$ |
| **Average** | $O(N * K)$ | $O(N * K)$ |
| **Worst** | $O(N * K)$ | $O(N * K)$ |

Let N be the number of strings, and K be the maximum length of a string.
Counting the characters for a string takes $O(K)$ time. Generating the tuple takes $O(26)$ = $O(1)$ time. Hash Map insertion takes $O(1)$ time.
We do this N times. Total time complexity is strictly $O(N \cdot K)$.
*(Note: If we used the sorting method, time complexity would be $O(N \cdot K log K)$).*
Space complexity is $O(N \cdot K)$ to store the strings in the Hash Map and the output array.

## Variants & optimizations

- **Prime Number Multiplication:** Another (mathematically risky) way to generate an $O(K)$ key is to map the 26 letters to the first 26 Prime Numbers (`a=2, b=3, c=5...`). The product of the characters' prime numbers yields a unique integer guaranteed to be the same for all anagrams (due to the Fundamental Theorem of Arithmetic). However, for strings longer than ~15 characters, this product rapidly overflows standard 64-bit integer limits!

## Real-world applications

- **Cryptography & Security:** Grouping variations of passwords or fuzzing inputs that share identical character entropies to analyze dictionary-attack vulnerabilities.

## Related algorithms in cOde(n)

- **[hash_01 - Two Sum](hash_01_two-sum.md)** — The basic introduction to using Hash Maps for $O(1)$ lookups.
- **[string_02 - Valid Anagram](../string/string_02_valid-anagram.md)** — The 1-to-1 comparison version of this problem using the exact same character-counting array.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*

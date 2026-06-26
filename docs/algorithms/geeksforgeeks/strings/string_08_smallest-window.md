# Smallest Window Containing All Characters

| | |
|---|---|
| **ID** | `string_08` |
| **Category** | strings |
| **Complexity (required)** | $O(N)$ Time, $O(1)$ Space |
| **Difficulty** | 8/10 |
| **Interview relevance** | 9/10 |
| **LeetCode Equivalent** | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) |

## Problem statement

Given two strings `s` and `t` of lengths `m` and `n` respectively.
Return the **minimum window substring** of `s` such that every character in `t` (including duplicates) is included in the window.
If there is no such substring, return the empty string `""`.

**Input:** A string `s` and a string `t`.
**Output:** A string representing the smallest window.

## When to use it

- The absolute pinnacle of **Sliding Window** problems in technical interviews.
- When you need to find the shortest contiguous segment that satisfies a complex frequency requirement.

## Approach

**1. The "Expand and Shrink" Sliding Window:**
We maintain a physical window defined by a `left` pointer and a `right` pointer.
- **Expand:** We move the `right` pointer to the right, swallowing characters into our window until our window finally contains all the required characters of `t`.
- **Shrink:** Once we have a valid window, it might be unnecessarily long (e.g., `"AxxxBxxxC"`). We attempt to shrink it by moving the `left` pointer to the right! We throw away characters from the back of the window one by one, recording the window size each time, UNTIL throwing away a character breaks our valid window!
- Once the window breaks, we resume expanding the `right` pointer to find the missing character again.

**2. Tracking Frequencies (The Hash Maps):**
How do we efficiently know if our window contains all characters of `t`?
We use two Hash Maps (or fixed-size arrays of 128 ASCII characters):
- `t_count`: Stores the absolute frequency of characters needed (e.g. `{'A': 1, 'B': 1, 'C': 1}`).
- `window_count`: Stores the frequency of characters currently trapped inside our sliding window.

**3. The `have` vs `need` Optimization:**
Checking if two Hash Maps are perfectly matched takes $O(26)$ or $O(128)$ time. Doing this at every step of the sliding window is slow.
Instead, we maintain two integer counters: `have` and `need`.
- `need` is the total number of UNIQUE characters in `t`.
- `have` starts at 0. Every time we add a character to our window, we update `window_count`. If `window_count[char]` exactly equals `t_count[char]`, we increment `have`!
- The exact moment `have == need`, we know our window is 100% valid, without ever iterating over the Hash Maps!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for string_08: Smallest Window.

Sliding window: smallest substring of s containing all chars of p.
"""


def solve(s, p):
    n = len(s)
    if not p or not s:
        return ""
    need = set(p)
    best = ""
    left = 0
    have = set()
    for right in range(n):
        if s[right] in need:
            have.add(s[right])
        while True:
            # Check if we have everything in the current window.
            covered = all((c in have) for c in need) if have else False
            if not covered or left > right:
                break
            window = s[left:right + 1]
            if not best or len(window) < len(best):
                best = window
            if s[left] in need:
                pass
            left += 1
            have = set()
            for k in range(left, right + 1):
                if s[k] in need:
                    have.add(s[k])
    return best
```

</details>

## Walk-through

`s = "ADOBECODEBANC"`, `t = "ABC"`.
`t_count = {'A':1, 'B':1, 'C':1}`. `need = 3`.

1. **Expand `right`:**
   - Add `A`. `have=1`.
   - Add `D, O, B`. `have=2`.
   - Add `E, C`. `have=3`.
2. **Valid Window Found!** `have == need`.
   - Window: `"ADOBEC"` (Indices 0 to 5). Length 6.
   - **Shrink `left`:** Remove `A`.
   - `window_count['A']` drops to 0. `have` drops to 2! Loop breaks.
   - `left` moves to 1.
3. **Expand `right`:**
   - Add `O, D, E, B, A`.
   - `A` added! `have` returns to 3!
4. **Valid Window Found!**
   - Window: `"DOBECODEBA"` (Indices 1 to 10). Length 10. (Length > 6, so we don't save it).
   - **Shrink `left`:** Remove `D, O, B, E, C`.
   - Removing `C` drops `have` to 2. Loop breaks.
   - `left` is now at index 6.
5. **Expand `right`:**
   - Add `N, C`.
   - `C` added! `have` returns to 3!
6. **Valid Window Found!**
   - Window: `"ODEBANC"` (Indices 6 to 12).
   - **Shrink `left`:** Remove `O, D, E`.
   - Window is `"BANC"` (Indices 9 to 12). Length 4! New Record!
   - Remove `B`. `have` drops to 2. Loop breaks.

End of string. Return `"BANC"`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(1)$ |
| **Average** | $O(N)$ | $O(1)$ |
| **Worst** | $O(N)$ | $O(1)$ |

The `right` pointer starts at index 0 and moves to index N-1, executing N steps.
The `left` pointer starts at index 0 and moves to index N-1, executing N steps.
A pointer NEVER moves backward. The characters are added to the window exactly once, and removed exactly once.
Total operations = 2N. The time complexity is strictly $O(N)$.
Space complexity is technically $O(1)$ constant time, because the string characters are ASCII (or Unicode), meaning the Hash Maps will never exceed a maximum size of 128 (or 256) keys, regardless of if the string is 10 million characters long!

## Variants & optimizations

- **Longest Substring Without Repeating Characters (`string_11`):** The exact same "Expand and Shrink" logic, but the shrinking condition is simply "While the newly added character is already inside the Hash Map".
- **Find All Anagrams in a String:** The same logic, but the window size is strictly fixed to `len(t)`. Instead of expanding and shrinking dynamically, `left` moves exactly in lockstep with `right`.

## Real-world applications

- **Network Packet Analysis:** Finding the tightest transmission window in a continuous stream of TCP packets where all required header flags were successfully logged before an error occurred.

## Related algorithms in cOde(n)

- **[two_pointers_01 - Two Sum Sorted](../two_pointers/two_pointers_01_two-sum-sorted.md)** — The simpler version of Two Pointers where pointers start at opposite ends. Sliding Window is a subset of Two Pointers where both pointers move in the same direction.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*

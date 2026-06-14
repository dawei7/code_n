# Longest Substring Without Repeating Characters

| | |
|---|---|
| **ID** | `hash_03` |
| **Category** | hashing |
| **Complexity (required)** | O(n) |
| **Difficulty** | 4/10 |
| **Interview relevance** | 9/10 |
| **Wikipedia** | [Sliding window](https://en.wikipedia.org/wiki/Sliding_window) |

## Problem statement

Given a string `s`, find the length of the **longest
substring** (contiguous) without repeating characters.

**Input:** a string `s`.
**Output:** the length of the longest substring with all
distinct characters.

**Example:**

| s | Answer | Substring |
|---|---:|---|
| `"abcabcbb"` | 3 | `"abc"` |
| `"bbbbb"` | 1 | `"b"` |
| `"pwwkew"` | 3 | `"wke"` |
| `""` | 0 | `""` |
| `"abcdef"` | 6 | `"abcdef"` |
| `"aab"` | 2 | `"ab"` |

## When to use it

- LeetCode #3. The canonical **sliding window + hash set**
  problem. Asked in phone screens at every company.
- Tests the "**expand right, contract left**" sliding-window
  pattern that recurs in many other problems (longest
  subarray with sum ≤ k, minimum window substring, etc.).

## Approach

**Sliding window** with a hash set tracking characters
currently in the window.

Maintain a window `[left, right]` (both inclusive) and a
hash set `in_window` of characters in that window.

For each `right` from `0` to `n-1`:
1. While `s[right]` is already in `in_window` (i.e.
   `s[right]` appears at some position ≥ `left`):
   - Remove `s[left]` from `in_window`.
   - Advance `left` by 1.
2. Add `s[right]` to `in_window`.
3. Update answer: `ans = max(ans, right - left + 1)`.

**Why it works:** the window is always "all distinct", and
we expand it greedily. When a duplicate would enter, we
shrink from the left until the duplicate is gone. Each
character enters and leaves the window at most once, so the
total work is O(n).

**Optimization with a hash map (last seen index):** instead of
a set + while-loop, store the last index where each
character appeared. When we'd add `s[right]`, jump `left` to
`max(left, last_seen[s[right]] + 1)`. This is O(n) with
O(1) work per character (no while loop), but conceptually
equivalent.

## Algorithm (pseudocode)

```
longest_unique_substring(s):
    in_window = set()
    left = 0
    best = 0
    for right, ch in enumerate(s):
        while ch in in_window:
            in_window.remove(s[left])
            left += 1
        in_window.add(ch)
        best = max(best, right - left + 1)
    return best
```

## Walk-through

`s = "abcabcbb"`. Expected: 3.

| right | ch | ch in window? | action | window | in_window | best |
|---:|---:|---|---|---|---|---:|
| 0 | a | no | add | "a" | {a} | 1 |
| 1 | b | no | add | "ab" | {a, b} | 2 |
| 2 | c | no | add | "abc" | {a, b, c} | **3** |
| 3 | a | yes | remove b, then remove a, then add a | "bca" | {b, c, a} | 3 |
| 4 | b | yes | remove c, remove a, remove b? No — b's at pos 1, after removing c (pos 2) and a (pos 3), window becomes "b", then add b | "ab" | {a, b} | 3 |
| 5 | c | no | add | "abc" | {a, b, c} | 3 |
| 6 | b | yes | remove a, remove b, then add b | "cb" | {c, b} | 3 |
| 7 | b | yes | remove c, remove b, then add b | "b" | {b} | 3 |

Answer: 3. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | O(n) | O(min(n, σ)) |
| **Average** | O(n) | O(min(n, σ)) |
| **Worst** | O(n) | O(min(n, σ)) |

`σ` = the size of the character set (e.g. 26 for lowercase
English, 128 for ASCII, ~65k for full Unicode). The hash
set holds at most `min(n, σ)` characters.

The hash-map variant uses O(min(n, σ)) space too.

## Variants & optimizations

- **Longest substring with at most K distinct characters** —
  same shape, but the window-validity predicate is "at
  most K distinct", not "no duplicates". The contraction
  is more involved (track counts, not just membership).
- **Longest substring with all unique vowels** — same
  shape, restrict to vowels.
- **Minimum window substring** — find the smallest window
  in `s` that contains all characters of `t`. Same sliding
  window; the predicate is "contains t's character set".
- **Longest substring with no more than K replacements** —
  add a counter for the most-frequent character; window
  is valid when `window_size - max_freq <= k`.
- **Longest repeating character replacement** — same
  shape as above.

## Real-world applications

- **String deduplication** — finding the longest run of
  distinct characters (used in compression, encoding).
- **Cache-line key uniqueness** — finding the longest
  contiguous run of unique keys in a memory access trace.
- **Bioinformatics** — finding the longest stretch of
  DNA without a repeated base in a window.
- **Compression** — LZ77-style compression looks for the
  longest already-seen prefix; this is the same shape.
- **Sliding-window aggregations** — the same pattern
  underlies many "longest / shortest / min / max subarray
  with property X" problems.

## Related algorithms in cOde(n)

- **[hash_01 — Two Sum](hash_01_two-sum.md)** — same hash-map
  approach, different problem. (d=4/10, r=9/10)
- **[hash_02 — Subarray Sum Equals K](hash_02_subarray-sum-equals-k.md)** —
  prefix-sum + hash map. (d=4/10, r=9/10)
- **[hash_04 — Group Anagrams](hash_04_group-anagrams.md)** —
  hash map as a categorizer. (d=4/10, r=9/10)
- **[string_03 — Longest Substring Without Repeating](string_03_longest-substring-without-repeating.md)** —
  same problem in the strings category. (d=4/10, r=7/10)

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-
programming reference sites. For the canonical encyclopedia
entry, follow the Wikipedia link at the top of the page.
Source repository: <https://github.com/dawei7/code_n>.*

## General

**Turning the definition into something that can be checked quickly**

A substring is balanced when every distinct character appearing in it has the same frequency. The word “distinct” matters: letters that do not occur in the substring are irrelevant. For example, `"aabb"` is balanced because its two present letters both occur twice, and `"zzz"` is balanced because its only present letter occurs three times. On the other hand, `"aab"` is not balanced because the frequencies are two and one.

The direct way to examine a substring would be to count all its letters and then compare all positive counts. Doing that independently for every pair of endpoints would repeat a large amount of work. The Optimal solution still considers every possible substring, which is acceptable because the input length is at most 1,000, but it reuses the counts while moving the right endpoint and reduces each balance test to one arithmetic equality.

**Fix the left endpoint and grow the substring**

The outer loop chooses `i`, the left endpoint of a possible substring. For this new `i`, the solution creates an empty frequency counter and sets both `mx` and `v` to zero:

- `cnt[c]` is the number of occurrences of character `c` in the current substring `s[i:j + 1]`.
- `mx` is the largest frequency among all characters currently present.
- `v` is the number of distinct characters currently present.

The inner loop advances `j` from `i` to the end of the string. When `s[j]` is appended, only that character's count changes. The code increments `cnt[s[j]]` and updates `mx` with the new count. It increments `v` only when that new count is one, because a count changes to one precisely when this character appears in the current substring for the first time. A second or later occurrence must not increase the number of distinct characters.

This incremental update is the main reuse of work. Once the counts for `s[i:j]` are known, the counts for `s[i:j + 1]` require only one counter increment and two small bookkeeping updates. There is no need to scan the substring again.

**Why `mx * v == length` exactly recognizes a balanced substring**

Let the current positive character frequencies be

$$
f_1, f_2, \ldots, f_v,
$$

where `v` is the number of distinct letters and `mx` is their maximum. The current substring length is the sum of those frequencies:

$$
L = f_1 + f_2 + \cdots + f_v.
$$

Every frequency is at most `mx`. Therefore,

$$
L \le v \cdot \texttt{mx}.
$$

Equality can happen only if every one of the `v` terms is equal to `mx`. If even one character occurred fewer than `mx` times, the sum would be strictly smaller than `v * mx`. Consequently,

$$
L = v \cdot \texttt{mx}
$$

is equivalent to saying that all present characters have exactly the same frequency. That is precisely the definition of a balanced substring.

The code computes `L` as `j - i + 1`, so its condition

`mx * v == j - i + 1`

is not a heuristic. It is a necessary and sufficient test. It avoids separately finding a minimum frequency or looping over every counter entry.

As a concrete trace, consider extending a substring through `"aabcbc"`:

| Current substring | Positive counts | `mx` | `v` | `mx * v` | Length | Balanced? |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| `"a"` | `a:1` | 1 | 1 | 1 | 1 | Yes |
| `"aa"` | `a:2` | 2 | 1 | 2 | 2 | Yes |
| `"aab"` | `a:2, b:1` | 2 | 2 | 4 | 3 | No |
| `"aabc"` | `a:2, b:1, c:1` | 2 | 3 | 6 | 4 | No |
| `"aabcb"` | `a:2, b:2, c:1` | 2 | 3 | 6 | 5 | No |
| `"aabcbc"` | `a:2, b:2, c:2` | 2 | 3 | 6 | 6 | Yes |

The equality becomes true exactly at the rows in which every displayed count matches.

**Why every possible answer is considered**

Every nonempty substring has one unique pair of endpoints `(i, j)` with `0 <= i <= j < n`. The outer loop visits every possible `i`, and for each such `i` the inner loop visits every possible `j` at or to its right. Therefore, the balance test is applied to every nonempty substring exactly once.

Whenever the condition is true, the solution updates `ans` with the maximum of its old value and the current length. Because the test is exact and no substring is skipped, `ans` is the greatest length among all balanced substrings after both loops finish.

The initialization `ans = 0` is safe even though a nonempty input always has an answer of at least one. On the first inner-loop iteration, the substring contains a single character, so `mx = 1`, `v = 1`, and its length is one. The condition succeeds and raises `ans` to at least one naturally.

## Complexity detail

Let `n` be the length of `s`. For a fixed left endpoint `i`, the inner loop performs `n - i` iterations. Summing over all left endpoints gives

$$
n + (n - 1) + \cdots + 1
= \frac{n(n+1)}{2}
= O(n^2).
$$

Each iteration performs a constant amount of work: one counter update, one maximum update, a possible increment of `v`, one multiplication and comparison, and possibly one update to `ans`. Python dictionary operations are expected $O(1)$, and here the input alphabet is restricted to the 26 lowercase English letters. Even in an implementation that explicitly inspected the whole frequency table, that table would have a fixed maximum size independent of `n`. The total time complexity is therefore $O(n^2)$.

The counter stores at most 26 entries. The remaining variables are a handful of integers, so the auxiliary space complexity is $O(1)$ with respect to `n`. The counter is recreated for each left endpoint, but the old one becomes unnecessary before the next outer iteration; the solution never keeps all those counters simultaneously. The input string itself is not counted as auxiliary space.

## Alternatives and edge cases

- **Recount every substring from scratch:** One could choose `i` and `j`, build a new frequency table for `s[i:j + 1]`, and then test its counts. Recounting costs up to $O(n)$ per substring, producing $O(n^3)$ time. Incrementally extending each fixed-left substring removes that unnecessary factor.
- **Compare the minimum and maximum positive frequencies:** A substring is balanced when its minimum positive count equals its maximum count. This is valid, but scanning the frequency table after every extension adds work and requires care not to include zero counts. The equality `mx * v == length` captures the same fact with the maintained statistics.
- **Prefix counts for all 26 letters:** Prefix-frequency arrays can recover the 26 counts of any substring in constant time relative to `n`, leading to $O(26n^2)=O(n^2)$ time and $O(26n)=O(n)$ space. It is correct, but the running-counter method is simpler and uses less memory.
- **Single-character substrings:** Every one-character substring is balanced because it has one distinct character with frequency one. The code detects these without a special case, which also guarantees a positive answer for every valid nonempty input.
- **A substring containing only one repeated letter:** A run such as `"aaaa"` remains balanced at every extension. Here `v` stays one, `mx` equals the length, and the equality continues to hold.
- **A newly introduced character:** When a letter first appears, its count becomes one and `v` increases. Forgetting this update would make `mx * v` too small and could miss balanced substrings containing that new letter.
- **Repeated appearances of an existing character:** The distinct count must not increase again. The condition `cnt[s[j]] == 1` is checked after incrementing, so `v` changes exactly once per character for each fixed `i`.
- **Maximum frequency never decreases:** While `j` moves right, counts only increase, so keeping `mx` through `max(mx, cnt[s[j]])` is sufficient. A full recomputation of the maximum is unnecessary. A new outer-loop iteration does reset `mx` because it starts a different family of substrings.
- **Letters absent from the substring:** They must not be treated as having frequency zero in the equality. The variable `v` counts only present letters, so the product uses exactly the frequencies relevant to the definition.
- **Overlapping candidate substrings:** Nothing is consumed or marked when a balanced substring is found. The loops continue extending it and later restart at every other left endpoint, so overlapping and nested answers are all considered.

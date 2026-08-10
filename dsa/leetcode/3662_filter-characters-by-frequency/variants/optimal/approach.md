## General

**The decision depends on the whole string**

A character occurrence is kept when that character’s total frequency in `s` is strictly less than `k`. The decision cannot be made from the prefix seen so far.

For example, the first `'a'` might initially appear rare but later occurrences can raise its final count to `k`, requiring every `'a'`—including the first—to be removed. This is why the source uses two passes rather than filtering while it counts.

**Count every character first**

`Counter(s)` builds a mapping from each distinct character to its total occurrence count. If `d` distinct letters appear, the map has `d` entries.

The input contains only lowercase English letters, so `d <= 26`, but describing the structure as `O(d)` keeps the method general.

Frequencies are global and based on the original string. Removing one character does not lower the frequency used to decide whether later occurrences qualify. The entire filter is determined before output construction begins.

**Scan the original order and keep all qualifying occurrences**

The second loop visits characters in exactly the order they occur in `s`. For character `c`, it tests

`cnt[c] < k`.

If true, it appends that occurrence to `ans`. If false, it skips it.

The comparison is strict. A character appearing exactly `k` times is removed, as is one appearing more than `k` times.

When one character qualifies, every occurrence qualifies because all use the same total `cnt[c]`. The task does not ask to keep only one representative or only the first `k - 1` copies. The source appends each qualifying occurrence encountered.

Because the loop never reorders characters, the result is a stable subsequence of `s`.

**Build the final immutable string efficiently**

Python strings are immutable. Repeatedly writing `result += c` can copy the growing prefix many times and lead to quadratic behavior.

The source collects characters in a list and performs

`"".join(ans)`

once. Join allocates the final string with the entries in list order. If no character qualifies, `ans` is empty and joining it correctly returns the empty string.

**Trace the first example**

For `"aadbbcccca"`, the global counts are:

- `a -> 3`
- `d -> 1`
- `b -> 2`
- `c -> 4`

With `k = 3`, only `d` and `b` have counts strictly below three. The second pass skips all `a` and `c` occurrences but appends `d` followed by both `b` occurrences, giving `"dbb"`.

The order is not alphabetic and does not follow frequency order. It is inherited from the original string.

**Why one global count and one stable scan are enough**

For every position `i`, the required output decision is exactly the predicate

`frequency of s[i] in the complete s < k`.

`Counter` computes that frequency correctly for every distinct character. The second pass evaluates the predicate once per position and appends precisely the qualifying positions. Therefore the joined list contains every required occurrence, no excluded occurrence, and the same relative order as `s`.

No sorting, window, or dynamic programming is involved because each output decision is independent once global counts are known.

## Complexity detail

Let `n` be the string length and `d` the number of distinct characters.

Counting visits all `n` characters in expected `O(n)` time. Filtering visits them again in `O(n)` time, and joining at most `n` retained characters costs `O(n)`. Total time is `O(n)`.

The frequency map uses `O(d)` space. The list `ans` and returned string can each contain `O(n)` characters. If unavoidable output construction is excluded from auxiliary-space accounting, the algorithmic auxiliary state is `O(d)`, matching the manifest. Counting every allocated buffer in the exact Python source gives `O(d + n)` peak working memory because `ans` exists while `join` creates the final string.

Since lowercase English letters limit `d` to 26, the frequency-table portion is also `O(1)` with respect to `n`, but `O(d)` states the intended data-structure cost.

## Alternatives and edge cases

- **Use a fixed 26-entry array:** Map each lowercase letter to an index. This gives the same `O(n)` time with constant-sized count storage.
- **Call `s.count(c)` inside the filter:** Each count scans the string, producing `O(n^2)` time in the worst case.
- **Filter during the first pass:** A later occurrence can change a character from qualifying to disqualified, so early output decisions are unsafe.
- **Sort qualifying characters:** Sorting destroys the required original order.
- **Keep one copy per qualifying character:** The statement keeps every occurrence, not only distinct representatives.
- **Frequency exactly `k`:** All occurrences are removed because the condition is “fewer than,” not “at most.”
- **`k = 1`:** Every present character has frequency at least one, so the result is empty.
- **All characters occur once and `k > 1`:** Every occurrence qualifies and the original string is returned.
- **One character fills the string:** It is removed when its frequency is at least `k`; with `k <= n`, the result is empty.
- **Empty result:** Joining an empty list returns `""` without special handling.
- **Repeated qualifying character:** Every copy is appended in its original position.
- **Input preservation:** Strings are immutable, and the method creates new count and output structures.
- **Missing import:** The stored source uses `Counter` without importing it. Standalone Python needs `from collections import Counter` unless the harness supplies it.

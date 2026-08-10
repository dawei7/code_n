## General

**Maintain the longest valid suffix ending at each position**

For every right endpoint `right`, the algorithm wants the longest substring ending at that position that contains no repeated character. A substring must be contiguous, so it can be represented by an inclusive interval

$$
[\texttt{left},\texttt{right}].
$$

Its length is `right - left + 1`. The right boundary advances one position per iteration. When the new character repeats something inside the current window, the left boundary jumps just far enough to exclude the earlier copy.

The important word is **inside**. A character may have appeared earlier in the string but already lie to the left of the current window. Such a stale occurrence must not make `left` move backward or shrink a valid window. The `max` in the implementation handles exactly this distinction.

**What the last-seen dictionary means**

The method initializes

```python
result, left = 0, 0
lookup = {}
```

For each character already processed, `lookup[character]` stores its most recent index. It is historical information about the scanned prefix, not a set containing only the current window.

Before processing `right`, the interval ending at `right - 1` and starting at `left` contains no duplicate character. Adding `s[right]` can create only one kind of violation: the new character may duplicate its latest previous occurrence. No two old characters can suddenly become duplicates because they were already valid before the extension.

If the new character has never been seen, no repair is needed. If it has been seen at index `lookup[s[right]]`, any valid window containing the new occurrence must begin after that prior index—provided that prior index is still inside the window.

**Why `left` uses `max`**

The update is

```python
left = max(left, lookup[s[right]] + 1)
```

There are two cases:

- If the last occurrence is at or after `left`, it lies inside the current window. Moving to `last_index + 1` removes that older copy and every character before it.
- If the last occurrence is before `left`, it is already outside the current window. `last_index + 1` would be no greater than `left`, so `max` leaves the boundary unchanged.

The left boundary must never move backward. Moving backward could reintroduce duplicates that were previously excluded and would make the algorithm count an invalid substring.

The short string `"abba"` shows the trap clearly:

| `right` | Character | Last occurrence | `left` after repair | Valid window |
|---:|:---:|---:|---:|---|
| `0` | `a` | none | `0` | `"a"` |
| `1` | `b` | none | `0` | `"ab"` |
| `2` | `b` | `1` | `2` | `"b"` |
| `3` | `a` | `0` | `max(2, 1) = 2` | `"ba"` |

At the final `a`, its old occurrence at index `0` is no longer in the window. Assigning `left = 1` without `max` would move backward and create `"bba"`, which is invalid. Keeping `left = 2` gives the correct candidate `"ba"`.

**Update history and measure the repaired window**

After any boundary repair, the code records the current occurrence:

```python
lookup[s[right]] = right
```

Future iterations need the most recent index, because it is the occurrence closest to a future right endpoint and therefore imposes the strongest left-boundary restriction. Older occurrences can be forgotten safely.

The algorithm then updates

```python
result = max(result, right - left + 1)
```

At this point, the window is valid. For this particular `right`, `left` is also as far left as validity permits:

- it never moved unless the new character repeated inside the window;
- when it moved, it stopped immediately after the conflicting occurrence.

Therefore `right - left + 1` is the longest duplicate-free substring ending at `right`. `result` retains the largest such length across all right endpoints.

**A full trace of `"pwwkew"`**

| `right` | Character | Previous latest index | New `left` | Current window | `result` |
|---:|:---:|---:|---:|---|---:|
| `0` | `p` | none | `0` | `"p"` | `1` |
| `1` | `w` | none | `0` | `"pw"` | `2` |
| `2` | `w` | `1` | `2` | `"w"` | `2` |
| `3` | `k` | none | `2` | `"wk"` | `2` |
| `4` | `e` | none | `2` | `"wke"` | `3` |
| `5` | `w` | `2` | `3` | `"kew"` | `3` |

The answer is `3`. `"wke"` and `"kew"` are both contiguous substrings of that length. The non-contiguous characters forming `"pwke"` are never treated as one window because `left` and `right` always describe a continuous interval.

**Why the final maximum is the required length**

After repair at each `right`, the current interval has no repeated character: the previous interval was valid, and any earlier copy of the only newly added character has been excluded. The reported length is therefore always attainable by a legal substring.

Now take an optimal duplicate-free substring ending at some index `r`. When the loop processes `r`, the algorithm's `left` cannot be to the right of that substring's start without a repeated character forcing it there. If such a repetition forced the boundary, any substring starting earlier and ending at `r` would contain the same duplicate and could not be valid. Thus the maintained window is the longest valid one for that endpoint. Since every endpoint is processed, `result` must eventually equal the global optimum.

For an empty string, `range(len(s))` is empty and the initialized `result = 0` is returned.

## Complexity detail

Let $n$ be the string length and $a$ the number of distinct characters possible in its alphabet.

- **Time complexity: $O(n)$ expected.** `right` takes each value from `0` through `n - 1` once. Every iteration performs a constant number of expected-$O(1)$ dictionary operations, arithmetic operations, and comparisons. Unlike a frequency-based window, this implementation jumps `left` directly and has no inner shrinking loop, although both designs are linear overall.
- **Space complexity: $O(\min(n,a))$.** `lookup` stores one latest index for each distinct character encountered. There can be no more than $n$ such characters in the string and no more than $a$ in the alphabet. The boundaries and result use constant space. The source comment's $O(1)$ can be interpreted under a fixed-size alphabet such as ASCII; for the general string contract, the manifest's $O(\min(n,a))$ bound states the dependency explicitly.

The dictionary retains characters that are no longer in the current window because their last indices are still useful for determining whether a future occurrence is stale. Retention does not exceed one entry per distinct character.

## Alternatives and edge cases

- **Counter-based sliding window:** Track frequencies and advance `left` one character at a time until the new duplicate disappears. It is also expected $O(n)$ time and $O(\min(n,a))$ space. The last-seen map is more direct for the “at most one copy” rule because it can jump over the conflict.
- **Set-based window:** A set can represent exactly the current characters, but removal proceeds incrementally from the left. It avoids stale historical entries conceptually, while the last-index map reduces boundary updates.
- **Brute-force substrings:** Testing all ranges repeats duplicate checks and costs at least $O(n^2)$, often $O(n^3)$ with a fresh scan per range. It is unnecessary once overlapping windows share state.
- **Direct-access index table:** For a guaranteed small alphabet, an array of last positions can replace the dictionary and give fixed $O(a)$ space with smaller constants. The dictionary makes no narrow ASCII-only assumption.
- **Omitting `max`:** Directly assigning `left = lookup[c] + 1` is wrong when the stored occurrence is already outside the window. `"abba"` is the standard counterexample because the last `a` would move `left` backward.
- **Empty string:** The loop is skipped and `0` is returned.
- **One character:** The dictionary stores index zero and the result becomes `1`.
- **All characters equal:** Every iteration after the first moves `left` to the current index, so the maximum remains `1`.
- **All characters distinct:** No repair executes, `left` remains zero, and the result reaches `n`.
- **A stale repeated character:** If its previous index is smaller than `left`, `max` deliberately ignores it while still updating the dictionary to the new latest index.
- **Spaces, digits, and symbols:** Every exact character is a valid dictionary key. Spaces are not ignored, and symbols are not normalized.
- **Case sensitivity:** `"a"` and `"A"` are different characters, so they occupy different keys.
- **Substring requirement:** The algorithm never deletes an interior character while keeping both sides. Moving a boundary always preserves a contiguous range.

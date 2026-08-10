## General

**A substring must stay contiguous**

The task is not to collect the largest set of different characters from anywhere in `s`. The answer must come from one uninterrupted range of indices. For example, `"pwke"` can be selected in order from `"pwwkew"`, but it skips a character, so it is a subsequence rather than a substring. A valid candidate is described by two boundaries and contains every character between them.

The solution maintains such a range with `l` as its left boundary and `r` as its right boundary. Both endpoints are inclusive, so its current length is

$$
r - l + 1.
$$

As `r` moves from left to right, the algorithm makes the current range valid—meaning that every character appears at most once—before using its length to update the answer. This moving range is a **sliding window**.

**Why checking every substring repeats too much work**

There are $O(n^2)$ possible substrings. Checking each substring from scratch for duplicates can add another factor of $n$. More importantly, neighboring candidates overlap heavily. If `s[l:r]` is already known to contain unique characters, extending it by one character should reuse that knowledge rather than rescan everything.

The Counter named `cnt` records character frequencies in the current window. Once the new rightmost character `c` is inserted, it tells the algorithm whether that extension created a duplicate. Removing characters from the left repairs the window without abandoning the still-useful suffix.

**The exact meaning of the state**

The code initializes

```python
cnt = Counter()
ans = l = 0
```

- `cnt[x]` is the number of occurrences of character `x` in the current window;
- `l` is the first index in the current window;
- `ans` is the largest valid-window length seen after completed repairs;
- `r` and `c`, supplied by `enumerate(s)`, are the current right index and `s[r]`.

Before a new character is added, the previous window contains no repeated character. The line

```python
cnt[c] += 1
```

extends the window to include index `r`. Because the old window was valid, `c` is the only character that can now have a frequency greater than one. Every other frequency is unchanged. This is why the repair condition only needs to inspect `cnt[c]`, not scan the entire Counter for any count above one.

**Shrink only until the newly added duplicate is gone**

If `cnt[c] > 1`, the new `c` has an earlier copy somewhere in the window. The loop

```python
while cnt[c] > 1:
    cnt[s[l]] -= 1
    l += 1
```

removes the leftmost window character and advances `l`. It may first remove unrelated characters that appear before the older `c`. That is necessary because a substring cannot skip over them: moving the left boundary is the only way to exclude the earlier duplicate while keeping `r`.

The loop stops as soon as the older copy of `c` has been removed and `cnt[c]` returns to `1`. At that moment:

- the new `c` appears once;
- every other character still appears at most once, because none of their counts increased;
- the range `s[l:r+1]` is a valid substring without duplicates.

Shrinking farther would also produce a valid window, but it would make the current candidate unnecessarily short. Stopping at the earliest valid `l` preserves the longest valid substring that ends exactly at `r`.

**Update the answer only after the window is valid**

The line

```python
ans = max(ans, r - l + 1)
```

appears after the `while` loop. This order matters. Before repair, `r - l + 1` may describe a window with repeated characters and must not be considered. After repair, it is a legal candidate.

For a fixed right endpoint `r`, the repaired `l` is the smallest left endpoint that produces a duplicate-free suffix ending at `r`. Therefore `r - l + 1` is the longest valid substring ending at that right endpoint. Taking the maximum over every `r` considers the best ending position for the global answer.

**Walk through `"pwwkew"`**

| `r` | New `c` | Window immediately after insertion | Repair | Valid window | `ans` |
|---:|:---:|---|---|---|---:|
| `0` | `p` | `"p"` | none | `"p"` | `1` |
| `1` | `w` | `"pw"` | none | `"pw"` | `2` |
| `2` | `w` | `"pww"` | remove `p`, then the older `w` | `"w"` | `2` |
| `3` | `k` | `"wk"` | none | `"wk"` | `2` |
| `4` | `e` | `"wke"` | none | `"wke"` | `3` |
| `5` | `w` | `"wkew"` | remove the older `w` | `"kew"` | `3` |

The longest length is `3`. The algorithm finds both `"wke"` and `"kew"` as valid windows of that size, but it returns only the requested length.

At `r = 2`, the removal sequence illustrates why a `while` loop is needed. The older `w` is not initially at the left boundary; `p` must leave before that `w` can leave. Removing only one character would leave `"ww"`, which is still invalid.

**Why the maximum cannot miss a better substring**

Consider any valid substring ending at index `r`. Its left endpoint cannot lie before the repaired `l`: if it did, it would still include both copies of the character that forced `l` forward. The repaired window is thus at least as long as every other valid substring with the same right endpoint.

The outer loop uses every index as `r`. When it reaches the ending index of an optimal substring, the repaired window is at least as long as that optimal substring. It cannot be longer than the true optimum by definition, so its length equals the optimum. Updating `ans` with every repaired length must therefore capture the correct maximum.

If `s` is empty, the loop performs no iterations and `ans` remains `0`, which is the length of the only possible substring.

## Complexity detail

Let $n$ be `len(s)`, and let $a$ be the number of distinct characters that can occur in the input alphabet.

- **Time complexity: $O(n)$.** The right boundary `r` advances exactly $n$ times. Although the inner `while` loop can run several times during one outer iteration, `l` only moves forward and can advance at most $n$ times over the complete execution. Each character is added once and removed at most once. The total boundary movements are at most $2n$, which simplifies to $O(n)$.
- **Space complexity: $O(\min(n,a))$.** `cnt` has at most one key for each distinct character encountered. A string of length $n$ cannot contain more than $n$ distinct characters, and the alphabet cannot contribute more than $a$. Thus the number of keys is bounded by $\min(n,a)$. The indices, answer, and current character use $O(1)$ additional space.

Counter entries whose counts fall to zero are not deleted by this implementation. That means the mapping can retain characters seen earlier but no longer present in the window. The number of retained keys is still at most the number of distinct characters in the whole string, so the stated bound remains $O(\min(n,a))$. Zero-count entries do not affect the repair condition for the newly inserted character.

Dictionary/Counter access is expected $O(1)$ per operation under the standard hash-table model. The conventional $O(n)$ time bound uses that expectation.

## Alternatives and edge cases

- **Optimized last-seen-index window:** Store each character's latest index and jump `l` directly past a repeated character. This also takes expected $O(n)$ time and $O(\min(n,a))$ space and can avoid step-by-step shrinking. The Counter version is often easier for beginners because its data directly describes the current window.
- **Set-based window:** Keep the current characters in a set, removing from the left until the new character is absent. It has the same asymptotic bounds. Frequencies make the repair condition explicit and generalize naturally to constraints that allow a limited number of copies.
- **Enumerate all substrings:** Generating every start/end pair is $O(n^2)$ even before duplicate checking. Rechecking characters can make it $O(n^3)$. It ignores the reusable overlap between neighboring windows.
- **Fixed-size frequency array:** If the alphabet is guaranteed small and known, an array indexed by character code can replace the Counter. It has fixed $O(a)$ space and often smaller constants, but the dictionary works directly for letters, digits, spaces, symbols, and a broader character set.
- **Empty string:** No window is created, so the initialized answer `0` is returned.
- **One character:** Its frequency becomes one, no shrinking occurs, and the answer becomes `1`.
- **All characters identical:** Every new character after the first causes the left boundary to remove the preceding copy. The window length remains `1`.
- **All characters distinct:** The repair loop never runs, `l` stays at zero, and the answer grows to `n`.
- **Duplicate already outside the window:** Its retained Counter count is zero. Adding the character raises the count to one, so the window does not shrink unnecessarily.
- **Spaces and symbols:** They are ordinary dictionary keys. A repeated space is a duplicate just like a repeated letter; no normalization or filtering should occur.
- **Case sensitivity:** Uppercase and lowercase characters are different keys, so `"aA"` has length `2`, consistent with comparing exact characters.
- **Substring versus subsequence:** Advancing `l` removes a whole prefix of the window and never skips a character inside it. Every candidate is therefore contiguous by construction.

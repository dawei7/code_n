## General

**Enumerate every substring by its start and end**

Every non-empty substring has a unique start index `i` and end index `j >= i`. The exact solution loops over every start and expands the end one character at a time.

For each new start, `cnt = Counter()` begins empty. When `j` advances, `cnt[s[j]] += 1` updates frequencies for exactly substring `s[i : j + 1]`.

Incremental counting avoids rescanning the entire substring for each end.

**Compute beauty from present characters only**

The beauty is the maximum frequency minus the minimum frequency among characters that occur in the substring.

`cnt.values()` contains counts only for characters already seen in the current range. Therefore:

`max(cnt.values()) - min(cnt.values())`

uses the correct positive frequencies and does not mistakenly include zero for absent alphabet letters.

This detail is essential. If absent letters with count zero participated, almost every substring would receive an inflated beauty equal to its maximum frequency.

**Why max and min are constant-factor work**

The string contains only 26 lowercase English letters. The Counter has at most 26 entries, so scanning its values for maximum and minimum takes at most 26 comparisons each.

Although those scans occur inside nested substring loops, 26 is a fixed constraint-domain constant. Thus each end extension has $O(1)$ alphabet work in asymptotic terms.

**Trace one expanding start**

For `s = "aabcb"` and start zero:

- Substring `"a"` has counts one and beauty zero.
- `"aa"` has only count two and beauty zero.
- `"aab"` has frequencies two and one, beauty one.
- `"aabc"` has two, one, one, beauty one.
- `"aabcb"` has counts two for `a`, two for `b`, and one for `c`, beauty one.

The same process restarts at every later start, capturing the other non-zero-beauty substrings.

**Why a single distinct character gives zero**

When a substring contains only one character value, the maximum and minimum present frequency are the same number. Their difference is zero.

This covers one-character substrings and longer homogeneous substrings naturally. No special branch is required.

**Accumulate rather than maximize**

The task asks for the sum of beauty over all substrings, not the greatest individual beauty. The source adds the current difference to `ans` immediately for every `i, j` pair.

Identical substring text at different positions counts separately because each has different endpoints and is visited separately.

**Counter reset is necessary**

When outer index `i` advances, substrings for the new start no longer contain `s[i - 1]`. Recreating the Counter avoids needing to subtract a departing character while the end restarts.

The inner loop then builds all ranges beginning at the new position from scratch in $O(n)$ extensions.

**Why the answer is correct**

The nested loops enumerate every non-empty substring exactly once. At each endpoint, the Counter holds exact frequencies for that substring by incremental construction.

Maximum and minimum over its present counts therefore produce its exact beauty. Adding that value for every endpoint pair yields precisely the requested total.

The phrase "present counts" is essential. Suppose the current substring is `aab`. Its useful frequency multiset is `{2, 1}`, so its beauty is $2-1=1$. The other 24 lowercase letters occur zero times, but they are not characters of this substring and therefore are not candidates for the least-frequent character. Including those zeroes would incorrectly change the result to two. Because the Counter creates keys only when a character is encountered, the implementation enforces this definition naturally.

## Complexity detail

Let $n$ be the string length and $A=26$ the fixed alphabet size. There are $n(n+1)/2=O(n^2)$ substrings. Updating one count is expected $O(1)$, and scanning at most $A$ frequencies is $O(A)=O(1)$ under the fixed alphabet. Total time is $O(n^2)$, matching the manifest.

The Counter stores at most 26 entries and is recreated one at a time. Aside from scalar loop and answer variables, no growing structure is retained. Auxiliary space is $O(1)$ under the lowercase-alphabet constraint.

If alphabet size were treated as variable, time would be $O(n^2A)$ and space $O(A)$.

## Alternatives and edge cases

- **Recount every substring:** Scanning each range from scratch can take $O(n^3)$ time.
- **Fixed array of 26 counts:** It avoids hash overhead and makes the bounded alphabet explicit, while retaining the same complexity.
- **Maintain frequency-of-frequencies:** It can update minima and maxima more cleverly, but is unnecessary for only 26 letters.
- **One-character string:** Its sole substring has beauty zero.
- **All characters equal:** Every substring has one frequency value, so total beauty is zero.
- **All characters distinct within a substring:** Every present count is one and beauty is zero.
- **Absent characters:** They must not contribute zero to the minimum.
- **Repeated substring text:** Different positions are distinct substrings and each contributes.
- **Counter reset per start:** Frequencies from earlier start positions must not leak.
- **End expansion:** Adding one character preserves exact counts without rescanning prior characters.
- **Non-zero beauty:** It requires at least two present characters with different frequencies.
- **Lowercase guarantee:** It bounds Counter size by 26.
- **No modulo:** The problem requests the full integer sum, and Python handles its magnitude.
- **Input preservation:** The string is read only and no substrings are materialized.

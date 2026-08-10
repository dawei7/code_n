## General

**Turn the search into a sequence of candidate starting positions**

Let $n$ be the length of `haystack` and $m$ the length of `needle`. If a match begins at index `i`, it occupies the half-open interval from `i` through `i + m`: the included character indices are `i, i + 1, ..., i + m - 1`.

For all $m$ pattern characters to fit, the final included index must satisfy

$$
i+m-1<n.
$$

Rearranging gives $i\le n-m$. Therefore the only possible starts are

$$
0,1,\ldots,n-m,
$$

which is exactly `n - m + 1` candidates when $m\le n$.

The selected source tests those candidates directly from left to right. It is a straightforward sliding-window comparison implemented with Python string slicing, not the KMP algorithm described later in the local editorial.

**Why the range includes the final legal start**

Python's `range(stop)` excludes `stop`. The loop uses

```python
for i in range(n - m + 1):
```

so its final value is `n - m`. Omitting the `+ 1` would fail to examine the window ending exactly at the end of `haystack`. For example, searching for `"sad"` inside `"butsad"` requires start `3 = 6 - 3`; `range(3)` would stop at two, while `range(4)` correctly includes three.

If `needle` is longer than `haystack`, then `n - m + 1` is zero or negative. Python produces an empty range, so the loop performs no slice and the method returns `-1`. The exact implementation therefore handles this case without a separate length check.

**Extract one window of exactly the pattern length**

For each candidate `i`, the expression

```python
haystack[i : i + m]
```

creates the substring beginning at `i` and ending just before `i + m`. Because the loop considers only legal starts, this slice always contains exactly $m$ characters. It is then compared with `needle` using ordinary string equality.

Equality is true only when the two strings have the same length and every corresponding character is equal. Their lengths are already both $m$, so this comparison precisely asks whether `needle[j] == haystack[i + j]` for every $0\le j<m$.

There is no hash and therefore no collision risk. A true comparison is an exact character match.

**Return immediately to guarantee the first occurrence**

Candidate starts are visited in strictly increasing order. When a matching slice is found, the source executes `return i` immediately. Every smaller start has already been tested and rejected, so `i` must be the first occurrence.

This remains true when occurrences overlap. Searching for `"aaa"` in `"aaaaa"` tests start zero first and returns zero; it does not need to reason separately about matches at one and two. If no candidate matches, control reaches `return -1`, which exactly represents absence.

**Trace the first example**

For `haystack = "sadbutsad"` and `needle = "sad"`, $n=9$ and $m=3$, so candidate starts range from zero through six.

At `i = 0`, the slice `haystack[0:3]` is `"sad"`. Equality succeeds and the method returns zero immediately. Although the same pattern also begins at six, that later candidate is never examined because the contract asks only for the first occurrence.

For `haystack = "leetcode"` and `needle = "leeto"`, the five-character windows begin at indices zero through three:

- `"leetc"` differs from `"leeto"`;
- `"eetco"` differs;
- `"etcod"` differs; and
- `"tcode"` differs.

The loop ends and returns `-1`.

**A loop invariant gives a compact correctness proof**

At the beginning of the iteration for index `i`, no occurrence of `needle` starts at any index smaller than `i`. This is true initially because there is no smaller nonnegative index. If the current slice differs, no occurrence starts at `i`, so the statement remains true for the next iteration. If it matches, the invariant proves that the returned `i` is the smallest matching start.

If the loop finishes, every legal start from zero through `n - m` has failed. A start after `n - m` cannot hold all $m$ characters, so no occurrence exists and `-1` is correct.

**Understand the importance of the non-empty-needle contract**

The Reference guarantees `needle.length >= 1`. Under that contract, the candidate reasoning above describes an ordinary non-empty substring search.

If the source were called with an empty `needle`, `m` would be zero, the first slice `haystack[0:0]` would be empty, and the function would return zero. That happens to match the convention used by many string APIs, but it is outside the stated input domain and is not needed for correctness here.

**This code favors simplicity over reuse of comparisons**

When a window almost matches and fails near its end, the next iteration starts comparison again for the window shifted by one. It does not use information about the shared prefix or suffix of `needle`. That simplicity is often perfectly adequate for short strings, but it determines the exact complexity and distinguishes the source from linear-time KMP.

## Complexity detail

Let $n=\lvert\texttt{haystack}\rvert$ and $m=\lvert\texttt{needle}\rvert$.

- **Exact worst-case time: $O((n-m+1)m)$ when $m\le n$, commonly simplified to $O(nm)$.** There are `n - m + 1` candidate windows. Python must create a length-$m$ slice, which copies $m$ characters, and equality may inspect up to $m$ characters. Inputs such as a long run of `a` characters searched with a pattern ending in `b` force nearly complete comparisons at every start.
- **When $m>n$: $O(1)$ loop work.** The range is empty and the function returns directly after computing lengths.
- **Peak auxiliary space: $O(m)$.** Each slice is a newly allocated string of length $m$. It becomes unreachable after its comparison, so slices do not accumulate across iterations, but one length-$m$ temporary can be live at a time.

The manifest lists $O(n+m)$ time and $O(m)$ space. The space claim matches the exact slicing behavior. The time claim would fit KMP or another genuinely linear matcher, but it does not describe this selected slice-at-every-start implementation. Even if string equality exits early on many ordinary inputs, worst-case analysis must include inputs that share long prefixes.

The output is a single integer and requires $O(1)$ space.

## Alternatives and edge cases

- **KMP prefix table:** Preprocess `needle` so a mismatch reuses the longest matching border instead of restarting. It guarantees $O(n+m)$ time and uses $O(m)$ extra space.
- **Character-by-character naive windows:** Compare without creating slices. It still has $O(nm)$ worst-case time but uses $O(1)$ auxiliary space and can stop a candidate at its first mismatch.
- **Rabin–Karp rolling hash:** Update a window hash in constant time and verify hash matches. It can be linear on average, but modular hashes require collision handling for deterministic correctness.
- **Built-in `haystack.find(needle)`:** In production Python it is concise and highly optimized, but it hides the algorithm and is not the selected source being explained.
- **Needle longer than haystack:** The computed range is empty, so `-1` is returned safely.
- **Equal strings:** There is one candidate at index zero, and it matches.
- **One-character needle:** Every slice has length one; the first equal character index is returned.
- **Match at the last legal start:** The `+ 1` in the range includes index `n - m`.
- **Overlapping matches:** Increasing start order and immediate return still select the earliest one.
- **Repeated prefixes:** They can trigger the quadratic-style worst case because this method does not reuse earlier comparison work.
- **Lowercase restriction:** The algorithm itself works for any Python string characters; the contract's lowercase alphabet needs no special handling.
- **Strings are not mutated:** Slicing creates temporary strings, while both `haystack` and `needle` remain unchanged.
- **Non-empty needle:** Guaranteed locally. For an out-of-contract empty pattern, the exact implementation returns zero.

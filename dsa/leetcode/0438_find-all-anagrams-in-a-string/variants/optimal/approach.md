## General

**Anagrams are determined by frequencies, not order**

A substring is an anagram of `p` exactly when it has the same length and the same count of every lowercase letter. The solution therefore compares a fixed reference Counter `cnt1 = Counter(p)` with a Counter for each length-`n` window of `s`, where `n = len(p)`.

Rebuilding the window counter from scratch at every start would repeat almost all work. Adjacent windows differ by only two events: one new character enters on the right, and one old character leaves on the left. A sliding counter applies those two constant-size updates.

If `len(s) < len(p)`, no substring is long enough. The early return avoids slicing or scanning and returns the empty answer.

**Initialize one character short of a full window**

The exact code constructs

`cnt2 = Counter(s[: n - 1])`.

This represents the first `n-1` characters. The loop then starts at `i = n - 1`, adds `s[i]`, and thereby completes the first full window `s[0:n]` immediately before comparison.

This “one short, then add” organization lets every loop iteration follow the same sequence:

1. add the new rightmost character;
2. compare a full length-`n` window;
3. remove the old leftmost character, leaving `n-1` characters ready for the next iteration.

There is no separate special case for the first window.

**Map loop index to window boundaries**

At the comparison point of iteration `i`, the current window ends at `i` and has length `n`. Its start is

`i - n + 1`.

If `cnt1 == cnt2`, that start is appended. Afterward the same expression identifies the character leaving before the next iteration:

`cnt2[s[i - n + 1]] -= 1`.

On the next loop, adding `s[i+1]` shifts the full window one position right.

**Why Counter equality is the exact test**

Both counters map characters to multiplicities. Equality means every letter occurs equally often. Because both correspond to strings of length `n` at comparison time, this is exactly the definition of an anagram.

The solution decrements outgoing counts but does not delete keys that become zero. In modern Python Counter equality treats missing entries as zero, so a stored zero count compares equal to an absent key. The fixed lowercase alphabet also limits either counter to at most 26 possible keys.

For `s = "abab"` and `p = "ab"`, initialization counts `"a"`. Iteration 1 adds `b`, matches, and records 0; it then removes `a`. Iteration 2 adds `a`, obtains counts for `"ba"`, and records 1. Iteration 3 similarly records 2.

**Sliding-window invariant**

Immediately before adding `s[i]`, `cnt2` represents the `n-1` characters ending at `i-1` that will remain in the next full window. Adding `s[i]` makes it represent exactly `s[i-n+1:i+1]`. After comparison, subtracting the start character restores the `n-1`-character invariant for the next index.

The invariant is true before the first iteration by the initialization slice. Induction proves every length-`n` substring is compared exactly once, in increasing start order. Therefore all and only anagram starts are appended.

**Why output order is increasing**

`i` increases from `n-1` to `m-1`, so `i-n+1` increases from zero upward. Although any output order is allowed, the implementation naturally returns sorted indices.

## Complexity detail

Let $m=\lvert s\rvert$ and $n=\lvert p\rvert$. When $m\ge n$, constructing the two counters costs $O(n)$. The loop has $m-n+1$ iterations. Counter updates are average $O(1)$, and equality examines at most the fixed 26-letter alphabet, which is constant. Total time is $O(m+n)=O(m)$ under $m\ge n$.

The steady counters use at most 26 entries each, or $O(1)$ space for the fixed alphabet. However, the exact expression `s[:n-1]` creates a temporary substring of length $O(n)$ before `Counter` consumes it. Peak auxiliary memory of the shipped Python implementation is therefore $O(n)$, despite the manifest's $O(1)$ claim. Iterating a range of characters without slicing would preserve constant auxiliary space. The returned index list can require $O(m)$ output space.

## Alternatives and edge cases

- **Two fixed arrays of length 26:** Update integer counts by character index and compare arrays. This avoids Counter semantics and uses constant space.
- **Maintain a mismatch counter:** Track how many letter counts differ so each window comparison is strictly $O(1)$ even for a nonconstant alphabet.
- **Sort every window:** Sorting length-`n` substrings costs roughly $O((m-n+1)n\log n)$ and allocates repeatedly.
- **Rebuild a Counter per window:** Correct but costs $O(mn)$ in the worst case.
- **Pattern longer than text:** The early return yields no indices.
- **Equal lengths:** Exactly one complete window is compared.
- **Pattern length one:** Initialization uses an empty slice; each text character is added, checked, then removed.
- **Overlapping anagrams:** Sliding by one preserves and reports them, as in `"abab"`.
- **Zero-count Counter entries:** They remain harmless under modern Counter equality but could be explicitly deleted for compatibility with older semantics.
- **Temporary slice:** It is convenient but is the only reason peak working space depends on `n` in this exact implementation.

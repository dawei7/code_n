## General

**Validity of a candidate substring**

Within a substring of length $W$, suppose the most frequent letter appears $F$ times. Keeping that letter and replacing every other character uses exactly $W-F$ operations. No target letter could require fewer replacements because no other letter occurs more than $F$ times. Therefore the substring is transformable into one repeated letter exactly when

$$
W-F \le k.
$$

This observation supports a sliding window. `cnt` stores character frequencies for the maintained window, `l` is its left endpoint, `r` is the current right endpoint, and `mx` is the largest useful character frequency seen as the window progresses.

**Expand with every new right endpoint**

For each `(r, c)`, the new character enters the window and `cnt[c]` increases. The update

`mx = max(mx, cnt[c])`

records a new frequency high if this character now appears more often than any frequency previously relevant to the scan. The code never decreases `mx` when the left edge later moves. This stale maximum is intentional and is what allows a compact non-shrinking-window formulation.

After insertion, the tentative window length is `r - l + 1`. If

`r - l + 1 - mx > k`,

the tentative size cannot be accepted under the maintained best frequency. The leftmost character is removed from `cnt`, and `l` advances once.

**Why one left move is enough**

This implementation is designed to preserve the largest achievable window length found so far, rather than to keep the current window exactly valid after every iteration.

Before adding `s[r]`, the maintained length is some $L$. Adding one character makes the tentative length $L+1$. If that larger size can be supported, the algorithm keeps it, so the maintained length grows to $L+1$. If it cannot, moving `l` once returns the maintained length to $L$. Thus the maintained length never decreases and grows only when evidence supports a larger answer.

A `while` loop would be needed in a conventional window that insists on exact current validity. Here the size can exceed the true validity of the current contents under a stale `mx`, but it never needs to shrink below the best length already established. One removal per right endpoint maintains that nondecreasing candidate size.

**Why a stale `mx` does not overstate the answer**

When the leftmost occurrence of a frequent character leaves, `cnt` decreases but `mx` is not recomputed. Consequently, `mx` may be larger than the maximum frequency in the current literal window. That can make the test look permissive. It still cannot create a fictitious best length.

Whenever `mx` reached a value $F$, there was an actual contiguous window containing $F$ copies of some letter. The maintained window length at that time was no larger than any later candidate length because lengths never decrease. If a later candidate size $W$ satisfies $W-F \le k$, the earlier region containing those $F$ copies can be extended, when necessary, to a length-$W$ substring within the overall string; the added positions number at most $W-F$ beyond the target copies and can be replaced. Thus a valid substring of that candidate length exists somewhere, even if the current window's exact frequencies no longer demonstrate it.

Equivalently, `mx` serves as historical evidence for whether a new global length is achievable, not as a promise that every maintained window is currently valid. Recomputing it downward would add work without changing the maximum length sought.

**Trace the growth behavior**

For `s = "AABABBA"` and `k = 1`, early windows build a high count of `A`. The candidate can grow to length four because a window such as `"AABA"` has three `A` characters and one replaceable `B`. Attempting to grow beyond four repeatedly violates the replacement budget relative to the best useful frequency, so each new right character is paired with one left move. The maintained length remains four through the end.

The code returns `len(s) - l`. At the final iteration, `r` is `len(s)-1`, so the maintained length is

`r - l + 1 = len(s) - l`.

Because that length never decreased and increased exactly when a larger feasible length was established, it equals the global optimum.

**Why every possible answer is considered**

The right endpoint visits every character. For any target length, the sliding process tests whether the current best length can grow by one while shifting across all relevant endings. If no position supports growth, left and right advance together, preserving the prior best while trying the next location. Once a larger valid substring is encountered, the window retains the increase. Therefore no achievable length is skipped.

## Complexity detail

Let $n = \lvert s \rvert$. The right pointer advances exactly $n$ times, and the left pointer advances at most $n$ times. Counter updates and comparisons are constant time, so total time is $O(n)$.

`cnt` holds at most 26 uppercase-English-letter keys. Since the alphabet size is fixed, this is $O(1)$ auxiliary space. More generally, for an unrestricted alphabet with $u$ distinct characters, the space bound would be $O(u)$.

## Alternatives and edge cases

- **Conventional exact-validity sliding window:** Recompute or maintain the true maximum count and shrink in a `while` loop until `window_length - true_max <= k`. This is correct but may require scanning 26 counts after removals; the stale-maximum technique avoids that work.
- **Try each target letter separately:** Run a two-pointer scan for every distinct uppercase character. It is $O(26n)$, asymptotically linear for a fixed alphabet but repeats the traversal.
- **Binary search the answer length:** Valid lengths are monotone, and a fixed-size window can test each length. This costs $O(n\log n)$ time, slower than the single expanding scan.
- **Enumerate all substrings:** Checking $O(n^2)$ candidates is unnecessary at the maximum input length.
- **`k == 0`:** A window grows only when its maintained evidence consists entirely of one letter, yielding the longest existing identical run.
- **`k >= len(s)`:** The complete string is transformable, and the window grows through all characters.
- **All characters identical:** `mx` grows with the window, the invalid condition never fires, and the answer is `n`.
- **All characters different:** A window can contain at most one unchanged target occurrence, so its maximum valid length is at most `k + 1`, capped by `n`.
- **Stale frequency after removal:** This is deliberate historical evidence for a maximum length; it is not a frequency report for reconstructing an actual transformed substring.
- **Single character:** The one-character window is already repeating and returns one.

## General

**A candidate is valid when all but at most one position match.** For every length-$m$ substring of `s`, where $m=\lvert\texttt{pattern}\rvert$, a direct comparison would find the first mismatch and then check the rest. Doing this independently at every start can repeat almost the same character comparisons and cost $O(nm)$. The source instead precomputes, for every start, how much matches from the left and how much matches from the right.

If a candidate differs from `pattern` at one position $q$, then its first $q$ characters match and its final $m-q-1$ characters match. Their lengths sum to $m-1$. If it matches exactly, the prefix and suffix information is even larger. With two or more mismatch positions, the characters between the earliest and latest mismatch leave a gap of at least two positions, so the matching prefix and suffix sum to at most $m-2$. This creates the test used by the source:

$$
\text{matchingPrefix}+\text{matchingSuffix}\ge m-1.
$$

**Use the Z algorithm to obtain every matching prefix.** For a text $T$, the Z value at index $i$ is the length of the longest prefix of $T$ that also begins at $i$. The helper `z_values` computes all such values in linear time.

The source builds `pattern + "#" + s`. The separator `#` cannot appear in either lowercase input, so a match cannot accidentally continue from the pattern through the separator. The source portion starts at `offset = pattern_length + 1`. Therefore

`forward[offset + start]`

is the number of initial pattern characters matching `s[start:]`. Capping it with `pattern_length` yields the candidate's matching prefix length.

**How the Z-box makes preprocessing linear.** Helper variables `left` and `right` describe the inclusive interval of the rightmost match segment already known to equal the text prefix. If a new `index` lies inside that interval, `values[index - left]` provides reusable prefix information. The code copies no more than the remaining box length with

`min(right - index + 1, values[index - left])`.

It then compares characters only beyond that guaranteed portion. If the match extends farther than the old `right`, the box is replaced. Although the inner `while` can perform several comparisons for one index, every extension advances the global right boundary; the total work remains linear.

**Reverse both strings to turn suffixes into prefixes.** A matching suffix of an original candidate becomes a matching prefix after reversal. The source computes a second Z array over `pattern[::-1] + "#" + s[::-1]`.

The original candidate occupies `s[start:start+m]`. In reversed `s`, that block begins at

$$
n-start-m.
$$

The code names this `reversed_start` and reads `backward[offset + reversed_start]`. After capping at $m$, this is the number of candidate characters matching the pattern from the right.

**Why the prefix-plus-suffix condition is exact.** Suppose there are zero mismatches. Both scans can match the whole pattern, so the condition certainly succeeds. Suppose the only mismatch is at offset $q$. The forward match has length $q$, the backward match has length $m-q-1$, and their sum is $m-1$.

Now suppose there are at least two mismatches, with earliest mismatch $p$ and latest mismatch $q>p$. The forward match stops no later than $p$, while the backward match covers at most the positions after $q$, of length $m-q-1$. Their sum is at most $p+m-q-1\le m-2$. Hence an invalid candidate cannot pass. The test remains safe if prefix and suffix matches overlap on an exact candidate because the requirement is an inequality, not a partition that must be disjoint.

The final loop considers `start` values from zero upward and immediately returns the first valid one. That order proves the returned index is the smallest, not merely some valid occurrence. If no start passes, it returns `-1`.

**Length-one pattern behavior.** When $m=1$, changing its sole character is allowed. Every one-character substring is therefore almost equal, including a different character. The threshold $m-1$ is zero, so start zero passes immediately, exactly as required.

The source comment says the solution was generated when another source was unavailable, but the algorithm stands on the independently checkable Z-array and mismatch-gap reasoning above.

## Complexity detail

Let $n=\lvert s\rvert$ and $m=\lvert\texttt{pattern}\rvert$. Each concatenated text has length $n+m+1$, and each Z computation is linear in that length. Reversing strings, constructing concatenations, and scanning the $n-m+1$ candidate starts are also linear. Total time is $O(n+m)$.

The two Z arrays each use $O(n+m)$ integers. Reversed strings and concatenated strings also occupy $O(n+m)$ temporary storage. The remaining variables are constant-size, so total auxiliary space is $O(n+m)$, matching the manifest.

## Alternatives and edge cases

- **Compare every candidate directly:** It uses $O(1)$ auxiliary space but can cost $O(nm)$ on repetitive strings where comparisons run nearly to the end at many starts.
- **Rolling hash plus longest-common-prefix searches:** Hashes can locate the first mismatch and verify the suffix in roughly $O(n\log m)$ time, but ordinary modular hashing introduces collision risk.
- **Extended KMP or prefix-function methods:** Other linear string-matching preprocessors can derive comparable left/right match lengths. The Z representation is especially direct for prefix-length queries.
- **More than one mismatch:** The earliest and latest mismatches force the prefix/suffix sum below $m-1$, so the candidate is rejected.
- **Exactly one mismatch at the first character:** Prefix length is zero and suffix length is $m-1$, which passes.
- **Exactly one mismatch at the last character:** Prefix length is $m-1$ and suffix length is zero, which also passes.
- **Exact match:** “At most one” includes zero changes, so it must pass even though prefix and suffix matches may overlap.
- **Pattern length one:** Every source character can be changed into it, and the smallest valid index is zero.
- **Pattern nearly as long as source:** The loop simply has few candidate starts; index mapping into the reversed string remains valid.
- **Separator choice:** `#` is safe only because inputs contain lowercase English letters. A general alphabet would require choosing a sentinel absent from both strings or representing symbols structurally.
- **Z-array first entry:** `values[0]` remains zero by convention. The algorithm never needs it for a candidate because all queried positions lie after the separator.
- **Follow-up with $k$ consecutive changes:** The one-gap prefix/suffix condition would become a bound on the unmatched middle block's length; additional care is needed because the changes must be consecutive.
- **First occurrence requirement:** Candidate starts are inspected in increasing order and the method returns immediately, which is what turns validity testing into the minimum-index answer.

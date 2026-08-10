## General

**A swap can repair only two positions**

The strings have equal length, so compare them at matching indices. Positions where `s1[i] == s2[i]` already agree and should remain undisturbed. If one swap is needed, its two chosen indices are the only positions whose characters can move.

This creates exactly three meaningful mismatch counts:

- zero mismatches means the strings are already equal, so using no swap satisfies "at most one";
- exactly two mismatches may be repairable if their characters cross-match;
- one mismatch or more than two mismatches cannot be repaired by one swap.

The protected solution detects these cases in one pass without storing mismatch indices or character-frequency arrays.

**Remember the first mismatched pair**

The loop visits paired characters `a` from `s1` and `b` from `s2` using `zip(s1, s2)`. Equal pairs require no work. At the first mismatch, the solution increments `cnt` to one and saves `c1 = a` and `c2 = b`.

Suppose the first mismatch is at index $i$, so `c1 = s1[i]` and `c2 = s2[i]`. If a later mismatch occurs at index $j$, swapping indices $i$ and $j$ in `s1` works precisely when

$$
\texttt{s1}[j]=\texttt{s2}[i]
\quad\text{and}\quad
\texttt{s2}[j]=\texttt{s1}[i].
$$

In the loop's local variables, these conditions are `a == c2` and `b == c1`. The solution rejects when their negation, `a != c2 or b != c1`, is true.

This is called a cross-match because the first string's character at one mismatched position must equal the second string's character at the other position, in both directions.

**Reject impossible mismatch patterns immediately**

On every mismatch, `cnt` increases. If it becomes larger than two, one swap cannot repair all affected positions, so the solution returns `false` immediately.

The condition is written with `or`: `cnt > 2 or (...)`. Python evaluates `or` from left to right and stops once the left side is true. Therefore, at a third mismatch the function rejects immediately without needing the saved pair for another comparison.

At the second mismatch, `cnt > 2` is false, so the cross-match test is evaluated. A failed cross-match returns `false`. A successful one means swapping these two positions repairs both mismatches. The assignment `c1, c2 = a, b` still runs after this successful check and replaces the stored pair, but no later mismatch can be accepted: a third mismatch triggers the first rejection condition. Consequently, that reassignment does not alter the final decision.

After the scan, the solution returns `cnt != 1`. This accepts zero mismatches and a successfully cross-matched pair of mismatches, while rejecting the single-mismatch case.

**Why exactly one mismatch is impossible**

If only one index differs, changing it through a swap necessarily exchanges its character with another position. Swapping with itself changes nothing. Swapping with a different index changes that other position too, so the original mismatch cannot be fixed while every other position remains equal.

Another way to see this is that swapping preserves the multiset of characters. Two equal-length strings that differ at exactly one position necessarily have different character counts, because one has `s1[i]` where the other has `s2[i]` and no second position balances the difference.

**Following representative inputs**

For `s1 = "bank"` and `s2 = "kanb"`, the first mismatch supplies pair `(b, k)`. The second mismatch supplies `(k, b)`, which cross-matches. Swapping the first and last indices in either one string makes the strings equal, so the scan ends with `cnt = 2` and returns `true`.

For identical strings such as `"kelb"` and `"kelb"`, `cnt` remains zero. No swap is required, and `0 != 1` evaluates to true.

For `"attack"` and `"defend"`, mismatches quickly exceed two or fail the cross-match test. The function correctly rejects without scanning more than necessary.

**Why the final decision is correct**

If the function returns `true` with zero mismatches, the strings already match. If it returns `true` with two mismatches, the second mismatch passed both cross-equality tests, so swapping those positions in `s1` makes each mismatched position agree and leaves every other position unchanged.

Conversely, suppose at most one swap can make the strings equal. If no swap is needed, there are zero mismatches. Otherwise, the two swapped positions are the only possible mismatches, and the characters must cross-match for the exchange to put both in their targets. The scan accepts exactly these two situations and rejects every other mismatch pattern, proving the result is correct.

## Complexity detail

Let $n$ be the common string length. In the worst case, `zip` supplies all $n$ character pairs and the loop performs constant work for each, so time complexity is $O(n)$. Early rejection can finish sooner but does not change the worst-case bound.

The solution stores one integer and two character references. Their number does not grow with $n$, giving $O(1)$ auxiliary space. It does not create slices, sorted copies, frequency maps, or a list of mismatch positions.

The equal-length guarantee is important for `zip`: Python stops at the shorter input. Under the stated contract both lengths are equal, so every position is examined.

## Alternatives and edge cases

- **Store mismatch indices:** Collect at most two indices, reject a third, then check crossed characters. This is also $O(n)$ time and $O(1)$ bounded space, but the protected solution stores the first characters directly.
- **Frequency maps plus mismatch count:** Equal 26-letter frequency arrays and exactly two differences are sufficient, yet cross-matching avoids the extra arrays.
- **Sort both strings:** Equal sorted strings prove they are anagrams but do not prove one swap is sufficient; mismatch positions still need checking, and sorting costs $O(n\log n)$.
- **Try every swap:** Testing all index pairs is at least quadratic and unnecessary once the mismatch structure is understood.
- **Zero mismatches:** No operation is allowed by "at most one," so identical strings correctly return `true`.
- **One mismatch:** It cannot be fixed by a swap and is the only mismatch count rejected at the final return.
- **Two cross-matching mismatches:** One exchange repairs both, even when the mismatches are far apart.
- **Two non-cross-matching mismatches:** A swap merely moves the wrong characters and cannot create equality.
- **More than two mismatches:** One swap changes at most two positions, so early rejection is conclusive.
- **Repeated letters:** They cause no ambiguity because only the characters at mismatched indices must cross-match.
- **Length one:** Valid equal one-character strings have zero mismatches; unequal ones have one and are rejected.
- **Swap in either string:** A successful crossed pair can be repaired by swapping those indices in `s1` or symmetrically in `s2`.
- **Same-index swap:** It changes nothing and matters only as an optional interpretation when strings are already equal.
- **Equal-length contract:** Reusing this exact `zip` loop for unequal strings would miss an unmatched suffix and would require an explicit length check.
- **Lowercase alphabet:** The direct comparison logic does not depend on alphabet size; the constraint simply defines valid inputs.

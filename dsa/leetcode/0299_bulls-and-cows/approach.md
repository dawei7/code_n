## General

The hint counts two different kinds of matches:

- A bull uses a secret digit and a guess digit at the same index.
- A cow uses equal digits at different indices after bull positions have been removed from consideration.

The words “after bull positions have been removed” are essential. One occurrence cannot be counted twice. A digit already used as a bull cannot also be rearranged to create a cow.

The exact source solves the two categories in one scan. It increments the bull count immediately for equal-position digits. For unequal positions, it records the remaining secret digit and remaining guess digit in separate frequency counters. After the scan, it computes how many occurrences of each digit those two unmatched collections have in common.

The local manifest describes fixed digit-frequency arrays. The executable source instead uses two `Counter` objects, so this explanation follows those counters. Because the alphabet contains only ten decimal digits, both representations still use constant-size frequency state.

**Separating bulls before counting cows**

The loop processes corresponding characters `a` from `secret` and `b` from `guess`.

If `a == b`, the position is unquestionably a bull. The source increments `x` and does not add either occurrence to a counter. This permanently pairs the two equal-position occurrences in the strongest category.

If `a != b`, the two occurrences cannot be bulls at this index. The secret occurrence may still match the same digit somewhere else in the guess, and the guess occurrence may still match the same digit somewhere else in the secret. The source records them independently:

- `cnt1[a] += 1` counts an unmatched occurrence available from the secret;
- `cnt2[b] += 1` counts an unmatched occurrence requested by the guess.

The counters do not attempt to pair digits immediately. Deferring the pairing avoids dependence on scan order. A matching guess occurrence may appear before or after the corresponding secret occurrence, and the final frequencies summarize both cases uniformly.

**Why a minimum gives the cow count for one digit**

Fix one digit $d$. Suppose that after all bulls are excluded, `cnt1[d] = s_d` and `cnt2[d] = g_d`.

Every cow of digit $d$ consumes one unmatched $d$ from the secret and one unmatched $d$ from the guess. Therefore, the number of such cows cannot exceed either available count. It is at most

$$
\min(s_d,g_d).
$$

That upper bound is also achievable. Pair any $\min(s_d,g_d)$ secret occurrences with the same number of guess occurrences. All these occurrences came from mismatching positions, so none was already used as a bull. The definition allows the non-bull digits to be rearranged, so their original mismatching positions do not prevent these equal-digit pairs from becoming cows.

Thus, digit $d$ contributes exactly `min(cnt1[d], cnt2[d])` cows.

Different digits cannot compete for the same occurrence: a secret `3` can match only a guessed `3`, never a `7`. The contributions are independent, so summing the per-digit minima gives the total cow count:

$$
y=\sum_d\min(\texttt{cnt1}[d],\texttt{cnt2}[d]).
$$

The source iterates only through keys in `cnt1`. That is sufficient. If a digit occurs only in `cnt2`, the secret has zero available copies, so its contribution would be `min(0, count) = 0`. Omitting explicit zero-contribution keys cannot change the sum.

**Tracing the duplicate-heavy example**

Consider `secret = "1123"` and `guess = "0111"`.

| Index | Secret | Guess | Classification | Remaining counters after the index |
| --- | --- | --- | --- | --- |
| 0 | 1 | 0 | mismatch | secret: `{1: 1}`, guess: `{0: 1}` |
| 1 | 1 | 1 | bull | unchanged |
| 2 | 2 | 1 | mismatch | secret: `{1: 1, 2: 1}`, guess: `{0: 1, 1: 1}` |
| 3 | 3 | 1 | mismatch | secret: `{1: 1, 2: 1, 3: 1}`, guess: `{0: 1, 1: 2}` |

There is one bull at index 1. Among the remaining occurrences, digit 1 contributes

$$
\min(1,2)=1
$$

cow. Digits 0, 2, and 3 have no counterpart in the other unmatched collection, so they contribute zero. The result is `"1A1B"`.

This example demonstrates why a membership-only test is insufficient. The guess contains two unmatched copies of digit 1, but the secret has only one unmatched copy after its bull is removed. Only one cow can be formed.

**Tracing the first example**

For `secret = "1807"` and `guess = "7810"`, index 1 contains 8 in both strings, producing one bull. The other unmatched secret digits are 1, 0, and 7, while the unmatched guessed digits are 7, 1, and 0. Each of those three digits appears once on both sides, so the sum of minima is three cows. Formatting gives `"1A3B"`.

**Why the two-pass logic is exact**

Every bull counted by `x` is valid because the two digits are equal at the same index. Every non-bull occurrence is placed into exactly one appropriate counter, so no occurrence disappears or appears twice.

For cows, the minimum frequency is an unavoidable upper bound for each digit and, through rearrangement, is attainable. Summing those exact independent maxima counts all and only the remaining matches. The bull and cow groups are disjoint because bull occurrences never enter the counters. Therefore, the formatted values represent precisely the required hint.

Finally, `f"{x}A{y}B"` inserts the decimal counts around the required literal separators `A` and `B`. Counts may contain more than one digit; formatted string interpolation handles that without special cases.

## Complexity detail

Let $n$ be the common length of `secret` and `guess`. The `zip` loop processes each aligned pair once, performing constant-time comparisons and counter updates. This costs $O(n)$ time.

The final sum iterates through at most ten possible keys because the inputs contain only decimal digits. Its work is $O(10)$, which is $O(1)$. Total time is therefore $O(n)$.

Each counter holds at most one entry for each of the ten digits. Although counts can grow with $n$, the number of stored keys does not. The frequency state uses $O(10)=O(1)$ auxiliary space, as do the bull and cow counters. This remains constant with respect to input length.

If the character alphabet were unbounded instead of decimal digits, a `Counter`-based solution would use $O(u)$ space for $u$ distinct unmatched characters. Under this problem's digit-only contract, the constant-space bound is exact.

## Alternatives and edge cases

- **Two fixed arrays of length ten:** Convert each unmatched digit to an index and increment two arrays, then sum their minima. This matches the manifest wording and avoids hash-table machinery, while preserving $O(n)$ time and $O(1)$ space. It is not the exact source representation.
- **One signed frequency array in one pass:** For each mismatch, a negative existing count for the secret digit reveals an earlier unmatched guess, and a positive count for the guess digit reveals an earlier unmatched secret. This can count cows online but is less immediately transparent than intersecting two final multisets.
- **Remove matched characters from mutable lists:** Repeated searching and deletion can become $O(n^2)$ and makes duplicate accounting more error-prone.
- **Set intersection:** Sets discard multiplicity. They would undercount when several copies can be cows and overinterpret presence when only one counterpart exists.
- **Counting all common digits before bulls:** The total multiset intersection includes bull occurrences. One may subtract bulls afterward if done carefully, but separating exact matches first makes disjointness explicit and avoids double counting.
- **All digits match in position:** Every index is a bull, both counters remain empty, and the result is `nA0B` with the numeric value of `n` formatted normally.
- **No digit appears in both strings:** Bulls and cows are both zero, yielding `"0A0B"`.
- **Same multiset in different order:** If no positions match but both strings contain the same digit multiplicities, there are zero bulls and $n$ cows.
- **Repeated secret digit:** The number of cows for that digit cannot exceed its unmatched secret frequency, regardless of how many copies the guess contains.
- **Repeated guess digit:** Symmetrically, cows cannot exceed the unmatched guess frequency even when the secret has more copies.
- **Leading zeros:** Inputs are strings rather than numeric values, so a leading `0` remains a real digit and is counted at its position.
- **Equal-length guarantee:** `zip` stops at the shorter input, but the contract guarantees equal lengths, so every position is processed. The source deliberately does not add a separate length check.
- **Length one:** The only pair is either a bull or a mismatch. A mismatching one-character guess cannot produce a cow because no equal digit exists elsewhere.
- **Maximum length:** The method performs one linear scan and stores only ten possible frequency entries, so length 1000 requires no special handling.
- **Output format:** The literal letters are always uppercase and appear in the exact order `A` then `B`, including when either count is zero.

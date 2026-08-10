## General

**Only presence matters, not frequency or order.** A letter is special when at least one lowercase occurrence and at least one uppercase occurrence appear anywhere in `word`. Ten copies do not count more than one copy, and uppercase may appear before or after lowercase.

The exact source therefore converts the string to `s = set(word)`. A set keeps one copy of every distinct character and supports expected constant-time membership tests.

**Pair corresponding lowercase and uppercase letters.** `ascii_lowercase` is `"abcdefghijklmnopqrstuvwxyz"` and `ascii_uppercase` is `"ABCDEFGHIJKLMNOPQRSTUVWXYZ"`. `zip` pairs characters at equal positions:

`(a,A), (b,B), ..., (z,Z)`.

For each pair `(a,b)` in the source's variable names, the Boolean expression:

`a in s and b in s`

is true exactly when both cases of that alphabet letter occur.

**Booleans can be summed in Python.** Python treats `True` as integer one and `False` as zero in arithmetic. The generator supplies 26 Boolean values to `sum`, so the returned integer is the number of letter pairs satisfying both membership tests.

The variable name `b` refers to an uppercase character from `ascii_uppercase`, not specifically the letter b. For the first iteration, `a` is lowercase `a` and `b` is uppercase `A`.

**A trace for `"aaAbcBC"`.** The set contains lowercase a, b, and c, and uppercase A, B, and C. Pairs a/A, b/B, and c/C each produce true. Every other pair lacks both or at least one case. The sum is three.

For `"abBCab"`, lowercase a and b occur, while uppercase B and C occur. Only b/B has both cases, so the result is one.

**Why a set is the correct abstraction.** The property is existential:

$$
\text{special}(c)
\iff
\text{lowercase }c\text{ appears}
\land
\text{uppercase }c\text{ appears}.
$$

A set records exactly these existence facts. Counts, positions, and original order contain no additional information relevant to version I.

**A direct correctness proof.** For every English letter $c$, `zip` creates exactly one pair containing its lowercase and uppercase forms. The membership expression returns true if and only if both forms occur in `word`, which is exactly the definition of special. Summing contributes one for each special letter and zero for each nonspecial letter. Since all 26 letters are examined once, the result is exact.

**Difference from version II.** This first version does not require lowercase occurrences to precede uppercase occurrences. The set deliberately forgets positions. That would be insufficient for problem 3121, but it is ideal here. An explanation that adds ordering requirements would solve the wrong contract.

**A manifest mechanism mismatch.** The local Optimal manifest says the source maintains two 26-bit masks. That is a valid constant-space alternative, but `solution.py` creates one Python set and tests paired characters. Its complexity bounds remain the same under the fixed alphabet, while the actual data structure should be documented faithfully.

**Case is significant.** Python sets distinguish `"a"` from `"A"` because they are different one-character strings. No normalization such as `lower()` is applied; normalizing would destroy exactly the information the problem asks to compare.

**The scan of the alphabet is constant-sized.** Even if `word` is short, the generator still tests all 26 pairs. This guarantees completeness and remains constant work relative to input length.

## Complexity detail

Building `set(word)` scans $n$ characters and takes expected $O(n)$ time. The generator performs exactly 26 pairs of expected $O(1)$ membership checks, adding $O(26)$. Total expected time is $O(n+26)=O(n)$.

The set can contain at most 52 distinct English letter characters. Under the fixed alphabet, auxiliary space is $O(52)=O(1)$ relative to $n$. In a generalized alphabet of size $A$, it would be $O(A)$.

The set construction is the only input-dependent allocation. `zip` and the generator are lazy.

## Alternatives and edge cases

- **Two bit masks:** Set a lowercase or uppercase bit for each character, AND the masks, then count set bits. This matches the manifest and uses constant integer state.
- **Two Boolean arrays:** Store 26 lowercase flags and 26 uppercase flags; equally clear and constant-sized.
- **Nested string membership without a set:** Test every alphabet character directly in `word`, costing up to $O(26n)$, still linear for a fixed alphabet but repeatedly scanning.
- **Only lowercase characters:** No uppercase partner exists, so answer is zero.
- **Only uppercase characters:** Symmetrically zero.
- **One matching pair:** Count is one regardless of how often either case appears.
- **Duplicates:** The set removes them because frequency does not matter.
- **Order:** Uppercase may appear first; version I still counts the letter.
- **Mixed unrelated cases:** Lowercase a and uppercase B do not form a pair.
- **Empty concern:** The contract gives at least one character; even an empty set would safely yield zero.
- **All 52 case variants:** Every letter pair succeeds and answer is 26.
- **Case-sensitive membership:** Essential to distinguish the two required forms.
- **Lazy zip:** It aligns corresponding alphabet positions without building a pair list.
- **No input mutation:** `word` is read to create a separate set.
- **Source/manifest mismatch:** Exact source uses a set rather than bit masks, though both have $O(n)$ time and fixed-alphabet $O(1)$ space.

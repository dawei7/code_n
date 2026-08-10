## General

The palindrome is defined after normalization: ignore every non-alphanumeric character and compare letters without regard to uppercase or lowercase. Building the normalized string would be simple, but it is unnecessary. Two pointers can perform filtering and comparison directly on the original input.

`i` begins at the left end and `j` at the right end. The algorithm moves inward, skipping ignored characters and comparing the next meaningful pair.

**What must match in a palindrome**

Imagine the filtered lowercase sequence as $c_0,c_1,\ldots,c_{m-1}$. It is a palindrome exactly when:

$$
c_k=c_{m-1-k}
$$

for every position in the first half.

The two pointers discover those pairs without storing the sequence. The left pointer finds the next unused normalized character from the front, and the right pointer finds the next unused normalized character from the back.

**The outer-loop invariant**

Before each iteration, all meaningful characters strictly outside `[i, j]` have already been paired successfully. Any characters skipped there were non-alphanumeric and do not belong to the normalized phrase.

Therefore the remaining palindrome question is entirely inside the current interval. If the pointers meet or cross, every required pair has matched and the method can return true.

**How the `if/elif` chain filters endpoints**

If `s[i]` is not alphanumeric, it cannot affect the normalized text, so the source increments `i`.

Only when the left endpoint is meaningful does the `elif` test the right endpoint. If `s[j]` is non-alphanumeric, `j` is decremented.

The chain skips at most one endpoint per outer iteration. That is still efficient: each skip permanently removes one input position from consideration, and neither pointer ever moves outward.

When both endpoints are non-alphanumeric, the left one is skipped first and the right one on a later iteration. The order changes only the number of loop iterations by a constant factor, not correctness.

**Comparing meaningful characters**

When both endpoints are alphanumeric, the source compares `s[i].lower()` with `s[j].lower()`.

For printable ASCII, letters normalize to their lowercase forms and digits remain unchanged. If the values differ, these are the next unmatched characters from opposite ends of the normalized sequence, so no later skipping or pairing can repair the mismatch. Returning false immediately is correct.

If they match, both positions have been successfully paired. `i` advances and `j` retreats so they are never examined again.

**Why reaching the middle means success**

Every iteration either:

- removes one ignored left character;
- removes one ignored right character;
- rejects a mismatched meaningful pair; or
- consumes a matched meaningful pair from both sides.

If no mismatch occurs, eventually `i >= j`. A single remaining meaningful character is the center of an odd-length palindrome and needs no partner. A single remaining ignored character contributes nothing. Crossing pointers means the normalized sequence had even length and all pairs matched.

Thus returning true after the loop covers both odd and even normalized lengths, including zero.

**Tracing the Panama phrase**

In `"A man, a plan, a canal: Panama"`, the initial `A` and final `a` compare equal after lowercase conversion.

The pointers move inward. Spaces, commas, and the colon are skipped when they reach an endpoint. Meaningful pairs compare as `m` with `m`, `a` with `a`, and so forth.

No normalized mismatch appears, and the pointers meet after effectively comparing `"amanaplanacanalpanama"` from both ends. The method returns true without ever allocating that normalized string.

**Tracing a mismatch**

For `"race a car"`, filtering conceptually yields `"raceacar"`. Outer pairs `r/r`, `a/a`, and `c/c` match, but the next meaningful pair is `e/a`.

The source returns false at that point. Characters closer to the center cannot change the already determined outer mismatch.

**All-ignored input**

For a string containing only spaces or punctuation, the loop repeatedly moves pointers past ignored positions. It never enters a mismatch branch and eventually returns true.

This matches the rule that the empty normalized string reads the same forward and backward.

**Why ASCII matters**

Python's `isalnum` and `lower` support Unicode, but the local contract restricts input to printable ASCII. Under that domain, “alphanumeric” means ASCII letters and digits, and lowercasing retains one character.

The source reads the string but does not modify it. Python strings are immutable in any case.

## Complexity detail

Let $n$ be the original string length. Pointer `i` increases at most $n$ times and `j` decreases at most $n$ times. Although one ignored character may consume one outer iteration, total work is $O(n)$.

The method stores two indices and temporary one-character lowercase results. Auxiliary space is $O(1)$.

No normalized copy, reversed string, regular-expression result, or character array is allocated. The Boolean output uses constant space.

Early mismatch can finish before reading the whole string, but worst-case palindromes and all-ignored inputs require a linear scan.

## Alternatives and edge cases

- **Normalize and reverse:** Filter alphanumerics, lowercase them, and compare the result with its reverse. It is concise but uses $O(n)$ additional space.
- **Competitive run-skipping loops:** Skip all ignored characters at each side before one comparison. It has the same asymptotic bounds and may use fewer outer iterations.
- **Regular-expression filtering:** Can remove non-alphanumerics, but character-class details and extra string allocation make it less direct.
- **Recursive outer comparison:** Mirrors the definition but can use $O(n)$ call-stack space.
- **One character:** The loop never runs and returns true.
- **Only punctuation or spaces:** Normalizes to empty and returns true.
- **Mixed case:** Lowercase conversion makes `A` match `a`.
- **Digits:** Digits are meaningful and must match exactly.
- **Letter versus digit:** They are both alphanumeric but unequal.
- **Ignored endpoints on both sides:** The `if/elif` chain removes them over separate iterations without losing a meaningful character.
- **Odd normalized length:** The center character needs no comparison.
- **Even normalized length:** Pointers cross after the final pair.
- **First mismatch:** Immediate false is safe because normalized outer order is fixed.
- **Printable ASCII domain:** Python's broader Unicode classification is irrelevant to the stated inputs.

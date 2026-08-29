## General

Two strings are anagrams exactly when every character has the same frequency in both strings. Their order is irrelevant; only the counts matter.

Because an operation may only append a character, an existing excess cannot be removed. If `s` contains more copies of a letter than `t`, those extra copies must be matched by appending that letter to `t`. If `t` contains more, the missing copies must instead be appended to `s`.

The exact solution records the signed difference for every letter and adds the absolute sizes of all differences.

**Count the characters already present in `s`**

`Counter(s)` creates a mapping from each character to its number of occurrences in `s`. Call the stored value for character $c$

$$
d_c=\operatorname{count}_s(c)
$$

at this initial stage.

There is no need to store positions because appending never changes how many copies already exist, and anagram equality does not care where a character appears.

**Subtract every character from `t`**

The loop over `t` executes `cnt[c] -= 1` for each character. After all of `t` has been processed, every mapping value is

$$
d_c=\operatorname{count}_s(c)-\operatorname{count}_t(c).
$$

A positive value means `s` has an excess and `t` lacks that many copies. A negative value means `t` has an excess and `s` lacks the magnitude. Zero means the two strings already agree for that letter.

Python's `Counter` returns zero for a missing key. Therefore, when `t` contains a character absent from `s`, decrementing it safely creates a negative entry. No separate union of the two alphabets is required.

**Translate one signed difference into required appends**

Suppose `d_c = 3`. The current strings differ by three copies of $c$, with `s` holding more. Since deletion is forbidden, the only way to equalize this letter is to append at least three copies to `t`. Appending exactly three is sufficient.

If `d_c = -2`, the symmetric action is to append two copies to `s`. In both cases the minimum number of steps devoted to $c$ is `abs(d_c)`.

Appending some different letter cannot repair this imbalance. Character counts are independent coordinates: an operation changes exactly one coordinate in exactly one string.

**Sum all independent deficits**

The return expression `sum(abs(v) for v in cnt.values())` adds the required operations for every stored letter.

This is a generator, so absolute values are produced one at a time rather than collected in a list. Letters with zero difference contribute zero.

For `s = "leetcode"` and `t = "coats"`, each signed difference identifies either letters that must be added to `t` or letters that must be added to `s`. The absolute values total seven, matching the example construction.

For `"night"` and `"thing"`, all frequency differences are zero even though positions differ. The sum is zero because the strings are already anagrams.

**Why the sum is a lower bound**

For each letter $c$, the strings begin with a count gap of $\lvert d_c\rvert$. One append changes that gap by at most one and only if the appended character is $c$ and it is added to the deficient string.

Therefore any successful sequence needs at least $\lvert d_c\rvert$ operations for letter $c$. Since one operation appends only one character, operations required for different letters cannot be shared. Every solution needs at least

$$
\sum_c\lvert d_c\rvert
$$

steps.

**Why the lower bound is achievable**

For every positive `d_c`, append exactly `d_c` copies of $c$ to `t`. For every negative value, append exactly `-d_c` copies to `s`.

After these actions, both strings have equal counts for every letter. They are therefore anagrams, regardless of the order in which the new characters were appended.

This construction uses exactly the returned sum, so the lower bound is achievable and hence minimal.

**Why original lengths need no separate handling**

If the strings have different lengths, the signed differences automatically reflect the total mismatch. In fact,

$$
\sum_c d_c=\lvert s\rvert-\lvert t\rvert.
$$

The absolute-value sum handles both the net length gap and mismatched character identities. Adding a separate length-difference term would double-count part of the required work.

## Complexity detail

Let $n=\lvert s\rvert$ and $m=\lvert t\rvert$. Building the counter scans $n$ characters, subtracting `t` scans $m$, and summing the entries scans at most the 26 lowercase letters. Total time is $O(n+m)$.

The input alphabet is fixed to 26 lowercase English letters, so the counter has at most 26 keys and uses $O(1)$ auxiliary space with respect to input lengths. More generally, for an unbounded alphabet with $A$ distinct characters, space would be $O(A)$.

The generator used by `sum` adds only constant iterator state and does not allocate a second collection. The manifest's $O(n+m)$ time and $O(1)$ space match the exact implementation.

## Alternatives and edge cases

- **Two fixed arrays:** Count each lowercase letter in separate 26-entry arrays and sum absolute differences. This has the same bounds and makes the constant alphabet explicit.
- **One signed array:** Increment for `s` and decrement for `t`, mirroring the Counter solution without hashing.
- **Sort both strings:** Sorting reveals count groups but costs $O(n\log n+m\log m)$ time and still requires reconciling unmatched runs.
- **Already anagrams:** Every difference is zero, so no append is needed even if the character order differs.
- **Disjoint alphabets:** Every existing character is unmatched, so the answer is `len(s) + len(t)`.
- **One string longer:** Length difference alone is not sufficient; the identity of excess letters still matters and is captured by signed counts.
- **Character only in `t`:** Counter's missing-key default becomes a negative frequency safely.
- **Repeated characters:** The magnitude records all missing copies rather than merely whether a character is present.
- **Append-only rule:** Excess characters cannot be removed, which is why the deficient string must be extended.
- **Order of appended letters:** Any order works because only final frequency equality defines an anagram.
- **Nonempty inputs:** The contract guarantees both strings contain at least one character, though the same logic would also handle empties.
- **Input preservation:** Strings are immutable, and all mutations occur in the separate Counter.
- **No double counting:** Each absolute difference represents operations for one letter coordinate exactly once.

## General

**Expand every possible substring start**

A substring is nice when every letter appearing in it is present in both lowercase and uppercase. The exact solution enumerates every substring by choosing a start `i` and extending an end `j` from `i` through the end of `s`.

For each fixed start, `ss` stores the distinct characters in the current substring `s[i : j + 1]`. When `j` advances, adding `s[j]` updates this set in constant expected time.

The method checks every candidate for niceness and replaces the best answer only when the candidate is strictly longer.

**Test both cases of every present letter**

The expression:

`all(c.lower() in ss and c.upper() in ss for c in ss)`

iterates over every distinct character currently present. For each character `c`, `c.lower()` identifies its lowercase form and `c.upper()` its uppercase form. Both must belong to `ss`.

If `c` is lowercase, the lowercase membership is already known but the uppercase membership is meaningful. If `c` is uppercase, the reverse is true. Checking both for every set entry is somewhat redundant, yet it makes the rule symmetric and exact.

Because the input contains only English letters, `ss` has at most 52 entries. The `all` test is therefore bounded by a constant alphabet factor even as `n` grows.

**Why all over the set is sufficient**

Suppose the condition succeeds. Every character present has both case forms in the set, so every underlying alphabet letter used by the substring appears in lowercase and uppercase. The substring is nice.

Suppose the substring is nice. For any `c` in its set, the definition guarantees both forms of that same letter are present. The generator condition is true for every `c`, so `all` succeeds.

Thus the test is exactly equivalent to the problem's niceness definition.

**Update only for a strictly longer candidate**

The length of inclusive substring `i..j` is `j - i + 1`. The source requires:

`len(ans) < j - i + 1`.

When both the niceness test and this strict inequality hold, it saves a copy `s[i : j + 1]` as the new answer.

Strict comparison implements the earliest-occurrence tie rule. Outer starts `i` are visited in increasing order. Once a nice substring of some length has been saved, another substring of equal length encountered later cannot replace it. Therefore the earliest start among maximum-length candidates remains stored.

For one fixed start, ends also increase, so longer candidates naturally replace shorter ones.

**Trace the first example**

For `"YazaAay"`, many early substrings fail because they contain `Y` without `y` or `z` without `Z`.

When start reaches the lowercase `a` before `A` and expansion reaches `"aAa"`, the set contains `a` and `A`. Both case forms exist for every set entry, so the substring is nice and has length three.

Longer candidates include letters missing one case and fail. The stored result remains `"aAa"`.

**Why a one-character substring cannot pass**

For any English letter, lowercase and uppercase are distinct characters. A one-character set contains only one form, so either `c.lower()` or `c.upper()` is absent. The niceness test returns false.

If no larger candidate passes, `ans` remains the empty string initialized before the loops. This naturally handles the “none exists” requirement.

**Enumeration completeness**

Every non-empty substring has a unique pair of endpoints `(i, j)` with `0 <= i <= j < n`. The nested loops visit exactly every such pair: the outer loop chooses `i`, and the inner loop visits all `j >= i`.

The set for each start incrementally represents exactly that current range because it begins empty and receives each successive character once. No candidate is skipped.

**Why the returned substring is correct**

The exact membership test accepts precisely nice candidates. The algorithm examines every substring, so it must encounter every possible answer.

It updates `ans` whenever a longer nice candidate appears and never replaces it for an equal length. Consequently, after enumeration, `ans` has maximum possible length and, among that length, the earliest occurrence. If no nice candidate exists, it correctly remains empty.

## Complexity detail

Let $n$ be the string length and let the alphabet size be $A=52$. There are $O(n^2)$ endpoint pairs. Each `ss.add` is expected $O(1)$, and the `all` expression examines at most $A$ set entries, so its cost is $O(A)=O(1)$ under the fixed English-letter alphabet. Substring copies occur only when a strictly longer best is found; there are at most $n$ such improvements and their total copy cost is $O(n^2)$. Overall time is $O(n^2)$.

For one start, `ss` holds at most 52 characters, which is $O(1)$ under the fixed alphabet. `ans` is one retained string slice of length at most $n$, and a replacement slice also has length at most $n$. Peak auxiliary storage is therefore $O(n)$ in the exact Python source.

This is tighter than the manifest's stated $O(n^2)$ space. The implementation does not store all substring sets or all candidates simultaneously; it retains only the current set and current best string.

## Alternatives and edge cases

- **Divide and conquer on a bad letter:** Any substring containing a letter without its opposite case cannot be nice as a whole, so split around such characters recursively. It can be elegant but has more involved tie handling.
- **Bitmasks:** Track 26 lowercase and uppercase presence bits while expanding. It avoids repeated set case conversions and keeps the same $O(n^2)$ time.
- **Brute-force rescanning each substring:** Rebuilding its character set from scratch adds another factor of $n$, leading toward $O(n^3)$.
- **Whole string nice:** It is eventually saved and cannot be beaten, so it becomes the answer.
- **One-character input:** No nice substring exists, and empty string is returned.
- **Only one case of every letter:** Every candidate fails.
- **Repeated characters:** Sets intentionally ignore multiplicity because niceness asks only whether both forms occur.
- **Several maximum answers:** Increasing start order plus strict length update preserves the earliest.
- **Uppercase-first pair:** Order inside a substring does not matter; only set membership matters.
- **Mixed unrelated letters:** Every included letter needs its own opposite case.
- **Fixed alphabet:** The $O(n^2)$ time analysis treats at most 52 membership checks as constant.
- **Set recreated per start:** Characters from a previous start must not leak into the next substring family.
- **String slicing:** Saving `s[i:j+1]` copies the candidate in Python, contributing up to linear space.
- **Empty initial answer:** It is both the no-solution result and a length-zero baseline for comparisons.

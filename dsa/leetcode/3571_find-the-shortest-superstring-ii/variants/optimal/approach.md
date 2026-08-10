## General

With only two strings, a shortest common superstring has one of three forms:

1. one string already contains the other;
2. a suffix of `s1` overlaps a prefix of `s2`;
3. a suffix of `s2` overlaps a prefix of `s1`.

If there is no containment, any shortest solution can be obtained by maximizing one of the two boundary overlaps. The source checks containment, then scans possible overlap lengths in decreasing order for both concatenation directions.

The manifest describes KMP prefix functions, but the exact implementation does not build or use KMP. It relies on Python’s substring, `startswith`, and `endswith` operations inside a loop.

**Normalize so s1 is not longer**

The source first compares lengths. If `len(s1) > len(s2)`, it recursively calls the same method with arguments swapped.

After at most one swap, `m = len(s1) <= n = len(s2)`. This simplifies containment: only the shorter string `s1` can fit entirely inside the longer `s2`. If lengths are equal and one contains the other, they must be identical.

The recursive swap cannot continue indefinitely because the swapped pair satisfies the length order.

**Containment is always the best case**

If `s1 in s2`, returning `s2` is optimal. Any result containing `s2` must have length at least `n`, and `s2` itself already contains both strings.

This check also handles identical strings and appearances of `s1` in the middle of `s2`. Boundary-overlap checks alone would miss middle containment.

After containment fails, a shortest result must include characters unique to both strings and therefore combines them at a boundary.

**Scanning overlap sizes from largest to smallest**

The loop index `i` ranges from zero through `m-1`. The candidate overlap length is `m-i`. As `i` increases, overlap length decreases:

`m, m-1, ..., 1`.

Full overlap length `m` at `i=0` cannot succeed after containment unless the strings have a special equal-boundary relation that would itself imply containment, but checking it is harmless.

**Direction 1: s1 before s2**

`s2.startswith(s1[i:])` asks whether suffix `s1[i:]` equals a prefix of `s2`.

If so, those characters can be shared. The merged string is

`s1[:i] + s2`.

It contains all of `s1`: the first `i` characters come from `s1[:i]` and the remaining suffix is the equal prefix of `s2`. It contains all of `s2` directly.

Its length is `i+n`. Smaller `i` means larger overlap and shorter total length.

**Direction 2: s2 before s1**

`s2.endswith(s1[:m-i])` asks whether a suffix of `s2` equals prefix `s1[:m-i]`.

If so, the nonoverlapping tail of `s1` is `s1[m-i:]`, and the merged result is

`s2 + s1[m-i:]`.

This also has length `n+i`.

At a fixed `i`, successful candidates in either direction have the same length. The problem allows any answer when several shortest strings exist, so the source may return the first condition it checks.

**Why the first successful loop iteration is globally shortest**

Both concatenation directions are checked for every `i` before the loop advances. A success at index `i` yields length `n+i`.

All later iterations have larger indices and therefore produce length at least `n+i+1`. No later overlap can be better. If the other direction had a larger overlap, it would have succeeded at an earlier iteration and already returned.

Thus the first success across the paired tests maximizes boundary overlap over both directions and minimizes merged length.

If no positive overlap exists in either direction, the strings must be concatenated without sharing characters. `s1+s2` has length `m+n` and is optimal; reversing the order would have the same length, so either is allowed.

**A representative trace**

For `s1="aba"` and `s2="bab"`, lengths are equal and neither contains the other.

At `i=0`, no full three-character boundary overlap exists. At `i=1`, suffix `s1[1:]="ba"` equals the prefix of `s2`. The method returns `s1[:1]+s2 = "a"+"bab" = "abab"`.

The overlap length is two, so the result length is four. No three-character superstring can contain two different length-three strings, making four optimal.

## Complexity detail

Let `m \le n` after normalization.

The manifest claims `O(m+n)` time through KMP, but the exact source has no prefix-function preprocessing. Under conventional algorithmic bounds, testing `s1 in s2` can take `O(mn)` worst-case with a straightforward substring search, though CPython uses optimized internal algorithms whose implementation-level behavior can be better on many inputs.

The overlap loop runs `m` iterations. It creates slices of total length up to `m` and performs prefix/suffix comparisons of up to `m` characters per iteration, giving `O(m^2)` worst-case work. Since `m \le n`, this is contained in `O(mn)`. A faithful portable upper bound is therefore `O(mn)`, not guaranteed `O(m+n)`.

Space for the returned string is `O(m+n)`. Each slice and concatenation may allocate temporary strings of `O(m+n)` size, but they are not all retained simultaneously. Auxiliary peak space is `O(m+n)` including such temporaries and the result. Recursion depth is at most two calls.

With the published maximum length 100, the quadratic scanning is easily fast enough despite the manifest mismatch.

## Alternatives and edge cases

- **KMP prefix functions:** Combining strings with a delimiter and computing prefix functions can find each maximum boundary overlap in linear time. This would realize the manifest summary, but it is not the current source.
- **Z algorithm:** Z-values on appropriate concatenations also find containment and maximum overlaps in `O(m+n)` time.
- **Try every merged string:** Brute-force alignment across both directions is similar in spirit to the source but can be expressed more explicitly; boundary overlap checks are the compact version.
- **One string contained in the other:** Return the containing string immediately, including middle containment.
- **Equal strings:** The containment test returns either identical string.
- **Original s1 longer:** One recursive swap normalizes the order without changing the symmetric problem.
- **Overlap in both directions:** The loop compares equal overlap lengths at the same `i`. Either result is allowed when lengths tie.
- **No overlap:** Direct concatenation is shortest and the chosen order is permitted.
- **One-character strings:** Equality is handled by containment; different characters have no overlap and concatenate.
- **Repeated-character patterns:** They can make naive substring/overlap comparisons approach their worst case, which is why the source cannot claim KMP’s linear guarantee.
- **Lexicographic order:** The problem asks only for minimum length, not the lexicographically smallest among ties, so returning the first equal-length candidate is correct.
- **Lowercase alphabet:** No delimiter concerns arise in the current scanning method. A KMP concatenation would need a separator outside the lowercase alphabet.
- **Substring versus subsequence:** Containment and overlaps require contiguous equality; the Python operations used enforce exactly that.

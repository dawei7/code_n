## General
**Equal strings share every subsequence**

If $a = b$, selecting any index sequence from one string selects the same characters from the other. No subsequence can belong to exactly one input, so return `-1`.

**Different lengths make the longer whole string uncommon**

When lengths differ, the longer input is a subsequence of itself but cannot be a subsequence of the shorter input. Its full length is therefore achievable, and no subsequence can be longer than its source string.

**Different strings of equal length are uncommon in full**

A subsequence having the same length as its source must retain every character. Thus one equal-length input could be a subsequence of the other only if the strings were identical. When they differ, either complete string is uncommon and their shared length is optimal.

**Collapse all cases into one expression**

The two nonidentical cases both return `max(len(a),len(b))`; only equality returns `-1`. No subsequence enumeration or dynamic programming is needed.

## Complexity detail
String equality may inspect all characters and lengths are constant-time metadata, giving $O(|a| + |b|)$ worst-case time. The method uses $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Enumerate all subsequences:** is correct but creates exponentially many candidates.
- **Longest-common-subsequence DP:** computes much more information than needed and takes $O(|a| \cdot |b|)$ time.
- **Explicit subsequence tests of both whole strings:** reaches the same conclusion but adds unnecessary scans.
- **Identical strings:** return `-1`, including identical one-character strings.
- **One string longer:** its whole length is immediately optimal.
- **Equal lengths but one differing position:** each complete string is already uncommon.
- **Repeated characters:** do not change the equality-based reasoning.

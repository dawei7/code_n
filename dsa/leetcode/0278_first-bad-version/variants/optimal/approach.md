## General

**The version predicate changes only once**

Maintain an inclusive interval containing the first bad version. If the midpoint is bad, keep it and search left; otherwise discard it and everything earlier.

The first bad version always lies in `[left, right]`. A bad midpoint makes `[left, middle]` the only relevant half; a
good midpoint makes `[middle + 1, right]` the only relevant half.

**Keeping a bad midpoint preserves the boundary candidate**

If the midpoint is good, monotonicity proves every earlier version is good and the boundary must be to its right. If it
is bad, the midpoint might itself be the first bad version, so the search retains it while discarding only later
candidates. Each update preserves the transition point until the interval contains one version, which must be the
answer.

LeetCode supplies `isBadVersion(version)` as a hidden judge API. The offline app receives its monotone boundary as
`bad` and defines a local predicate over that fixture; the binary-search body then makes the same predicate calls as
the native solution.

## Complexity detail

Each API call reduces the inclusive search interval to at most half its previous size, so the search makes at most
$\lceil \log_2 n \rceil$ calls. This is $O(\log n)$ time and $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Scan from version one:** may make $O(n)$ API calls.
- **First version is bad:** every midpoint is bad, so the right boundary contracts to one.
- **Last version is bad:** every earlier midpoint is good, so the left boundary advances to `n`.
- **Single version:** `left == right` initially, so no API call is needed and version one is returned.
- **Fixed-width midpoint overflow:** computing `left + (right - left) // 2` avoids adding two potentially large version
  numbers before division.

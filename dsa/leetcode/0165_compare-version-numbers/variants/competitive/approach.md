## General
Given two **version strings**, `version1` and `version2`, compare them. A version string consists of **revisions** separated by dots `'.'`. The **value of the revision** is its **integer conversion** ignoring leading zeros, the algorithm executes a single-pass linear scan through input elements. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(m + n)$ — Operation count bound.
- **Space Complexity**: $O(m + n)$ — Auxiliary memory allocation bound.

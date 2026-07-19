## General
**Identify every palindrome by its center**

Each palindromic substring has exactly one center. Odd-length palindromes center on one character, while even-length palindromes center between two adjacent characters. Enumerating both center types covers every possible palindrome without duplication.

**Expand while mirrored characters agree**

For a chosen left/right center pair, compare the two characters. Every successful comparison identifies one palindrome; then move the endpoints outward and repeat until a boundary is crossed or the characters differ.

**Count index ranges rather than distinct text**

Increment immediately for every valid expansion. Two equal strings at different locations arise from different center expansions or radii and therefore contribute separately, as required.

**Why the count is exact**

Every successful expansion produces a contiguous range whose mirrored characters match, so it is a palindrome. Conversely, every palindrome shrinks symmetrically to either one central character or one central gap; the expansion from that unique center reaches its exact radius and counts it once. Thus the procedure is both sound and complete.

## Complexity detail
There are $2N - 1$ centers. A center may expand across $O(N)$ characters, giving $O(N^2)$ worst-case time, attained when all characters are equal. The two indices and counter use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Dynamic programming by endpoints:** mark a range palindromic when its endpoints match and its interior is palindromic; it also takes $O(N^2)$ time but uses $O(N^2)$ space.
- **Enumerate and verify every substring:** checks $O(N^2)$ ranges and may scan each range, costing $O(N^3)$ time.
- **Manacher's algorithm:** computes palindrome radii in $O(N)$ time, but is substantially more intricate when only the total count is needed.
- Every single character is a palindrome.
- Even-length palindromes require centers between characters.
- Repeated characters create multiple overlapping palindromic ranges.
- The same palindrome text at different positions counts more than once.

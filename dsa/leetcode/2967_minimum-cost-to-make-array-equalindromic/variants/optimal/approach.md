## General

For an unconstrained integer target, the sum of absolute deviations is
minimized by a median of the array. As the target moves away from the median
interval, the cost cannot decrease. Therefore, after requiring the target to be
palindromic, an optimum is the closest allowed palindrome on either side of
that interval.

Sort the values and take the upper median. Generate the palindromes immediately
around it by mirroring the leading half after small prefix changes. Also include
the all-nine lower digit boundary and the `100...001` upper boundary, because
the closest palindrome may change digit length. Keep only positive candidates
strictly below $10^9$, and evaluate the total absolute-difference cost for this
constant-size set.

Mirroring the unchanged or neighboring prefixes contains the predecessor and
successor palindromes of the median within its digit length; the explicit
boundaries contain the cross-length neighbors. Convexity of absolute-deviation
cost rules out every palindrome farther outside these neighbors, so the minimum
evaluated cost is globally optimal.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$. Sorting takes $O(N\log N)$ time. Generating
palindrome candidates depends only on at most nine decimal digits, and each
constant-number candidate costs $O(N)$ to evaluate, so total time remains
$O(N\log N)$. The sorted copy uses $O(N)$ space.

## Alternatives and edge cases

- **Selection sort before the median search:** It preserves the method's result but takes $O(N^2)$ time.
- **Enumerate every palindrome below $10^9$:** Precomputation is possible but unnecessary when only the median's neighbors can be optimal.
- **Median already palindromic:** Include it as a candidate; it may give zero cost when all values already match.
- **Even array length:** Every value in the median interval minimizes unconstrained cost, and checking palindromes around the chosen upper median still covers the best constrained target.
- **Digit boundary:** Values near `100...0` require considering the shorter all-nine palindrome and the longer `100...001` palindrome.
- **Upper limit:** `999999999` is the largest permitted palindromic target because the target must be strictly below $10^9$.

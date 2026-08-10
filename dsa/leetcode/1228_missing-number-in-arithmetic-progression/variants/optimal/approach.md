## General

**Recover the missing value from a sum identity**

The original array was an arithmetic progression with \(n+1\) values, where \(n\) is the length of the remaining `arr`. Exactly one interior value was removed. Because neither endpoint was removed, `arr[0]` and `arr[-1]` are still the first and last terms of the original progression.

An arithmetic progression has a useful sum formula:

\[
\text{sum}
=\frac{(\text{first term}+\text{last term})\cdot
\text{number of terms}}{2}.
\]

The original progression therefore had total

\[
T=\frac{(\texttt{arr[0]}+\texttt{arr[-1]})\cdot(n+1)}{2}.
\]

The current array contains every original term except the missing value \(x\), so

\[
\sum \texttt{arr}=T-x.
\]

Rearranging gives

\[
x=T-\sum \texttt{arr}.
\]

The exact solution is this formula written as one return expression.

**Why the arithmetic-progression sum formula works**

Pair the first original term with the last, the second with the second-to-last, and so on. Every pair has the same sum, first plus last, because moving one step forward adds the common difference while moving one step backward subtracts that same difference.

If the number of terms is even, there are half as many pairs. If it is odd, the middle term is exactly half of first plus last, so the same formula still applies. This proof works for increasing, decreasing, and constant progressions.

The method never needs to calculate the common difference or locate the gap. It uses the fact that the missing term is exactly the difference between the complete total and the observed total.

**Following the first example**

For `arr = [5, 7, 11, 13]`, the remaining length is four, so the original length was five. The complete progression’s sum must be

\[
\frac{(5+13)\cdot5}{2}=45.
\]

The observed sum is \(5+7+11+13=36\). Their difference is \(45-36=9\), which is the removed term.

For the decreasing example `[15, 13, 12]`, the original length was four. The complete sum is

\[
\frac{(15+12)\cdot4}{2}=54.
\]

The observed sum is 40, so the missing value is 14. Nothing in the formula assumes a positive common difference.

**Why integer division is exact**

The source computes

`(arr[0] + arr[-1]) * (len(arr) + 1) // 2`.

For every integer arithmetic progression, the product in the numerator is even. If the number of original terms is even, that factor supplies the two. If the number of terms is odd, the first and last terms have the same parity because their index distance is even, so their sum is even. Consequently, `// 2` performs exact division rather than rounding down a fractional result.

Python also evaluates multiplication before floor division, matching the mathematical numerator. Parentheses around the endpoint sum make the intended grouping explicit.

**Why endpoints being preserved is essential**

The formula uses the current first and last values as the original endpoints. If an endpoint could have been removed, those values would instead be interior terms, and many different original progressions could have the same remaining list. The statement’s guarantee is what makes the complete total uniquely recoverable.

**Constant progressions**

If the common difference is zero, every original value is equal. The first and last terms are the same value \(c\), and the formula gives \(c(n+1)\) as the original total. The observed array sums to \(cn\), so the difference is \(c\), correctly returning the missing repeated value.

The missing “value” need not be distinguishable by position in this case, but every possible removed interior position contains the same answer.


Let \(A\) be the complete arithmetic progression and \(x\) the one removed element. Since the original endpoints remain, the standard progression formula computed by the code equals \(\sum A\). The input array contains exactly the multiset \(A\) with one occurrence of \(x\) removed, so `sum(arr)` equals \(\sum A-x\). Subtracting it from the computed complete sum yields exactly \(x\). No search or case distinction is needed.

**What the concise source does and does not do**

The implementation reads the two endpoints and array length in constant time, but `sum(arr)` must still visit every element. The formula is algebraically direct, not logarithmic-time. It also leaves `arr` unchanged and creates no auxiliary collection.

Python integers have arbitrary precision, so the multiplication cannot overflow. In fixed-width languages, the product should be computed in a sufficiently wide integer type before division.

## Complexity detail

Let \(n=\lvert\texttt{arr}\rvert\). Computing `sum(arr)` scans all \(n\) values, so the exact implementation takes \(O(n)\) time. Endpoint access, length, arithmetic, and subtraction take \(O(1)\) additional operations.

The method uses only scalar intermediate integers, giving \(O(1)\) auxiliary space. The manifest’s \(O(\log n)\) time does not describe this exact source. A binary search based on the expected value at each index can achieve \(O(\log n)\), but the shipped sum formula is linear because it explicitly sums the array.

## Alternatives and edge cases

- **Binary search for the first shifted index:** Derive the common difference from the preserved endpoints, compare `arr[mid]` with its expected value, and find the first mismatch in \(O(\log n)\) time and \(O(1)\) space. This matches the manifest but is more complex.
- **Linear difference scan:** Derive the common difference and return the first expected value that does not match. It has the same \(O(n)\) time as the sum formula with more branching.
- **Increasing progression:** The complete-total formula works without locating the unusually large adjacent gap.
- **Decreasing progression:** Endpoint order and negative difference do not affect the sum identity.
- **Constant progression:** Every term is equal, and subtracting totals returns that repeated value.
- **Missing value repeated elsewhere:** In a constant progression, the numerical value is not unique to one position, but the requested number is still unambiguous.
- **Preserved endpoints:** The method depends critically on this guarantee. Allowing an endpoint deletion would invalidate the complete-sum calculation.
- **Exact integer arithmetic:** The numerator is always even for a valid integer progression, so floor division does not lose information.
- **Overflow in other languages:** Endpoint values and lengths should be promoted before multiplication. Python’s arbitrary-precision integers avoid this issue.
- **Input validity:** The code does not verify that the remaining values came from a valid progression with one interior deletion; it relies on the contract.

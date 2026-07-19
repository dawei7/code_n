## General
**Invert one adjacent XOR at a time**

XOR is its own inverse: if `encoded[i] = arr[i] XOR arr[i + 1]`, XORing both sides with `arr[i]` cancels that known value and gives `arr[i + 1] = arr[i] XOR encoded[i]`. Begin the decoded array with `first`, which supplies the recurrence's initial value.

**Extend the unique decoded prefix**

Scan `encoded` from left to right. At each step, the last decoded value is `arr[i]`, so append `decoded[-1] XOR encoded[i]`. By induction, every appended value is the only value that can satisfy the current adjacent equation. Once every encoded entry has been consumed, the result contains all $n$ original elements and recreates every supplied XOR.

## Complexity detail
The algorithm performs one constant-time XOR and one append for each of the $n-1$ encoded values, so it takes $O(n)$ time. The returned decoded array contains $n$ integers and therefore uses $O(n)$ space; beyond that required output, the algorithm uses $O(1)$ auxiliary state.

## Alternatives and edge cases
- **Recompute each prefix:** Deriving `arr[i]` by XORing `first` with `encoded[0:i]` independently is correct but repeats work and takes $O(n^2)$ time.
- **In-place reuse of `encoded`:** The input storage can be overwritten with decoded suffix values, but a separate returned array preserves the caller's input and makes the leading `first` explicit.
- **Zero encoded value:** An encoded zero means the two adjacent original values are equal.
- **Zero first value:** The recurrence is unchanged; XOR has no special failure case at zero.
- **Maximum values:** XOR may produce values beyond either individual operand's decimal pattern, but ordinary non-negative integer XOR remains exact.

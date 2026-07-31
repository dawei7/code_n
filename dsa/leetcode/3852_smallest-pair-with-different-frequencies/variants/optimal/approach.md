## General

**Count the bounded value domain**

The constraints restrict every array value to the integers from `1` through `100`. Build a frequency array indexed by those values. This records the count of every possible value in one pass through `nums` and also provides the values in numerical order without sorting.

**Fix the smallest possible first value**

Let `x` be the smallest value that occurs. If any valid pair exists, then some present values `a < b` have different frequencies. If `x` and `a` have different frequencies, `[x, a]` is valid; otherwise `x` has the same frequency as `a` and therefore a different frequency from `b`, making `[x, b]` valid. Thus every nonempty set of valid pairs includes one whose first element is the smallest present value. No larger first element can be lexicographically preferable.

After fixing this `x`, scan larger values in ascending order. Skip absent values and present values whose frequency equals the frequency of `x`. The first remaining value is exactly the smallest possible `y`, so return `[x, y]`. Reaching the end means every other present value has the same frequency as `x`; no valid pair exists, and the required result is `[-1, -1]`.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$ and let $V=100$ be the fixed size of the legal value domain. Counting takes $O(N)$ time, and the two bounded scans take $O(V)$ time. The total is $O(N+V)=O(N)$ because $V$ is a source constraint independent of $N$. The frequency array uses $O(V)=O(1)$ auxiliary space under the same bounded-domain contract.

The benchmark defines size as $N$ and uses arrays of distinct values. Equal frequencies force the complete value-domain scan and prevent early return. The accepted implementation performs one input pass plus bounded scans, whereas the correct slower control repeatedly rescans the entire array to count each distinct value and then examines all candidate pairs, requiring $O(N^2)$ time on these tiers.

## Alternatives and edge cases

- **Hash map plus sorting:** A counter keyed only by present values followed by sorting those keys takes $O(N+D\log D)$ time and $O(D)$ space for $D$ distinct values; it is more general but does not exploit the fixed value domain.
- **Repeated full-array counting:** Counting each distinct value with a separate scan and then checking candidate pairs is correct, but can require $O(N^2)$ time.
- **Single distinct value:** With no second distinct value, the scan finishes and returns `[-1, -1]`.
- **Uniform frequencies:** Any number of distinct values may all have the same frequency; none of their pairs is valid.
- **Skipped equal-frequency values:** A smaller candidate `y` with the same frequency as `x` must be ignored, but it does not prevent a later value with a different frequency from forming the answer.
- **Input order:** The pair is ordered by the values themselves, not by their first positions in `nums`.
- **Domain endpoints:** Values `1` and `100` are both ordinary legal indices in the frequency array.

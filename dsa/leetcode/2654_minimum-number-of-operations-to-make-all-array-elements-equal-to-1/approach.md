## General

**An existing one changes the problem completely**

For any positive integer $a$:

$$
\gcd(a,1)=1.
$$

Therefore, once a one exists, an operation on an adjacent pair containing that one can replace the neighboring value with one. The one can spread left and right through the array.

The solution first counts existing ones with `nums.count(1)`.

If there are $c>0$ ones, exactly $n-c$ positions are not one. Each operation can replace at most one array element, so at least $n-c$ operations are necessary. Spreading from existing ones converts every non-one in exactly one operation each, so $n-c$ is also sufficient.

The function returns this value immediately.

**Without a one, first create one**

If no element equals one, propagation cannot begin. An operation replaces one endpoint of an adjacent pair by their gcd.

Repeatedly combining values along a contiguous subarray can produce the gcd of that entire subarray at one of its positions.

Thus a one can be created exactly when some contiguous subarray has gcd one.

The shortest such subarray is best because combining a length-$L$ segment into one gcd value takes $L-1$ operations.

**Enumerate every starting position**

For each start index `i`, running gcd `g` begins at zero. Python's gcd satisfies:

$$
\gcd(0,a)=a,
$$

so the first update naturally sets `g` to `nums[i]`.

As end index `j` advances:

`g = gcd(g, nums[j])`

makes `g` the gcd of `nums[i..j]`.

Whenever `g == 1`, the code updates `mi` with subarray length `j - i + 1`.

It continues scanning even after reaching one. Since $\gcd(1,a)=1$, later extensions stay one but are longer and cannot improve this start. An early `break` could reduce constant work, but its absence does not affect correctness or the quadratic bound.

**Why only contiguous subarrays matter**

Each operation acts on adjacent indices. Before a one exists, the ancestry of a value produced at some position consists of values combined through a connected interval of the array.

A disconnected set cannot be merged without including the elements between its parts. Therefore, the first generated one must be the gcd of some contiguous segment.

Searching all intervals covers every possible source for the first one.

**Why length $L$ needs $L-1$ operations**

Take a segment:

$$
a_0,a_1,\ldots,a_{L-1}
$$

with total gcd one.

Combine adjacent values progressively, replacing one endpoint with their gcd. After one operation, a value can represent the gcd of two original elements; after another adjacent combination, it can represent three, and so on. In $L-1$ operations, one position can hold:

$$
\gcd(a_0,a_1,\ldots,a_{L-1})=1.
$$

Conversely, each binary adjacent operation can merge the influence of at most two connected components. Combining $L$ original values into one derived gcd requires at least $L-1$ merges. So the count is exact.

**After creation, spread to every other position**

Once the first one exists, the array still has $n-1$ other positions. Repeated adjacent gcd operations can turn each into one, one per operation.

Because the original array had no ones, none of those $n-1$ positions was already complete before creation in the counting argument. The minimal total for a shortest gcd-one segment of length $L$ is:

$$
(L-1)+(n-1).
$$

The return expression:

`n - 1 + mi - 1`

is exactly this formula.

**Trace `[2,6,3,4]`**

There is no initial one.

Subarray `[3,4]` has gcd one and length two, so `mi=2`. One operation on that pair creates a one.

Then three more operations convert the other $n-1=3$ positions. Total:

$$
(2-1)+(4-1)=4.
$$

This matches the example.

**Recognize impossibility**

If no subarray has gcd one, `mi` remains sentinel `n+1` and the function returns `-1`.

Equivalently, if the gcd of the whole array is greater than one, every subarray-derived value remains divisible by a common factor and one is impossible.

The exhaustive scan directly detects the absence without a separate whole-array gcd check.


If initial ones exist, the lower bound of one changed position per operation and the spreading construction both give $n-c$.

Otherwise, any valid process has a first operation after which some position becomes one. Its contributing original values form a contiguous gcd-one segment of length at least `mi`, requiring at least `mi - 1` operations. Converting the remaining $n-1$ positions needs at least $n-1$ more changes.

The shortest segment construction achieves both lower bounds, so the returned sum is optimal. If no such segment exists, no first one can be created.

## Complexity detail

There are $O(n^2)$ start-end pairs. Each performs one gcd operation. Under the usual convention that bounded-integer gcd is treated as small or $O(\log V)$, time is $O(n^2)$ or more precisely $O(n^2\log V)$ bit-operation style.

The algorithm stores only counters, indices, the running gcd, and shortest length. Auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Break once running gcd reaches one:** Safe because extensions stay one and are longer; improves constants.
- **Whole-array gcd precheck:** If greater than one, return `-1` immediately, but interval search already detects impossibility.
- **Dynamic distinct gcd sets:** Can reduce work for larger $n$ by tracking compressed gcd states per endpoint.
- **All elements already one:** Count branch returns zero.
- **Some existing ones:** Each non-one needs exactly one spreading operation.
- **Adjacent pair gcd one:** First one costs one operation, the smallest possible without an existing one.
- **No gcd-one subarray:** Return `-1`.
- **Shortest segment:** It minimizes only the creation phase; propagation always costs $n-1$ afterward.
- **Positive integers:** Gcd never involves zero-valued input, though zero initialization is a convenient identity.
- **Input preservation:** The algorithm analyzes possible operations but never mutates `nums`.

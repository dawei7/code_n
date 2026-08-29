## General

**Build the derived array exactly as defined**

The pairing does not use the original `nums` values directly. First, each index `i` produces a derived value

$$
P_i=\gcd(\texttt{nums}[i],M_i),
$$

where

$$
M_i=\max(\texttt{nums}[0],\ldots,\texttt{nums}[i])
$$

is the inclusive prefix maximum.

Computing `M_i` by rescanning `nums[0:i+1]` for every index would repeat work and take quadratic time. Prefix maxima have a simple rolling recurrence:

$$
M_i=\max(M_{i-1},\texttt{nums}[i]).
$$

The source stores the current value in `mx`. It starts at zero, which is below every positive input. At each `x`, it executes `mx = max(mx,x)` and then stores `gcd(x,mx)` in `prefix_gcd[i]`.

The update must occur before the GCD because the prefix maximum is inclusive: it includes the current element. When `x` establishes a new maximum, `mx=x` and the derived value is `gcd(x,x)=x`.

**Why one scalar maximum is enough**

Future indices need only the greatest value seen so far, not which position supplied it or the complete prefix. Once `mx` is updated, smaller previous values can never become a later prefix maximum. This compresses the editorial's conceptual prefix-maximum array into one scalar while still producing the full derived array required for sorting.

For `nums=[2,6,4]`:

- index zero has `mx=2` and derived value `gcd(2,2)=2`;
- index one updates `mx=6` and produces six; and
- index two keeps `mx=6` and produces `gcd(4,6)=2`.

Thus `prefix_gcd=[2,6,2]`.

**Sort because pairing is based on rank**

The problem next requires the smallest unpaired derived value to pair with the largest unpaired value, then the second-smallest with the second-largest, and so on. These are rank-based positions, so the source sorts `prefix_gcd` in non-descending order.

After sorting an array `a` of length `N`, pair number `i` is

$$
(a[i],a[N-1-i]).
$$

Python's negative index `-i-1` is another spelling of `N-1-i`, so the generator computes

`gcd(prefix_gcd[i], prefix_gcd[-i - 1])`.

The range `range(n // 2)` produces exactly `\lfloor N/2\rfloor` pair indices. For each such `i`, the left index is strictly less than the right index, so no element is reused. When `N` is odd, the middle index `N//2` is not included and is correctly ignored.

Summing these GCD values gives the required answer. There is no optimization over alternative pairings: sorting and opposite-end pairing are mandated by the contract, and the source simulates them directly.

**State progression**

During the first loop, after index `i`:

- `mx=M_i`, the maximum of exactly the processed prefix; and
- `prefix_gcd[j]=P_j` for every `j\le i`.

The maximum recurrence and immediate GCD assignment preserve this invariant. After the loop, the list contains exactly every defined `P_i`.

Sorting changes order but not the multiset. The problem explicitly asks for sorted order before pairing, so this transformation is required. The symmetric indices then enumerate the specified pairs from the outside inward. Every formed pair contributes its GCD once, and the generator sum contains no other terms.

**Trace the even example**

For `nums=[3,6,2,8]`, the running maxima are `3,6,6,8`. The derived values are

$$
3,\;6,\;2,\;8.
$$

Sorting yields `[2,3,6,8]`. With `N//2=2`:

- `i=0` pairs two with eight and contributes `gcd(2,8)=2`;
- `i=1` pairs three with six and contributes `gcd(3,6)=3`.

The sum is five.

For the odd example `[2,6,4]`, sorting the derived array yields `[2,2,6]`. Only `i=0` is generated, pairing two and six for contribution two. The middle two is ignored.

**Relationship to the local editorial**

The editorial builds a separate prefix-maximum array and then zips it with `nums` to build `prefixGcd`. The protected source performs both steps in one loop, retaining only the current maximum. This saves one length-`N` array without changing the algorithm or its result.

The source relies on `gcd`, normally imported from `math`.

## Complexity detail

Let `V=max(nums)`. Constructing the derived list performs `N` GCD computations. Euclid's algorithm takes `O(\log V)` time per call, giving `O(N\log V)`.

Sorting `N` integers takes `O(N\log N)` time. The pairing stage performs `\lfloor N/2\rfloor` additional GCD computations, another `O(N\log V)`. Total time is

$$
O(N\log N+N\log V),
$$

matching the manifest and editorial.

The `prefix_gcd` list uses `O(N)` space. Python's in-place list sort may use `O(N)` temporary memory in the worst case, while the generator used by `sum` is lazy and constant-sized. Overall auxiliary space remains `O(N)`, matching the manifest. The source avoids the editorial's second `O(N)` prefix-maximum array, but both have the same asymptotic bound.

The returned sum can contain up to `N/2` terms of size at most `V`. Python integers are safe; fixed-width languages should use a sufficiently wide accumulator.

## Alternatives and edge cases

- **Recompute every prefix maximum:** Calling `max(nums[:i+1])` per index takes `O(N^2)` total time. A rolling maximum updates in constant time.
- **Store the full prefix-maximum array:** This follows the editorial literally and remains `O(N)` space, but one scalar `mx` is enough while building the derived list.
- **Pair original values:** Incorrect. Sorting and pairing apply to `gcd(nums[i],M_i)` values, which may differ substantially from `nums[i]`.
- **Pair before sorting:** The required pairs depend on value rank, not original position. Sorting is semantically necessary.
- **Repeatedly pop the first and last list elements:** It simulates the wording, but popping index zero from a Python list shifts elements and can make pairing `O(N^2)`. Symmetric indexing avoids mutation.
- **Two explicit pointers:** Initialize left zero and right `N-1`, add their GCD, and move inward. This is equivalent to the generator and may be easier to port to languages without negative indexing.
- **New prefix maximum:** When `nums[i]` exceeds all earlier values, the derived value is the number itself because `gcd(x,x)=x`.
- **Value below the prefix maximum:** Its derived value is a divisor shared with that maximum and may be much smaller than either value.
- **Odd length:** Exactly the sorted middle element remains unpaired. `range(N//2)` omits it automatically.
- **Singleton array:** `N//2=0`, so `sum` receives an empty generator and returns zero, matching the no-pair rule.
- **Two elements:** One symmetric pair is formed after deriving and sorting both values.
- **Duplicate derived values:** Sorting keeps all copies, and each position participates according to multiplicity. Stability of the sort is irrelevant because equal values are indistinguishable for GCD.
- **Positive-input initialization:** `mx=0` is safe because every value is at least one. With a generalized domain containing negatives, initialization and maximum semantics would need adjustment.
- **GCD import:** The protected source requires `math.gcd` or an equivalent available name.

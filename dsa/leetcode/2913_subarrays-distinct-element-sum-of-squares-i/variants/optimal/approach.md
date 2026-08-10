## General

Every subarray is determined by a left endpoint $i$ and a right endpoint $j$ with $i\le j$. For that subarray, let $\operatorname{distinct}(i,j)$ be the number of different values it contains. The required answer is

$$
\sum_{0\le i\le j<n}\operatorname{distinct}(i,j)^2.
$$

The constraints of this first version allow us to enumerate all $O(n^2)$ subarrays. The important improvement over rebuilding each subarray from scratch is to reuse its set of distinct values while the right endpoint moves.

For each fixed left endpoint $i$, the solution creates an empty set `s`. It then extends $j$ from $i$ to $n-1$:

1. Add `nums[j]` to `s`.
2. The set now contains exactly the distinct values in `nums[i:j+1]`.
3. Add `len(s) * len(s)` to the answer.

After every right endpoint has been processed, the next outer-loop iteration chooses a new $i$ and creates a fresh set. This reset is necessary because the next family of subarrays starts at a different position.

**Why the set is the exact state we need**

A mathematical set keeps one copy of each value, regardless of how many times that value occurs. Python's `set.add` has the same behavior:

- adding a value that is not present increases `len(s)` by one;
- adding a duplicate leaves `len(s)` unchanged.

This precisely matches the definition of a distinct-element count.

The invariant of the inner loop is:

> Immediately after adding `nums[j]`, `s` equals the set of values occurring from index $i$ through index $j$, inclusive.

It is true at $j=i$ because the formerly empty set receives exactly `nums[i]`. If it is true for $j-1$, adding `nums[j]` extends the represented range by exactly the next element. Whether that element is new or duplicated, the resulting set is exactly the distinct values of the extended subarray. This proves the invariant by induction.

Once the invariant holds, `len(s)` is $\operatorname{distinct}(i,j)$, so squaring it produces the required contribution of this specific subarray.

**Why every subarray contributes exactly once**

The outer loop visits every possible left endpoint $i$. For that fixed $i$, the inner loop visits every possible right endpoint $j\ge i$. Therefore every legal endpoint pair $(i,j)$ is reached.

No pair is repeated: two different loop iterations must differ in $i$, in $j$, or in both. Since a contiguous subarray is uniquely identified by its endpoint pair, its squared distinct count is added exactly once. Summing those contributions gives the requested total.

For example, with `nums = [1, 2, 1]` and $i=0$, the set sizes as $j$ advances are $1,2,2$. The contributions are $1,4,4$. The final $1$ is a duplicate, so it does not raise the distinct count. When $i=1$, a new set is used for subarrays `[2]` and `[2,1]`, producing sizes $1,2$. Finally, $i=2$ contributes the one-element subarray `[1]`. This accounts for all six subarrays.

**Why no frequency map is required**

For a fixed $i$, the right endpoint only moves forward. Values are added but never removed from the current subarray. We only need to know whether a value has appeared, not how many times it appears, so a set is sufficient.

A frequency map would become useful in a sliding window where both endpoints move and elements leave the window. That is not the access pattern here. Avoiding unnecessary counts keeps the implementation close to the mathematical quantity.

**Why this is considered optimal for this version**

There are $n(n+1)/2$ subarrays, and this implementation explicitly evaluates the requested contribution of each one in expected constant incremental time. That $O(n^2)$ strategy fits the smaller constraints of the “I” problem. A more advanced version can aggregate how the distinct count changes over many subarrays at once, but such machinery is unnecessary here and would make the reasoning and implementation substantially more complex.

## Complexity detail

Let $n$ be the number of elements in `nums`.

The outer loop runs $n$ times. For a chosen $i$, the inner loop runs $n-i$ times. Hence the total number of iterations is

$$
\sum_{i=0}^{n-1}(n-i)
=
n+(n-1)+\cdots+1
=
\frac{n(n+1)}{2}
=O(n^2).
$$

Each iteration performs one expected-$O(1)$ hash-set insertion, obtains the set length in $O(1)$, squares it, and adds it to `ans`. The total expected time is therefore $O(n^2)$. The expected qualification comes from the usual average behavior of Python hash tables.

For one fixed left endpoint, `s` can contain at most $n$ distinct values, so its peak auxiliary space is $O(n)$. Sets from earlier outer iterations are discarded before the next is created; their sizes do not add together. The scalar answer and loop indices take $O(1)$ extra space.

## Alternatives and edge cases

- **Build every subarray separately:** Slicing each `nums[i:j+1]` and converting it to a set takes up to $O(n)$ work per subarray, leading to $O(n^3)$ total time and repeated allocation.
- **Use a frequency dictionary:** This also produces the distinct count but stores counts that never need to be decremented. A set is the smaller and clearer state for a one-directional extension.
- **Advanced contribution aggregation:** The larger version of this problem can update the sum of squared distinct counts for many left endpoints together, often using range data structures. That complexity is unnecessary for the constraints and exact source used here.
- **All elements equal:** Every subarray has exactly one distinct value and contributes $1$. Repeated `set.add` calls correctly leave the size at one.
- **All elements distinct:** A subarray of length $\ell$ has $\ell$ distinct values and contributes $\ell^2$. The set grows by one at every extension.
- **One-element subarrays:** Each outer iteration starts with $j=i$, adds one value, and contributes $1^2$. These subarrays are included naturally.
- **Set reset between left endpoints:** Reusing the old set would retain values lying before the new $i$ and corrupt the invariant. Creating `s = set()` inside the outer loop is essential.
- **No modulo reduction:** This first-version contract asks for the exact sum, and the source solution returns the full Python integer. Adding an unrequested modulo would change correct outputs.
- **Duplicate occurrences:** A duplicate must not increase the distinct count, but it still defines a different endpoint and therefore a different subarray contribution. The algorithm handles both facts simultaneously.
- **Input order matters for subarrays:** A global set of all array values is insufficient because distinct counts depend on the selected contiguous range. The per-left incremental set preserves those boundaries.

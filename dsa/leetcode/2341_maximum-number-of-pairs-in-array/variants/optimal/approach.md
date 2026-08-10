## General

**Pairs can be counted independently for each value**

A pair must contain two equal integers. An occurrence of value `x` can never pair with an occurrence of another value, so choices for different values do not interact.

If `x` appears `f` times, exactly `floor(f / 2)` pairs can be formed from it. Each pair consumes two copies, leaving `f mod 2` copies—either zero or one.

The order in which pairs are removed does not matter. Every operation within one value group reduces its frequency by two, and the maximum number of such reductions is determined solely by quotient and remainder.

**Build all frequencies once**

`Counter(nums)` creates a mapping from each distinct integer to its number of occurrences. The code calls this mapping `cnt`.

For the example `[1,3,2,1,3,2,2]`, the frequencies are:

- value 1 occurs twice;
- value 3 occurs twice;
- value 2 occurs three times.

These groups produce one, one, and one pair, with one copy of 2 left.

**Sum the pair quotient from every group**

The generator `v // 2 for v in cnt.values()` computes the number of pairs contributed by every frequency `v`. Their sum is stored in `s`.

This is maximal because each reported pair has two available equal copies. It is also an upper bound: no value group with frequency `v` can supply more than `v // 2` disjoint pairs. Adding the exact maxima of independent groups gives the global maximum.

**Derive leftovers from how many elements were consumed**

Every one of the `s` pairs removes exactly two integers. Starting from `len(nums)` elements, the number left is

`len(nums) - 2 * s`.

The returned result `[s, len(nums) - s * 2]` therefore contains the requested pair count followed by the leftover count.

This is equivalent to summing `v % 2` over all frequencies. The subtraction form avoids a second traversal of the Counter values and directly connects leftovers to the completed operations.

**Why arbitrary pairing order cannot improve the result**

Fix a value with frequency `f`. Any legal result using that value consists of disjoint two-occurrence groups, so `2p <= f` and `p <= floor(f/2)`. Grouping any two copies repeatedly achieves exactly that upper bound.

Since copies of different values cannot share a pair, maximizing each value group separately does not compete for resources. Therefore `s` is both achievable and no smaller than any other legal pair total.

Once no group has two copies remaining, every residual frequency is zero or one and no further operation is possible. The returned leftover count describes exactly that terminal state.

**The bounded value domain makes storage constant in problem terms**

Values range only from zero through 100, so the Counter has at most 101 keys regardless of input length. Although it is a dynamic hash map, its maximum size is fixed by the problem's value universe.

A fixed 101-entry frequency array could express this bound more visibly. The Counter keeps the implementation concise and stores only values that actually occur.

## Complexity detail

Let `n` be the input length and `u` the number of distinct values. Building the Counter takes `O(n)` expected time, and summing its values takes `O(u)`, with `u <= 101`. Total time is `O(n)`.

The Counter uses `O(u)` space. Under the fixed value range, `u <= 101` is constant, so the manifest reports `O(1)` auxiliary space. In a generalized problem with unbounded values, the same implementation would use `O(u)` or `O(n)` space in the worst case.

The input is read without removing elements. The returned two-element list is constant-size output.

## Alternatives and edge cases

- **Fixed 101-entry frequency array:** Increment by value, then sum quotients and remainders. It has the same time and makes constant bounded storage explicit.
- **Toggle membership in a set:** Add the first unpaired occurrence; when the same value appears again, remove it and increment the pair count. The final set size is leftovers and storage remains bounded.
- **Sort the array:** Equal values become consecutive and can be paired in a scan, but sorting costs `O(n \log n)` and may mutate the input.
- **Physically remove pairs:** Repeated list deletion is unnecessary and can become quadratic.
- **One element:** Its frequency quotient is zero and one element remains.
- **Exactly two equal elements:** One pair forms and no element remains.
- **Odd frequency:** One copy remains after forming `floor(f/2)` pairs.
- **Even frequency:** The entire group is consumed.
- **All values distinct:** Every quotient is zero, so all `n` elements remain.
- **All values equal:** The answer is `[n // 2, n % 2]`.
- **Value zero:** It is an ordinary value and pairs with another zero.
- **Pair order:** Any two copies of a value are interchangeable, so indices do not affect the count.
- **Counter hash behavior:** Complexity uses expected constant-time dictionary updates; the tiny integer key domain is especially well behaved.
- **Input preservation:** Frequencies are counted in separate storage and `nums` is unchanged.

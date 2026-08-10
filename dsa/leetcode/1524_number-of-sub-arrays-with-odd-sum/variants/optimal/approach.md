## General

**Turn subarray sums into differences of prefixes**

Let a prefix sum be the total of all elements before a boundary. The sum of a subarray is the later prefix sum minus an earlier prefix sum.

Only parity matters. A difference is odd exactly when its two prefix sums have opposite parity:

- Even minus odd is odd.
- Odd minus even is odd.
- Equal parities produce an even difference.

The stored solution counts how many earlier prefix sums have each parity and uses the current prefix as the right boundary.

**Meaning of cnt**

`cnt[0]` is the number of even prefix sums seen so far, and `cnt[1]` is the number of odd prefix sums.

It starts as `[1, 0]`. The one even prefix is the empty prefix before the array, whose sum is zero. Including it allows a subarray starting at index zero to be counted: its sum equals the current prefix minus zero.

`s` is the running prefix sum. After adding current element `x`, `s & 1` is zero for an even prefix and one for an odd prefix.

**Reading the compact opposite-parity expression**

The source adds

`cnt[s & 1 ^ 1]`

to the answer. Bitwise AND binds before XOR in Python, so the index is `(s & 1) ^ 1`. XOR with one flips a single parity bit:

- Current parity zero becomes index one.
- Current parity one becomes index zero.

Thus the code adds exactly the number of earlier prefixes with opposite parity. Each such earlier boundary defines one odd-sum subarray ending at the current element.

After counting those subarrays, `cnt[s & 1] += 1` records the current prefix for future endpoints. The current prefix must be added after querying so it is not paired with itself to create an empty subarray.

**A trace on three odd values**

Start with one even empty prefix and no odd prefixes.

After the first one, current parity is odd. It pairs with the one earlier even prefix, adding one. Odd-prefix count becomes one.

After adding the second odd value, the total prefix is even. It pairs with the one earlier odd prefix, adding one. Even-prefix count becomes two.

After the third, current prefix is odd. It pairs with both earlier even prefixes, adding two. The total is four, matching the example.

**Why every valid subarray is counted exactly once**

Every nonempty subarray has a unique right endpoint and a unique prefix boundary immediately before its left endpoint. When the loop reaches that right endpoint, the earlier prefix has already been recorded.

If the subarray sum is odd, those prefix parities differ, so the earlier boundary is included in the added count. If they have the same parity, the subarray is even and is not counted.

The pair is never reconsidered at another iteration because its right endpoint is fixed. This proves completeness without duplication.

**Why actual sums are unnecessary**

The exact source maintains full `s`, but it could maintain only its parity by XORing or reducing modulo two. Adding an even value preserves parity, while adding an odd value flips it.

Keeping the full sum is still correct under the constraints and makes the prefix-sum interpretation direct. Python integers cannot overflow.

**Modulo handling**

`ans` is reduced modulo $10^9+7$ after every contribution. Counts in `cnt` are not reduced because they represent actual prefix multiplicities used for later additions. They are at most $n+1$, so they remain small.

Modular addition guarantees that repeated reduction produces the same final requested remainder.

## Complexity detail

Let $N$ be the array length. The loop visits each element once and performs constant arithmetic and two fixed-array accesses, so time is $O(N)$.

The two-entry count list and scalar variables use $O(1)$ auxiliary space, matching the manifest. No prefix-sum array or subarray objects are created.

The answer can be $O(N^2)$ before modular reduction, but online modulo keeps it bounded. Counter values remain $O(N)$ numerically without affecting the number of stored variables.

## Alternatives and edge cases

- **Track odd-ending and even-ending subarrays:** Update two counts based on each element's parity. It is equivalent dynamic programming with constant space.
- **Store every prefix parity:** A list is unnecessary because only the number of prior even and odd prefixes matters.
- **Enumerate all subarrays:** Running sums reduce checking cost but still require $O(N^2)$ pairs.
- **All even elements:** Every prefix stays even, so no opposite-parity prefix exists and the answer is zero.
- **All odd elements:** Prefix parity alternates, and the two counters count all cross-parity boundary pairs.
- **Subarray starting at zero:** The initial empty even prefix is essential for counting it.
- **Single odd element:** It pairs with the empty prefix and returns one.
- **Single even element:** It finds no earlier odd prefix and returns zero.
- **Update order:** Recording the current prefix before querying would include an empty subarray when looking for same state; the exact query-first order is correct.
- **Operator precedence:** The expression means `(s & 1) ^ 1`; explicit parentheses would improve readability without changing behavior.

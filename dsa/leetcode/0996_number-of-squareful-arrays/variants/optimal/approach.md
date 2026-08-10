## General

**View a valid permutation as a path through compatible indices**

Two values can be adjacent only when their sum is a perfect square. Imagine one vertex for every array index, with a connection between two distinct indices when their values satisfy that condition. A squareful permutation is then an ordering that visits every index once and uses only compatible connections between consecutive positions.

The array has at most twelve elements, so a bitmask can represent exactly which indices have already been placed. This supports a dynamic program over subsets instead of enumerating all `N!` index orders blindly.

**Define the subset state precisely**

The table has shape `(1 << n)` by `n`:

`f[mask][j]` means the number of squareful sequences that use exactly the indices whose bits are set in `mask` and end with index `j`.

Index identity matters during this DP, even when two indices store equal values. The duplicate-value correction happens only after all full index sequences are counted.

A state ending at `j` is meaningful only when bit `j` belongs to `mask`. This is why the transition loop first checks `i >> j & 1`.

**Initialize every one-element sequence**

For each index `j`:

`f[1 << j][j] = 1`.

A sequence containing only `nums[j]` has no adjacent pair, so it satisfies the squareful condition vacuously. There is exactly one index sequence using that singleton and ending there.

These base states allow larger subsets to be formed by appending one final index.

**Remove the final index to obtain the predecessor state**

Suppose a sequence uses mask `i` and ends at index `j`. If it has more than one element, let `k` be the index immediately before `j`.

Then:

- `k` must also be present in `i`;
- `k != j`;
- `nums[k] + nums[j]` must be a perfect square;
- everything before `j` is a valid sequence using mask `i` without bit `j` and ending at `k`.

The predecessor mask is

`i ^ (1 << j)`.

Because bit `j` is known to be set, XOR clears it. For every compatible predecessor `k`, the code adds

`f[i ^ (1 << j)][k]`

to `f[i][j]`.

Every predecessor sequence becomes one longer sequence by appending index `j`, and different predecessor endings or sequences produce different index orders.

**Check perfect squares safely**

For a candidate pair, the code computes `s = nums[j] + nums[k]` and `t = int(sqrt(s))`. It accepts the edge only when `t * t == s`.

Taking an integer conversion alone is not enough, because it floors square roots of nonsquares. Multiplying the candidate root by itself verifies exact equality. The largest sum is at most two billion, comfortably within the precision needed for this check, and Python integers represent `t * t` exactly.

Zero is correctly recognized as a perfect square because its square root and squared candidate are both zero.

**Why masks are processed in a valid dependency order**

The outer loop visits masks from zero upward. Clearing a set bit `j` changes `i` to `i - 2^j`, which is numerically smaller. Therefore, every predecessor table entry has already been computed when the current transition reads it.

No separate sorting by subset size is necessary, although that would be another valid organization.

**Collect all possible final indices**

The full mask is `(1 << n) - 1`, with all `n` bits set. A complete squareful index permutation may end at any index, so

`sum(f[full_mask][j] for j in range(n))`

adds all disjoint ending cases.

At this point, the total treats equal-valued elements at different indices as distinguishable. That is appropriate for constructing the DP but not yet for the problem's definition of different permutations.

**Remove overcounting caused by duplicate values**

The problem distinguishes permutations by their value at each position. Swapping two equal-valued occurrences does not create a new value sequence.

Suppose a value appears `c` times. For any fixed value permutation, its `c` original indices can be assigned to the positions containing that value in `c!` ways, and all those index assignments have identical adjacency sums. For several repeated values, these independent assignments multiply.

Thus every distinct value permutation is counted exactly

`\prod_v count(v)!`

times by the index DP. The loop over `Counter(nums).values()` divides `ans` by `factorial(v)` for every multiplicity, leaving the number of distinct value permutations.

The divisions are exact; they are not approximations or heuristic duplicate removal.

**Trace `[1, 17, 8]`**

Compatibility is:

- `1 + 8 = 9`, a square;
- `8 + 17 = 25`, a square;
- `1 + 17 = 18`, not a square.

The only ways to visit all three indices while following compatible edges are `1, 8, 17` and `17, 8, 1`. The full-mask states sum to two. All values are distinct, so every factorial divisor is one and the returned answer remains two.

For `[2, 2, 2]`, every adjacent sum is four, so the index DP counts all `3! = 6` index orders. The value two has multiplicity three, and dividing by `3!` produces one distinct value permutation.

**Why the recurrence counts exactly all squareful index sequences**

For singleton masks, the initialized value is correct. Assume all smaller-subset states are correct. Every sequence counted into `f[i][j]` comes from a valid predecessor ending at `k` and passes the square test for the new adjacent pair, so the appended sequence is squareful.

Conversely, take any squareful sequence represented by state `(i, j)`. Removing its final index `j` leaves a squareful predecessor sequence ending at some `k` in the smaller mask. Its final pair passes the compatibility test, so the recurrence includes it. The final predecessor `k` is unique for that sequence, preventing double counting within the state.

Induction proves the full-mask sum counts every squareful index order exactly once. Factorial division then converts that exact index count into the required distinct value-permutation count.

## Complexity detail

Let `N` be the array length. There are `2^N` masks and `N` possible final indices. For each valid `(mask, j)` state, the code scans up to `N` predecessor indices. Time complexity is `O(2^N N^2)`.

The DP table stores `2^N \cdot N` integers, so auxiliary space is `O(2^N N)`. The counter and loop variables are smaller. These are the precise bounds of the protected subset-DP implementation.

The constraints cap `N` at twelve, making at most 4096 masks practical.

## Alternatives and edge cases

- **Backtracking over a frequency counter:** Choose a compatible remaining value recursively and decrement its count. It naturally avoids duplicate permutations but may explore up to factorially many prefixes.
- **Backtracking over sorted indices with duplicate skipping:** Skip equal unused values at the same recursion depth. This is simpler to visualize but lacks the subset DP's reuse of equivalent states.
- **Precompute compatibility:** Build an `N \times N` Boolean matrix of square-sum pairs once. It avoids repeated square-root checks inside transitions at the cost of `O(N^2)` extra space.
- **Memoized recursion:** Use `(mask, last_index)` as a cache key. It expresses the same DP top down and visits only reachable states.
- **Single element:** Its singleton state contributes one, and factorial correction leaves one.
- **All equal values:** If twice the value is square, the answer is one; otherwise, arrays longer than one have no valid adjacency and the answer is zero.
- **Zero values:** Zero plus zero is a square, and zero plus another value is compatible exactly when that value itself is a square.
- **No compatible full path:** Full-mask states remain zero, and duplicate division preserves zero.
- **Duplicate indices in one sequence:** Bitmasks prevent an index from appearing twice because each transition adds a previously excluded final index.
- **Floating square root:** The explicit `t * t == s` test rejects nonsquares after conversion.

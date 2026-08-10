## General

The required final order is not ordinary numerical order. Every number has a two-part sorting key:

1. its decimal digit sum, and
2. the number itself, used when two digit sums are equal.

The solution first determines the unique destination of every value. It then views the current arrangement as a permutation of those destinations. The minimum number of arbitrary swaps is obtained by decomposing that permutation into cycles.

**Constructing the exact target order**

The helper `f(x)` computes a value’s digit sum by repeatedly adding `x % 10` and removing the last digit with `x //= 10`. For example, `f(43) = 4 + 3 = 7`.

The expression

`arr = sorted((f(x), x) for x in nums)`

creates one tuple `(digit_sum, value)` per input number and sorts the tuples lexicographically. Python compares the first tuple component first, so smaller digit sums come first. If those are equal, it compares the second component, so the smaller number comes first. That is exactly the order required by the statement.

The input values are distinct. Therefore every tuple has a distinct second component, and every value has exactly one final position. The dictionary

`d = {a[1]: i for i, a in enumerate(arr)}`

records that position: `d[value]` is the index where `value` belongs in the completely sorted array. If duplicate values were allowed, a single dictionary entry per value would not distinguish their occurrences, but the distinctness guarantee makes this representation exact.

**Turning the rearrangement into a permutation**

At an original index `j`, the current value is `nums[j]`. Its target index is `d[nums[j]]`. Thus the rule

`j -> d[nums[j]]`

maps every current index to one target index. Every current value is distinct, every target position belongs to one value, and no target is repeated. Consequently this mapping is a permutation of the indices `0` through `n - 1`.

Every permutation splits into disjoint cycles. A cycle of length one means that its value is already in the correct place. A longer cycle describes values rotating among several positions. For instance, if index `0` should go to `2`, index `2` should go to `1`, and index `1` should go to `0`, those three indices form one cycle of length three.

The code finds these cycles with `vis`. Whenever the outer loop reaches an unvisited index `i`, that index starts a previously undiscovered cycle. The inner loop marks the current index `j` and advances to `d[nums[j]]`. Because this is a permutation, following destinations can neither leave the valid index range nor merge into a different unfinished path. Eventually it returns to an already visited position, completing that cycle.

**Why a cycle of length c needs exactly c - 1 swaps**

For the upper bound, pick one position in the cycle as an anchor. Swap the correct value into that anchor, then repeat with one of the remaining incorrect positions. Every swap permanently fixes one position, and after `c - 1` swaps the final remaining value must also be correct. So `c - 1` swaps are sufficient.

For the lower bound, initially the `c` positions belong to one nontrivial cyclic dependency. One arbitrary swap can increase the number of correctly separated permutation cycles by at most one. To turn a single cycle into `c` length-one cycles therefore requires at least `c - 1` swaps. Equivalently, one swap can place at most one new cycle component into its final independent state. Thus fewer than `c - 1` swaps cannot resolve the whole cycle.

The lower and upper bounds match, proving that the minimum for a length-`c` cycle is exactly `c - 1`. Since disjoint cycles contain disjoint sets of positions, their costs add.

**Why the unusual counter produces the same formula**

The standard total is

$$
\sum_{\text{cycles}} (c - 1)
= \left(\sum_{\text{cycles}} c\right) - \text{number of cycles}
= n - \text{number of cycles}.
$$

The implementation initializes `ans = n`. It subtracts one each time the outer loop discovers a new cycle. After all indices are visited, `ans` is therefore `n - number_of_cycles`, exactly the minimum-swap formula. A length-one cycle still causes one subtraction, contributing `1 - 1 = 0` swaps as it should.

**Tracing the example with equal digit sums**

For `nums = [18, 43, 34, 16]`, the sorting keys are:

- `18 -> (9, 18)`
- `43 -> (7, 43)`
- `34 -> (7, 34)`
- `16 -> (7, 16)`

Sorting the tuples produces values `[16, 34, 43, 18]`. Their destination map is `16 -> 0`, `34 -> 1`, `43 -> 2`, and `18 -> 3`.

Following destinations from index `0` gives `0 -> 3 -> 0`, a two-cycle. Starting at the next unvisited index `1` gives `1 -> 2 -> 1`, another two-cycle. Each contributes one swap, so the answer is `2`. Notice that the tie among digit sums of seven is resolved numerically as `16, 34, 43`; ignoring that tie-breaker would construct the wrong target permutation.

## Complexity detail

Let `n` be the number of values and let `V` be the largest value. Computing a digit sum takes `O(\log V)` time, so producing all sorting keys takes `O(n \log V)` time. Sorting `n` tuples takes `O(n \log n)` time. Building the dictionary is `O(n)` expected time, and cycle traversal is `O(n)` because each index becomes visited once.

The total time is therefore

$$
O(n \log n + n \log V).
$$

Under the stated bound `nums[i] \le 10^9`, each value has at most ten decimal digits, so digit extraction is bounded by a constant. The conventional complexity then simplifies to `O(n \log n)`, matching the manifest.

The tuple list `arr`, destination dictionary `d`, and visited array `vis` each hold `O(n)` information. Python’s sorting machinery may also use linear temporary storage. The auxiliary space complexity is therefore `O(n)`.

## Alternatives and edge cases

- **Sort indexed records:** One can sort records containing each value’s original index, then construct an explicit index-to-index permutation. This avoids mapping by value and naturally supports duplicates if occurrence identities are preserved, but the current dictionary is simpler because the problem guarantees distinct values.
- **Swap values in a working array:** Another method repeatedly swaps each incorrect value into its target position while updating a position map. It also achieves `O(n \log n)` overall and directly counts swaps, but it mutates an auxiliary copy and has more state to keep synchronized.
- **Selection-style greedy swapping:** Repeatedly searching the remaining suffix for the next required value can count correct swaps, but without a position map it takes `O(n^2)` time and is too slow for `n = 10^5`.
- **Already sorted input:** Every index is a length-one cycle. The algorithm discovers `n` cycles, changes `ans` from `n` to zero, and correctly reports no swaps.
- **One input value:** The only permutation contains one length-one cycle, so the answer is zero.
- **Equal digit sums:** Numerical value must be the second sorting key. Python tuple ordering supplies this tie-breaker automatically.
- **Distinctness is essential to this implementation:** The dictionary `d` stores one target index for each value. Duplicate values would overwrite entries and require occurrence-aware matching, but duplicates are explicitly excluded.
- **Large positive values:** The arithmetic digit-sum loop works for the full allowed range, including powers of ten and values containing internal zeros.
- **No input mutation:** The method builds keys, a destination map, and visitation state but never rearranges `nums` itself.
- **Why arbitrary swaps matter:** The cycle formula assumes any two distinct positions may be exchanged. If only adjacent swaps were permitted, the answer would instead depend on inversion count, and this algorithm would not solve that different problem.

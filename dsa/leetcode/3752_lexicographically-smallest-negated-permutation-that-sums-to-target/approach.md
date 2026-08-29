## General

**Reduce sign choices to a subset-sum target**

If every magnitude `1..n` were positive, their total would be

$$
T=\frac{n(n+1)}2.
$$

Negating magnitude `v` changes its contribution from `+v` to `-v`, reducing the total by `2v`. If the negative magnitudes sum to `N`, the signed array sum is

$$
T-2N.
$$

To reach `target`, the required negative subset sum is

$$
N=\frac{T-\texttt{target}}2.
$$

A solution is impossible when `|target|>T` or `T-target` is odd. The first condition places the target outside the maximum possible signed range; the second makes `N` non-integral.

When both pass, `0<=N<=T`.

**Greedily choose negative magnitudes from largest to smallest**

The source scans `value=n,n-1,...,1`. If the remaining `negative_sum` is at least `value`, it marks that magnitude negative and subtracts it.

For consecutive magnitudes, this greedy choice always completes the subset. Before considering `v`, the remaining sum is within what `1..v` can represent. If it is at least `v`, choosing `v` leaves at most

$$
\frac{v(v+1)}2-v=\frac{v(v-1)}2,
$$

which smaller magnitudes can represent. If it is below `v`, including `v` would overshoot, so skipping is mandatory. By induction, the remainder reaches zero.

More precisely, before processing `v` the invariant is that the current remainder lies between zero and `v(v+1)/2`. The include case leaves it within the representable range of `1..v-1`. In the skip case the remainder is below `v`, so the smaller complete sequence can represent it. This maintains feasibility at every step.

**Why the greedy subset gives lexicographic minimum**

For a fixed sign assignment, the smallest permutation is its values sorted numerically:

- Negative values appear first from most negative upward, meaning descending magnitude.
- Positive values follow in ascending magnitude.

Across different feasible sign subsets, making a larger magnitude negative introduces a smaller numeric element `-v` at the earliest place where the sorted arrays can differ. Therefore, whenever magnitude `v` can be included while still completing the required subset sum, including it is lexicographically preferable.

The feasibility calculation above proves the descending greedy includes `v` exactly when it can do so. It thus chooses the lexicographically smallest feasible negative set.

The output construction mirrors numeric sorting:

`[-value for value in range(n,0,-1) if is_negative[value]]`

emits selected negatives from `-n` upward, then positive magnitudes are appended from one through `n`.

For `n=3` and target zero, `T=6` and `N=3`. Greedy selects magnitude three as negative. The sorted signed values are `[-3,1,2]`, matching the required minimum.

For `n=4` and target zero, `T=10` and `N=5`. Greedy selects four, skips three and two while the remainder is one, and finally selects one. The signed values sort to `[-4,-1,2,3]`. Any feasible solution without `-4` begins with a larger integer.

**Why absolute values remain a permutation**

Each magnitude has one Boolean sign and is emitted exactly once, either in the negative comprehension or positive extension. No magnitude is duplicated or omitted. Ordering changes only positions, which the problem permits.

The emitted sum equals `T-2N=target` by construction, so all constraints hold.

No separate permutation search is needed after signs are fixed. Sorting signed values is lexicographically smallest because swapping any adjacent inversion places the smaller integer earlier and strictly improves the array.

**No hidden target values are missed**

The set `{1,2,...,n}` is a complete sequence: every integer from zero through `T` can be represented as a subset sum. The descending proof demonstrates this constructively. Therefore the magnitude and parity checks are not merely necessary; they are sufficient.

## Complexity detail

Computing feasibility is constant time. The descending sign scan visits `n` magnitudes, and the two output passes together visit another $O(n)$ positions. Total time is $O(n)$.

`is_negative` uses $O(n)$ space, and the required output has `n` integers. Auxiliary plus output construction space is $O(n)$. The arithmetic total can exceed 32-bit range, so fixed-width implementations need 64-bit integers.

## Alternatives and edge cases

- **General subset-sum DP:** It would be far too expensive for totals near $n^2$. Consecutive magnitudes make descending greedy exact.
- **Choose small negatives first:** It may reach the sum but produces lexicographically larger arrays because large negative values are smaller numeric prefixes.
- **Emit values in magnitude order:** Lexicographic minimum requires ordinary signed numeric order, with large-magnitude negatives first.
- **Target above `T` or below `-T`:** No sign assignment can reach it.
- **Parity mismatch:** Every sign flip changes the all-positive total by an even amount, so reachable sums share `T`'s parity.
- **Target equals `T`:** `N=0`, no values are negative, and the answer is `[1,2,...,n]`.
- **Target equals `-T`:** Every magnitude is negative, emitted as `[-n,...,-1]`.
- **`n=1`:** Only targets one and negative one are reachable.
- **Duplicate values:** Absolute values are a permutation, so magnitudes are unique; the Boolean array maps one-to-one.
- **Remainder after greedy:** The complete-sequence invariant guarantees it is zero once feasibility passes.
- **Lexicographic comparison:** A more negative first unequal element is smaller, which is why the algorithm prioritizes large negative magnitudes.

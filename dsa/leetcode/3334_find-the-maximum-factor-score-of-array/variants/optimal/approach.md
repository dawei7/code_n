## General

**Evaluate no deletion and every single deletion.** The factor score is $\gcd(\text{array})\cdot\operatorname{lcm}(\text{array})$. Removing an element changes both aggregates, so a locally unusual value can improve the product. Testing each deletion by recomputing over all remaining elements would be quadratic. Prefix and suffix aggregates let the source combine the elements on either side in constant aggregate operations.

**Build suffix GCD and LCM arrays.** `suf_gcd[i]` is the GCD of `nums[i:]`, while `suf_lcm[i]` is its LCM. The base identities are zero for an empty GCD and one for an empty LCM:

$$
\gcd(0,x)=x,\qquad\operatorname{lcm}(1,x)=x.
$$

The source encodes these with `suf_gcd[n] = 0` and `suf_lcm[n] = 1`, then fills indices right to left.

The score with no removal is immediately `suf_gcd[0] * suf_lcm[0]` and initializes `ans`. This is necessary because removal is optional.

**Maintain aggregates strictly before the current index.** Before loop iteration $i$, `pre_gcd` and `pre_lcm` represent `nums[:i]`. Suffix entries at `i + 1` represent `nums[i+1:]`. Combining them excludes exactly `nums[i]`:

$$
G_i=\gcd(\text{preGCD},\text{suffixGCD}_{i+1}),
$$

$$
L_i=\operatorname{lcm}(\text{preLCM},\text{suffixLCM}_{i+1}).
$$

Their product is the score after removing index $i$. Only after evaluating that candidate does the source incorporate current `x` into the prefix aggregates. This update order prevents the removed value from leaking into its own candidate.

**Why aggregate halves can be combined.** GCD and LCM are associative and commutative. The aggregate of all elements except one is therefore the aggregate of the prefix and suffix aggregates, regardless of internal grouping. No original element list needs to be revisited.

**Empty-side identities handle endpoints.** Removing the first value leaves an empty prefix, so `gcd(0,suffix)` and `lcm(1,suffix)` return the suffix aggregates. Removing the last value symmetrically uses the completed prefix and empty suffix identities.

For a single-element array, the no-removal score is $x^2$ because both GCD and LCM equal $x$. The deletion candidate combines empty sides to GCD zero and LCM one, producing score zero, matching the specified empty-array score. The maximum correctly keeps $x^2$.
The initialized candidate covers the legal choice of deleting nothing. Every later iteration covers exactly one deletion index and computes exact remaining aggregates by associativity. These $n+1$ possibilities exhaust “at most one” removal. Taking their maximum returns the optimal factor score.

The method reads `nums` without sorting or mutation. It assumes `gcd` and `lcm` are imported, normally from Python's `math` module.

## Complexity detail

There are two linear passes. Each step performs a constant number of GCD/LCM operations. Euclid's algorithm gives logarithmic arithmetic time in operand magnitude, so a conventional bound is $O(n\log M)$ under the small-value constraints, though intermediate LCM operands may exceed individual $M$.

The two suffix arrays use $O(n)$ space. Prefix state and answer are constant-size. Python arbitrary-precision integers prevent overflow; fixed-width translations must ensure the LCM product range fits.

## Alternatives and edge cases

- **Recompute per deletion:** It uses $O(1)$ extra space but $O(n^2\log M)$ time.
- **Prefix arrays on both sides:** Store prefix and suffix GCD/LCM arrays. It is equally linear but uses more arrays than the running-prefix source.
- **Exclude no element:** This candidate must be included because deletion can reduce the score, as in arrays already balancing GCD and LCM well.
- **One element:** No deletion yields $x^2$, while deleting it yields the defined empty score zero.
- **Remove first or last:** Empty aggregate identities make endpoint cases require no branches.
- **All values equal:** No-removal score is $x^2$; deletion leaves the same score unless the array had one element.
- **Value one:** It can reduce GCD without increasing LCM, so removing it may improve the score.
- **LCM growth:** Even small elements can create a large LCM; Python handles it but other languages need wide types or overflow analysis.
- **Duplicate values:** Aggregates naturally account for multiplicity; deleting one duplicate may leave GCD and LCM unchanged.
- **Update order:** Prefix aggregates must be updated after evaluating deletion $i$.
- **Import requirement:** The snippet depends on both `gcd` and `lcm` being available.
- **Input preservation:** Suffix construction and prefix scanning never modify `nums`.
- **Why both aggregates are needed:** Optimizing only the GCD or only the LCM is insufficient because deletion can improve one while worsening the other. The score compares their product for each complete candidate.
- **Suffix base construction:** `[0] * (n + 1)` and `[0] * n + [1]` deliberately give different empty identities. Swapping them would corrupt every endpoint deletion.
- **Small bounded values:** Although each input is at most 30, the LCM can combine prime powers from many values. Complexity and integer-width reasoning should use aggregate magnitudes, not only one element's magnitude.
- **Optional deletion proof:** The initial no-removal score is not duplicated by the loop conceptually; even if some deletion produces the same numeric value, both are legal candidates and `max` handles equality harmlessly.

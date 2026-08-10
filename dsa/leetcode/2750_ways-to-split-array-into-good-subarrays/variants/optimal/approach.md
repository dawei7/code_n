## General

**Every output subarray must own exactly one one**

Suppose the positions of ones are:

$$
p_0<p_1<\cdots<p_{r-1}.
$$

Any valid split must place one subarray around each one. No subarray can contain two consecutive one positions, and no subarray can contain zero ones.

The only choices are where to cut inside the zeros separating consecutive ones.

**Count choices between two consecutive ones**

Take previous one at index `j` and current one at index `i`. A boundary must separate them.

The previous good subarray may end at any position from `j` through `i-1`. Equivalently, the next subarray may start at any position from `j+1` through `i`.

There are exactly:

$$
i-j
$$

possible boundary locations. If the ones are adjacent, the difference is one and the cut is forced. If there are $z$ zeros between them, the difference is $z+1$.

**Boundary choices are independent**

Choosing a cut between `p_0` and `p_1` does not restrict where to cut between `p_1` and `p_2`. Each gap separates a different pair of neighboring ones.

Therefore the total number of splits is the product:

$$
\prod_{t=1}^{r-1}(p_t-p_{t-1}).
$$

The code computes this product during one scan instead of storing all positions.

**Meaning of j and ans**

`j` stores the index of the most recently seen one. It starts at `-1` to mean that no one has appeared.

`ans` starts at one, the multiplicative identity. When a new one occurs at index `i` and `j > -1`, multiply by `i-j` and reduce modulo $10^9+7$. Then update `j=i`.

Zero entries require no action; they are accounted for automatically in the distance between one positions.

**Leading and trailing zeros create no extra choices**

Before the first one, all leading zeros must belong to the first good subarray. Cutting among them would create an initial subarray with zero ones, which is invalid.

After the last one, all trailing zeros must belong to the final good subarray. Cutting among them would create a trailing zero-one-free subarray.

Thus only internal zero gaps contribute factors.

**No ones means no valid split**

If the scan finishes with `j == -1`, the entire array contains zero ones. Every nonempty subarray would then contain zero ones, so no partition into good subarrays exists.

The exact return handles this separately with zero. This is why initializing `ans=1` does not incorrectly report one for the all-zero case.

**Exactly one one means one split**

When only one one exists, no internal gap factor is applied and `ans` remains one.

The only valid partition is the entire array as one subarray: leading and trailing zeros surround the single one. Any additional cut would create a subarray without a one.

**Trace zero, one, zero, zero, one**

The first one is at index one, so record `j=1`.

The next one is at index four. Their distance is three, corresponding to cuts after indices one, two, or three:

- `[0,1] | [0,0,1]`;
- `[0,1,0] | [0,1]`;
- `[0,1,0,0] | [1]`.

Multiply `ans` by three and return three.

**Several gaps**

If ones occur at positions two, five, and nine, the first gap has three choices and the second has four. Every choice from the first can be combined with every choice from the second, producing twelve splits.

This product reasoning avoids dynamic programming because the exact-one constraint isolates the boundaries.

**Modulo handling**

The number of products can be very large. Applying modulo after each multiplication preserves the required final residue and keeps intermediate `ans` bounded.

Position differences themselves are at most the array length.


Every valid partition needs exactly one boundary between each consecutive pair of ones and cannot place boundaries that create leading or trailing zero-only pieces. For positions `j<i` of consecutive ones, exactly `i-j` boundary locations separate them. Choices in different gaps are independent, so their product counts all valid splits uniquely. The scan multiplies precisely these factors, returns one for a single one, and zero when no one exists. Therefore its result is exact.

## Complexity detail

Let $n$ be the array length. The algorithm examines each element once and performs constant work at ones, giving $O(n)$ time.

It stores only `mod`, `ans`, `j`, and loop variables, so auxiliary space is $O(1)$. It does not retain the list of one positions.

Modulo arithmetic keeps the accumulator within a fixed numeric range in the conventional problem model.

## Alternatives and edge cases

- **Store every one position first:** Leads to the same product but uses $O(r)$ space instead of updating the previous position online.
- **Dynamic programming by prefixes:** Can count splits but is unnecessary because gap choices factor independently.
- **Enumerate cut subsets:** Exponential in the number of array boundaries.
- **All zeros:** No good subarray exists, so return zero.
- **Exactly one one:** The whole array is the unique good subarray, so return one.
- **Adjacent ones:** Their gap factor is one and the boundary is forced.
- **Long internal zero run:** Contributes one plus its zero count as boundary choices.
- **Leading zeros:** Must stay with the first one and add no factor.
- **Trailing zeros:** Must stay with the last one and add no factor.
- **Modulo:** Applied after every multiplication to satisfy the large-answer requirement.

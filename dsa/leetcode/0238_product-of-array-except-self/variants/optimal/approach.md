## General

For each index `i`, the answer needs every factor in `nums` except `nums[i]`. The most direct-looking formula is “multiply the whole array, then divide by `nums[i]`,” but division is forbidden. It also behaves poorly around zero: division by zero is undefined, and a total product of zero loses the information needed to distinguish the position of the only zero from all other positions.

The useful observation is that every element other than `nums[i]` lies in exactly one of two disjoint regions:

- the elements strictly to the left of `i`; and
- the elements strictly to the right of `i`.

Therefore,

$$
\text{answer}[i]
=
\left(\prod_{j=0}^{i-1}\text{nums}[j]\right)
\left(\prod_{j=i+1}^{n-1}\text{nums}[j]\right).
$$

This identity excludes `nums[i]` by construction, so it needs no division. The exact solution computes the left product for every position in a forward pass, stores those products directly in the output array, and then multiplies them by right products generated during a backward pass.

**Why the empty-side product is one**

At index `0`, there are no elements to the left. At index `n - 1`, there are no elements to the right. The product of an empty collection is defined as `1`, the multiplicative identity. That choice is not an arbitrary special case: multiplying by `1` leaves the existing product unchanged. Consequently, the first answer becomes the product of its right side, and the last answer becomes the product of its left side.

The variables `left` and `right` both begin at `1` for this reason.

**Forward pass: store the exclusive prefix product**

Before processing index `i`, `left` equals the product of all elements whose indices are smaller than `i`:

$$
\text{left}=\prod_{j=0}^{i-1}\text{nums}[j].
$$

The solution first assigns `ans[i] = left`. Only afterward does it execute `left *= nums[i]`, preparing `left` for the next index. This order is essential. If `nums[i]` were multiplied first, `ans[i]` would include the very element that must be excluded.

After the forward loop, every `ans[i]` contains the complete left factor needed by the formula. The output array is serving as useful working storage; no separate prefix array is necessary.

For `nums = [1, 2, 3, 4]`, the states written to `ans` are:

| Index `i` | `left` before including `nums[i]` | Stored `ans[i]` | `left` after update |
|---:|---:|---:|---:|
| 0 | 1 | 1 | 1 |
| 1 | 1 | 1 | 2 |
| 2 | 2 | 2 | 6 |
| 3 | 6 | 6 | 24 |

Thus the intermediate output is `[1, 1, 2, 6]`, precisely the exclusive prefix products.

**Backward pass: generate suffix products on demand**

The second loop travels from `n - 1` down to `0`. Before processing index `i`, `right` equals the product of all elements strictly after `i`:

$$
\text{right}=\prod_{j=i+1}^{n-1}\text{nums}[j].
$$

At that moment, `ans[i]` already holds the product strictly before `i`. Multiplying `ans[i] *= right` combines the two disjoint sides and produces the final product except self. The solution then runs `right *= nums[i]`, adding the current element only for the benefit of the next index to the left.

Again, update order matters. The suffix accumulator must be used before `nums[i]` enters it; otherwise the result would incorrectly contain the excluded element.

Continuing the example, the backward pass behaves as follows:

| Index `i` | Stored left product | `right` before update | Final `ans[i]` | `right` after update |
|---:|---:|---:|---:|---:|
| 3 | 6 | 1 | 6 | 4 |
| 2 | 2 | 4 | 8 | 12 |
| 1 | 1 | 12 | 12 | 24 |
| 0 | 1 | 24 | 24 | 24 |

The result is `[24, 12, 8, 6]`.

**Why the method is correct**

The forward-pass property holds initially because `left = 1` is the product of the empty prefix before index `0`. After storing it at index `i`, multiplying by `nums[i]` extends that prefix exactly far enough for index `i + 1`. Therefore, after the first pass, `ans[i]` is the product of precisely the indices less than `i`.

The backward-pass property is symmetric. It begins at the last index with `right = 1`, the empty suffix product. The algorithm uses that exclusive suffix and only then includes `nums[i]`, so the property remains true at the next index to the left. When `ans[i]` and `right` are multiplied, their index sets contain every array position except `i`, with no overlap and no omission. Their product is therefore exactly the required answer for `i`. Since the second pass finalizes every index, the returned array is correct.

**Zeros require no special branch**

The prefix-suffix formulation naturally preserves zero information. Suppose `nums = [-1, 1, 0, -3, 3]`. At the zero's index, neither its left product nor its right product includes the zero, so their product is `9`. At every other index, either the exclusive prefix or exclusive suffix crosses the zero and is therefore zero. The result is `[0, 0, 9, 0, 0]`.

With two or more zeros, every “all elements except this one” selection still contains at least one zero, so every output is zero. Negative values likewise need no special handling; ordinary multiplication automatically gives the correct sign.

## Complexity detail

Let $n$ be the number of elements in `nums`. The forward pass visits all $n$ indices once, and the backward pass visits all $n$ indices once. Each visit performs a constant amount of work, so the total running time is $O(n)$. The two passes are additive—$O(n)+O(n)=O(n)$—rather than multiplicative.

The returned array contains $n$ values and necessarily uses $O(n)$ output storage. Under the problem's stated convention, output storage is not counted as auxiliary space. Beyond that array, the solution stores only `n`, `left`, `right`, the loop index, and a temporary element value, all constant-sized quantities. Its auxiliary space complexity is therefore $O(1)$.

This is asymptotically optimal in time because every input value can affect many outputs, and at minimum the algorithm must read all $n$ inputs and produce all $n$ answers.

## Alternatives and edge cases

- **Total product followed by division:** This can be linear time for arrays without zero, but division is explicitly forbidden. It also needs special counting logic for zero values and is therefore not the intended formulation.
- **One multiplication loop per output:** For each index, multiplying every other element is simple but repeats almost all work. It takes $O(n^2)$ time and is too slow for up to $10^5$ elements.
- **Separate prefix and suffix arrays:** Building `left[i]` and `right[i]` arrays makes the same identity visually explicit and still runs in $O(n)$ time, but it consumes $O(n)$ auxiliary space. The implemented solution compresses one side into the output and the other into one scalar.
- **One zero:** Only the zero's own position can have a nonzero result; the two-pass multiplication obtains this without detecting the zero explicitly.
- **Multiple zeros:** Every output contains a zero among its included factors, so all results are zero. No branch or reset is required.
- **Negative elements:** Prefix and suffix multiplication preserve signs normally. An odd number of included negative factors gives a negative output; an even number gives a nonnegative output.
- **Array of length two:** The forward and backward invariants still apply. For `[a, b]`, the empty products ensure the answer is `[b, a]`.
- **Values equal to one or minus one:** They do not break either invariant. They merely preserve or flip the accumulated product as ordinary multiplication dictates.
- **Overflow assumptions:** The statement guarantees that the relevant products fit in a 32-bit integer. Python integers can grow beyond that anyway, but implementations in fixed-width languages may rely on the stated guarantee rather than introducing division or floating-point arithmetic.
- **In-place overwrite of `nums`:** Reusing the input array would destroy original values still needed by the backward pass unless they were saved elsewhere. Using the required output array as prefix storage avoids that dependency and preserves the input.

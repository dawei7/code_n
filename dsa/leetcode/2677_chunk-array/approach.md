## General

**A chunk is one consecutive half-open range**

The output must preserve every element and its order while grouping consecutive elements into subarrays of at most `size` elements.

For a chunk beginning at index `i`, the intended indices are:

$$
i,i+1,\ldots,\min(i+\texttt{size},n)-1.
$$

JavaScript's `slice(start, end)` uses exactly this half-open convention: it includes `start` and stops before `end`.

**Start only at chunk boundaries**

The loop initializes `i = 0` and advances with `i += size`. Its successive values are:

$$
0,\texttt{size},2\cdot\texttt{size},\ldots
$$

These are precisely the first indices of the desired chunks. There is no need for an inner loop to search for boundaries because the positive chunk size fixes them.

At each boundary, the implementation appends:

`arr.slice(i, i + size)`.

That slice becomes one independent subarray in `ans`.

**Why the final chunk needs no special branch**

The last starting index may have fewer than `size` elements remaining. `slice` safely limits its end to `arr.length` when `i + size` lies beyond the array.

For `arr = [1, 9, 6, 3, 2]` and `size = 3`:

- `slice(0, 3)` produces `[1, 9, 6]`;
- `slice(3, 6)` reaches the physical end and produces `[3, 2]`.

The result follows the contract without padding and without reading nonexistent values.

**Why no empty chunk is appended**

The loop condition is `i < n`, where `n = arr.length`. A slice is created only when at least one original element remains at index `i`.

After the last nonempty slice, adding `size` makes `i` at least `n`, and iteration stops. This avoids a trailing empty array when the length is exactly divisible by the chunk size.

**Trace an exactly divisible input**

For six elements and `size = 2`, the starting indices are 0, 2, and 4.

The slices cover index ranges `[0, 2)`, `[2, 4)`, and `[4, 6)`. The next candidate start is 6, but `6 < 6` is false.

Every chunk has exactly two elements and no fourth chunk appears.

**Trace a chunk size larger than the array**

If there are five elements and `size = 6`, the first slice asks for `[0, 6)`. JavaScript stops at index 5 and copies all five elements.

The increment then changes `i` to 6, so the loop ends. The output contains exactly one subarray holding the complete input.

**The empty-array case**

When `arr.length` is zero, `i < n` is false before the first iteration. `ans` remains empty and is returned as `[]`.

This distinction is important: an empty input produces no chunks, not one empty chunk.

**Why all elements appear exactly once**

The slice intervals are consecutive. The interval beginning at `i` ends immediately before `i + size`, which is the next loop's start.

Therefore two chunks never overlap, so no element is duplicated. There is also no gap between their ranges, so every index below $n$ belongs to some chunk. Preserving the order inside each slice and ordering slices by increasing start preserves the full original order.

**Slices are shallow copies**

`slice` creates new subarray objects but copies element values only one level deep.

For primitive elements, this behaves like copying the values. If an element is an object or nested array, the chunk contains the same reference as the original array. The challenge asks to regroup elements, not deep-clone them, so shallow copying is appropriate.

The outer input array itself is not modified.

**Why the stride cannot be zero**

If `size` were zero, `i += size` would never advance and the loop would be infinite. The contract guarantees a positive size, so every iteration moves toward termination.

This is a good example of using a constraint as part of the termination proof rather than adding an unnecessary defensive case.

**Why this is optimal**

The output contains all $n$ original elements distributed among new subarrays. Creating that result requires copying or placing $\Omega(n)$ element references.

The exact solution performs one slice copy for each chunk, and across all slices exactly $n$ elements are copied. Its linear work therefore matches the unavoidable output cost.

**Number of output chunks**

For nonempty input, the number of chunks is:

$$
\left\lceil\frac{n}{\texttt{size}}\right\rceil.
$$

The stride loop creates exactly this many slices. This formula also explains why the last chunk is shorter precisely when `n % size` is nonzero.

## Complexity detail

The loop itself runs $\lceil n/\texttt{size}\rceil$ times. A slice copies the number of elements in its range, and the ranges partition all $n$ elements. Total time is therefore $O(n)$ rather than the number of chunks multiplied by $n$.

The returned inner arrays collectively store $n$ element references, and the outer result stores one reference per chunk. Total output space is $O(n)$. Apart from the required output, `ans`, `i`, and `n` use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Nested loops with `push`:** Also $O(n)$ and avoids `slice`, but requires more manual boundary bookkeeping.
- **Use `reduce`:** It can append to the latest chunk or create a new one, though the stride formulation exposes boundaries more directly.
- **Use `splice`:** It can remove chunks from the front, but it mutates the input and front removals can be costly.
- **Lodash `_.chunk`:** Explicitly disallowed by the problem.
- **Empty input:** Returns `[]` rather than `[[]]`.
- **Size one:** Produces one single-element subarray per input element.
- **Size equal to length:** Produces one full-size chunk.
- **Size larger than length:** Produces one shorter chunk for nonempty input.
- **Non-divisible length:** Only the final chunk has fewer than `size` elements.
- **Exactly divisible length:** No trailing empty chunk is created.
- **Object elements:** References are copied shallowly; nested objects are not cloned.
- **Input preservation:** `slice` leaves `arr` and its ordering unchanged.
- **Positive-size guarantee:** It ensures the loop advances and terminates.

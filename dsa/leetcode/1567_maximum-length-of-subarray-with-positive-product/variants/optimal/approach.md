## General

**Track product sign instead of product magnitude**

The product may become enormous, but its sign depends only on whether the number of negative factors is even or odd and whether a zero occurs.

For each index `i`, the source stores two suffix lengths:

- `f[i]` is the longest subarray ending exactly at `i` whose product is positive.
- `g[i]` is the longest subarray ending exactly at `i` whose product is negative.

A zero value makes every nonempty product ending there zero, so neither a positive nor negative suffix exists.

This state records exactly the information needed when the next sign arrives.

**Initialize the first value**

`f[0] = int(nums[0] > 0)` gives one for a positive first value and zero otherwise.

`g[0] = int(nums[0] < 0)` gives one for a negative first value and zero otherwise.

For zero, both remain zero. The initial answer is `f[0]` because only a positive suffix qualifies.

Python converts the Boolean comparisons to integers zero and one.

**Append a positive value**

Multiplying by a positive number preserves sign.

Any positive-product suffix ending at `i-1` can extend through `nums[i]`, so:

`f[i] = f[i - 1] + 1`.

Even when `f[i-1]` is zero, the new positive value alone forms a positive length-one subarray, and the formula correctly gives one.

A negative suffix can extend only if one already exists. If `g[i-1]` is zero, no negative suffix ends at the previous position and `g[i]` stays zero. Otherwise it becomes `g[i-1] + 1`.

**Append a negative value**

Multiplying by a negative value flips sign.

A previous negative suffix becomes positive, so if `g[i-1]` exists:

`f[i] = g[i - 1] + 1`.

If no negative suffix exists, no positive suffix can end at the new negative value, and `f[i]` is zero.

A previous positive suffix becomes negative when extended. If none exists, the current negative value alone is a valid negative suffix of length one. Both cases are captured by:

`g[i] = f[i - 1] + 1`.

When `f[i-1]` is zero, this yields one for the singleton.

**Handle zero through initialized defaults**

The arrays begin filled with zeros. The loop has branches only for positive and negative values.

When `nums[i] == 0`, neither branch runs, leaving `f[i]` and `g[i]` at zero. This resets both sign histories because no positive- or negative-product subarray can cross a zero.

At the next nonzero value, transitions read zeros and naturally begin a new segment.

**Update the global answer**

`ans` stores the longest positive suffix seen at any ending index. After processing each value, the source takes `max(ans, f[i])`.

Every subarray has one final index. If its product is positive, its length is no greater than the longest positive suffix recorded for that endpoint.

Therefore maximizing `f[i]` across all endpoints finds the globally longest qualifying subarray.

**Tracing the first example**

For one, positive length is one and negative length zero.

Appending negative two flips the positive suffix into a negative suffix of length two; no positive suffix ends there.

Appending negative three flips that negative suffix back into a positive suffix of length three. A negative singleton also exists.

Appending positive four preserves both signs and extends the positive suffix to length four. The answer becomes four.

**Tracing a zero reset**

For zero, both state lengths are zero. The following positive one starts a positive suffix of length one.

Negative two converts that positive suffix into a negative suffix of length two. Negative three converts it back into a positive suffix of length three.

Negative four then makes the longest ending product negative, while a shorter positive suffix may be obtained from the prior negative state. The recorded maximum remains three.

**Why the recurrence is correct**

Assume `f[i-1]` and `g[i-1]` correctly describe all best signed suffixes ending at the previous index.

Every nonempty subarray ending at `i` is either the singleton current value or an ending-at-`i-1` suffix extended by that value. The three sign cases enumerate exactly how these possibilities transform.

Choosing the longest available source suffix yields the longest destination suffix of each sign. Induction proves all states, and the global maximum proves the returned answer.

**Avoiding overflow**

No product is ever calculated. Only signs and lengths are propagated.

This avoids overflow in fixed-width languages and avoids expensive growth of arbitrary-precision products in Python.

## Complexity detail

Let $N$ be array length. Initialization is constant, and the loop processes each remaining value once with constant work. Time is $O(N)$, matching the manifest.

The exact stored source allocates two arrays of length $N$, so its auxiliary space is $O(N)$, not the manifest's stated $O(1)$.

Only the previous positive and negative lengths are needed for the next transition. Replacing `f` and `g` with two rolling scalar variables would realize the manifest's $O(1)$ space bound without changing the recurrence.

## Alternatives and edge cases

- **Rolling two-state DP:** Keep only current positive and negative lengths to achieve true constant auxiliary space.
- **Multiply every subarray:** It costs quadratic time and risks overflow.
- **Count negatives between zeros:** For each zero-free segment, remove a prefix through the first negative or a suffix from the last negative when the count is odd. It is also linear.
- **All positive values:** The positive length grows through the entire array.
- **Single negative value:** It creates only a negative suffix, so the positive answer remains zero.
- **Two negatives:** Their combined product is positive and can form length two.
- **Zero:** It resets both suffix states.
- **Several zeros:** Each independently separates zero-free segments.
- **Positive after zero:** It begins a new positive suffix of length one.
- **Negative after zero:** It begins a negative suffix of length one.
- **No positive-product subarray:** The initialized answer remains zero.
- **Large magnitudes:** They do not matter because only each value's sign is examined.
- **Manifest mismatch:** Constant space belongs to the rolling-state form, while the exact source retains all endpoint states.

## General

**Track indices instead of materializing the sequence**

The initial list may contain up to $10^{15}$ integers, so simulation is impossible. Every sweep keeps roughly half the current entries, and the survivors follow a simple arithmetic mapping back to their positions before the sweep.

The recursive helper `survivor(length, from_left)` returns the one-based position, within a conceptual sequence of `length` consecutive slots, of the eventual survivor when the next sweep begins from the indicated side.

The values in the original list equal their one-based positions, so the top-level returned position is also the required integer.

**A sweep keeps the first visited item**

The contract says to start from one side, keep the first encountered number, delete the second, and alternate.

From the left, survivors occupy old positions

$$
1,3,5,\ldots.
$$

Their count is $\lceil L/2\rceil=(L+1)//2$. Reduced survivor position $r$ maps back to old position

$$
2r-1.
$$

This mapping is the same for both even and odd $L$ when sweeping from the left.

**A right sweep depends on parity**

From the right, the rightmost item is kept and the next one to its left is deleted.

If $L$ is odd, the kept positions in normal left-to-right order are again

$$
1,3,5,\ldots,L,
$$

so reduced position $r$ maps to $2r-1$.

If $L$ is even, the kept positions are

$$
2,4,6,\ldots,L,
$$

so reduced position $r$ maps to $2r$.

This is why the source uses the odd-position formula when

`from_left or length % 2 == 1`

and uses the even-position formula only for a right-to-left sweep of an even-length sequence.

**Solve the reduced alternating problem first**

After one sweep, the number of survivors is

`(length + 1) // 2`.

The next sweep comes from the opposite direction, so the source recursively computes

`survivor((length + 1) // 2, not from_left)`.

This returned `reduced_index` identifies which entry survives within the compressed list. The parity mapping then converts it to the corresponding position in the current larger list.

The base case `length == 1` returns position one because the only entry is already the survivor.

**Trace `n=8` through the recurrence**

For length eight from the left, the reduced problem has length four from the right.

Length four from the right reduces to length two from the left. Length two from the left reduces to length one from the right, whose reduced answer is one.

Mapping outward:

- length two, left sweep: $2\cdot1-1=1$;
- length four, right sweep and even length: $2\cdot1=2$;
- length eight, left sweep: $2\cdot2-1=3$.

The answer is three, matching the literal sequences `[1,3,5,7]`, then `[3,7]`, then `[3]`.

**Trace the parity change for `n=5`**

Length five from the left reduces to length three from the right. That right sweep has odd length, so its survivors correspond to odd positions. Length three reduces to length two from the left, and then to one.

Every outward mapping selects reduced position one, eventually returning original position one. This matches the example.

**Why the recurrence preserves the exact survivor**

One sweep partitions the current sequence into deleted positions and an ordered survivor subsequence. The mapping formulas are bijections from reduced positions $1..\lceil L/2\rceil$ onto exactly those kept old positions.

The recursive call finds the ultimate survivor's index within that kept subsequence under all later alternating sweeps. Applying the appropriate bijection gives the same element's index before the current sweep.

Starting from the trivial one-element base and applying this argument outward proves every recursive level returns the exact current-sequence position. The top level consequently returns the original integer.

## Complexity detail

Each recursive call replaces `length` with $\lceil\texttt{length}/2\rceil$. The number of calls is therefore $O(\log N)$; for $N\le10^{15}$ it is only about fifty levels.

Every level performs constant arithmetic, so time is $O(\log N)$. The recursive call stack stores $O(\log N)$ frames, matching the manifest's space bound.

No sequence, deletion mask, or list of survivors is allocated.

## Alternatives and edge cases

- **Literal list simulation:** It needs $O(N)$ initial memory and work, impossible for $N$ up to $10^{15}$.
- **Iterative affine tracking:** One can maintain the first value, spacing, count, and direction without recursion; the source instead maps survivor indices recursively.
- **Always map with `2r-1`:** This fails for an even-length right sweep, whose survivors occupy even old positions.
- **Always map with `2r` from the right:** This fails for odd lengths, where the leftmost position is retained.
- **Use `length//2` survivors:** Odd lengths keep one extra element, so the correct size is `(length+1)//2`.
- **Forget to alternate direction:** Every recursive level must negate `from_left`.
- **`n=1`:** The base case returns one without performing a sweep.
- **`n=2`:** The left sweep keeps one and deletes two, returning one.
- **Odd current length:** Both sweep directions retain odd-indexed positions when written left to right.
- **Even current length:** Left keeps odd positions while right keeps even positions.
- **Large input:** Recursion depth is logarithmic and safely small for the stated bound.
- **One-based mapping:** Formulas use positions 1 through `length`, matching the original values `[1,2,...,n]`.
- **No input mutation:** Only integer lengths, directions, and mapped indices are used.

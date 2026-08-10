## General

Because the output must begin positive and every consecutive pair must have opposite signs, the sign of every output position is predetermined:

- even indexes $0,2,4,\ldots$ must contain positive values;
- odd indexes $1,3,5,\ldots$ must contain negative values.

The equal-count guarantee ensures there are exactly enough values of each sign to fill those positions.

**Prepare the fixed output layout**

The exact solution allocates `ans = [0] * len(nums)`. These zeros are placeholders only; zero never appears in the input because every legal value has absolute value at least one.

Two cursors identify the next open slot for each sign:

- `i = 0` is the next even index for a positive;
- `j = 1` is the next odd index for a negative.

Each cursor advances by two after a placement, so it remains on indexes of its assigned parity.

**Read the source in original order**

The loop `for x in nums` visits elements from left to right. When `x > 0`, the code writes `ans[i] = x` and then performs `i += 2`. Otherwise, the constraints imply `x < 0`, so it writes `ans[j] = x` and advances `j` by two.

Processing in source order is what preserves relative order within each sign. Suppose positive value $p_1$ appears before positive value $p_2$ in `nums`. The loop encounters $p_1$ first and gives it the earlier unused even slot. The cursor then advances, so $p_2$ receives a later even slot. The same reasoning applies independently to negatives and odd slots.

No later placement can overwrite an earlier one because each cursor always moves forward to an unused index.

**Why alternation is automatic**

After all placements, every even slot holds a positive and every odd slot holds a negative. Index zero is even, so the result begins positive. Any consecutive indexes have opposite parity, hence their values have opposite signs. All three requirements follow from the fixed layout.

For `[3,1,-2,-5,2,-4]`, positive encounters fill indexes zero, two, and four with `3,1,2`. Negative encounters fill indexes one, three, and five with `-2,-5,-4`. The result is `[3,-2,1,-5,2,-4]`.

**Why the cursors stay in bounds**

If the input length is $n$, there are exactly $n/2$ positive values and $n/2$ negative values. The positive slots are the $n/2$ even indexes, and the negative slots are the $n/2$ odd indexes. Therefore the final placement of either sign uses its last valid slot. The cursor advances beyond the array only after that final write and is never used again.

Without the equal-count guarantee, this direct placement strategy would need additional logic for leftover values. Under the contract, no leftovers exist.

**Why the output is uniquely determined**

The sign constraints determine which positions belong to each sign, and stability determines the order within those positions. The first positive must occupy index zero, the first negative index one, the second positive index two, and so on. Therefore there is only one valid rearrangement for a given input, and the two cursors construct it.

**Why an auxiliary array is appropriate**

The problem explicitly says in-place modification is not required. Stable in-place rearrangement can require shifting many elements or a more complex algorithm. Writing once into a fresh result provides clear linear behavior and directly mirrors the output constraints.

## Complexity detail

Let $n$ be the length of `nums`. Allocating `ans` initializes $n$ positions. The loop reads each input value once and performs one constant-time assignment and cursor update. Total time is $O(n)$.

The output array contains $n$ integers, so it requires $O(n)$ space. If required output is not counted as auxiliary space, the additional cursor and loop variables use $O(1)$; the manifest counts the constructed result and reports $O(n)$.

The input list is never modified. All rearrangement occurs in `ans`.

## Alternatives and edge cases

- **Separate positive and negative lists:** Filter both signs, then alternate values from the two lists. This is also $O(n)$ time but uses two extra collections in addition to the result.
- **In-place stable rearrangement:** Rotating misplaced elements can preserve order but may degrade to $O(n^2)$ time. More advanced stable partitioning is unnecessarily complex here.
- **Sort by sign:** Sorting can place signs into blocks rather than alternating them and generally destroys relative order.
- **Use one output append cursor:** Maintain queues of signs and append alternately. This works but needs extra sign collections; direct parity cursors fill positions in one source pass.
- **Two-element input:** The single positive goes to index zero and the single negative to index one, regardless of source order.
- **Input already valid:** The method reconstructs the same ordering because each sign subsequence is already stable.
- **Input grouped by sign:** Even if all negatives precede all positives, independent cursors still place each group into the correct alternating slots.
- **No zero values:** The `else` branch safely means negative because the constraints exclude zero.
- **Equal sign counts:** This guarantee prevents an out-of-range cursor and ensures every placeholder is replaced.
- **Stable positives:** Their encounter order is exactly their increasing sequence of even output indexes.
- **Stable negatives:** Their encounter order is exactly their increasing sequence of odd output indexes.
- **Maximum length:** The single pass remains linear for $2\cdot10^5$ values.
- **Placeholder zeros:** They are never observable in the returned legal result because every slot receives one input value.
- **Input preservation:** Returning a new list honors the statement that modification in place is unnecessary and leaves `nums` unchanged.

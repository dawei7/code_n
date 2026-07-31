## General

For each position, count the alternating subarrays that end exactly there. Such a subarray must be a suffix of the prefix processed so far. If the current value differs from the previous value, every alternating suffix ending at the previous position can be extended by the current value, and the one-element suffix starting here is also valid. Therefore the number ending here increases by one.

If two adjacent values are equal, no subarray containing that adjacent pair can remain alternating. The only alternating subarray ending at the current position is then its singleton, so the maintained suffix length resets to one.

Let `ending_here` denote this number. After processing index `i`, it is also the length of the longest alternating suffix ending at `i`: that suffix has exactly one valid starting position for each length from one through `ending_here`. Adding `ending_here` to the answer at every index counts every alternating subarray once, classified by its unique right endpoint.

## Complexity detail

Let $n$ be the length of `nums`, as defined in the function contract. The scan performs constant work at each position, so it takes $O(n)$ time. Only the running suffix length and accumulated answer are stored, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Maximal-run summation:** Split the array wherever adjacent values are equal. An alternating run of length $L$ contributes $L(L+1)/2$ subarrays. This is also linear but requires careful treatment of the boundary element when a new run begins.
- **Dynamic-programming array:** Store the number of alternating subarrays ending at every index and sum the array. It uses the same recurrence but consumes $O(n)$ space even though only the previous value is needed.
- **Enumerate all subarrays:** Test or extend every possible range. This is correct, but a fully alternating input forces $\Theta(n^2)$ work.
- **Single element:** The only subarray is alternating, so the answer is one.
- **Equal adjacent values:** Equality resets the suffix count to one; it does not reset it to zero because the current singleton remains valid.
- **Large result:** A fully alternating array contributes $n(n+1)/2$, so the return value may exceed a 32-bit signed integer even though each input value is binary.


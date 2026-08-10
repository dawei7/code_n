## General

**A player may end the game immediately**

When the current array has length `m`, a legal move may remove any nonempty contiguous subarray of length strictly less than `m`. In particular, removing `m - 1` elements is legal.

There are two especially important such moves:

- remove every element except the current first element;
- remove every element except the current last element.

The removed elements form a contiguous suffix or prefix, respectively. Either move leaves one element and ends the game immediately.

This means the full minimax game tree is unnecessary. Alice can choose an endpoint on her first turn, and Bob can choose an endpoint on his first turn if Alice does not already finish.

**Alice can guarantee the larger original endpoint**

Let

$$
M=\max(\texttt{nums}[0],\texttt{nums}[N-1]).
$$

If the first element equals `M`, Alice removes the suffix `nums[1..N-1]`. If the last element equals `M`, she removes the prefix `nums[0..N-2]`.

Both removed blocks have length $N-1<N$, so they are legal whenever $N>1$. The selected endpoint is left alone, the game ends before Bob moves, and the final value is `M`.

For a one-element array, no move is needed and both endpoints refer to that same value. Thus Alice can always ensure a result of at least `M`.

This already proves why an interior maximum does not automatically decide the game. Alice cannot keep an arbitrary interior element by deleting everything else in one move: the elements on both sides of an interior position form two separated blocks, not one contiguous subarray.

**Bob can prevent any value above the larger original endpoint**

To establish the exact minimax result, it is not enough to show what Alice can obtain. We must also show that she cannot force anything larger than `M`.

Consider any first move by Alice. She removes one proper contiguous block `[l,r]`.

Because the removed block is not the entire array, at least one element survives. More specifically, Alice cannot remove both original endpoints unless she removes the whole array: a contiguous block containing index 0 and index $N-1$ contains every index between them. Therefore at least one of the two original endpoints survives.

Any surviving original first element remains the first element of the concatenated array. Any surviving original last element remains its last element. Deleting a middle block changes adjacency but does not move an outside element past another surviving element.

If Alice's move already leaves one element, that survivor can only be an original endpoint. Removing $N-1$ contiguous elements leaves either index 0 or index $N-1$, never a strict interior index. Its value is at most `M`.

If at least two elements remain, Bob can end the game on his turn. He compares the current first and last values and keeps the smaller one by deleting the other `m-1` elements as one prefix or suffix. Since at least one current endpoint is a surviving original endpoint, the smaller current endpoint is no greater than that surviving endpoint, which is itself at most `M`.

Thus, regardless of Alice's first deletion, Bob has a response ensuring the final value is at most `M`.

**Matching guarantees determine the value**

Alice has a strategy guaranteeing at least `M`. Bob has a strategy guaranteeing at most `M`. These bounds match, so the optimal-play value is exactly

$$
\max(\texttt{nums}[0],\texttt{nums}[-1]).
$$

The exact source returns that expression directly.

For `[1,5,2]`, the interior 5 looks tempting, but Alice cannot isolate it with one contiguous deletion. She can guarantee 2 by removing `[1,5]` and keeping the last endpoint. If she makes a longer game instead, Bob can still cap the result at 2. The answer is therefore 2.

For `[3,7]`, Alice removes the first element and keeps 7. The game ends immediately, giving the larger endpoint.

**Why intermediate concatenation needs no simulation**

The upper-bound argument uses only one structural fact after Alice's move: at least one original endpoint is still a current endpoint. It does not matter which interior elements survive or become adjacent.

Since Bob can immediately reduce the resulting array to one current endpoint, there is never a need to analyze a third turn under optimal play. The enormous collection of possible subarray deletions collapses to an endpoint strategy.

## Complexity detail

The source reads `nums[0]` and `nums[-1]` and computes one maximum. Running time is $O(1)$, independent of $N$. It does not need to scan interior elements because the minimax proof establishes that they cannot change the game value.

Only the two accessed values and the returned integer are involved, so auxiliary space is $O(1)$.

This is stronger than the usual $\Omega(N)$ requirement for array problems: the rules mathematically prove that all interior input values are irrelevant to the answer, so not reading them is safe.

## Alternatives and edge cases

- **Recursive minimax:** Enumerating every removable subarray at every state creates an explosive game tree and repeats many array states. It is useful only as a tiny-input verification model.
- **Dynamic programming over intervals:** Surviving arrays after middle deletion can concatenate separated original pieces, so an interval DP is not even a natural complete state; the endpoint theorem eliminates the need.
- **Choose the global maximum:** This is wrong when the maximum is strictly interior. Alice cannot isolate an interior element by deleting one contiguous proper block.
- **One element:** No move is possible or necessary, and `nums[0]` equals `nums[-1]`.
- **Two elements:** Alice can remove either one, so she directly chooses the larger.
- **Equal endpoints:** Their common value is the minimax result, regardless of all interior values.
- **Very large interior value:** It does not exceed Bob's endpoint-based cap unless it is itself an original endpoint.
- **Alice ends immediately:** Removing a prefix or suffix of length $N-1$ is legal because the condition is strictly less than the current length, not at most $N-2$.
- **Bob's cap after a middle deletion:** At least one original endpoint survives as a current endpoint, and Bob keeps the smaller current endpoint.
- **Positive-value constraint:** The proof uses only ordering and would remain valid for arbitrary integers; positivity is not needed by the source.

## General

Applying every update directly would touch every array position inside its range. An update covering almost the entire array would cost $O(\texttt{length})$, and many such updates could become far too expensive. The exact solution records only where each increment starts and where its effect stops.

This boundary representation is called a difference array. Instead of storing the final value at each index immediately, `d[i]` stores how much the running value should change when a left-to-right scan reaches index `i`.

**From array values to boundary changes.**

Suppose an update adds `c` to every index from `l` through `r`, inclusive. The running value should increase by `c` when the scan enters index `l`. It should remain elevated through index `r`. At index `r + 1`, it should decrease by `c` so later positions are unaffected.

The source records exactly those events:

```text
d[l] += c
d[r + 1] -= c     if r + 1 is inside the array
```

No interior index needs a direct change. A later prefix sum carries the starting increment across the complete range.

**Why the right boundary is `r + 1`.**

The update interval includes index `r`, so subtracting at `r` would cancel the increment one position too early. The cancellation belongs at the first index outside the range, `r + 1`.

If `r` is the last valid index, there is no later array position at which the effect must stop. The condition `r + 1 < length` skips the subtraction rather than indexing beyond `d`.

**Reconstructing values with a prefix sum.**

After all boundaries have been marked, `accumulate(d)` yields the running prefix sums:

$$
\texttt{answer}[i]=\sum_{p=0}^{i}\texttt{d}[p].
$$

Every update whose start is at or before `i` has contributed its positive boundary by this point. If that update ended before `i`, its negative boundary has also been included and cancels it. Therefore the running sum contains exactly the increments from updates satisfying

$$
\texttt{startIdx}\le i\le\texttt{endIdx}.
$$

Converting the `accumulate` iterator to a list produces the required concrete result array.

**A single-update trace.**

For an array of length five and update `[1, 3, 2]`, the difference array begins as

```text
[0, 0, 0, 0, 0]
```

Adding two at index one and subtracting two at index four gives

```text
[0, 2, 0, 0, -2]
```

Its prefix sums are

```text
[0, 2, 2, 2, 0]
```

which adds two exactly to inclusive indices one through three.

**How overlapping updates combine.**

Boundary marks use ordinary addition, so several updates can contribute to the same start or stop position. Their effects superpose automatically.

For the first example:

- `[1,3,2]` marks `+2` at `1` and `-2` at `4`.
- `[2,4,3]` marks `+3` at `2`; its range reaches the final index, so no in-array stop mark is needed.
- `[0,2,-2]` marks `-2` at `0` and `+2` at `3`. A negative increment starts by lowering the running value and stops by adding its opposite.

The combined difference array is `[-2,2,3,2,-2]`. Prefix accumulation produces `[-2,0,3,5,3]`.

**Why update order does not matter.**

Each final position is the original zero plus the sum of all increments whose ranges cover it. Integer addition is associative and commutative, so applying update boundaries in a different order produces the same `d` values and the same prefix sums.

This allows the algorithm to postpone all actual array reconstruction until every update has been processed. The problem asks for only one final array, so there is no need to answer intermediate range queries.

**A useful invariant during accumulation.**

Just before output index `i` is emitted, the running prefix total equals the sum of all update increments that have begun but have not ended before `i`. A start mark activates an update at its inclusive left boundary. A stop mark at `r + 1` deactivates it immediately after its inclusive right boundary.

The invariant begins at zero before index zero and is preserved by adding `d[i]`, which contains exactly the activation and deactivation events scheduled for that position. It proves every emitted value is correct.

**The source starts from a zero array.**

Because the original `arr` is all zeros, the prefix sum of update differences is already the final value. If the original array contained arbitrary values, one could either add the reconstructed increments to it or first encode its own adjacent differences before applying range boundaries.

The method does not modify `updates`. It allocates `d` and returns a separate list produced by accumulation.

## Complexity detail

Let $n$ be `length` and let $q$ be the number of updates.

Each update performs one unconditional boundary addition and at most one boundary subtraction, both constant-time operations. Processing all updates takes $O(q)$ time. Prefix accumulation visits all $n$ difference entries once, and list construction stores all $n$ results, taking $O(n)$ time. Total time is $O(n+q)$.

The difference array uses $O(n)$ space. The returned list also contains $n$ values; while it is constructed, both `d` and the output coexist. Peak storage is therefore $O(n)$, matching the manifest. Apart from these arrays, the loop variables and accumulation running total use $O(1)$ space.

## Alternatives and edge cases

- **Apply every range directly:** Loop from `l` through `r` for each update. This is simple but takes $O(nq)$ time in the worst case when ranges are large.

- **One extra sentinel slot:** Allocate `length + 1` difference entries and always subtract at `r + 1`. This removes the boundary branch, after which only the first `length` prefix sums are returned.

- **Fenwick tree:** Supports interleaved range updates and point queries efficiently. It is unnecessary when every update arrives before one final full-array read.

- **Lazy segment tree:** Useful when range updates and range queries are mixed online, but substantially more complex than two boundary marks for this offline task.

- **No updates:** `d` remains all zeros, and accumulation returns the original zero-filled array.

- **Update covers the whole array:** Mark only `d[0] += c`; no stop boundary exists inside the result, so every prefix value includes `c`.

- **Single-index update:** For `[i, i, c]`, start at `i` and stop at `i + 1`, affecting exactly one output position.

- **Negative increments:** The same equations work. Starting a negative update subtracts from the running sum, and its stop marker adds the magnitude back.

- **Overlapping ranges:** Contributions add at each position; no special merging logic is required.

- **Multiple identical updates:** Every copy contributes its own boundary marks, so the final increment is multiplied by the number of occurrences.

- **Inclusive right endpoint:** The cancellation must occur at `r + 1`, never at `r`. This is the most common off-by-one trap.

- **Integer magnitude:** Python integers grow as needed. In fixed-width languages, choose a type that can hold the sum of up to `q` increments.

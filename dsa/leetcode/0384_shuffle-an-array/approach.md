## General

**Two pieces of state serve different purposes**

The object must support two behaviors that pull in opposite directions. `shuffle()` may rearrange the working array, while `reset()` must always recover the exact configuration supplied at construction.

The exact solution keeps:

- `self.nums`, the current working arrangement;
- `self.original`, a copied snapshot of the initial arrangement.

The constructor assigns `self.nums = nums` and creates the independent snapshot with `self.original = nums.copy()`. Copying is essential. If both names referred to the same list, every swap performed by `shuffle()` would also alter the supposed original, making a true reset impossible.

The current list is allowed to change repeatedly. The original snapshot must never be mutated by either operation.

**Reset creates a fresh working copy**

`reset()` executes `self.nums = self.original.copy()` and returns the new working list. It does not assign `self.nums = self.original` directly. A direct assignment would make later shuffles mutate the saved snapshot. Copying keeps the original protected while restoring all values and their order.

The cost of this protection is deliberate: reconstructing an $n$-element array requires copying $n$ values. The returned array represents the current configuration, while `self.original` remains the private baseline for future resets.

**Why repeatedly swapping with an arbitrary position is not enough**

A tempting shuffle is to visit every index and swap it with a random index chosen from the entire array. That looks random, but it does not generally make all permutations equally likely. It creates $n^n$ possible random-choice sequences, and those sequences do not divide evenly among the $n!$ permutations for most $n$.

The Fisher–Yates algorithm avoids this bias by shrinking the eligible random range. At iteration `i`, positions before `i` are already finalized. The method chooses `j` uniformly from `i` through `len(self.nums) - 1` and swaps positions `i` and `j`. It then moves to `i + 1`, never touching the finalized prefix again.

Conceptually, each iteration chooses which one of the still-unplaced elements should occupy the next output position. Swapping removes that chosen element from the unresolved suffix without needing a separate container.

**The loop invariant**

Immediately before iteration `i`:

- indices `0` through `i - 1` contain the first `i` finalized choices;
- indices `i` through `n - 1` contain exactly the elements not yet placed in the prefix;
- conditional on the already-fixed prefix, every ordering of the unresolved suffix remains equally possible.

The algorithm chooses one of the `n - i` unresolved positions with equal probability and moves its element to `i`. Since every remaining element occupies exactly one eligible position, each has probability $1/(n-i)$ of becoming the next finalized element. The swap places the displaced element back into the unresolved region, so the suffix still contains every not-yet-finalized element exactly once. This maintains the invariant for the next iteration.

At the last index, the random range contains only that index. The self-swap does nothing, but it completes the same uniform process without needing a special case.

**Why swapping an element with itself must be allowed**

`random.randrange(i, len(self.nums))` includes `i`. Selecting `j = i` means the element already at position `i` is chosen for that final position.

Excluding `i` would forbid that legitimate choice. For a two-element array, always forcing the first element to swap with the second would always reverse the array and would never return the original ordering. Allowing a self-swap gives the unchanged and reversed permutations equal probability $1/2$.

More generally, at every iteration all remaining elements—including the one currently at `i`—must have the same chance to occupy position `i`. The inclusive lower endpoint is therefore part of the correctness argument, not merely an implementation convenience.

**A complete three-element trace**

Start with `[1, 2, 3]`.

At `i = 0`, `j` is chosen uniformly from `{0, 1, 2}`:

- choosing `0` keeps `1` first;
- choosing `1` places `2` first;
- choosing `2` places `3` first.

Each first element has probability $1/3$. Suppose `j = 2`, leaving `[3, 2, 1]`.

At `i = 1`, `j` is chosen uniformly from `{1, 2}`. The remaining values are `2` and `1`, so each has probability $1/2$ of taking the second position. The final position then receives the only remaining value.

The two possible outcomes under the already-chosen first value `3` are `[3, 2, 1]` and `[3, 1, 2]`, each with probability

$$
\frac{1}{3}\cdot\frac{1}{2}=\frac{1}{6}.
$$

Repeating the same reasoning for first values `1` and `2` accounts for all six permutations, each with probability $1/6$.

**Why all permutations are equally likely**

For any particular target permutation, there is exactly one required sequence of choices:

- at position `0`, choose the location containing the target’s first value;
- at position `1`, choose the location containing its second value among the remaining suffix;
- continue until the final position is forced.

The probability of this exact choice sequence is

$$
\frac{1}{n}
\cdot \frac{1}{n-1}
\cdot \frac{1}{n-2}
\cdots
\frac{1}{1}
= \frac{1}{n!}.
$$

Every permutation has one such sequence and therefore the same probability. The choices also cover all $n!$ permutations, so no ordering is missing.

This proof does not require the starting arrangement to be the original order. It works from any arrangement containing the same distinct elements. Consequently, calling `shuffle()` several times without `reset()` still produces a uniform permutation on every call: Fisher–Yates uniformly permutes whatever current ordering it receives, and the set of possible resulting arrangements is unchanged.

**Why in-place swapping is efficient**

A conceptual “draw from a bag without replacement” algorithm could copy all elements, choose and remove a random one for each output position, and build a new array. Removing an arbitrary list entry shifts later entries and can make the process quadratic.

Fisher–Yates simulates removal without physically shrinking the list. Once a chosen element is swapped into the finalized prefix, future random ranges exclude that prefix. The chosen element is therefore logically removed from the pool in constant time, while the unresolved elements remain packed in the suffix.

**State behavior across operations**

After construction, `original` is a protected copy of the input order and `nums` is the working arrangement. A `shuffle()` mutates and returns `nums`. A later `shuffle()` starts from that current arrangement but is still uniform. A `reset()` replaces `nums` with a new copy of `original`, restoring the precise initial order. Further shuffles mutate that new working copy, not the snapshot.

The returned random arrangement in the example is only one possible result. A correct test cannot demand a particular shuffle; it should verify that the output is a permutation and that the random process is unbiased across repeated trials.

## Complexity detail

Let $n$ be the array length.

The constructor copies `nums` once, taking $O(n)$ time. `reset()` also copies all $n$ elements, so it takes $O(n)$ time. `shuffle()` performs exactly $n$ iterations, each with one random-index generation and one constant-time swap, for $O(n)$ time.

The saved original copy requires $O(n)$ persistent auxiliary space. The current array is part of the object’s required state; the constructor initially retains the supplied list, and resets create a working copy. At a high level, the object stores two $n$-element configurations, so its storage is $O(n)$.

Within `shuffle()` itself, only indices `i` and `j` are additional, and swaps occur in place, so the shuffle operation uses $O(1)$ incremental auxiliary space beyond the object’s stored arrays. `reset()` temporarily allocates the new $O(n)$ working copy. The overall class space bound remains $O(n)$, as recorded in the variant manifest.

## Alternatives and edge cases

- **Draw and delete from an auxiliary list:** Repeatedly choose a random remaining element and remove it. This mirrors sampling without replacement but Python middle deletion costs linear time, producing $O(n^2)$ shuffle time and another $O(n)$ temporary list. Fisher–Yates performs logical removal by shrinking the eligible suffix.

- **Swap with a random index from the entire array:** Reusing the full range at every iteration is generally biased because different final permutations can be reached by different numbers of random-choice sequences. The lower bound must advance with `i`.

- **Assign random keys and sort:** Giving every element a random key and sorting by those keys costs $O(n\log n)$ and requires careful handling of key collisions. Fisher–Yates is linear and has a direct uniformity proof.

- **Omitting self-swaps:** Choosing only indices strictly after `i` excludes valid outcomes and creates severe bias. The current index must be part of the random range.

- **Single-element array:** Every random range contains only index `0`. The self-swap preserves the sole possible permutation, and `reset()` returns the same one-element configuration.

- **Distinct-elements guarantee:** Uniqueness lets the statement speak of $n!$ visibly different value permutations. Fisher–Yates also works on arrays with duplicates, but several index permutations would look identical; equality of visible arrays would then require discussing multiplicities rather than $n!$ distinct outputs.

- **Negative and large values:** Values are moved but never used as indices or arithmetic operands. Their sign and magnitude have no effect on the algorithm.

- **Repeated `shuffle` calls:** A reset is not required between shuffles. Uniformly permuting any current arrangement gives a uniform result over the same set of permutations.

- **Repeated `reset` calls:** Each call creates another faithful working copy of `original`; the visible result is unchanged and future shuffles still cannot damage the snapshot.

- **Input aliasing:** The constructor assigns the supplied list directly to `self.nums`, so the first shuffle mutates that caller-provided list. The original snapshot remains safe. A more defensive constructor could copy both fields, but the exact source relies on the platform’s ownership convention.

- **Returned-list aliasing:** Both methods return the internal working list. External mutation of that returned object could change later shuffle behavior. LeetCode’s operation model observes returned values without adversarially mutating the internal list; a public production API might return a copy instead.

- **Pseudorandom generator quality:** Fisher–Yates is mathematically uniform when each `randrange` outcome is uniform and independent enough for the model. The algorithm cannot compensate for a biased random-number generator; standard library randomness is assumed by the problem.

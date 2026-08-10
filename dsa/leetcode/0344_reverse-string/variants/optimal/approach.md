## General

**Reversal pairs each position with one mirrored position.**

For an array of length $n$, the character originally at index $p$ belongs at index

$$
n-1-p
$$

in the reversed array. This mapping is symmetric: the character at `n - 1 - p` belongs at `p`. Therefore reversal can be performed by swapping mirrored pairs rather than creating a second array.

The exact source keeps two indices:

- `i = 0`, initially pointing at the first character;
- `j = len(s) - 1`, initially pointing at the last character.

At every iteration, `i` and `j` identify a mirrored pair that has not yet been placed. Swapping `s[i]` and `s[j]` sends both characters directly to their final reversed positions. The pointers then move inward with `i + 1` and `j - 1`.

**Why the swap is safe in Python.**

The assignment

`s[i], s[j] = s[j], s[i]`

evaluates the right-hand values before writing the left-hand positions. Conceptually, it remembers both old characters and then places them in opposite slots. The first write cannot destroy the value needed by the second write.

In a language without tuple assignment, the same operation would use one temporary character:

1. save the left character;
2. copy the right character into the left position;
3. copy the saved character into the right position.

That temporary is constant-sized, so either form remains an in-place, $O(1)$-auxiliary-space algorithm.

**The key loop invariant.**

Before each loop-condition check:

- every position strictly before `i` already contains its final reversed character;
- every position strictly after `j` already contains its final reversed character;
- positions from `i` through `j` are the only part still needing work.

Initially, there are no positions before zero and no positions after `n - 1`, so the invariant is true.

During an iteration, index `i` is mirrored with `j`. At the first iteration, these are `0` and `n - 1`. After both pointers have moved the same number of steps inward, they remain mirrored because

$$
j=n-1-i.
$$

The swap puts both boundary characters of the unresolved interval into their final positions. Incrementing `i` and decrementing `j` then moves those positions into the already-correct outer regions, preserving the invariant.

**Why the loop uses `i < j`.**

When `i < j`, two different unresolved positions remain, so they must be swapped. When `i == j`, an odd-length array has reached its middle character. That character's mirrored index is itself, so it is already in the correct reversed position and does not need a self-swap.

When `i > j`, all mirrored pairs have been processed. This occurs immediately after the final pair in an even-length array, or after the pointers pass the untouched middle in an odd-length array.

Using `i <= j` would still produce the same values, but it would perform an unnecessary middle self-swap for odd lengths. The strict condition expresses the actual work precisely.

**Walk through `['h','e','l','l','o']`.**

The pointers begin at indices zero and four.

- Swap `h` and `o`, producing `['o','e','l','l','h']`; move to `i = 1`, `j = 3`.
- Swap `e` and the right-side `l`, producing `['o','l','l','e','h']`; move to `i = 2`, `j = 2`.
- The pointers meet at the middle `l`, so the loop stops.

The middle element remains where it belongs, and all outer pairs have been reversed.

For an even-length input such as `['a','b','c','d']`, the swaps are indices `(0,3)` and `(1,2)`. The pointers then cross, leaving `['d','c','b','a']`.

**Why every character is placed correctly.**

At iteration $t$, the left pointer is $t$ and the right pointer is $n-1-t$. The swap moves the original character from index $t$ to its required reversed index $n-1-t$, and it moves the original right character back to index $t$.

No processed index is visited again because both pointers move strictly inward. Every index belongs to exactly one mirrored pair, except an odd-length middle index, which maps to itself. Thus no character is lost, duplicated, or left in an incorrect position.

When the loop ends, the invariant says all positions outside the unresolved interval are correct, and the unresolved interval contains either zero positions or one self-mirrored position. Therefore the entire array is reversed.

**Mutation satisfies the return contract.**

The function intentionally has no `return` statement. It changes the elements of the same list object that the caller supplied. Any reference to that list observes the reversed order after the call.

Creating and returning a different reversed list would not satisfy this mutation requirement, even if its characters were numerically correct. The two-pointer swaps preserve the identity and length of `s`.

## Complexity detail

Let $n$ be `len(s)`. Each iteration finalizes two positions, so the loop performs $\lfloor n/2\rfloor$ swaps. Each swap and pointer update is constant time. Total time complexity is $O(n)$.

The source uses only two indices and the constant-sized temporary behavior of tuple assignment. It allocates no array proportional to the input and uses no recursion, so auxiliary space is $O(1)$.

The input array itself is required storage and is modified in place; it is not auxiliary memory.

## Alternatives and edge cases

- **Create a reversed copy:** Slicing with `s[::-1]` or building a new list is concise, but a standalone copy uses $O(n)$ extra memory. Assigning a slice back may also allocate temporary storage and therefore misses the strict $O(1)$ requirement.

- **Built-in in-place reverse:** A library method such as `s.reverse()` typically performs the same mirrored swaps and can satisfy the contract, but the explicit source makes the two-pointer reasoning visible.

- **Recursive mirrored swaps:** Swap the ends and recurse inward. It mutates the list in place but consumes $O(n)$ call-stack space, violating the constant-extra-memory requirement.

- **One character:** `i` and `j` both equal zero, the loop skips, and the single character remains correctly unchanged.

- **Two characters:** Exactly one swap occurs, after which the pointers cross.

- **Odd length:** The unique center character maps to itself and is intentionally left untouched when the pointers meet.

- **Even length:** Every position belongs to a two-element mirrored pair, and the pointers cross after the final swap.

- **Repeated characters:** Equal values may be swapped or left visually unchanged, but their positions are still processed correctly. Reversal depends on indices, not value uniqueness.

- **Printable characters:** The algorithm never interprets character content. Letters, digits, punctuation, and spaces are all moved identically.

## General

**Read indices as destinations**

The contract says the character currently at position `i` must move to position `indices[i]`. This is a destination mapping, not a list of source positions to read in result order.

The stored solution allocates `ans = [None] * len(s)`, giving one output slot for every character. It then iterates with `zip(s, indices)`. Each pair contains current character `c` and that character's destination `j`, so `ans[j] = c` places it directly where it belongs.

After every character has been placed, `"".join(ans)` converts the list of one-character strings into the returned string.

**Why a list is necessary in Python**

Python strings are immutable. Assigning directly to a position of `s` is not allowed. A list provides mutable slots during reconstruction, and joining once is efficient.

Initializing with `None` is safe because the permutation guarantee ensures every slot is overwritten with a string before `join`. If the indices were malformed, an unfilled `None` would cause joining to fail, which would expose the violated contract rather than silently inventing a character.

**The permutation guarantee**

Every `indices[i]` lies from zero through `n-1`, so no assignment is out of bounds. All index values are unique and there are exactly `n` of them. Therefore, they form a permutation of every valid output position.

Uniqueness means two characters never compete for the same slot. Having `n` distinct destinations within an `n`-element range also means no output slot is omitted.

This is the central reason direct placement works without collision handling.

**A trace for codeleet**

The first character `c` is paired with destination four, so output slot four receives `c`. The next character `o` goes to five, and so on. The character `l` from input position four goes to output position zero.

After all eight assignments, the slots read left to right as `l`, `e`, `e`, `t`, `c`, `o`, `d`, `e`. Joining produces `leetcode`.

For identity indices zero, one, two, and so on, each character is written back to the same position, so the result equals the input.

**A useful invariant**

After processing the first `t` pairs from `zip`:

- For every processed input position `i<t`, output slot `indices[i]` contains `s[i]`.
- No unprocessed character has written into any of those slots.

The invariant holds before the loop. One new assignment writes the correct character to its valid unique destination, and uniqueness prevents it from overwriting a processed result. After all `n` pairs, every destination is correct.

**Why reversing the mapping would be wrong**

A tempting expression is to read `s[indices[i]]` as output character `i`. That interprets `indices` as a source mapping. The contract gives the inverse direction: source `i` names destination `indices[i]`.

The direct assignment follows the statement literally and does not need to construct the inverse permutation.

**How zip depends on equal lengths**

`zip` stops when the shorter input is exhausted. The guaranteed equality `len(s) == len(indices)` ensures all characters and all destinations are processed. Without that guarantee, direct indexing with an explicit range could make a mismatch more visible.

**Repeated characters**

Characters in `s` need not be unique. Their identity is their source position, not their value. Two equal letters can move to different destinations without ambiguity, because the loop processes occurrences separately.

This also explains why no character-frequency bookkeeping is useful here. The task is not to determine which letters exist; it is to preserve every occurrence while changing its position according to the paired index.

## Complexity detail

Let $N$ be string length. Creating the result list takes $O(N)$ time. The loop performs $N$ constant-time assignments, and joining copies $N$ characters into the final string. Total time is $O(N)$.

The mutable list has $N$ slots, and the returned immutable string has $N$ characters. Auxiliary reconstruction space is $O(N)$, matching the manifest. The small `zip` iterator and loop variables use constant additional state.

No sorting is needed. Sorting source-destination pairs would add $O(N\log N)$ time to solve a problem that direct addressing handles linearly.

## Alternatives and edge cases

- **Sort by destination:** Zip each character with its index, sort pairs, and join characters. It is correct but unnecessarily costs $O(N\log N)$.
- **Build the inverse permutation:** First record which source belongs to each destination, then read the string. It adds an extra pass without improving bounds.
- **Identity permutation:** Every assignment writes to the same position and returns the original string.
- **Single character:** Its only valid destination is zero.
- **Repeated letters:** Each occurrence is placed according to its own paired destination.
- **Destination zero or n minus one:** Both endpoints are ordinary valid list indices.
- **Malformed duplicate destination:** It would overwrite a slot and leave another unfilled, but uniqueness excludes this case.
- **Unequal input lengths:** `zip` would truncate, but equal lengths are guaranteed.
- **String immutability:** The list is required for indexed writes; repeated string concatenation would be less efficient.
- **Required type import:** `List` must be available for the annotation in a standalone module.

## General

Maintain `target_index`, the position of the next character required from `str2`, and scan `str1` from left to right. A source character can represent the next target character in exactly two ways: leave it unchanged, or increment it by one cyclic step. The cyclic successor calculation makes `z` match `a` as well as making each other letter match its ordinary successor.

Whenever either choice matches `str2[target_index]`, use the current source position and advance `target_index`. Otherwise skip that source character. Return `true` once every target character has been matched; if the scan ends first, return `false`.

**Why the earliest feasible match is safe**

Suppose the next required target character could be matched by the current source position and also by a later one. Choosing the current position leaves every later source position available, whereas choosing the later position discards at least the same prefix. The earlier choice therefore cannot remove an option needed by the unmatched target suffix. Repeating this exchange argument shows that if any valid ordered selection exists, the greedy scan finds one.

Each accepted source position is strictly later than the previous accepted position, so the matched characters preserve order and form a subsequence. The match test also guarantees that every accepted character is either unchanged or incremented exactly once, which is precisely the allowed operation. If unmatched target characters remain after the final source position, no alternative earlier choices could have left more source characters available, so no valid construction exists.

## Complexity detail

Let $n = \lvert\texttt{str1}\rvert$. Each character of `str1` is inspected at most once, and `target_index` only advances, so the time complexity is $O(n)$. The scan stores only the target index and the current cyclic successor, using $O(1)$ auxiliary space.

The benchmark keeps `str1` twice as long as `str2` and forces the scan to skip alternating characters. This linear traversal is contrasted with a correct dynamic-programming subsequence formulation whose table grows with the product of the two string lengths.

## Alternatives and edge cases

- **Dynamic programming over both strings:** A subsequence reachability table is correct, but it uses $O(\lvert\texttt{str1}\rvert\lvert\texttt{str2}\rvert)$ time for a decision whose greedy choices never need revision.
- **Recursive include-or-skip search:** Exploring both choices can reproduce the contract, but without careful memoization it repeats states exponentially; even memoized, it retains the unnecessary product-state bound.
- **Cyclic wrap:** `z` can increment to `a`; a comparison that only checks adjacent character codes misses this case.
- **At most one operation:** Any set of indices may be chosen together, but each selected position advances exactly once. A source letter cannot jump two or more alphabet steps.
- **Target longer than source:** A subsequence needs one distinct source position per target character, so this case is immediately impossible.
- **Repeated letters:** Every repeated target character must consume a different, later source position.
- **Unchanged letters:** The selected index set may omit any position, and the entire operation may be skipped when `str2` is already a subsequence.

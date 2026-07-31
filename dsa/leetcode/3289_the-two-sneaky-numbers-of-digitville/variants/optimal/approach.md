## General

Maintain a set of values already encountered. When the scan reaches a value for the first time, add it to the set. When the value is already present, append it to the answer instead.

Every value normally occurs exactly once, so only the two sneaky numbers can trigger the already-seen branch. Each of those numbers occurs exactly twice, so each is appended exactly once. The answer therefore contains precisely the required two values after the scan finishes.

## Complexity detail

Let $n$ be the size of the intended range; `nums` contains $n+2$ elements. The single scan takes $O(n)$ expected time under standard hash-set behavior. The set can hold all $n$ distinct values, so it uses $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Frequency array:** An array of $n$ counters also gives $O(n)$ time and space, but stores more state than the membership test needs.
- **Algebraic recovery:** Sums and sums of squares can determine the two duplicates with constant extra space, but the derivation is less direct and fixed-width implementations must avoid overflow.
- **In-place marking:** Mutating `nums` can encode visits with constant extra space, but it complicates handling the value zero and unnecessarily changes the caller's input.
- **Adjacent duplicates:** The second copy is recognized immediately even when it follows the first copy directly.
- **Return order:** The problem permits either order; this implementation returns duplicates in the order their second occurrences are encountered.

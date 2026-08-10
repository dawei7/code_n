## General

**Measure how far each letter is from `a`**

An operation advances every occurrence of one currently chosen letter by one position in the circular alphabet:

`a -> b -> c -> ... -> z -> a`.

For a non-`a` letter with zero-based alphabet index

`index = ord(c) - ord('a')`,

the number of forward steps needed to reach `a` is

`26 - index`.

Examples:

- `z` needs one step.
- `y` needs two.
- `b` needs 25.

The source writes `ord(c) - 97` because 97 is the code point of lowercase `a`.

**One operation moves a whole current letter group**

All equal letters are transformed together. Once two original groups become the same letter, they merge permanently: future operations on that letter advance both groups at once.

This merging is why the answer is not the sum of individual distances. For `"yz"`, `y` first advances to `z`, merging with the existing `z`. One shared `z -> a` operation then finishes both groups, for two operations rather than three.

**The farthest non-`a` letter supplies a lower bound**

Choose a present non-`a` character with maximum circular distance `D` to `a`.

Every occurrence in that group must advance through `D` alphabet transitions before it can become `a`. One operation can advance its current group by at most one transition. Even after it merges with other groups, it still cannot skip a letter.

Therefore any valid strategy needs at least `D` operations.

**The same bound is achievable**

Let the farthest group be the alphabetically smallest present non-`a` letter. Advance its current letter repeatedly toward `a`.

As it moves forward, it encounters every later letter on the alphabetic path. Whenever an existing group has that letter, the moving group merges with it. Subsequent operations advance the combined group together.

By the time the original farthest group completes its `D` steps and wraps from `z` to `a`, every other non-`a` group has been encountered and absorbed because its own distance was no larger.

Existing `a` characters never need to move. The final wrap merges the traveling group into them.

Thus `D` operations are sufficient. Combined with the lower bound, the minimum is exactly the maximum distance among present non-`a` letters.

**Why `a` is excluded from the generator**

Letter `a` already satisfies the target and needs zero operations. Plugging its index zero into `26 - index` would incorrectly produce 26 rather than zero, because the formula describes a positive wraparound distance for letters that still need movement.

The source filters with `if c != "a"`. If every character is `a`, the generator is empty and `max(..., default=0)` returns zero.

**Trace the first example**

For `"yz"`, distances are two for `y` and one for `z`. Their maximum is two.

Advance `y -> z`, producing `"zz"`. Then advance `z -> a`, producing `"aa"`. The two-step lower bound is attained.

**Trace multiple separated letters**

Suppose the string contains `b`, `m`, and `z`. Their distances are 25, 14, and one. Advancing the `b` group forward eventually reaches `m` and absorbs that group, then reaches `z` and absorbs it, and finally wraps to `a`. The full process takes 25 operations, not 40.

The positions and multiplicities of letters do not matter because an operation affects every occurrence of the chosen current character globally.

**How the source computes the maximum**

The generator scans all characters, skips `a`, and yields each circular distance. `max` retains the largest.

Repeated occurrences yield the same distance repeatedly. Deduplicating with a set is unnecessary; duplicates do not change a maximum, and avoiding a set preserves constant auxiliary space.

## Complexity detail

Let `n` be the string length. The generator examines every character once, with constant-time code-point arithmetic. Time complexity is `O(n)`.

The generator is lazy and `max` stores only the current best value. Auxiliary space is `O(1)`.

The string itself is immutable and is not transformed or copied by the source. The proof constructs a possible operation sequence, but the method only returns its minimum length.

## Alternatives and edge cases

- **Simulate all operations:** It can reproduce a witness sequence but may repeatedly scan or rebuild the string. The maximum-distance formula is sufficient.
- **Sum distances of distinct letters:** It overcounts because groups merge and share later operations.
- **Use the minimum distance:** The farthest group still needs more transitions and sets the lower bound.
- **Include `a` in `26 - index`:** This assigns a false distance of 26 to an already finished character.
- **All characters are `a`:** The generator is empty and the default answer is zero.
- **Only `z` appears:** One global `z -> a` operation finishes the string.
- **Only one non-`a` letter with many copies:** All copies move together, so multiplicity does not increase the answer.
- **Several letters merge:** Once equal, one future operation advances every merged occurrence.
- **Letter `b` present:** Its distance 25 is the maximum possible nonzero answer.
- **Order of characters in the string:** It has no effect because operations select values globally, not positions.
- **Circular alphabet:** The final `z -> a` step is essential; without circularity, transformation would be impossible for non-`a` letters.
- **Input preservation:** The method reads `s` and returns a count without constructing the transformed string.

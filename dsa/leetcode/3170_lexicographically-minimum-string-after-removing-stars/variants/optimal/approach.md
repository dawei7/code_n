## General

**Store available positions by character**

While scanning left to right, dictionary `g` maps each lowercase letter to a stack of positions seen and not yet deleted.

When ordinary character `c` appears at index `i`, `g[c].append(i)` makes it available to a future star.

When a star appears, it and one earlier smallest character must be removed. Array `rem` marks deleted indices without physically changing the string.

**Choose the smallest letter, then its rightmost occurrence**

The loop over `ascii_lowercase` visits letters from `'a'` upward. The first bucket with an available position is therefore the smallest legal character.

If that smallest character occurs several times, the code uses `g[a].pop()`, deleting its rightmost available occurrence.

Why rightmost? All tied candidates contain the same character. Keeping an earlier occurrence preserves that small character at an earlier output position. Deleting an earlier copy would shift intervening, lexicographically no-smaller content left sooner. Therefore, deleting the rightmost tied copy produces the smallest final string.

For `"aaba*"`, all three `a` values are smallest. Removing the rightmost at index 3 leaves `"aab"`, smaller than alternatives such as `"aba"`.

**Process stars in their forced order**

The operation always deletes the leftmost remaining star. A left-to-right scan encounters stars in exactly that order.

At a star, `g` contains precisely undeleted non-star characters to its left. Characters to the right have not been scanned and are not incorrectly eligible.

After selecting a position, popping removes it from future consideration. Marking the star itself ensures neither appears in final construction.


At each star, alphabetical scanning chooses the required smallest available character. Among identical smallest choices, deleting the rightmost is locally lexicographically optimal while leaving the same multiset of available characters for later stars except for one identical copy.

This tie choice cannot harm future feasibility or character categories because identical copies are interchangeable for later smallest-letter requirements; only their positions affect lexicographic output, and retaining earlier positions is best.

Inductively, every processed star follows an optimal choice given the forced earlier operations. The input guarantee ensures some character exists to delete, so the inner loop always finds a bucket.

After scanning, the final generator emits exactly indices not marked in `rem`, preserving original relative order. All stars and their paired letters are absent, and the result is lexicographically minimum.

**Why deletion is deferred**

Removing characters from an immutable string during scanning would shift indices and cost repeated copying. Boolean marks keep original positions stable. Position stacks can therefore reference indices safely until final filtering.

**A more precise tie argument**

Suppose equal smallest characters occur at positions $p<q$ before the current star. Compare deleting $p$ with deleting $q$, while making identical later choices whenever possible. Before $p$, outputs agree. At the first place they can differ, the version deleting $q$ still contains the smallest character from $p$, while the version deleting $p$ exposes some later character. That exposed character is either the same—postponing the first difference—or larger, making deletion of $q$ lexicographically better. Repeating this exchange moves any optimal tied deletion to the rightmost occurrence without worsening the result.

Because the removed copies have identical values, this exchange does not change which character frequencies remain available to later stars. It changes only positions, in the favorable direction of preserving earlier small letters.

**Stacks remain valid despite marked stars**

Only ordinary-character positions are pushed. When a position is popped, it is immediately marked and permanently removed from its bucket. Therefore, bucket tops are always currently available occurrences; no lazy cleanup loop is needed.

The final scan consults `rem` for both character and star indices. It never emits a deleted position even though the original string itself was untouched.

**Alphabet bound**

Each star scans at most 26 buckets. Since this is a fixed lowercase alphabet, that is constant time per star. A larger or dynamic alphabet would need a heap or ordered set to retain linear-logarithmic efficiency.

## Complexity detail

Let $n$ be string length.

Each ordinary character is pushed once and popped at most once. Every star checks at most 26 letters. With fixed alphabet, time is $O(n)$.

The position lists collectively store at most $n$ indices, and `rem` has length $n$, so auxiliary space is $O(n)$. Final output also uses $O(n)$ space.

The manifest's $O(n)$ time and space match the exact implementation.

Dictionary access is expected constant time; the dominant fixed 26 scan is deterministic.

## Alternatives and edge cases

- **Min-heap of letters and positions:** It can select a smallest character, but enforcing rightmost position among equal letters needs careful heap keys and lazy deletion.
- **26 stacks plus active bit mask:** A bit mask can find the smallest nonempty bucket faster in constant bit operations.
- **Physically erase characters:** Repeated string or list deletion can become quadratic and invalidates stored positions.
- **No stars:** Nothing is marked, so original string is returned.
- **Several equal smallest letters:** The rightmost available one must be deleted for lexicographic minimality.
- **Different available letters:** The alphabet loop always chooses the smallest, as the operation requires.
- **Consecutive stars:** Each consumes one remaining earlier character; popped positions cannot be reused.
- **Star at beginning:** Excluded by the feasibility guarantee unless prior deletions semantics somehow supply a character, which they cannot.
- **All earlier characters deleted:** The guarantee prevents a star from encountering that state.
- **Original order:** Unremoved characters retain their relative positions during final join.
- **Star markers:** Every star's own index is always marked before selecting its paired character.
- **Fixed lowercase alphabet:** It justifies treating 26-bucket scanning as $O(1)$.

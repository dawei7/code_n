## General

**Fix one anchor and count directions**

For a fixed point `start`, every other point on the same line as `start` has the same slope relative to it. The competitive solution counts how many later points produce each slope.

For each anchor index `i`, only points with index greater than `i` are examined. `slope_count[slope]` counts distinct later points on that direction, while `same` counts the anchor plus exact duplicate coordinates.

The current Reference guarantees unique coordinates, so `same` remains one. The duplicate branch is retained for compatibility with older versions of the problem.

**Represent ordinary and vertical slopes**

For different points with unequal x-coordinates, slope is computed as:

`(start.y - end.y) * 1.0 / (start.x - end.x)`

Reversing both differences from the more common `end - start` form does not change the ratio. Points on opposite sides of the anchor on one line also produce the same slope because both numerator and denominator change sign together.

When x-coordinates match, division would be undefined. The source uses `float("inf")` as one common key for every vertical direction.

Horizontal slopes may appear as positive or negative zero depending on difference signs, but Python treats `0.0` and `-0.0` as equal dictionary keys.

**Why one slope bucket plus the anchor gives a line count**

Every point placed in a slope bucket lies on the line through `start` having that slope. Conversely, every nonduplicate point on that line produces the same slope and enters the bucket.

The bucket count omits the anchor itself, so the code adds `same`. Under unique input, that is simply one.

If duplicates were allowed, an identical point has no defined direction but lies on every line through the anchor. Adding `same` to each bucket correctly includes those duplicates. If no slope bucket exists, `current_max = same` still covers a group consisting only of duplicates.

**Why considering only later points is enough**

An anchor does not count points with smaller input indices. As with many pair-enumeration algorithms, choose the smallest-index point on a maximum line as the anchor. Every other point on that line is later, so its slope bucket contains the full remaining group.

Other anchors may produce partial counts, but taking the global maximum preserves the complete count found at the earliest anchor.

The algorithm initializes `max_points` to zero. With the guaranteed nonempty input, each anchor makes `current_max` at least one, so the final answer is at least one.

**Floating precision under the stated bounds**

Using reduced integer pairs is generally more robust than using a float. For this specific domain, coordinate differences are bounded in magnitude by $2\cdot10^4$. Two distinct rational slopes with such denominators are separated by much more than ordinary double-precision spacing across the allowed range, so the representation is practically safe under the Reference constraints.

The conceptual risk remains if coordinate bounds grow substantially: different exact rational slopes could round to the same floating value. A normalized `(dy, dx)` integer key avoids that dependency altogether.

**Current interface mismatch**

The source expects each point to be a `Point` object and reads `.x` and `.y`. The current Reference supplies each point as a two-element list `[x, y]`.

Passing the current contract directly to this source would raise `AttributeError`. The quadratic algorithm is correct for its declared legacy `Point` interface, but adapting it requires indexing coordinates or converting input arrays into `Point` objects.

The module-level `Point` class is legacy harness structure, not part of the current list-of-lists method signature.

## Complexity detail

Let $n$ be the number of points.

For each anchor, the inner loop considers at most $n-i-1$ points. Summed over anchors, this is $O(n^2)$ slope calculations and expected constant-time dictionary updates. Scanning `slope_count` for `current_max` adds at most another $O(n)$ work per anchor, so total expected time remains $O(n^2)$.

The largest slope map for one anchor holds at most $n-1$ keys. It is discarded before the next anchor, giving $O(n)$ auxiliary space. These bounds match the manifest.

Arithmetic on bounded floats and coordinates is treated as constant time.

## Alternatives and edge cases

- **Normalized `(dy, dx)` key:** Divide both differences by `gcd(abs(dy), abs(dx))` and standardize sign. It retains $O(n^2)$ time and eliminates float rounding concerns.
- **Cross-product triple enumeration:** Test every third point against every defining pair. It uses $O(1)$ space but costs $O(n^3)$ time.
- **Global normalized line equation:** Count canonical `(A, B, C)` lines. It requires careful normalization and duplicate-pair handling.
- **One point:** Its anchor has no slopes, `current_max` is one, and one is returned.
- **Vertical points:** All use the infinity bucket.
- **Horizontal points:** Signed zeros compare as the same key in Python.
- **Opposite directions:** Equal line slope is preserved because numerator and denominator signs flip together.
- **Duplicate coordinates:** The legacy `same` logic supports them even though the current constraints exclude them.
- **Interface mismatch:** Replace `start.x`/`start.y` and `end.x`/`end.y` with list indexing for the current Reference input.
- **Larger coordinate domains:** Prefer normalized integer directions if floating slopes could collide.
- **Empty input outside the contract:** The source returns zero, while the valid domain begins at one point.

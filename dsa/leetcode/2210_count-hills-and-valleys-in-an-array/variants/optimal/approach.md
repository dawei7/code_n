## General

**Evaluate one representative per plateau**

Keep `previous` as the closest distinct value to the left of the current plateau. Scan adjacent pairs `current, following`. When they are equal, the plateau continues, so defer all work. When they differ, `current` is the plateau's final occurrence and `following` is its closest distinct value on the right.

At that boundary, count one feature exactly when `current` is strictly greater than both distinct neighbors or strictly less than both. Then assign `current` to `previous` before processing the next plateau.

Every qualifying plateau has a unique final index where this comparison occurs. The stored left value and immediate differing right value are precisely the closest non-equal neighbors required by the definition. Thus every hill or valley is counted once, continued plateaus are never duplicated, and endpoint plateaus are excluded because one required neighbor is missing.

## Complexity detail

Let $n$ be the length of `nums`. The scan visits each adjacent position once and performs constant work, so it takes $O(n)$ time.

Only the previous distinct value and the feature counter are retained, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Explicit compression:** Building an array with consecutive duplicates removed and checking its interior triples is clear and still $O(n)$ time, but uses $O(n)$ extra space.
- **Search outward at every index:** Repeatedly scanning across equal neighbors can take $O(n^2)$ time and must still avoid counting one plateau repeatedly.
- **Monotone sequence:** A wholly increasing or decreasing compressed sequence contains no hill or valley.
- **Endpoint plateau:** Equal values at either end lack a non-equal neighbor on one side and cannot form a feature there.
- **Long plateau:** Any number of adjacent equal values contributes at most one hill or valley.
- **Strict comparisons:** A feature is recognized only after equal neighbors have been skipped; the two remaining comparisons must both be strict.

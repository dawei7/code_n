## General

Every query asks for the nearest occurrence of one of only three colors. Answering a query by scanning the array outward could take linear time, and repeating that for up to $5\cdot10^4$ queries could become quadratic. The Optimal solution instead preprocesses, for every array position and every color, the nearest matching index on the left and the nearest matching index on the right. Each query can then compare two candidate distances in constant time.

**Nearest occurrence at or to the right**

The table `right` has `n + 1` rows and three columns. Color value one uses column zero, color two uses column one, and color three uses column two. Every entry starts as positive infinity. The extra row `right[n]` represents the empty suffix after the array; no color occurs there.

The code scans `i` from `n - 1` down to zero. It first copies all three values from `right[i + 1]` into `right[i]`. Those values are the nearest known occurrences in the suffix starting one position later. Then it executes

`right[i][colors[i] - 1] = i`.

For the color actually present at index `i`, the nearest occurrence at or to the right is now `i` itself, which is closer than every later index. The other two columns retain their nearest later positions. After this update, `right[i][c - 1]` is the smallest index at least `i` whose color is `c`, or positive infinity if none exists.

**Nearest occurrence at or to the left**

The `left` table also has `n + 1` rows and three columns, but it starts with negative infinity. Row zero represents the empty prefix before the array.

The loop uses `enumerate(colors, 1)`, so its table-row variable starts at one while `c` is the original color at array index `i - 1`. It copies `left[i - 1]` and then sets

`left[i][c - 1] = i - 1`.

Consequently, row `left[i]` describes the prefix containing original positions zero through `i - 1`. Its color entry is the greatest matching index in that prefix, or negative infinity if the color has not appeared.

This one-position shift is why a query at original index `i` reads `left[i + 1]`. That row includes positions through `i` itself. If `colors[i]` equals the requested color, both a left-side and right-side candidate can be index `i`, correctly producing distance zero.

**Answering a query from two candidates**

For query `[i, c]`, the nearest matching occurrence must fall into one of two categories: its index is at most `i`, or its index is at least `i`. The closest match in the first category is the largest matching index on the left, and the closest in the second category is the smallest matching index on the right. The code computes

`i - left[i + 1][c - 1]`

and

`right[i][c - 1] - i`,

then takes their minimum. A farther occurrence on the same side cannot improve the answer, so no other candidate needs to be inspected.

Infinity values make missing-side handling uniform. If no requested color exists on the left, subtracting negative infinity gives positive infinity. If none exists on the right, positive infinity minus `i` remains positive infinity. If one real side exists, the minimum chooses its finite distance. If neither side exists, `d` is infinite.

The code appends `-1 if d > n else d`. Any real distance between two valid array positions is at most `n - 1` and therefore never exceeds `n`. Only the infinity sentinel passes the `d > n` test, so `-1` is returned exactly when the color is absent from the whole array.

**Why the preprocessing facts are sufficient**

The reverse scan maintains the nearest-right statement because row `i` inherits the best future occurrence for every color, then replaces the current color’s entry with the even nearer current index. The forward scan maintains the symmetric nearest-left statement.

Given those two statements, consider a query’s truly nearest matching index. It is either on the left side or the right side, with index `i` allowed in both categories. The corresponding table stores a match no farther away on that side. Taking the smaller stored distance therefore equals the global minimum. When no match exists, both sentinels survive and the code returns `-1`. Appending answers while iterating through `queries` preserves query order.

## Complexity detail

Let $n$ be the number of colors and $q$ be the number of queries. The alphabet of colors has fixed size three.

Building `right` scans $n$ positions and copies three entries per position, taking $O(3n)$ time. Building `left` does the same. Every query performs a fixed number of table lookups, subtractions, a minimum, and a comparison, so query processing takes $O(q)$. The total time is $O(6n+q)$, which simplifies to $O(n+q)$.

Each table contains $3(n+1)$ entries. Together they use $O(6n)=O(n)$ auxiliary space. The answer list uses $O(q)$ output space. Including returned output gives $O(n+q)$ total storage; excluding it, auxiliary space is $O(n)$.

The tables intentionally store indices rather than distances. Distances are calculated only when a query arrives. Python’s `inf` and `-inf` sentinels interact safely with integer subtraction and comparison in this code.

## Alternatives and edge cases

- **Sorted index lists plus binary search:** Store the occurrence indices for each color. For a query, binary-search the target index and check its predecessor and successor. This uses $O(n)$ space and $O(n+q\log n)$ time rather than constant time per query.
- **Two distance passes in one table:** One can initialize a distance matrix, sweep left-to-right for nearest-left distances, and sweep right-to-left to minimize with nearest-right distances. It has the same $O(n+q)$ time and $O(n)$ space.
- **Scan per query:** Expanding or scanning the array separately for every query can degrade to $O(nq)$ time.
- **Requested color at the query index:** The relevant table entries contain `i`, so both subtraction logic and the final result correctly allow distance zero.
- **Color absent everywhere:** Both candidates are infinite, `d > n` succeeds, and the result is `-1`.
- **Color appears on only one side:** One candidate is infinite and the other finite. `min` automatically chooses the existing side without a branch.
- **Query at index zero:** `left[1]` includes original index zero, while `right[0]` covers the full array. No negative table index is needed.
- **Query at the final index:** `left[n]` covers the full prefix and `right[n - 1]` includes the last element, so the boundary remains valid.
- **Color-to-column conversion:** Subtracting one is necessary because input colors are one through three while Python list columns are zero through two.
- **Sentinel threshold:** A legitimate distance is at most `n - 1`. Testing `d > n` is therefore safe, although an explicit infinity comparison could express the sentinel check more directly.

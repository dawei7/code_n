## General

**Convert “one value from every list” into a colored-window problem.** Each number can be labeled by the index of the list it came from. The comprehension

`[(x, i) for i, v in enumerate(nums) for x in v]`

creates one pair `(value, list_index)` for every input element. Sorting these pairs by value produces a single nondecreasing sequence while retaining each element's source “color.”

Now any contiguous window in that sorted sequence spans the numerical range from its first value to its last value. That range covers all input lists exactly when the window contains at least one pair of every list index. The problem has become: find the narrowest sorted window containing every color.

**Why considering contiguous sorted windows is sufficient.** Suppose a valid numerical range is `[a,b]`. All flattened values inside that range occupy one contiguous section of the sorted sequence. That section contains a representative of every list. Conversely, any sorted window containing all list indices defines a valid inclusive range from its left value to its right value. Therefore, searching valid windows searches all possible answer ranges.

**Maintain source coverage with a counter.** `cnt[v]` is the number of elements from source list `v` in the current window `t[j:i+1]`. The right pointer `i` advances through the sorted sequence. Adding pair `(b,v)` increments `cnt[v]`.

The implementation deletes a counter key when its count reaches zero. Because of that cleanup, `len(cnt)` is exactly the number of distinct source lists represented in the window. The condition

`len(cnt) == len(nums)`

means every list is covered.

**Shrink every valid window as far as possible.** Once all lists are represented, the current endpoints are `a = t[j][0]` and `b` from the right-loop pair. The method evaluates that range, then removes the leftmost pair, advances `j`, and repeats while coverage remains complete.

Shrinking is essential. For a fixed right endpoint, any unnecessary leftmost element only makes the range start earlier and cannot improve its width. The loop enumerates every valid left boundary until removing one color's final occurrence makes the window invalid. At that moment, further shrinking cannot produce a valid range for this right endpoint, so advancing the right pointer is the only way to restore coverage.

**Apply both comparison rules exactly.** The statement first compares width and then, on equal width, smaller start. The source computes

`x = b - a - (ans[1] - ans[0])`.

- `x < 0` means the current width is smaller;
- `x == 0 and a < ans[0]` means widths tie and the current range starts earlier.

Only in those cases is `ans` replaced.

The initialization `ans = [-inf, inf]` gives infinite width, so the first valid window always wins. Since every input list is nonempty, at least one full-coverage window exists, and the returned endpoints are ordinary input integers rather than infinities.

**Why removal updates coverage correctly.** Let `w = t[j][1]` be the source color leaving the window. Decrementing `cnt[w]` accounts for that one element. If the count becomes zero, no representative of list `w` remains, so the key is popped. If the count stays positive, another value from the same list still lies in the window and coverage remains valid.

**Why the final range is optimal.** For each right endpoint, the inner loop checks every valid window ending there while moving the left endpoint monotonically right. Across the full scan, every candidate that could be minimal is examined: a valid window with a removable redundant left element is dominated by its narrower successor, while a minimal valid window is evaluated just before removing its necessary left color. The answer comparison retains the globally smallest width and the required smallest start on ties.

For the sample lists, a late window contains values 20 from list 2, 22 from list 3, and 24 from list 1. Its endpoints are 20 and 24, so the range is `[20,24]`. Shrinking beyond 20 loses list 2 before a replacement appears, making that candidate locally tight.

Duplicates cause no difficulty. Equal values from different lists can produce a zero-width range, and tuple sorting groups them together. Equal values from the same list simply increase that color's count and may later be removed as redundant.

## Complexity detail

Let $T$ be the total number of elements across all lists and $K$ the number of lists. Flattening takes $O(T)$ time and stores $T$ pairs. Sorting them costs $O(T\log T)$. Each pair enters the sliding window once and leaves at most once, so the two-pointer scan is $O(T)$.

The exact implementation therefore runs in $O(T\log T)$ time and uses $O(T+K)$ auxiliary storage: $O(T)$ for the flattened list and sort workspace, plus at most $O(K)$ counter entries.

The manifest advertises $O(T\log K)$ time and $O(K)$ space. Those bounds belong to the alternative $K$-way min-heap method that keeps one current element per list. They do not describe this literal flatten-sort source. Both methods are correct, but their resource claims must remain attached to the right implementation.

## Alternatives and edge cases

- **K-way min-heap:** Keep one value from each list, track the current maximum, and advance the list that supplied the minimum. This achieves the manifest's $O(T\log K)$ time and $O(K)$ space.
- **Scan all current list heads:** Use one pointer per list and find the minimum by scanning all $K$ heads each step. It is simpler but can cost $O(TK)$.
- **One list:** Every single element covers all lists; the smallest range is `[first_value, first_value]` because the list is sorted.
- **Common value across all lists:** A zero-width range is optimal and will be found when the window contains those equal-valued colors.
- **Duplicate values within one list:** The counter distinguishes multiplicity and removes the color only after its final window occurrence leaves.
- **Equal-width ranges:** The explicit `a < ans[0]` test enforces the smaller-start tie rule.
- **Negative numbers:** Sorting and subtraction work without special handling.
- **Nonempty-list guarantee:** It ensures a full-coverage window exists; an empty input list would make the task impossible.
- **Counter cleanup:** Leaving zero-count keys in `cnt` would make `len(cnt)` falsely report coverage.
- **Inclusive endpoints:** Values equal to `a` or `b` are inside the returned range, matching the window endpoints.
- **Manifest mismatch:** Cite $O(T\log T)$/$O(T+K)$ for this source and reserve $O(T\log K)$/$O(K)$ for the heap alternative.

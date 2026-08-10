## General

**Make the shorter string control memory**

The method first checks whether `word1` is shorter than `word2`. If so, it calls itself once with the arguments reversed. This is safe because Levenshtein distance is symmetric: reversing a transformation exchanges insertion with deletion, leaves replacement as replacement, and preserves the number of operations. Therefore converting `word1` to `word2` costs the same as converting `word2` to `word1`.

After the possible swap, `word2` is no longer than `word1`. The rolling array has `len(word2) + 1` entries, so this choice makes its size $O(\min(m,n))$. The recursive call cannot repeat indefinitely: after swapping, the first string is at least as long as the second, so the condition is false on the next entry. Its maximum added call depth is one.

**Give each rolling entry a precise meaning**

Conceptually, define $D(i,j)$ as the minimum edits that transform `word1[:i]` into `word2[:j]`. A full table would use the base values $D(0,j)=j$ and $D(i,0)=i$.

`distance` begins as `[0, 1, 2, ..., len(word2)]`, which is exactly row zero: creating each prefix of `word2` from an empty source requires that many insertions. Before row `i` is processed, `distance[j]` stores $D(i-1,j)$, the previous row.

At the start of the row, `pre_distance_i_j = distance[0]` saves $D(i-1,0)$. Then `distance[0] = i` writes $D(i,0)$, because converting `word1[:i]` to empty requires `i` deletions.

**Recover three neighbors while overwriting one array**

When processing column `j`, the recurrence needs three values:

- `distance[j - 1]` has already been updated in this row, so it is $D(i,j-1)$. Adding one represents inserting `word2[j-1]`.
- `distance[j]` has not yet been overwritten, so it is $D(i-1,j)$. Adding one represents deleting `word1[i-1]`.
- `pre_distance_i_j` stores the old diagonal $D(i-1,j-1)$. It represents matching equal final characters for free or replacing unequal characters for one operation.

The variables `insert`, `delete`, and `replace` are therefore not guesses; each is the cost of an exhaustive category for resolving the ends of the current prefixes. If the characters differ, one is added to the diagonal replacement cost. If they match, the diagonal cost is left unchanged. The minimum becomes $D(i,j)$.

**Save the next diagonal before destroying it**

The order of two final assignments is crucial. Before writing the new value into `distance[j]`, the source assigns its old value to `pre_distance_i_j`. That old value is $D(i-1,j)$, which will be the needed diagonal $D(i-1,(j+1)-1)$ at the next column.

Only after preserving it does the code overwrite `distance[j]` with the new minimum. Reversing these two assignments would save the current-row value instead of the previous-row diagonal and corrupt later transitions. The scalar acts as the one table cell that an in-place left-to-right overwrite would otherwise erase too soon.

**Derive the recurrence from a final edit**

If the last prefix characters match, an optimal transformation can leave them paired and use $D(i-1,j-1)$. If they differ, a valid transformation must resolve the boundary by deleting the source character, inserting the destination character, or replacing one with the other. These choices give

$$
D(i,j)=1+\min\bigl(D(i-1,j),D(i,j-1),D(i-1,j-1)\bigr).
$$

The categories cover every allowed operation and are mutually interpretable by their last edit. Appending each edit to an optimal smaller transformation gives a valid candidate, while any complete transformation has a last boundary-resolving edit belonging to one of them. The minimum is consequently exact.

**A rolling-row invariant**

Before inner-loop column `j`, `distance[0:j]` contains current-row values $D(i,0),\ldots,D(i,j-1)$, `distance[j:]` still contains previous-row values $D(i-1,j),\ldots$, and `pre_distance_i_j` equals $D(i-1,j-1)$. Initialization at the start of each row establishes this split.

The three candidate calculations read precisely the left, above, and diagonal states. Saving the old above value advances the diagonal, and writing the minimum extends the current-row prefix by one cell. Thus the invariant holds at the next column. At the end of a row, the entire array is row `i`. After the final row, `distance[-1]` is $D(\operatorname{len}(word1),\operatorname{len}(word2))$, the required complete-string distance.

**Empty inputs require no special branch**

If `word2` is empty after ordering, `distance` contains only zero. Every outer iteration changes that entry to `i`, and the final value is the source length, representing all deletions. If `word1` is empty and `word2` is not, the initial swap makes the nonempty string first and reduces to the same case. If both are empty, neither loop runs and the initial zero is returned.

## Complexity detail

Let $m$ and $n$ be the original string lengths. Swapping references takes constant time. The nested loops still evaluate every pair of character positions, so time is $O(mn)$, matching the manifest. Each state performs constant arithmetic and character comparisons.

After ordering, the list length is one more than the shorter input length. The scalar diagonal and loop variables use constant extra storage, so auxiliary space is $O(\min(m,n))$, exactly matching the manifest. The one recursive swap adds only one stack frame and does not change the asymptotic bound.

## Alternatives and edge cases

- **Full two-dimensional table:** It makes all dependencies visible and can aid operation reconstruction, but uses $O(mn)$ space when only the distance is requested.
- **Two rolling rows:** Avoid the diagonal-preservation trick by keeping both rows. It remains linear in one dimension but uses about twice the row storage.
- **Memoized recursion:** Cache each prefix pair and express edit choices naturally. It has the same state count but requires $O(mn)$ cache space plus recursion depth.
- **Banded dynamic programming:** If a small maximum allowed distance were supplied, work could be restricted near the diagonal. This problem provides no such threshold.
- **Input swap:** It changes only orientation, not the distance; insertion and deletion are inverse operations of equal cost.
- **Both strings empty:** The initialized array is `[0]`, and zero is returned.
- **One string empty:** The sole rolling entry eventually equals the other string's length.
- **Matching characters:** The diagonal is used without adding an operation.
- **Unequal characters:** Insertion, deletion, and replacement are all considered before selecting a minimum.
- **Identical strings:** Every state along the relevant diagonal propagates zero, producing distance zero.
- **Update order:** The old `distance[j]` must be saved before it is overwritten, or the next diagonal will be wrong.
- **Repeated letters:** Prefix coordinates distinguish positions, so repeated character values do not merge states incorrectly.
- **Maximum lengths:** At 500 characters each, the method evaluates 250,000 pairs while storing only 501 integers.
- **Unused `Solution2`:** The file's second class stores the full table and is not selected by the `Solution` name; it should not be confused with this rolling implementation.

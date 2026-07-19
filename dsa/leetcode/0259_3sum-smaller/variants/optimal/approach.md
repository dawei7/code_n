## General
**Sorting turns one valid pair into a valid block**

After sorting, fix index `i` and place two pointers at $i + 1$ and the last index. Their ordered movement counts many valid third indices at once.

For fixed `i`, when `nums[i] + nums[left] + nums[right]` is small enough, every index from `left + 1` through `right` also forms a valid triple with `i` and `left`. Add `right - left` and advance `left`; otherwise decrease `right`.

**Each pointer move settles every pair it skips**

When the sum at `(left, right)` is below the target, replacing `right` by any index between `left + 1` and `right` can only decrease the sum. Those `right - left` pairs are all valid and are counted together before `left` advances. When the sum is too large, any larger `left` value would keep it too large, so the current `right` cannot form a valid remaining pair and may be discarded. The sweep therefore settles all pairs for every fixed first index without omission or double counting.

## Complexity detail
Sorting costs $O(n \log n)$. Each of `n` first indices performs one linear pointer sweep, for $O(n^2)$ total time; the sorted copy uses $O(n)$ space.

## Alternatives and edge cases
- **Enumerate all triples:** takes $O(n^3)$.
- The inequality is strict; duplicates represent different index choices; fewer than three values produce zero.

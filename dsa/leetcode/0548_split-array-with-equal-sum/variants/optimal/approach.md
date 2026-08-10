## General

Three separator indices `i < j < k` are excluded from the four subarrays. The goal is to make these four sums equal:

1. indices zero through `i - 1`;
2. `i + 1` through `j - 1`;
3. `j + 1` through `k - 1`;
4. `k + 1` through `n - 1`.

Trying every triplet would take cubic time. The solution fixes the middle separator `j`, summarizes every valid left split by its shared sum, and then tests right splits against that set.

**Build prefix sums with an exclusive endpoint.** Array `s` has length `n + 1` and meaning:

`s[t]` is the sum of `nums[0 : t]`, covering indices zero through `t - 1`.

It begins with `s[0] = 0`, and:

`s[i + 1] = s[i] + v`

adds each value. Therefore any inclusive interval `l...r` has sum `s[r + 1] - s[l]`.

**Choose only legal middle separators.** The loop:

`for j in range(3, n - 3)`

starts `j` at three so there is room for at least one element before `i`, one between `i` and `j`, and the separator `i` itself. It stops before `n - 3` so there is symmetric room for `k` and the final two nonempty sections.

If `n < 7`, this range is empty and the method correctly returns false.

**Collect feasible equal sums on the left of `j`.** For a fixed `j`, the loop considers:

`i in range(1, j - 1)`.

Index `i = 1` leaves element zero in the first section. Stopping before `j - 1` ensures at least index `i + 1` lies between separators `i` and `j`.

The first section sum is:

`s[i]`.

The second section, indices `i + 1` through `j - 1`, has sum:

`s[j] - s[i + 1]`.

The `s[i + 1]` subtraction excludes every element through separator `i`, and `s[j]` stops before separator `j`.

When these values are equal, their common sum is added to `seen`. The set does not need to remember which `i` produced it, because any one matching left split is sufficient when a compatible right split is found.

Negative and zero sums work because the set stores exact integers and makes no monotonicity assumption.

**Test legal right separators.** The loop:

`for k in range(j + 2, n - 1)`

leaves at least one element at `j + 1` before `k` and at least one element after `k`.

The third section, `j + 1` through `k - 1`, has sum:

`s[k] - s[j + 1]`.

The fourth section, `k + 1` through the end, has sum:

`s[n] - s[k + 1]`.

The condition first requires these two right sums to be equal. It then checks whether that common right sum belongs to `seen`. Membership proves there exists some legal `i` for the same fixed `j` whose first two sums equal the same value.

When both facts hold, all four sums are equal and the method returns true immediately.

For `[1,2,1,2,1,2,1]`, choose `j = 3`. Left separator `i = 1` gives first sum one and second sum one, so one enters `seen`. Right separator `k = 5` gives third and fourth sums one. Membership succeeds and the method returns true.

**Why separator values are excluded.** Every formula jumps past its separator using `i + 1`, `j + 1`, or `k + 1` in the appropriate prefix subtraction. None of `nums[i]`, `nums[j]`, or `nums[k]` contributes.

**Why every returned result is valid.** A return occurs inside legal index ranges. The right equality proves sections three and four match. Set membership came only from a legal left `i` where sections one and two matched. Because the stored and tested common sums are equal, all four sections match.

**Why every valid triplet is found.** For a valid `(i, j, k)`, the outer loop eventually fixes that `j`. The left loop visits its `i` and inserts the shared sum. The right loop later visits its `k`, confirms the right equality, and finds the same sum in `seen`. It returns true.

If no middle separator produces a matching left and right sum, every legal triplet has been ruled out and false is correct.

## Complexity detail

Let $n$ be the array length. Prefix construction takes $O(n)$. There are $O(n)$ middle indices, and each performs $O(n)$ total left/right separator checks. Time is $O(n^2)$.

For one `j`, `seen` holds at most $O(n)$ distinct sums and is discarded before the next middle index. Prefix array `s` also uses $O(n)$ space. Total auxiliary space is $O(n)$, matching the manifest.

Set lookup and insertion use expected $O(1)$ hashing time.

## Alternatives and edge cases

- **Enumerate all triplets:** Prefix sums make each check constant time, but $O(n^3)$ triplets are still too many.
- **Two sets split around `j`:** The implemented one-set method builds left possibilities and streams right checks, avoiding extra storage.
- **Assume positive values:** Values may be negative, so sliding-window monotonicity does not apply.
- **Fewer than seven elements:** Three separators plus four nonempty sections cannot fit; loop ranges naturally return false.
- **Separator values:** They must be omitted, and the prefix formulas explicitly skip them.
- **Zero shared sum:** Zero is a normal set value and can validate a split.
- **Negative shared sum:** Hash membership works without ordering assumptions.
- **Several left indices with one sum:** The set intentionally stores the sum once because only existence matters.
- **Valid split at extreme legal indices:** Loop endpoints include `i = 1` and `k = n - 2` while preserving one-element outer sections.
- **No valid middle separator:** Completing all loops returns false.

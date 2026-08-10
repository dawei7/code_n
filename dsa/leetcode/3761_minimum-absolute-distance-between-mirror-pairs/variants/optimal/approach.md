## General

**Store what future value each earlier index needs**

For an earlier index `j` to pair with a future value, that future value must equal `reverse(nums[j])`. The dictionary `pos` maps this required future value to the latest earlier index that produces it.

When current value `x=nums[i]` arrives, checking `x in pos` immediately finds an earlier `j` with

$$
\operatorname{reverse}(\texttt{nums}[j])=x.
$$

Then `i-j` is a valid mirror-pair distance.

After checking, the source computes `reverse(x)` and stores `pos[reverse(x)]=i` so the current index can serve as the left endpoint of a future pair.

The check happens before insertion, ensuring `i<j` direction and preventing an index from pairing with itself.

The dictionary keys deserve special attention. A key is not necessarily a value already seen in the array. It is the value that would complete a pair for some earlier index. For example, after reading 120, the map contains key 21 because a future 21 is wanted. This “store the future requirement” viewpoint allows the current lookup to use `x` directly.

**Reverse digits arithmetically**

The helper repeatedly takes `x%10` and appends it to `y` using `y=y*10+digit`. Integer division removes the processed digit.

Trailing zeros of the original become leading zeros of the reversed sequence and naturally disappear numerically. For 120, steps build zero, two, then 21, producing the required result.

This directionality matters: reversing 120 gives 21, but reversing 21 gives 12, not 120.

For a positive number with `D` decimal digits, the loop runs exactly `D` iterations. Each iteration transfers the current last digit into the result. When the original number ends in zero, that zero is transferred first while `y` is still zero, so it does not create a visible leading digit. No special trimming rule is needed.

**Why only the latest index per required value is needed**

For a fixed current right endpoint `i` and required value `x`, the closest valid earlier index minimizes `i-j`. Among all earlier indices stored under key `x`, the largest `j` is therefore always best.

Overwriting `pos[reverse(x)]` with the current index discards older endpoints that can never beat it for any future right endpoint. If future index `t>i` needs the same key, `t-i<t-j` for every older `j`.

The global `ans` keeps the minimum across all current endpoints and required-value keys.

For `[12,21,45,33,54]`, processing 12 stores key 21 at index zero. Current 21 finds it and records distance one. Processing 45 later stores key 54, which current 54 finds at distance two; the global minimum remains one.

For `[21,120]`, processing 21 stores key 12. Current 120 does not find key 120, so no pair is reported, correctly respecting direction.

A short map trace for `[120,8,21]` makes the order concrete. At index zero, 120 is not found and the scan stores `pos[21]=0`. At index one, 8 is not found, then `pos[8]=1` is stored because 8 reverses to itself. At index two, current value 21 finds index zero, producing distance two. Only after that lookup does the scan store `pos[12]=2`.

**Why every valid pair is considered**

Take any mirror pair `(j,i)`. When `j` was processed, its reversed value was inserted under the exact future key `nums[i]`. It may later be overwritten only by a closer index with the same reversed value, which forms an equal or smaller-distance valid pair with `i`. Thus the scan cannot miss the optimum.

Every dictionary hit was created by reversing an earlier value, so every measured distance is valid. Infinity remaining unchanged means no pair exists and maps to `-1`.

Using infinity as the initial answer avoids inventing a numeric sentinel that might accidentally look like a real distance. All real distances are positive integers because the endpoints are distinct and ordered. If at least one pair is encountered, a finite value replaces infinity; otherwise the final conditional returns the contract's `-1`.

## Complexity detail

Let `n` be the array length and `D` the maximum decimal digit count. Reversing one value takes $O(D)$ time, so total expected time is $O(nD)$ including hash operations.

Because values are at most $10^9$, `D<=10` is a fixed constant, and the manifest simplifies this to $O(n)$. The more explicit $O(nD)$ bound exposes the digit-reversal work.

The dictionary stores up to `n` keys, requiring $O(n)$ auxiliary space. The reversal helper uses constant numeric state.

Several earlier indices may generate the same required key, so the map can be smaller than `n`, but $O(n)$ is the safe worst-case bound. The scan itself is iterative, and the size of the result integer and loop temporaries does not grow with the number of array elements.

## Alternatives and edge cases

- **Check all index pairs:** Reversing and comparing every pair costs $O(n^2D)$. Required-value hashing reduces the pair search.
- **Store the earliest index:** That maximizes rather than minimizes distance for a fixed future endpoint. Latest is required.
- **Reverse the current value and search original earlier values:** That changes the directional condition for trailing-zero cases and is not equivalent.
- **String reversal:** `int(str(x)[::-1])` is valid and has the same digit complexity; the exact source uses arithmetic.
- **Palindromic value:** It can pair with the same value at a later distinct index.
- **Trailing zeros:** Arithmetic reversal omits their new leading zeros automatically.
- **Single element:** No earlier endpoint exists, so answer is `-1`.
- **Multiple valid earlier endpoints:** Overwriting retains the closest one.
- **Repeated palindromes:** For values such as 7 or 121, each new copy first pairs with the previous copy and then replaces it as the nearest endpoint for the future.
- **Distance one:** It is the smallest possible and may be found for adjacent mirror values.
- **Hash collisions:** Python dictionary semantics provide expected constant-time lookup while preserving exact key equality.
- **Manifest time:** Linear time assumes the bounded digit width; generalized complexity is $O(nD)$.

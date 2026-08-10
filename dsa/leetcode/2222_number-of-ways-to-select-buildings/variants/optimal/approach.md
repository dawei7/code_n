## General

**Only two selected type patterns are valid**

The three selected indices must be strictly increasing because they describe buildings along the street. “No two consecutive selected buildings have the same type” refers to adjacency within the chosen triple, not necessarily adjacency on the street.

With binary types, an alternating triple can only be `010` or `101`. Once the middle building's type is known, both the first and third selected buildings must have the opposite type. This suggests counting valid triples by choosing each position as the middle.

For a current building of type `x`, the number of valid triples centered there is

$$
(\text{opposite-type buildings to its left})
\times
(\text{opposite-type buildings to its right}).
$$

Every left choice can be paired independently with every right choice, and their indices automatically satisfy `left < current < right`.

**Maintain counts on both sides of the current index**

The solution uses two two-element arrays:

- `l[0]` and `l[1]` count office and restaurant buildings already passed on the left;
- `r[0]` and `r[1]` count those still on the current position or to its right before the loop adjusts the current character.

It initializes `l = [0, 0]` because nothing is left of the first building. It initializes `r` with `s.count("0")` and `s.count("1")`, so both entries initially count the entire street.

The loop converts each character to integer zero or one with `for x in map(int, s)`. This makes `x` usable as an index into both arrays.

**Move the current building out of the right side first**

At the beginning of an iteration, `r[x]` still includes the current building. The statement `r[x] -= 1` removes it before counting triples. After that subtraction:

- `l` contains exactly the buildings at indices smaller than the current index;
- `r` contains exactly the buildings at indices larger than the current index.

This timing prevents the current building from being selected again as its own left or right partner.

The opposite binary type is `x ^ 1`. XOR with one changes zero to one and one to zero:

- `0 ^ 1 = 1`;
- `1 ^ 1 = 0`.

Therefore, `l[x ^ 1]` is the number of legal choices for the first building and `r[x ^ 1]` is the number for the third. Their product is added with

`ans += l[x ^ 1] * r[x ^ 1]`.

Finally, `l[x] += 1` moves the current building into the processed-left counts so it can serve as a first building for later middle positions.

**Why multiplication gives exactly the triples for one middle**

Suppose the current type is zero. A valid triple centered here must be `101`. If there are `a` ones on the left and `b` ones on the right, each of the `a` left indices can be combined with each of the `b` right indices. This gives `a \cdot b` distinct index triples.

No pair of choices produces the same triple because a triple uniquely identifies its left and right indices. No invalid triple is included because both selected side buildings have type one while the middle has type zero.

The current-type-one case is symmetric and counts `010` triples using zeros on both sides.

**Why every valid selection is counted once**

Every selection of three increasing indices has one unique middle index: the second selected building. When the scan reaches that index, the first selected index has already entered `l` and the third remains in `r` after removing the current item. If the triple alternates, both side types equal `x ^ 1`, so their pair contributes once to the product.

The triple cannot be counted at another iteration because no other chosen index is its middle. Thus, the method includes all valid triples and never double-counts one.

Conversely, every pair represented by a product chooses one index to the left and one to the right, both of the type opposite the current building. Those three positions are ordered and form `010` or `101`. Every counted combination is valid.

These two directions establish that the accumulated `ans` is exactly the required number.

**Trace the counts for a useful middle**

Consider `s = "001101"`. When the scan reaches the first `1` at index two, `l` contains two zeros and no ones. After removing the current `1` from `r`, the right side contains one zero at index four. The product for opposite type zero is `2 \cdot 1 = 2`, counting triples `[0, 2, 4]` and `[1, 2, 4]`.

At the next `1`, the left still contains two zeros and the right still contains one zero, creating two more `010` triples. Later, when index four's zero is the middle, two ones lie to its left and one lies to its right, creating two `101` triples. The total is six.

**The exact code uses middle counting, not a length-state DP**

The manifest summary describes counting alternating subsequences of lengths one, two, and three. That is another valid one-pass framing, but the stored Optimal Python solution specifically uses left and right type counts around each middle. The result and asymptotic bounds are the same, while the explanation above matches the actual data flow.

Building positions need not be adjacent in the street. Counts include all earlier and later matching types, correctly treating the choice as a subsequence of indices.

## Complexity detail

Let `n = len(s)`. The two `s.count(...)` calls each scan the string, taking `O(n)` time in total. The main loop scans it once more and performs constant work per character. Three sequential linear scans are still `O(n)` time.

The arrays `l` and `r` each contain exactly two integers, and `ans` and `x` are scalar values. Their storage does not grow with `n`, so auxiliary space is `O(1)`. The `map` object is lazy and does not materialize a list of all digits.

The number of triples can be on the order of `n^3` even though it is counted in linear time. Python integers grow as needed, preventing overflow. A fixed-width solution should use a 64-bit integer for `ans` under the stated constraints.

## Alternatives and edge cases

- **Enumerate all triples:** Three nested index loops can test every selection directly but require `O(n^3)` time, which is infeasible for `n = 10^5`.
- **Choose the middle with prefix arrays:** Precompute zeros and ones before every index and obtain corresponding suffix counts. This gives `O(n)` time but uses `O(n)` extra storage instead of four running counts.
- **Alternating-subsequence DP:** Maintain counts of subsequences `0`, `1`, `01`, `10`, `010`, and `101` while scanning. It is also `O(n)` time and `O(1)` space, but the middle-product formulation is especially direct for exactly three buildings.
- **Count only adjacent street buildings:** That misreads the problem. Selected indices may have unselected buildings between them; only consecutive members of the selected triple must differ.
- **All one type:** Every middle has zero opposite-type choices on at least one side, so the result is zero.
- **Length exactly three:** The only possible selection is the whole string. It contributes one if the pattern is `010` or `101` and zero otherwise.
- **No opposite type on the left or right:** One factor is zero, correctly contributing no triple for that middle.
- **Current-building exclusion:** `r[x]` must be decremented before multiplication. Otherwise, side counts would not represent strictly later positions.
- **Repeated types in long blocks:** Counts, rather than adjacency checks, correctly combine every earlier opposite-type index with every later one.
- **Large answer:** The count can exceed 32-bit range. Python handles it automatically; fixed-width implementations need a wide integer.
- **Type toggle:** `x ^ 1` is valid only because `x` is guaranteed to be binary. The character-to-integer conversion makes this exact.
- **Input order:** The scan never sorts or rearranges buildings, so every counted choice respects street order.

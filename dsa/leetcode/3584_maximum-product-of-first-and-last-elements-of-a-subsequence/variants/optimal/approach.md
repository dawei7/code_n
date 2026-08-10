## General

Only the first and last selected values affect the product. The middle `m-2` subsequence elements matter only for feasibility.

If index `i` is the last endpoint, a first endpoint `p` is feasible exactly when `p\le i-m+1`. Then at least `m-2` indices lie between them and can fill the subsequence.

The source scans possible last endpoints and maintains the minimum and maximum values among all currently eligible first endpoints.

**Eligibility boundary**

The first possible last endpoint is `m-1`. At last index `i`, index `i-m+1` becomes newly eligible as a first endpoint.

The loop assigns:

`y=nums[i-m+1]`

and folds `y` into running `mi` and `mx`. Those extrema then cover exactly prefix indices zero through `i-m+1`.

Earlier eligible indices stay eligible for every later last endpoint, so no removal is needed.

**Why only minimum and maximum are needed**

For fixed last value `x`, the product `x*y` is a linear function of eligible first value `y`.

- If `x` is positive, the largest `y` maximizes the product.
- If `x` is negative, the smallest, most negative `y` maximizes it.
- If `x=0`, every product is zero.

Checking both `x*mi` and `x*mx` covers every sign without branching. No interior eligible value can beat both extremes.

**Subsequence existence**

For endpoints `p` and `i` with `i-p\ge m-1`, there are at least `m-2` positions strictly between them. Selecting any `m-2` in increasing order creates a size-`m` subsequence with those endpoints.

If the gap is smaller, there are not enough positions. The eligibility boundary is therefore necessary and sufficient.

**m equals one**

For a one-element subsequence, its first and last element are the same, so the score is `nums[i]^2`.

When `m=1`, the loop starts at zero and newly eligible `y` is `nums[i]`. Because the current value is included in extrema before products are tested, every square is considered. Other earlier values are also checked, but could they create an invalid two-index interpretation? For positive/negative combinations, the maximum with current extrema is at least the current square and might produce a cross product larger than all squares only if opposite magnitudes interact; by `|ab|\le\max(a^2,b^2)` for same-sign positive product and opposite signs give negative product. Thus cross candidates cannot exceed the best square already considered. The returned maximum remains correct.

**Why the scan is complete**

Every feasible subsequence has a unique last index. At that iteration, its first value lies within the maintained eligible prefix. The best product for that last endpoint occurs at one of the stored extrema and is checked.

Conversely, each checked endpoint pair has enough intervening indices to form a valid subsequence when `m>1`. Taking the global maximum yields the answer.

## Complexity detail

The loop processes each possible last endpoint once. Updating extrema and evaluating products are constant-time, so time is `O(n)`.

Only `ans`, `mi`, `mx`, and scalar loop values are stored. Auxiliary space is `O(1)`.

## Alternatives and edge cases

- **Enumerate endpoint pairs:** Testing all `p,i` costs `O(n^2)`; the eligible extrema summarize every useful first value.
- **Sort eligible values:** Maintaining a sorted prefix is unnecessary because a linear product needs only two extremes.
- **All positive values:** The running maximum first value determines every endpoint’s best product.
- **All negative values:** Pairing a negative last value with the minimum eligible first value can produce the largest positive product.
- **Mixed signs:** Checking both extremes handles positive and negative last values uniformly.
- **Zero values:** They can produce zero, which may beat negative feasible products.
- **m equals n:** Only the complete array is a size-`n` subsequence, and the loop has one iteration using its endpoints.
- **m equals one:** The maximum square is returned as explained, despite extrema containing earlier values.
- **Duplicate values:** Not prohibited or needed for the proof; endpoints are chosen by index.
- **Large magnitude:** Products reach `10^{10}`, safely handled by Python integers.
- **Subsequence, not subarray:** Intermediate elements need not be contiguous, which is why endpoint distance alone establishes feasibility.
- **Input preservation:** The algorithm reads values without sorting or mutation.
- **Initialization with infinities:** The first loop iteration replaces both extrema before any product is evaluated.
- **Why middle values never affect the objective:** Once endpoint indices leave enough room, the remaining positions can be selected solely to reach size `m`. Their numeric values are not multiplied into the score, so optimizing or sorting them would solve a condition the problem never asks about.
- **Order-preserving endpoints:** The first index must precede the last, which is why only a growing prefix is summarized. A global minimum or maximum from the entire array could lie after `i` and would produce an invalid subsequence orientation.
- **Two extreme products:** Evaluating both is constant work and avoids fragile sign cases. It remains correct when an extreme is zero or when minimum and maximum are the same single eligible value.

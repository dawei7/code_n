## General

**Process positions left to right because each decision becomes forced**

When the scan reaches index `i`, no flip starting after `i` can ever change `nums[i]`: a length-`k` flip affects its starting index and positions to the right. All flips that could start before `i` have already been decided.

Therefore:

- if the effective bit at `i` is one, starting a flip there would unnecessarily turn it to zero;
- if the effective bit at `i` is zero, a flip must start exactly at `i`, because no future decision can repair this position.

This makes the greedy choice forced rather than merely plausible. It also establishes minimality: the algorithm never performs an optional flip.

**Track flip effects without changing every covered bit**

Actually toggling `k` array positions for each operation could take `O(Nk)` time. The solution instead uses a difference array `d` of length `n + 1` and a running value `s`.

When a flip starts at `i` and ends just before `i + k`, the code records:

`d[i] += 1` and `d[i + k] -= 1`.

As the scan moves right, adding `d[i]` to `s` starts any flip whose range begins here and removes any flip whose range ended here. Thus `s` is the number of chosen flips currently covering index `i`.

Only the parity of `s` matters. An even number of toggles leaves a bit unchanged; an odd number inverts it.

**Recognize when the effective bit is zero**

The effective bit is conceptually

`x XOR (s % 2)`.

For binary values, this result is zero in exactly two cases:

- `x = 0` and `s` is even;
- `x = 1` and `s` is odd.

In both cases, `s % 2 == x`. That is why the code uses the perhaps surprising condition

`if s % 2 == x:`

to mean “the current effective bit is zero and needs a flip.”

If the values differ, the effective bit is already one and no operation starts.

**Update the running state for a newly forced flip**

At the beginning of an iteration, `s += d[i]` applies all range-boundary changes scheduled for this index. If a new flip must start, `d[i] += 1` records its formal start and `d[i + k] -= 1` schedules its expiration.

Because `s` already incorporated the old value of `d[i]` before this new decision, the code also executes `s += 1` immediately. This makes the newly started flip affect the current bit and every following position until its scheduled negative endpoint is reached.

Variable `ans` increases once for the chosen operation.

One might wonder why `d[i] += 1` is needed if `s` is updated directly. The start marker makes the difference array a complete representation of all ranges, while the explicit `s += 1` handles the fact that the sweep has already passed the point where it normally consumes `d[i]`.

**Detect impossibility at the first unrepairable zero**

A flip starting at `i` is legal only when its last covered index `i + k - 1` lies inside the array, equivalently `i + k <= n`.

If the effective bit at `i` is zero but `i + k > n`, the required flip cannot fit. Earlier decisions are already fixed, and later flips cannot affect `i`, so no solution exists. Returning `-1` immediately is conclusive, not just a failure of this particular greedy attempt.

The extra difference-array slot at index `n` safely stores an expiration marker for a flip ending exactly at the array boundary.

**Trace the main example**

For `nums = [0, 0, 0, 1, 0, 1, 1, 0]` and `k = 3`:

- At index zero, `s = 0` and `x = 0`, so a flip is forced over indices zero through two. Set an expiration at three, make `s = 1`, and set `ans = 1`.
- At indices one and two, the original zeros are inverted by odd parity and are effectively one, so no new flips start.
- At index three, the first flip expires, returning `s` to zero. Original bit one is already correct.
- At index four, original zero under even parity forces a flip over four through six. Now `ans = 2` and `s = 1`.
- At index five, original one under odd parity is effectively zero, so another flip over five through seven is forced. Now `ans = 3` and `s = 2`.
- The remaining bits evaluate to one as the scheduled ranges expire.

The method returns three without ever rewriting the covered elements.

**The sweep invariant**

Immediately after `s += d[i]`, `s` equals the number of previously selected flip ranges that cover index `i`. All indices before `i` are already effectively one and can no longer be changed by future starts.

If the current effective bit is one, doing nothing preserves that completed prefix. If it is zero, starting at `i` is the only decision that can fix it; the difference markers and explicit increment make that range active. Either way, the invariant advances to the next position.

By induction, if the scan finishes, every position is one. If it returns `-1`, the first failing position has no legal remaining flip that can affect it, proving impossibility.

**Why the flip count is minimum**

At every index where the algorithm starts a flip, any valid solution must also have an odd additional flip affecting that index whose start is not earlier than the current undecided point. The only possible such start is `i` itself. Thus every counted flip is mandatory.

At indices already effectively one, the algorithm adds no redundant flip. Since it performs exactly the forced operations and no optional ones, no valid solution can use fewer flips.

**Difference arrays as range-update compression**

A difference array records where a range effect begins and ends rather than writing the effect into every position. Its prefix sum reconstructs the active effect at each index. Here the range effect is “one additional toggle,” and only prefix-sum parity influences the bit.

## Complexity detail

Let `N` be the length of `nums`.

The algorithm makes one left-to-right pass. Each iteration performs constant-time arithmetic and array access, so time complexity is `O(N)`.

The exact protected implementation allocates difference array `d` with `N + 1` integers, so its auxiliary space complexity is `O(N)`. The input array is not modified. A related in-place marker implementation can achieve `O(1)` auxiliary space, but that is a different storage strategy from the code documented here.

## Alternatives and edge cases

- **Flip all `k` elements explicitly:** The same greedy decisions are correct, but modifying each range costs up to `O(Nk)` time.
- **Queue of flip start indices:** Remove expired starts and use queue-length parity to determine the effective bit. It runs in `O(N)` time and uses up to `O(k)` space.
- **In-place start markers:** Reuse values in `nums` to mark where flips began, obtaining constant auxiliary space at the cost of mutating the input and overloading its value domain.
- **Boolean start array:** Record whether a flip starts at each index and maintain active parity. This is conceptually similar to the difference array and also uses `O(N)` space.
- **`k = 1`:** Every zero forces a one-element flip, so the answer is exactly the number of zeros.
- **`k = N`:** Only a flip starting at zero is possible. The array is solvable only if doing zero or one full-array flip makes all bits one.
- **Already all ones:** No equality condition triggers under even parity, and the answer is zero.
- **Unrepairable suffix:** If a zero becomes visible within the last `k - 1` positions and a full range cannot start, the method returns `-1` immediately.
- **Overlapping flips:** Their effects combine through `s`; two overlapping flips cancel each other on shared positions because only parity matters.
- **Expiration at `n`:** The `N + 1` difference-array length makes `d[i + k]` safe for a flip ending at the final boundary.
- **Input preservation:** Unlike constant-space marking variants, this solution only reads `nums`.

## General

**Powers of two turn subset sum into bit accounting.** Every array value is a power of two. A subsequence can select any subset of positions because the original relative order can always be preserved when selected indices are listed increasingly. Therefore, the task is to obtain enough pieces of each binary size to assemble `target`.

Splitting one $2^j$ creates two $2^{j-1}$ pieces and costs one operation. Repeating down to $2^i$ costs $j-i$ operations and leaves useful sibling pieces at intermediate sizes.

**Reject insufficient total value immediately.** Splitting preserves total sum. If `sum(nums) < target`, no sequence of operations can create a subsequence with the required sum, so the source returns negative one.

For powers of two, total sum at least target is also enough in principle because every piece can ultimately be split into ones. The remaining work is to minimize how many splits are actually needed.

**Count pieces by exponent.** `cnt[i]` is the number of available pieces equal to $2^i$. The source creates 32 buckets for bit positions zero through thirty-one.

For every input `x`, it scans all 32 positions and increments the bucket whose bit is set. Since `x` is guaranteed to be one power of two, exactly one bucket changes. A direct `bit_length` computation could locate it faster in constant factors, but the fixed loop remains constant work per number.

**Process required target bits from low to high.** Variable `i` advances to the next set bit of `target`. Satisfying lower bits first is essential. A small required unit cannot be synthesized from larger pieces without splitting, whereas unused smaller pieces can be combined conceptually to cover a larger binary unit for free.

The algorithm does not physically merge array elements. Carrying two $2^p$ pieces into one count at $2^{p+1}$ is bookkeeping that says those two selected pieces have the same total value as the higher bit.

**Carry surplus smaller pieces upward.** Pointer `j` tracks the lowest bucket not yet normalized for the current target bit. While `j < i`, the code performs

`cnt[j + 1] += cnt[j] // 2`

`cnt[j] %= 2`.

Every pair of smaller pieces can jointly satisfy value $2^{j+1}$, so the quotient becomes available higher-level capacity. At most one unpaired piece remains. This operation costs zero because the problem permits selecting both existing pieces directly; no forbidden merge operation is being claimed.

After carrying through level `i`, `cnt[i]` reflects all ways unused pieces of size at most $2^i$ can cover one target unit $2^i$.

**Use an available piece without splitting.** If `cnt[i] > 0`, the upward-search loop does not move. The code adds zero operations, decrements `cnt[i]` to consume one unit for the target bit, resets `j = i`, and advances to later target bits.

**Split the nearest larger piece when necessary.** If `cnt[i] == 0`, the loop

`while cnt[j] == 0`

searches upward for the first exponent with an available piece. While moving from a missing level $p$ to $p+1$, it assigns `cnt[p] = 1`.

This assignment represents the leftover sibling produced when a future larger piece is split downward. Splitting one $2^{p+1}$ creates two $2^p$ pieces: one continues down toward the required $2^i$, while the other remains available at level $p$. At the bottom level, one $2^i$ is consumed for the current target bit and its sibling remains recorded as one.

When the first available larger bucket $J$ is found, `cnt[J] -= 1` consumes that original piece. The number of necessary split operations is $J-i$, so `ans` increases by `j - i`. The lower-level ones written during the search are exactly the leftovers from that split chain.

The code then resets `j` to `i` so later target bits can carry those leftovers upward as needed.

**A trace for one split.** Suppose a target needs $2^2=4$ but only one piece $2^5=32$ is available. Splits are $32\to16+16$, then one sixteen to two eights, then one eight to two fours: three operations. One sixteen, one eight, and one four remain as siblings, while the other four satisfies the current bit. The loop writes one into buckets two, three, and four, consumes one bucket-five piece, and adds $5-2=3$.

**Why the nearest larger piece is optimal.** If no combination of unused smaller pieces covers $2^i$, every valid solution must split some piece above level $i$. A piece at level $J$ requires at least $J-i$ splits before any $2^i$ piece exists. Choosing the nearest available $J$ minimizes that unavoidable cost. The generated siblings are never worse than alternatives because they preserve all leftover value in the largest useful denominations for future higher bits.

Processing bits low to high prevents spending a small piece on a higher target bit when that piece is uniquely needed below. Induction shows that after satisfying each bit, `ans` is the minimum split cost for the processed target prefix and `cnt` accurately represents all unused value.

**Why total sum prevents the search from failing.** After lower target bits are satisfied, if no piece or carried combination existed at or above a required bit, the remaining total value would be smaller than that required remaining target contribution. The initial sum check rules this out. Under the stated bit bounds, the 32 buckets provide enough room for carries.

## Complexity detail

For each of $n$ input values, the exact source checks 32 bit positions, taking $O(32n)=O(n)$ time. The target-processing pointers range over only 32 positions. Even with upward searches and resets, their work is bounded by a constant depending on the fixed 32-bit domain, at worst $O(32^2)$.

Total time is therefore $O(n)$ under the fixed-width constraints. The count array always has 32 entries, so auxiliary space is $O(1)$. If the maximum exponent were a variable $B$, a more general statement would be $O(nB+B^2)$ for this literal bit-detection and search structure, with $O(B)$ space.

Computing the initial sum is $O(n)$. Python integer arithmetic safely handles the maximum total of up to one thousand copies of $2^{30}$.

The returned operation count is small enough for ordinary integers, but Python avoids overflow regardless.

## Alternatives and edge cases

- **Direct exponent lookup:** Use `x.bit_length() - 1` to increment one bucket per value, reducing the input-counting constant while keeping $O(n)$ time.
- **Standard per-bit greedy loop:** For every bit from zero upward, use a local piece if target needs it; otherwise find the next larger bucket, explicitly propagate split leftovers downward, then carry pairs upward. This is equivalent but often easier to visualize.
- **Priority queue of pieces:** Repeatedly split selected large values, but deciding which pieces serve target bits is more cumbersome and adds logarithmic overhead.
- **Total sum below target:** Splitting preserves sum, so negative one is immediately necessary.
- **Target already formable:** Smaller pieces carry into every required bit, no larger piece is split, and answer is zero.
- **One large piece:** Reaching a low required bit costs exactly the exponent difference, with every split sibling retained.
- **Duplicate powers:** Counts allow any number of identical pieces and pair them upward without physical operations.
- **Target bit zero:** `i` skips it; available pieces remain for later carrying rather than being consumed.
- **Power $2^0=1$:** It cannot be split, but pairs of ones can still contribute to higher target bits through bookkeeping.
- **Subsequence order:** Any selected subset of array positions is a subsequence in its original order, so only multiset counts affect attainable sums.
- **No real merging:** Carry operations represent selecting two smaller pieces for equal total value and do not add to `ans`.
- **Fixed 32 buckets:** They cover input powers through $2^{30}$, target below $2^{31}$, and one carry level above the input maximum.

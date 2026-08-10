## General

**Why the state needs more than just the alternating sum**

A subsequence is built in original index order by either skipping or taking each array value. If a chosen value becomes the first, third, fifth, and so on element of the subsequence, it is added to the alternating sum. If it becomes the second, fourth, sixth, and so on, it is subtracted.

This means the effect of the next chosen value depends on the current subsequence length parity:

- extending an even-length subsequence makes the new value occupy an even subsequence index, so the value is added;
- extending an odd-length subsequence makes the new value occupy an odd subsequence index, so the value is subtracted.

The algorithm must therefore remember both the current alternating sum and whether the chosen length is even or odd. It must also remember enough product information to maximize the product without exceeding `limit`.

The protected solution combines two related dynamic programs:

- `products` handles subsequences containing no zero and records their exact positive product;
- `without_zero` and `with_zero` are reachability bitsets used to detect whether product `0` is attainable, especially when no positive-product answer exists.

Separating zero is powerful. Once a subsequence contains a zero, its product is always zero no matter which later values are selected. There is no reason to keep many identical product-zero entries. Nevertheless, its alternating sum still changes when later values are appended, so zero-containing subsequences need their own sum-and-parity reachability state.

**Representing many alternating sums with one integer**

All `nums[i]` are nonnegative. Let

`S = sum(nums)`.

The alternating sum of any subsequence lies between `-S` and `S`. The source maps mathematical sum `x` to bit position `S + x` in an integer of width `2S + 1`. The middle bit at offset `S` represents sum zero.

For each pair of bitsets, index `0` represents reachable even-length subsequences and index `1` represents reachable odd-length subsequences. A set bit means that at least one non-empty subsequence of that category reaches the corresponding sum.

Bit shifts update every reachable sum simultaneously:

- appending positive value `v` to an even-length subsequence produces an odd length and adds `v`, so its bits shift left by `v`;
- appending `v` to an odd-length subsequence produces an even length and subtracts `v`, so its bits shift right by `v`.

The mask `(1 << width) - 1` removes bits shifted beyond the valid upper boundary. Right shifts naturally discard bits below zero.

If `abs(k) > S`, no subsequence can possibly have alternating sum `k`, so the early return of `-1` is sound.

**The zero-free and zero-containing reachability bitsets**

`without_zero = [even_without, odd_without]` describes non-empty subsequences selected from processed values that contain no zero. `with_zero = [even_with, odd_with]` describes non-empty subsequences that contain at least one zero.

When the current value `v` is positive, the source first snapshots all four bitsets. It updates the zero-free pair by preserving skipped subsequences and adding extensions:

- new even zero-free states are old even states plus old odd states shifted right by `v`;
- new odd zero-free states are old odd states plus old even states shifted left by `v`, plus the singleton subsequence `[v]` at sum `v`.

The zero-containing pair follows the same parity and sum transitions, but no singleton is added because a positive singleton contains no zero.

When `v = 0`, adding or subtracting the value does not change the alternating sum; it only flips length parity and changes the “contains zero” category when this is the first selected zero. Therefore:

- even zero-containing states include previously even zero-containing subsequences that skip zero, previously odd zero-containing subsequences that append it, and odd zero-free subsequences that append their first zero;
- odd zero-containing states analogously include old odd zero-containing, old even zero-containing, old even zero-free, and the singleton `[0]`.

The zero-free bitsets remain unchanged on a zero iteration because their only valid action is to skip that zero.

Snapshots are essential in all transitions. They guarantee that one input position is used at most once. Updating an odd state and immediately using it to update an even state would accidentally select the same array element multiple times.

**Tracking exact positive products**

The dictionary `products` maps a reachable positive product `p` to two bitsets: alternating sums reachable with even and odd subsequence lengths, using only nonzero selected values and having product exactly `p`.

For each positive input value `v`, a fresh `additions` dictionary collects states that use this occurrence:

- if `v <= limit`, the singleton `[v]` creates product `v`, odd length, and sum `v`;
- for every existing product `p`, the extension has product `p * v`;
- if `p * v > limit`, that extension is discarded permanently because all values are nonnegative integers and every nonzero selected value is positive, so later multiplication cannot reduce the product;
- otherwise, odd states for `p` shift right by `v` into even states for `p * v`, and even states shift left into odd states.

The loop iterates over `list(products.items())`, a snapshot of states from before the current element. This again prevents reuse of the same array position. Only after all extensions are calculated are `additions` merged into `products`. Existing dictionary entries remain in place, representing the choice to skip `v`.

Zero is never inserted into `products`. Its product is handled completely by `with_zero`, while zero-free alternating-sum reachability remains available for transitions in which a zero is selected later.

**Choosing the final answer**

The bit `1 << (S + k)` represents the target alternating sum. The source scans every positive product state. If either parity bitset contains the target bit, some non-empty zero-free subsequence has that exact product and alternating sum. Taking the maximum such product gives the best positive answer not exceeding `limit`.

If a positive answer exists, it is always at least `1` and therefore better than product zero. If no positive answer exists, the source checks the union of the even and odd `with_zero` bitsets. A target bit there proves that a non-empty zero-containing subsequence reaches `k`, so the correct answer is `0`. If neither category reaches the target, it returns `-1`.

This ordering correctly distinguishes three outcomes that a simpler DP could confuse: the best positive product, a valid product of zero, and no valid subsequence.

**Why the dynamic program is complete**

Process the array from left to right. Every recorded state corresponds to a real subsequence of the processed prefix because it is created only as a singleton or by extending a previously real subsequence with the current position. Conversely, take any non-empty subsequence of the processed prefix. If it omits the current value, its prior state is preserved. If it uses the current value, removing its last element yields a subsequence represented before the iteration, and the appropriate parity shift reconstructs its alternating sum. The product dictionary reconstructs it when all chosen values are positive and its product is within the limit; the zero-containing bitsets reconstruct it when at least one chosen value is zero.

By induction, every relevant feasible subsequence is represented and no transition violates index order. The final maximum therefore considers exactly the feasible positive products, with the zero reachability check covering the remaining valid product class.

## Complexity detail

Let `n = len(nums)`, `L = limit`, and `S = sum(nums)`. There are `2S + 1` possible alternating sums and two parity states.

At most `L` distinct positive product keys can exist because every key is an integer from `1` through `L`. For each of `n` values, the source may inspect every product key and perform constant many bitset shifts and OR operations. Treating an operation on a width-`O(S)` bitset as `O(S)` gives the manifest bound `O(nLS)` time. The four global reachability bitsets add only `O(nS)` work, which is dominated when `L \ge 1`.

More precisely, Python stores a bitset integer in machine-word-sized limbs, so a shift or OR costs `O(\lceil S / w \rceil)` word operations for word size `w`. The practical bound can be written as `O(nL\lceil S/w\rceil)`, plus dictionary overhead. Many product values may be unreachable, so the observed number of dictionary entries can be much smaller than `L`.

Each product key stores two width-`O(S)` bitsets, requiring `O(LS)` bits in the abstract analysis. `additions` can temporarily hold another comparable set during one iteration. The four reachability bitsets use `O(S)` bits. Thus the stated auxiliary-space bound is `O(LS)`. Python object and hash-table overhead increases constants but does not change that asymptotic bound.

The early impossibility test takes `O(n)` time to compute `S`. The final scan is `O(LS)` under bit-operation accounting and is dominated by the full transition work.

## Alternatives and edge cases

- **Three-dimensional boolean table:** A direct state such as `dp[parity][sum][product]` expresses the same recurrence and can be easier to invent, but iterating every sum separately costs large constants. Integer bitsets perform all sum transitions in parallel.
- **Store only the maximum product for each sum and parity:** This is unsafe because multiplication and the upper limit do not preserve a simple dominance order. A smaller current product may accept a later factor that would push a larger product beyond `limit`, and can ultimately become the best feasible result.
- **Enumerate all subsequences:** There are `2^n - 1` non-empty subsequences, which is infeasible for `n = 150`.
- **Merge product zero into the ordinary product dictionary:** It can be made correct, but zero is special because multiplying by later values never changes it. The protected separation avoids repeatedly materializing one identical product key while retaining all alternating-sum possibilities.
- **Ignore length parity:** Alternating sum is based on positions inside the chosen subsequence, not positions in `nums`. Without parity, the algorithm cannot know whether the next selected value must be added or subtracted.
- **Use the original array index for the sign:** Skipped elements do not occupy subsequence positions. The sign flips only when an element is selected.
- **Empty subsequence:** It would have product and sum conventions that could falsely make `k = 0` appear feasible. All source states are explicitly non-empty; the zero sum is added only by a real singleton zero or a real extension.
- **Target outside `[-S,S]`:** The early `abs(k) > S` test correctly returns `-1` before constructing the bit range.
- **Zero as the only valid product:** The positive-product scan intentionally leaves `answer = -1`, after which `with_zero` can return `0`. Returning immediately after the positive scan without this check would be wrong.
- **Value one:** Multiplying by one keeps the same product key, but it still flips parity and changes the alternating sum. The temporary `additions` dictionary and later OR merge preserve both using and skipping that occurrence.
- **Repeated values:** Processing positions sequentially makes equal values distinct choices. Snapshot iteration prevents one occurrence from being selected twice.
- **Product pruning:** It is safe only because every nonzero factor is a positive integer. Once a positive product exceeds `limit`, later nonzero multiplication cannot bring it back down, while choosing zero belongs to the separate zero-containing category.
- **Inclusive product limit:** States with product exactly `limit` are retained because the source discards only `next_product > limit`.
- **Large bit shifts:** The mask is needed after left shifts to keep only sums through `S`. Right shifts automatically discard sums below `-S` in the offset representation.

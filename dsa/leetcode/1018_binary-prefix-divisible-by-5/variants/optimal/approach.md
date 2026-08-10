## General

**How one more binary digit changes a prefix**

Let the numeric value of the prefix ending just before the current bit be `P`. Appending a binary bit `v` shifts every existing digit one place to the left and places `v` in the units position. Numerically, the new prefix is

$$
P_{\text{new}} = 2P + v.
$$

For example, binary `101` has value five. Appending zero gives `1010`, whose value is ten, and appending one would give `1011`, whose value is eleven. This recurrence makes a left-to-right traversal natural: the next prefix depends only on the preceding prefix and the next bit.

A tempting implementation would store the complete value and repeatedly compute `P = 2 * P + v`. The array may contain `10^5` bits, however, so the full prefix can have tens of thousands of decimal digits. Fixed-width languages would overflow quickly, and even Python's arbitrary-precision integers would spend increasing time and memory manipulating enormous numbers.

The task never asks for the prefix values themselves. It asks only whether each value is divisible by five. Divisibility depends solely on the remainder modulo five, so all information beyond that remainder can be discarded.

**Why keeping only the remainder loses nothing**

Suppose `P = 5q + r`, where `r` is the remainder and therefore lies between zero and four. After appending `v`,

$$
2P + v = 2(5q + r) + v = 10q + 2r + v.
$$

The term `10q` is divisible by five. It contributes nothing to the new remainder. Consequently,

$$
(2P + v) \bmod 5 = (2r + v) \bmod 5.
$$

This identity is the entire reason the algorithm can remain constant-sized. Whether the discarded quotient `q` is small or unimaginably large makes no difference to the next remainder.

The variable `x` stores this remainder. It begins at zero, which is the value of the empty prefix modulo five. For each input bit `v`, the statement `x = (x << 1 | v) % 5` computes the next remainder.

The expression `x << 1` shifts `x` left by one bit and is numerically equal to `2 * x`. Because a left shift makes the low bit zero and `v` is guaranteed to be either zero or one, bitwise OR with `v` puts that bit into the newly opened low position. Therefore, `x << 1 | v` equals `2 * x + v` for every valid input. The parentheses ensure the complete append operation is reduced modulo five afterward.

After the update, `ans.append(x == 0)` adds a Boolean for the prefix that now includes `v`. A number is divisible by five exactly when its remainder modulo five is zero. The comparison produces Python `True` or `False` directly, so no later conversion is needed.

**A step-by-step trace**

Take `nums = [0, 1, 1]`. Initially `x = 0` and `ans` is empty.

The first bit is zero. Shifting zero and appending zero still gives zero, and zero modulo five is zero. The code appends `True`. This correctly recognizes that the one-bit prefix `0` represents the number zero, which is divisible by five.

The second bit is one. The update computes `2 * 0 + 1 = 1`, whose remainder is one. The code appends `False`. Notice that the written prefix `01` is allowed in the input even though standard integer representations do not use a leading zero; its numeric value is still one.

The third bit is one. The update computes `2 * 1 + 1 = 3`, whose remainder is three. The code appends another `False`. The final result is `[True, False, False]`.

For a trace that demonstrates remainder reuse, consider prefix value `13`, whose remainder modulo five is three. Appending bit one creates `27`. The algorithm does not need thirteen: it computes `2 * 3 + 1 = 7` and reduces that to remainder two, exactly matching `27 \bmod 5`.

**The invariant that establishes correctness**

After processing the bit at index `i`, `x` equals `x_i \bmod 5`, where `x_i` is the actual integer represented by `nums[0..i]`. At the same moment, `ans[i]` is `True` exactly when that remainder is zero.

Before any bit is processed, `x = 0` correctly represents the empty prefix's remainder. Assume the invariant holds before reading a bit `v`. Appending `v` makes the actual prefix value `2x_i + v`. The update uses the old remainder in precisely the congruent expression `(2 * x + v) % 5`. The modular identity above shows that the resulting `x` is the new full prefix's remainder. The appended comparison is therefore true exactly for a divisible prefix. By induction, the invariant holds at every index.

When traversal ends, one Boolean has been appended for every input bit and in the same order. No prefix is skipped, and no result is delayed or reordered. Thus the returned list satisfies both the value requirement and the required indexing.

**Why the remainder must be taken on every iteration**

If the code postponed `% 5` until the end, `x` would become the full binary integer, bringing back the overflow and large-integer problem. Reducing after every digit is safe because modular equivalence is preserved by multiplication and addition. It also ensures `x` is always one of only five states: zero, one, two, three, or four. The shift therefore acts on a tiny integer regardless of the length of `nums`.

This can be viewed as a five-state machine. Each state is the current remainder, and each input bit chooses a transition to `(2x + v) % 5`. State zero is the accepting state for the current prefix. That viewpoint explains why no earlier bits need to be retained once their remainder has been incorporated.

## Complexity detail

Let `N = len(nums)`. The `for` loop processes each of the `N` bits exactly once. Every iteration performs one shift, one bitwise OR, one remainder operation on a value smaller than ten, one comparison, and one append. All are constant-time operations here because `x` is always below five. Total time is therefore `O(N)`.

This is asymptotically optimal. The output contains `N` Boolean values, and every input bit can change its corresponding prefix result and all later remainders. Any correct method must at least read the full input and produce the full output, requiring `\Omega(N)` time.

The manifest's `O(1)` space bound refers to auxiliary space excluding the required result. Apart from `ans`, the method stores only `x`, the current bit `v`, and loop machinery. The remainder never grows with `N`, so auxiliary storage is `O(1)`. The returned list itself contains `N` Booleans and necessarily uses `O(N)` output space.

## Alternatives and edge cases

- **Build every full prefix integer:** This follows the same recurrence but omits the per-step modulo. It is mathematically simple, yet it overflows fixed-width types and makes Python arithmetic progressively more expensive. Retaining only the remainder is both safer and more efficient.
- **Convert each prefix slice independently:** Joining `nums[0..i]` into text and parsing it repeats almost all earlier work for every index, leading to quadratic total input processing and many temporary objects.
- **Use decimal divisibility rules:** Rules based on the final decimal digit do not apply directly to a binary digit stream. The modular recurrence works in any base and uses the actual base-two construction.
- **Store a table of five transitions:** A small table could map each pair of current remainder and next bit to the next remainder. That is equivalent to the formula and can remove arithmetic, but it is less transparent and does not improve the asymptotic bounds.
- **Use addition instead of bitwise OR:** `(x * 2 + v) % 5` or `((x << 1) + v) % 5` is equally correct. OR works only because valid `v` is zero or one and the shifted value's low bit is zero.
- **Leading zeroes:** Prefixes may begin with one or many zeroes. They do not require special handling because appending zero to remainder zero keeps it zero, and numeric value is independent of written leading zeroes.
- **The value zero:** Zero is divisible by five. Therefore, any all-zero prefix correctly produces `True`.
- **A one-element array:** The loop appends exactly one answer. Input `[0]` returns `[True]`, while `[1]` returns `[False]`.
- **Long input:** Even at the maximum length of `10^5`, `x` never exceeds four after an iteration. The method's numeric state is completely independent of the potentially enormous full prefix.
- **Why equality with zero is enough:** There is no need to test `x % 5` again when appending. The assignment has already reduced `x` into the canonical remainder range.
- **Order of operations:** The modulo must apply after appending the new bit. Reducing the old `x` is already implicit in the invariant, but testing before the update would report divisibility for the previous prefix rather than the current one.

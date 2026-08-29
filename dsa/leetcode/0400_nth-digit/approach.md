## General

**Group the infinite sequence by number width**

Writing the concatenated sequence until position `n` would perform work proportional to `n` and would be far too slow for positions near $2^{31}-1$. Decimal numbers have a regular block structure:

- one-digit numbers run from `1` through `9`;
- two-digit numbers run from `10` through `99`;
- three-digit numbers run from `100` through `999`;
- and so on.

Every number in one block contributes the same number of digits. The algorithm skips entire blocks until it reaches the block containing the requested position, then identifies the exact number and digit using division and remainder.

**Describe one block**

For width `k`:

- the first number is $10^{k-1}$;
- there are $9\cdot10^{k-1}$ such numbers;
- the block contains $k\cdot9\cdot10^{k-1}$ digits.

The exact solution stores `k` as the current width and `cnt` as the number of values in that block. It starts with `k = 1`, `cnt = 9`.

After skipping a block, `k += 1` moves to the next width and `cnt *= 10` changes `9` to `90`, then `900`, and so forth.

**Keep `n` relative to the current block**

Initially, `n` is one-based within the complete infinite sequence. While the current block contains fewer digits than the remaining position, the algorithm subtracts the whole block:

```text
while k * cnt < n:
    n -= k * cnt
    k += 1
    cnt *= 10
```

After each subtraction, `n` becomes the one-based position within the sequence beginning at the next block.

When the loop stops, `1 <= n <= k * cnt`, so the desired digit lies among the `k`-digit numbers.

**Why the loop condition is strict**

The condition is `k * cnt < n`, not `<= n`. If `n` equals the exact number of digits in the current block, the requested position is the final digit of that block and must remain there.

For example, the one-digit block contains nine digits. With `n = 9`, the answer is digit `9`; subtracting the block on equality would incorrectly move to the two-digit block with a zero relative position. The strict comparison preserves boundary positions.

If `n = 10`, then `9 < 10` is true. The algorithm subtracts nine, leaving `n = 1` inside the two-digit block, whose first digit is the `1` in `10`.

**Convert from one-based position to a number offset**

Inside a width-`k` block, `n` is still one-based. Subtracting one turns it into a zero-based digit offset:

$$
z=n-1.
$$

Every number occupies `k` consecutive digit positions. Therefore:

- `z // k` is the zero-based number offset within the block;
- `z % k` is the zero-based digit index within that number.

The exact source computes

```text
num = 10 ** (k - 1) + (n - 1) // k
idx = (n - 1) % k
```

Adding the number offset to the first `k`-digit value identifies the containing number. The remainder identifies which decimal digit of that number is requested, counting from the left.

**Why subtracting one prevents off-by-one errors**

Without converting to zero-based indexing, positions divisible by `k` would incorrectly appear to belong to the next number. For example, in the two-digit block:

- relative positions `1` and `2` belong to `10`;
- positions `3` and `4` belong to `11`.

At relative position `2`, `(2 - 1) // 2 = 0`, correctly selecting the first number, and `(2 - 1) % 2 = 1`, selecting its second digit. Using `2 // 2` would incorrectly select number offset one.

**Trace `n = 11`**

The one-digit block has `1 * 9 = 9` digits, which is less than eleven. Subtracting it leaves relative position `2` in the two-digit block. Now `k = 2`, `cnt = 90`.

The containing number is

$$
10^{1}+\left\lfloor\frac{2-1}{2}\right\rfloor=10+0=10.
$$

The digit index is

$$
(2-1)\bmod2=1.
$$

Converting `10` to the string `"10"` and reading index one returns character `"0"`, which `int` converts to integer zero.

**Another block-boundary trace**

The one- and two-digit blocks together contain

$$
9+90\cdot2=189
$$

digits. Position `189` is the final `9` of number `99`. The loop skips the first block but retains the two-digit block because its remaining position equals `180`. The formulas select offset `(180 - 1) // 2 = 89`, giving number `99`, and digit index one, giving its final digit.

Position `190` subtracts both complete blocks and becomes position one in the three-digit block, selecting the first digit of `100`.

**Why the result is correct**

Each loop iteration removes a complete block that lies entirely before the requested digit, preserving the desired digit’s relative position in the unskipped suffix. When the loop stops, the position is guaranteed inside the current fixed-width block.

Division by `k` partitions that block into consecutive groups corresponding one-to-one with its numbers, while remainder selects the position inside a group. Adding the block’s first number maps the group index to the exact integer. Thus the extracted digit is precisely the original one-based `n`th digit.

## Complexity detail

The loop advances once per decimal width. The width containing position `n` is $O(\log n)$, so block skipping takes $O(\log n)$ time. Exponentiation and converting the selected number to decimal involve at most its digit width, also $O(\log n)$ in a general unbounded-input model. Total time is $O(\log n)$.

The arithmetic state uses a constant number of integers. The exact final expression creates `str(num)`, whose length is $O(\log n)$ for unbounded `n`; strict language-level auxiliary space is therefore $O(\log n)$. Under the stated fixed 32-bit input constraint, the selected number has a bounded number of digits, so this storage is constant and the manifest’s $O(1)$ space bound applies.

An arithmetic digit extraction can avoid the string entirely by dividing `num` by the appropriate power of ten and taking modulo ten.

## Alternatives and edge cases

- **Generate and concatenate numbers:** This is easy to understand but needs $O(n)$ time and storage near the requested position. Block arithmetic skips almost all digits.

- **Binary search for the containing number:** Compute how many digits appear through a candidate integer and binary-search the number. This can work in $O(\log n)$ time but is more complex than directly skipping the small number of width blocks.

- **Arithmetic digit extraction:** After finding `num` and `idx`, compute `(num // 10 ** (k - 1 - idx)) % 10`. This preserves $O(1)$ auxiliary space without a string conversion.

- **Positions `1` through `9`:** The first block is not skipped, `num = n`, `idx = 0`, and the digit is the number itself.

- **First digit of a block:** After all earlier blocks are subtracted, relative `n = 1`; quotient and remainder are both zero, selecting the first digit of the first number.

- **Last digit of a block:** The strict loop condition keeps equality in the current block, and zero-based arithmetic selects the final number’s final digit.

- **Zeros in the sequence:** Zero does not appear as a standalone starting number, but it appears inside values such as `10` and `100`; string or arithmetic extraction returns it normally.

- **One-based versus zero-based positions:** All block subtraction keeps `n` one-based. The single `(n - 1)` conversion is what makes quotient and remainder align correctly.

- **Large input:** Only about ten width iterations are needed under the 32-bit constraint, regardless of the billions of preceding digits.

- **Integer overflow in other languages:** Products such as `k * cnt` and powers of ten should use a wide integer type. Python expands integers automatically.

## General

**View IPv4 addresses as consecutive 32-bit integers**

CIDR alignment and block size are easiest to reason about numerically. The solution converts the four decimal octets into one unsigned integer by repeatedly shifting the accumulated value eight bits left and combining the next octet.

For octets `a.b.c.d`, the result is

`(a << 24) | (b << 16) | (c << 8) | d`.

Consecutive IP addresses then correspond to consecutive integers. The required interval begins at `current` and contains `remaining` addresses.

**CIDR blocks have power-of-two sizes and alignment**

A prefix length `p` fixes the first `p` bits and leaves `32 - p` bits free. Such a block contains

`2^(32 - p)`

addresses. Its base address must be divisible by that block size, because all free low bits of the base are zero.

At every iteration, the next block must begin exactly at `current`. Beginning later would leave a gap; beginning earlier would cover an address outside the requested interval.

**Find the largest block aligned at the current address**

For a positive integer, `current & -current` isolates its lowest set bit. Its value is the largest power of two dividing `current`, which is exactly the largest power-of-two block size aligned at that address.

When `current == 0`, the expression is zero even though address zero is aligned to every IPv4 block size. The special case replaces it with `1 << 32`, the size of the entire IPv4 space.

**Do not exceed the remaining interval**

The largest power of two no greater than `remaining` is

`1 << (remaining.bit_length() - 1)`.

The chosen block size is the smaller of this remaining-size limit and the alignment limit. It is therefore:

- A power of two.
- Properly aligned at `current`.
- No larger than the uncovered suffix.
- The largest block satisfying both restrictions.

**Convert size to prefix length**

For a power-of-two `block_size`, `block_size.bit_length() - 1` is its base-two exponent. If that exponent is `b`, the block leaves `b` address bits free, so the prefix length is `32 - b`.

A size-one block becomes prefix 32. A size-eight block becomes prefix 29.

The integer base is converted back to dotted decimal by extracting the groups shifted by 24, 16, 8, and 0 bits and masking each with 255.

**Advance without gaps or overlap**

After appending the block, the solution adds its size to `current` and subtracts the same amount from `remaining`. The next iteration therefore begins at the first address not yet covered.

Every block is disjoint from earlier blocks, and their concatenated ranges cover one continuous prefix of the requested interval. When `remaining` reaches zero, coverage is exact.

**Why taking the largest legal block is optimal**

Any exact cover must place some block at the first uncovered address. That block cannot be larger than the chosen one: a larger power of two would violate either base alignment or the remaining range.

If another solution starts with a smaller block, the address interval covered by the greedy block can be partitioned into aligned smaller CIDR blocks, so using the single greedy block never requires more blocks for that prefix. Replacing those initial smaller blocks with the greedy block cannot hurt the remaining suffix.

Applying the same exchange argument after advancing proves inductively that the greedy decomposition uses the minimum possible number of blocks.

**Trace the alignment idea**

At address `255.0.0.7`, the integer is odd, so the largest aligned block has size one and prefix 32. The next address ends in binary `1000`, making it aligned to size eight. If at least eight addresses remain, the algorithm emits a `/29` block. It then advances to address 16, where the final uncovered address can be emitted as another `/32`.

## Complexity detail

Let `B` be the number of returned CIDR blocks. Each loop iteration emits one block and performs constant-width 32-bit arithmetic and formatting, so time is `O(B)`.

For a consecutive interval, `B` is logarithmic in the range length up to the fixed 32-bit address-width contribution, commonly written `O(log n)`. The returned list and strings use `O(B)` output space; auxiliary working space apart from the output is `O(1)`.

## Alternatives and edge cases

- **Emit every address as `/32`:** This is exact but uses `n` blocks and is not minimal.

- **Choose only by remaining size:** A large block may start at a misaligned address and cover a different CIDR range. Both size and alignment constraints are mandatory.

- **Choose only by alignment:** The aligned block may extend beyond the requested final address. Limit it by the largest power of two no greater than `remaining`.

- **Starting address zero:** `current & -current` needs the explicit `2^32` alignment interpretation.

- **Single address:** Remaining size forces block size one and prefix 32.

- **Crossing an octet boundary:** Integer arithmetic handles carries automatically; dotted formatting is performed only for emitted bases.

- **Exact coverage:** Advancing by each block size prevents both gaps and overlaps.

- **IPv4 limit:** The contract guarantees every implied address remains valid, so no overflow handling is required.

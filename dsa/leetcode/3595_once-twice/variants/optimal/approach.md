## General

All ordinary values appear three times. Counting every bit position modulo three makes those values disappear, leaving a mixture of:

- the once-occurring value `A`;
- the twice-occurring value `B`.

The source first finds a bit where `A` and `B` differ. It then partitions the array by that bit, placing the two exceptional values in separate groups. A second modulo-three pass recovers one exception from each group.

**Two-register modulo-three counter**

For every bit position, `seen_once` and `seen_twice` encode its occurrence count modulo three:

- `00` means count zero modulo three;
- `01` means count one;
- `10` means count two.

For each `value`:

`seen_once=(seen_once ^ value) & ~seen_twice`

toggles bits into or out of the once state while excluding bits currently assigned to twice.

Then:

`seen_twice=(seen_twice ^ value) & ~seen_once`

updates the twice state while excluding the newly computed once state.

At a single bit, repeated appearances cycle:

`00 -> 01 -> 10 -> 00`.

Because bitwise operations process all positions in parallel, two integers maintain the modulo-three counts for the complete 32-bit patterns.

**What remains after the first pass**

Every value appearing three times contributes zero modulo three at every bit.

For a bit:

- if only `A` has it, total count modulo three is one and the bit appears in `seen_once`;
- if only `B` has it, its two occurrences give state two and the bit appears in `seen_twice`;
- if both have it, contribution is `1+2=3` and vanishes;
- if neither has it, it is zero.

Therefore:

`seen_once | seen_twice`

has exactly the bit positions where `A` and `B` differ—the bit pattern of `A XOR B`.

The two exceptional values must be different because one array element value cannot simultaneously have total frequency one and two. Hence at least one differing bit exists.

**Choosing a separating bit**

`x & -x` isolates the least significant set bit of a nonzero integer. The source applies it to the union above, producing `differing_bit`.

Exactly one of `A` and `B` has this bit. Partitioning all input values by it places the two exceptions into different groups.

Every ordinary triple consists of three identical values, so all three copies go to the same group and still cancel modulo three.

**Second pass**

Each group receives its own once/twice registers.

After the pass:

- the group containing `A` has `A` in its once register;
- the group containing `B` has `B` in its twice register;
- triple values have vanished.

If `seen_once & differing_bit` is nonzero in the global first-pass result, the once-occurring exception `A` has separating bit one. It is therefore in the `one` group, so return:

`[one_once, zero_twice]`.

Otherwise `A` is in the zero group and `B` in the one group, so return:

`[zero_once, one_twice]`.

This preserves the required output order: once-occurring first, twice-occurring second.

**Why one pass alone is insufficient**

The global modulo-three registers contain different bits from `A` and `B`, but shared one bits cancel because one plus two is three. They do not directly store the two complete values.

Separating the exceptions ensures their bits no longer interact, allowing each complete pattern to survive in its correct register.

**Negative integers**

Python bitwise operations use an unbounded two’s-complement-style model for negative numbers. XOR, complement, lowest-set-bit isolation, and partition testing remain consistent across all sign-extension bits.

The modulo-three register formulas are standard bitwise state transitions and can retain a negative exceptional integer as a negative Python integer. This is essential because the constraints include the signed 32-bit range.

## Complexity detail

The algorithm makes two linear passes. Every element causes a constant number of bitwise operations, so time is `O(n)`.

It stores a fixed number of integer registers and one separating bit. Auxiliary space is `O(1)`, satisfying the explicit requirement.

## Alternatives and edge cases

- **Frequency dictionary:** It is simpler but uses `O(n)` space in the worst case and violates the required constant-space bound.
- **Sort the array:** Frequencies become adjacent, but sorting costs `O(n\log n)` and may mutate input.
- **Per-bit array of 32 counters:** It uses constant space and can find global modulo counts, but still needs separation logic to distinguish once from twice.
- **Use XOR only:** Triples do not cancel under XOR because three copies reduce to one copy, so ordinary values would remain.
- **Shared one bits of A and B:** They vanish in the first pass, which is why direct register output would be incomplete.
- **Least significant differing bit:** Any differing bit would separate the exceptions; choosing the lowest is a convenient constant-time method.
- **Triple values in a partition:** All identical copies choose the same side and continue to cancel.
- **Once value has separator bit:** Global once register identifies this orientation and selects the correct return registers.
- **Twice value has separator bit:** The alternate return branch handles it.
- **Zero as an exception:** Its bits are all zero, but it is separated from a distinct other exception by one of the other value’s set bits.
- **Negative exceptions:** Sign-extension behavior remains consistent under the same partition and modulo formulas.
- **Minimum signed integer:** `x & -x` works with Python’s arbitrary-precision integers, avoiding fixed-width overflow on negation.
- **Output order:** Orientation logic is necessary; simply returning the two group residues could swap once and twice.
- **Input guarantee:** The proof relies on exactly one frequency-one value, one frequency-two value, and every other frequency exactly three.
- **No input mutation:** Both passes read values only.

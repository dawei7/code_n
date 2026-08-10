## General

**Characterize when one element can equal the whole OR**

For nonnegative integers, say `a` is a bit-subset of `x` when every bit set in `a` is also set in `x`. The source tests this relation with

`(a | x) == x`.

Suppose a subarray contains an occurrence of value `x`. Its total OR equals `x` exactly when every other element in the subarray is a bit-subset of `x`:

- including `x` ensures all bits of `x` appear in the OR;
- allowing only bit-subsets ensures no additional bit appears.

Therefore a good subarray can be counted through an index whose value dominates the bits of every element in that interval.

**Choose a unique witness to avoid duplicate counting**

A good subarray may contain its OR value more than once. For example, `[3,3]` has OR three and two possible witness indices. Counting it under both would overcount.

The exact source assigns every good subarray to its **leftmost** occurrence of the OR value. This differs from the manifest summary, which says “rightmost.” The boundary behavior makes the source's convention unambiguous:

- an equal value to the left blocks index `i` from being the assigned witness;
- an equal value to the right is allowed, because `i` remains the leftmost occurrence.

For each index `i` with `x=nums[i]`, the algorithm finds:

- `l[i]`: the nearest index to the left that is not a strict bit-subset of `x`; this includes an incompatible value or an equal `x`;
- `r[i]`: the nearest index to the right whose value is not any bit-subset of `x`; an equal value is a subset and does not block.

Then every interval with

$$
l[i]<left\le i\le right<r[i]
$$

has OR `x` and uses `i` as its leftmost OR-valued witness.

**Why strict subset on the left is written with a numeric comparison**

The first pass pops while

`nums[top] < x and (nums[top] | x) == x`.

For nonnegative integers, a bit-subset of `x` is numerically at most `x`. It is strictly smaller exactly when it is a proper bit-subset. Thus the two conditions mean “the stack-top value contributes no forbidden bit and is not equal to the witness.”

Such a value may safely lie to the left inside an interval assigned to `i`, so it is removed while searching for a blocker.

An equal value is not popped because the strict numeric comparison fails. If an interval started at or before that equal occurrence, `i` would not be the leftmost witness. An incomparable value having a bit outside `x` is also not popped because its OR with `x` differs from `x`; including it would make the interval OR larger.

After popping all allowable strict subsets, the remaining top is the closest blocking index, or minus one if none exists.

**Why a stack can find the blocker without rescanning**

An index removed earlier was dominated by a later stack value. If that later value is itself popped as a strict bit-subset of the current `x`, transitivity says every value it dominated is also a bit-subset of `x`. Those hidden indices cannot be blockers.

If a later stack value is not removable, it is closer to `i` than every index beneath it and is already the nearest required blocker. This is the usual monotone-stack compression argument, with bit-subset order replacing ordinary less-than order.

Each index enters the stack once and leaves at most once.

**Right boundary allows every subset, including equality**

The reverse pass pops while

`(nums[top] | nums[i]) == nums[i]`.

There is no strict comparison. Every bit-subset to the right is allowed inside an interval assigned to `i`, including another occurrence equal to `nums[i]`. That later equal occurrence does not stop `i` from being the leftmost witness.

The nearest remaining stack index has a bit absent from `nums[i]` and would make the interval OR larger, so it becomes `r[i]`. If no blocker exists, `r[i]=N`.

The same transitive popping argument proves that all skipped indices between `i` and `r[i]` are subsets of the witness value.

**Count endpoint combinations**

There are

$$
i-l[i]
$$

legal left endpoints: `l[i]+1` through `i`.

There are

$$
r[i]-i
$$

legal right endpoints: `i` through `r[i]-1`.

Every left choice combines independently with every right choice, so index `i` contributes

$$
(i-l[i])(r[i]-i)
$$

subarrays. The source sums this over all indices.

**Why every good subarray appears exactly once**

Take a good interval and call its OR `x`. Choose the leftmost index `i` inside the interval with `nums[i]=x`.

Every interval element is a bit-subset of `x`; otherwise the OR would have an extra bit. Before `i` inside the interval there is no equal `x` by the witness choice, so all those left-side elements are strict subsets. To the right, subsets including equal values are allowed. The interval endpoints therefore lie inside `i`'s computed boundaries and the product counts it.

No other index can count the same interval. An earlier element is not equal to the OR, and a later equal element has `i` as an equal blocker on its left. The assignment is unique.

For `[3,3]`, index zero counts `[0,0]` and `[0,1]`, while index one counts only `[1,1]`. This confirms the leftmost convention.

For `[4,2,3]`, each singleton is counted. Witness three at index two allows value two to its left because two is a bit-subset of three, counting `[2,3]` by values. Value four is incompatible with three and forms the blocking boundary, so the full interval is excluded.

## Complexity detail

Each index is pushed once and popped at most once in each of the two stack passes. Both passes take `O(N)` time. Filling arrays and summing contributions are also linear, so total time is `O(N)`.

Arrays `l` and `r` and the stack each use `O(N)` space. The second stack reuses the variable after the first is discarded, but the two boundary arrays remain. Total auxiliary space is `O(N)`. These bounds match the manifest, although its witness-direction wording does not match the source.

The answer can be `N(N+1)/2` when every subarray is good. Python integers handle it; fixed-width implementations should use 64-bit storage.

## Alternatives and edge cases

- **Enumerate every subarray:** Maintain its OR and search for a matching element, but there are `O(N^2)` intervals. The witness-boundary products count many intervals together.
- **Store all distinct ORs ending at each position:** This is useful for many OR-subarray problems and gives an extra bit-width factor, but it still needs witness-presence accounting. The subset stacks exploit this problem's stronger condition.
- **Assign to the rightmost witness:** A symmetric algorithm is possible, but equal values would need opposite boundary treatment. The protected source assigns to the leftmost witness.
- **Use numeric `<=` without the OR test:** Numeric order does not imply bit-subset order. For example, a smaller number can contain a bit absent from a larger one.
- **Equal witness values:** Equality blocks on the left and is allowed on the right, preventing duplicates.
- **Zero:** Zero is a subset of every value. A zero witness can dominate only zeros because any positive value has an outside bit.
- **All equal values:** Every subarray is good and is assigned to its leftmost index.
- **Single element:** It is always good because its OR equals itself; the product contributes one.
- **Incompatible nearby value:** It becomes a boundary even if it is numerically smaller, because bit containment—not magnitude—is decisive.
- **Nonnegative constraint:** The subset/numeric strictness equivalence relies on ordinary nonnegative bit representations, which the contract guarantees.
- **Manifest wording:** Do not describe this exact source as rightmost-witness counting; its equal-value boundary rules prove the opposite convention.

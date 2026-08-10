## General

**Run a modulo-three counter at every bit position**

The primary `Solution` uses two integer masks named `one` and `two`. Although each variable is one Python integer, every bit position behaves as an independent tiny state machine.

For a particular position, the pair `(one_bit, two_bit)` records how many one-bits have appeared there modulo three:

| Count modulo three | `one_bit` | `two_bit` |
|---:|---:|---:|
| 0 | 0 | 0 |
| 1 | 1 | 0 |
| 2 | 0 | 1 |

The state `(1, 1)` is deliberately never used. When another input number has a one at that position, the state cycles:

$$
(0,0)\rightarrow(1,0)\rightarrow(0,1)\rightarrow(0,0).
$$

When the input bit is zero, the state remains unchanged.

Because bitwise operations apply the same Boolean formula to every position simultaneously, two machine-word masks implement all of these counters in parallel.

**Read the first transition equation**

The new value of `one` is:

`(~x & one) | (x & ~one & ~two)`

There are two ways a position belongs in the new `one` mask.

First, if the current bit of `x` is zero and it was already in `one`, `~x & one` preserves it. A zero input should not advance the count.

Second, if the current bit of `x` is one and the old state was neither `one` nor `two`, this is the first occurrence modulo three. The term `x & ~one & ~two` sets it.

If a bit was already in `one` and `x` also has it, neither term keeps it, so it leaves `one` and advances toward the twice-seen state.

**Read the second transition equation**

The new value of `two` is:

`(~x & two) | (x & one)`

The term `~x & two` preserves a twice-seen bit when the current input bit is zero. The term `x & one` moves a bit from the old once-seen state into the twice-seen state when another one arrives.

If the old state was `two` and `x` contains one, both terms are zero, so the bit leaves `two`. It has now appeared three times modulo three and returns to state zero.

**Why simultaneous assignment is essential**

Python evaluates the complete right-hand side of:

`one, two = new_one_expression, new_two_expression`

before assigning either left-hand variable. Therefore, both formulas read the old `one` and old `two`.

That detail is required. The second expression uses `x & one` to recognize bits that were in the once-seen state before this input. If `one` were overwritten first in a separate statement, the second expression would see the new state and implement a different, incorrect transition.

**Why `one` is the final singleton**

Every number occurring three times contributes each of its set bits three times. Those bit positions complete a full state cycle and return to `(0, 0)`.

The unique number contributes its set bits once. Those positions finish in `(1, 0)`, meaning they are set in `one`. Positions absent from the singleton finish in state zero after all triple contributions cancel.

Thus `one` contains exactly the complete bit pattern of the singleton. The function returns it.

This reasoning works independently of input order. The finite-state update counts occurrences modulo three; the three copies do not need to be adjacent.

**Signed integers in Python**

Python bitwise NOT produces values consistent with an unbounded two’s-complement model. The masks may therefore become negative when their sign-extended high bits are set, but the Boolean state equations still work position by position. At completion, `one` has the same signed bit pattern as the unique Python integer, so it can be returned directly without a separate 32-bit sign conversion.

The file also contains `Solution2`, `Solution3`, `Solution4`, and `SolutionEX`, but the selected class is the first class named `Solution`. Those later classes are alternatives or a different frequency problem and are not part of the primary execution path.

## Complexity detail

Let $n$ be the number of input integers.

The primary loop processes each value once. It performs a fixed number of bitwise operations and one simultaneous assignment per element, so time is $O(n)$ under the contract’s fixed 32-bit value domain.

Only `one`, `two`, `x`, and iterator state are used. Their count does not grow with the array, giving $O(1)$ auxiliary space.

In Python, arbitrary-precision bitwise cost generally depends on operand width, but every input is within the signed 32-bit range and the state masks stay within the corresponding effective pattern. The manifest’s $O(n)$ time and $O(1)$ space are therefore appropriate.

The `collections` import is unused by the primary `Solution`; it supports a later alternative and does not create input-proportional state.

## Alternatives and edge cases

- **Count 32 bit positions explicitly:** Sum `(num >> i) & 1` modulo three for each position, with special handling for the sign bit in Python. It is easier to derive but scans the array 32 times.
- **Carry-mask formulation:** Update once-seen and twice-seen masks with XOR, compute their overlap as a carry, and clear bits that reached three. The file’s `Solution2` demonstrates this equivalent state machine.
- **Frequency dictionary:** It is simple and linear expected time but uses $O(n)$ extra memory.
- **Sort by value:** Triples become adjacent, allowing a grouped scan, but time rises to $O(n\log n)$.
- **Arithmetic set formula:** It needs $O(n)$ set storage. The file’s `Solution4` also uses `/`, so under Python 3 it returns a floating-point value rather than the required integer.
- **Counter subtraction alternative:** The file’s `Solution3` uses Python-2-style indexing on `.keys()`; in Python 3, the keys view is not subscriptable as written.
- **One value:** Its set bits move from state zero to `one` and are returned.
- **Negative singleton:** The bitmask state machine returns the signed value directly under Python’s bitwise semantics.
- **State disjointness:** Valid transitions preserve `one & two == 0`. Changing formula order or using newly updated state accidentally can violate the intended three-state encoding.
- **Malformed counts:** A value occurring twice would leave its bits in `two`, not `one`; multiple exceptional frequencies make the requested answer undefined.
- **Different problem in `SolutionEX`:** That class targets values appearing four times with one appearing twice, so its three masks and return value must not be substituted for this contract.

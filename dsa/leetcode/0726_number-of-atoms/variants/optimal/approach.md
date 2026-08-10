## General

**Why scanning from right to left simplifies multipliers**

In a chemical formula, a number appears after the thing it multiplies. It may be the count of one atom, as in `H2`, or the multiplier for a parenthesized group, as in `(OH)2`. A right-to-left scan encounters that number before it encounters the atom or closing parenthesis to which the number belongs.

The exact solution uses this direction so a parsed number can be held in one variable, `pending`, and applied to the next meaningful token on its left. If no written number exists, the implicit multiplier is one.

Nested groups add another requirement: an atom must receive the product of every enclosing group multiplier. The stack `multipliers` stores cumulative products. It begins with `[1]`, representing no enclosing multiplication.

**Parse a multi-digit number in reverse**

When the current character is a digit, the scanner consumes the entire consecutive digit run from right to left. Because the least significant digit is encountered first, it builds the value using `place`:

- Start with `factor = 0` and `place = 1`.
- Add `digit * place`.
- Multiply `place` by ten before reading the next digit to the left.

For the text `123`, the scan sees `3`, then `2`, then `1` and accumulates `3 + 20 + 100 = 123`. It stores that result in `pending` and uses `continue` because the index already points to the character immediately before the number.

Under a valid formula, this pending number belongs either to the atom immediately on its left or to a group whose closing parenthesis is immediately on its left.

**Entering a group while scanning backward**

When the scanner encounters `)`, it is moving backward into the parenthesized group. Every atom encountered until the matching `(` must be multiplied by the number that followed this closing parenthesis.

The solution appends

`multipliers[-1] * pending`

to the stack. This is a cumulative multiplier: it combines the new group’s factor with all outer groups already active. `pending` is then reset to one.

For example, while scanning `(ON(SO3)2)2` backward, the outer `)2` makes the current cumulative multiplier two. Reaching the inner `)2` pushes four, so atoms inside that nested group receive both factors.

When the scan later reaches `(`, it has moved out of the current group. Popping the stack restores the cumulative multiplier of the surrounding context.

**Extract a complete atom name**

An atom name begins with one uppercase letter and may continue with lowercase letters. In a backward scan, the first encountered character of a multi-letter atom is its final lowercase character.

The solution records `end = index + 1`, then moves left while characters are lowercase. Valid syntax guarantees that it stops at the atom’s uppercase first letter. The slice `formula[index:end]` reconstructs the name in its normal left-to-right order without reversing it.

The atom’s contribution is

`pending * multipliers[-1]`.

The first factor is its explicit count or the implicit one. The second is the product of all enclosing group multipliers. This amount is added into `counts[atom]` because the same atom may appear in several locations. Afterward `pending` resets to one, and the scan continues before the uppercase letter.

**Trace `Mg(OH)2`**

Scanning from the right:

1. Read digit `2`, so `pending = 2`.
2. Meet `)` and push cumulative multiplier `2`; reset `pending`.
3. Read atom `H` and add `1 * 2 = 2`.
4. Read atom `O` and add `1 * 2 = 2`.
5. Meet `(` and pop, restoring multiplier `1`.
6. Read lowercase `g`, move left to uppercase `M`, reconstruct `Mg`, and add one.

The accumulated mapping is `H: 2`, `O: 2`, and `Mg: 1`.

**Produce the canonical output**

The required output orders atom names lexicographically. The solution iterates over `sorted(counts)`. For each atom it appends the atom name and appends the decimal count only when the count is greater than one.

This correctly omits the implicit `1`. Thus `Mg` remains `Mg` rather than `Mg1`, while hydrogen becomes `H2`. Joining all generated pieces forms the final formula string.

**Why the parser is correct**

At every scan position, `multipliers[-1]` equals the product of the multipliers for exactly the groups that contain that position. Meeting a closing parenthesis while moving backward enters a group and pushes its factor; meeting its opening parenthesis exits and pops it. Valid balanced syntax guarantees these operations match.

Whenever a digit sequence is parsed, `pending` carries its exact integer value to the token directly on the left. An atom therefore receives its own explicit count and every enclosing multiplier, while a closing parenthesis incorporates its pending number into the group stack. Every atom occurrence is processed once and added to its name’s total. Sorting and formatting then produce exactly the requested canonical representation.

## Complexity detail

Let `n` be the formula length, `A` the number of distinct atom names, and `d` the maximum nesting depth.

The backward index only moves left. Digit runs and lowercase name suffixes are consumed as parts of that same movement, so all parsing work is `O(n)`. Sorting the `A` distinct names costs `O(A log A)`. Formatting is linear in the output length, which is bounded by the parsed information and count digits. The total standard bound is `O(n + A log A)`.

The count map stores `A` entries, and the multiplier stack stores at most `d + 1` cumulative values. Auxiliary space is `O(A + d)`, excluding the returned string.

The problem guarantees that output counts fit in 32-bit integers. Python integers also avoid overflow during intermediate multiplication.

## Alternatives and edge cases

- **Recursive descent from left to right:** Parse one group into a local count map, recursively parse nested groups, and multiply a completed child map after its closing parenthesis. This closely follows the grammar but uses recursion depth `O(d)` and merges maps.

- **Stack of count maps:** Push an empty map at `(`, then pop, multiply, and merge at `)`. It is iterative and intuitive, but multiple maps may store repeated atom names. The exact reverse scan keeps one global count map and a multiplier stack.

- **Regular-expression tokenization:** A regex can extract atoms, numbers, and parentheses before a reverse pass. It shortens token recognition but introduces a separate token collection and makes the grammar less explicit.

- **Forgetting cumulative multiplication:** Pushing only the newest group factor would fail for nested groups. The stack stores `outer_product * new_factor` so an inner atom receives every enclosing multiplier.

- **Multi-letter atoms:** The backward lowercase scan must continue to the uppercase initial. Treating each letter independently would turn `Mg` into two nonexistent atoms.

- **Multi-digit counts:** The place-value loop reconstructs the digits in correct order even though they are read backward.

- **Implicit count one:** After every consumed atom or group multiplier, `pending` resets to one. No literal `1` is needed in the valid input.

- **Repeated atom names:** Contributions are added in `counts` rather than overwriting one another.

- **Nested groups without explicit multipliers:** A closing parenthesis with no preceding digit in the backward scan sees `pending = 1` and preserves the outer cumulative multiplier.

- **Output count one:** Formatting appends digits only for totals greater than one, matching chemical-formula notation.

## General

**Use the stack to separate low-precedence terms**

Addition and subtraction divide the expression into terms. Multiplication and
division belong inside the current term because they have higher precedence.
The exact solution stores each completed additive term in `stk`:

- a term preceded by `+` is stored as a positive value;
- a term preceded by `-` is stored as a negative value;
- `*` and `/` immediately combine the next number with the most recent stack
  term instead of creating another term.

After every multiplication and division chain has been collapsed, summing the
stack is equivalent to evaluating all remaining additions. This avoids a full
operator-precedence parser because the grammar has only two precedence levels
and no parentheses.

**`sign` describes the operator before the number being built**

The parser starts with `sign = '+'`. This imaginary leading plus makes the
first number follow the same processing rule as later positive terms.
Variable `v` accumulates the current number. For every digit `c`, the update
`v = v * 10 + int(c)` shifts existing decimal digits left and appends the new
digit. Thus `"205"` builds 2, then 20, then 205.

When the scan reaches an operator, that operator comes after the number in
`v`. The number must be processed using the previous `sign`, not using the
newly encountered operator. Only afterward does `sign = c` save the current
operator for the number to its right.

For `3+2*2`, the first `+` causes 3 to be processed under the initial plus and
placed on the stack. That encountered plus becomes the pending sign. At `*`,
the value 2 is appended under plus; then `*` becomes pending. At the final 2,
the pending multiplication pops the previous 2, multiplies it by the current
2, and pushes 4. The final stack is `[3, 4]`, whose sum is 7.

**Process a number when an operator or the physical end is reached**

The condition `i == n - 1 or c in '+-*/'` is the parser's token boundary. An
operator always ends the preceding number. The last character must also force
the final number to be applied because no later operator exists to trigger it.

This handles both a final digit and trailing spaces. If the last character is
a digit, the first `if` adds it to `v` before the boundary condition processes
the full number. If the expression ends in spaces, intermediate spaces leave
`v` untouched and the final space triggers processing of the number already
built. Ordinary spaces elsewhere match neither branch and are simply ignored.

After processing a boundary, the method assigns `v = 0` so digits of the next
number start fresh. It also assigns `sign = c`. At a true operator boundary,
that saves a valid operator. At the final digit or space, the stored value is
not an operator, but the loop ends immediately, so that last assignment is
never observed and is harmless under valid input.

**How each pending operator updates the stack**

The `match sign` statement selects one of four actions:

- For `+`, append `v`. It begins a new positive additive term.
- For `-`, append `-v`. Turning subtraction into addition of a negative value
  means the final operation can be a simple `sum`.
- For `*`, pop the most recent term, multiply it by `v`, and append the product.
  Replacing rather than adding a stack entry ensures multiplication is resolved
  before any surrounding addition.
- For `/`, pop the most recent term, divide it by `v`, truncate toward zero,
  and append the resulting term.

Multiplication and division have the same precedence and must associate from
left to right. Immediate replacement provides that order. For `24/4*3`, the
division first replaces 24 with 6; the multiplication then replaces that 6
with 18. Delaying both operations independently would lose their required
left-to-right relationship.

The popped term may be negative because a preceding subtraction stores its
number with a negative sign. This is desirable. For `10-7/2`, the stack first
contains `[10, -7]`; division replaces `-7` with `int(-7 / 2) = -3`. Summing
gives 7, which equals `10 - trunc(7/2)`.

**Why `int(a / b)` implements the required division rule here**

Python's `//` rounds down toward negative infinity, so `-7 // 2` is -4 and
would be wrong for this problem. The expression `/` produces a quotient, and
`int(...)` discards the fractional part toward zero, making
`int(-7 / 2) = -3` and `int(7 / 2) = 3`.

This route passes through floating-point arithmetic. Under the stated
32-bit bounds for numbers and running calculations, the relevant integer
values are exactly representable with ordinary Python floating-point precision,
so the conversion is safe for the contract. A more general arbitrary-size
integer implementation would avoid floats by dividing absolute values and
restoring the sign.

**Why summing the final stack is correct**

After each processed number, the stack represents the already parsed portion
as a sum of signed terms. A plus or minus appends exactly the next signed term.
A multiplication or division modifies only the most recent term, which is
precisely the operand immediately to the left within the current high-precedence
chain. Therefore the stack representation remains equivalent to the parsed
expression after every boundary.

At end of input, the physical-end condition has processed the last number. No
unresolved operator remains, and all multiplication or division has already
been folded into stack entries. `sum(stk)` evaluates the remaining signed
addition and returns the full expression.

**The exact source is not the manifest's constant-space implementation**

The manifest summary says the branch retains only a finalized sum and current
term, with $O(1)$ space. The exact source creates `stk` and may append one entry
for every additive term, so its worst-case auxiliary space is $O(n)$. The
constant-space technique from the editorial is a valid alternative, but this
document follows the executable stack source and reports its actual storage.

The `match` syntax requires Python 3.10 or newer. The method does not use
`eval` or any other built-in expression evaluator.

## Complexity detail

Let $n$ be the number of characters in `s`. The `for` loop visits each
character once, and every stack item is appended and popped at most a constant
number of times. The final `sum` visits all remaining stack entries. Total time
is $O(n)$.

In an expression containing only additions and subtractions, the stack can hold
one value per number, which is $O(n)$ entries relative to string length. Thus
the exact auxiliary-space bound is $O(n)$, not the manifest's $O(1)$. Variables
`v`, `n`, `sign`, `i`, and `c` use constant additional space.

## Alternatives and edge cases

- **Finalized sum plus current term:** Add the previous term to a running result only when a new `+` or `-` starts, while folding `*` and `/` into one `last` value. It achieves the same $O(n)$ time with $O(1)$ space and matches the manifest summary.
- **Two-stack precedence parser:** Maintain separate number and operator stacks and reduce according to precedence. It generalizes more easily to parentheses and more operators but adds unnecessary machinery here.
- **Recursive descent:** Parse additive and multiplicative grammar levels with functions. It is clear and extensible, but this no-parentheses grammar can be handled more compactly by one pass.
- **Trailing spaces:** Only the final physical character triggers completion. The accumulated `v` survives all preceding spaces, so the last number is still applied exactly once.
- **Leading spaces:** They perform no action; the initial plus remains pending for the first number.
- **Multi-digit zero-containing numbers:** Decimal accumulation correctly distinguishes values such as 0, 10, and 105.
- **Division truncation for a negative term:** `int(stk.pop() / v)` truncates toward zero, unlike floor division. This matters because subtraction can make the stored term negative even though lexical numbers are nonnegative.
- **Division by zero:** A valid expression under the intended arithmetic contract does not require evaluating division by zero; the source has no special guard.
- **Long multiplication/division chain:** Each operator immediately replaces the last term, preserving left-to-right evaluation without growing the stack for every factor.
- **Only one number:** The end condition appends it under the imaginary leading plus, and `sum` returns it.
- **No parentheses:** Parentheses are outside this problem's input alphabet. Supporting them would require saved contexts or a fuller parser.
- **Intermediate range:** The reference guarantees signed 32-bit intermediate results, which also keeps the source's float-assisted division exact for these values.

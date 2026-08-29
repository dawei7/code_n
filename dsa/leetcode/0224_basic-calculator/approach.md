## General

**Addition and subtraction can be accumulated as signed terms**

There is no multiplication or division, so outside parentheses every number or
parenthesized result contributes either positively or negatively to the current
sum. The algorithm does not need an operator-precedence stack. It keeps:

- `ans`, the running value of the expression at the current parenthesis depth;
- `sign`, either 1 or -1, which says how the next number or parenthesized group
  contributes to that running value;
- `stk`, which saves the surrounding result and sign when a new parenthesized
  expression begins.

Rewriting subtraction as addition of a negative term explains the model. For
example, `8 - 3 + 2` is `8 + (-3) + 2`. Once a complete number is read, the
source immediately performs `ans += sign * x`. A following `+` sets `sign = 1`,
and a following `-` sets `sign = -1` for the next term.

The reference permits unary minus. At the beginning of the expression or just
inside an opening parenthesis, `ans` is zero. Encountering `-` sets the sign to
-1, so the next number or group is subtracted from zero. No separate unary
operator implementation is required. Unary plus is excluded by the contract.

**Parse a whole multi-digit number before adding it**

The outer pointer `i` scans the string. When `s[i]` is a digit, a second pointer
`j` advances across the complete contiguous digit run. The number begins at
zero, and each digit updates it with
`x = x * 10 + int(s[j])`. Multiplying by ten shifts the previous decimal digits
left by one place, and adding the new digit fills the units place. Thus the
characters `"123"` become 1, then 12, then 123.

After the run, the source adds `sign * x` to `ans`. It assigns `i = j - 1`
because the common `i += 1` at the bottom of the outer loop will advance to
exactly `j`, the first non-digit character. Without the `-1`, that common
increment would skip the operator or parenthesis immediately after the number.

Although there is a nested digit loop, characters are not repeatedly scanned:
the outer pointer jumps over the digits consumed by `j`. Across the whole
expression, each character participates in constant work.

**An opening parenthesis saves exactly two pieces of outer context**

Suppose parsing has reached `outerAns + outerSign * (...)`. The contents inside
the parentheses must be evaluated independently before they can be combined
with the outer expression. On `(`, the exact source pushes `ans` first and
`sign` second:

1. `stk.append(ans)` saves everything already evaluated at the surrounding
   depth.
2. `stk.append(sign)` saves whether the group should be added or subtracted.
3. `ans, sign = 0, 1` starts a fresh inner expression with a neutral sum and a
   positive default sign.

No explicit opening-parenthesis marker is stored. The expression is guaranteed
valid, and each nesting level contributes exactly two stack entries, so the
matching close can recover the latest pair in last-in-first-out order.

Resetting both variables is essential. Carrying the outer running total into
the group would count it again, while carrying an outer negative sign into each
inner term would distribute that sign incorrectly when nested subtraction is
involved. The group must first obtain its own complete value.

**A closing parenthesis combines the completed group with its parent**

When `)` is reached, the current `ans` is the value of the entire inner
expression because every number was added immediately and the expression is
valid. The top stack entry is the sign saved immediately before `(`, and the
next entry is the outer running result. The source evaluates

`ans = stk.pop() * ans + stk.pop()`.

Python evaluates the right-hand side before assigning the new `ans`. The first
pop retrieves the saved sign, multiplies it by the inner result, and the second
pop retrieves the outer result. The order matches the earlier push order
`[outer result, outer sign]`.

For `1 - (2 + 3)`, parsing 1 makes the outer `ans` equal to 1. The minus sets
`sign` to -1. The opening parenthesis pushes 1 and then -1, then resets the
inner state. Inside, 2 and 3 produce inner `ans = 5`. At `)`, the computation
is `(-1) * 5 + 1 = -4`.

Nested parentheses work for the same reason. Each opening adds its own result
and sign pair above all older contexts. Each closing removes only the most
recent pair and turns the completed inner expression into one signed term of
its immediate parent.

**Spaces need no branch beyond being ignored**

Characters not matching a digit, `+`, `-`, `(`, or `)` reach no special action;
the bottom-of-loop increment simply passes them. Under the reference alphabet,
those remaining characters are spaces. Whitespace cannot split the digits of
one integer in a valid expression, so ignoring it preserves the intended token
sequence.

**Trace nested subtraction**

Consider `1-(2-(3))`. After reading `1-(`, the stack is `[1, -1]` and the inner
state is reset. Reading `2-(` pushes another pair, producing
`[1, -1, 2, -1]`, and resets again. The deepest group evaluates to 3. Its close
pops -1 and 2, giving `-1 * 3 + 2 = -1`. The outer close then pops -1 and 1,
giving `-1 * (-1) + 1 = 2`. This demonstrates why the sign belongs to the
whole group rather than only its first number.

**Why the running state represents the parsed expression**

Within one parenthesis depth, every completed numeric token has been added to
`ans` with the operator immediately preceding it. A `+` or `-` changes only
the sign of the next term. An opening parenthesis postpones one term while
preserving the exact partial sum and sign needed to incorporate it. A closing
parenthesis restores that context and replaces the entire group with its
computed signed value.

These operations cover every allowed token, and valid input guarantees balanced
parentheses and legal operator placement. When the scan ends, every number has
already been accumulated and every group has been combined, so `ans` is the
complete expression value. Unlike a common alternative implementation, this
source does not retain an unfinished `operand` that must be added after the
loop.

The method performs its own tokenization and arithmetic and never invokes
`eval` or any equivalent expression evaluator.

## Complexity detail

Let $n$ be the number of characters in `s`. The outer loop and the number parser
together consume every character once. Each stack entry is pushed and popped
once, so total time is $O(n)$.

Let $d$ be the maximum parenthesis nesting depth. Each open group stores two
integers, so the stack uses $2d = O(d)$ auxiliary space, matching the manifest.
All other variables use $O(1)$ space. In the worst syntactically valid case,
$d$ can be proportional to $n$, so the general worst-case space can also be
written $O(n)$.

## Alternatives and edge cases

- **Recursive-descent parser:** Define a function that parses until a matching `)` and returns both the value and new position. It mirrors the grammar naturally but can use $O(d)$ call-stack space and risks Python recursion limits for very deep input.
- **Reverse scan with an operand/operator stack:** Reverse the expression so stack popping preserves subtraction order, then evaluate each closed group. It is correct but processes more stack items and makes multi-digit parsing less intuitive.
- **Global accumulated sign:** Maintain the effective sign contributed by every enclosing parenthesis, using a sign-context stack. This can be compact but requires careful handling of unary minus and context restoration.
- **Leading unary minus:** Initial `ans = 0`; `-` sets `sign = -1`; the following number or parenthesized result is therefore subtracted from zero.
- **Unary minus before parentheses:** In `-(2+3)`, the saved outer context is result 0 and sign -1, so the close produces -5.
- **Multiple digits:** The inner digit loop forms the entire integer before applying its sign, preventing `123` from being treated as three separate terms.
- **Spaces anywhere between tokens:** They trigger no state change and are skipped by the common pointer increment.
- **Deeply nested groups:** Every opening contributes exactly two stack entries and every closing consumes exactly two. Valid balancing prevents underflow, though memory grows with nesting depth.
- **Subtraction after a closed group:** The close leaves the combined value in `ans`; the following `-` overwrites `sign` for the next term, exactly like subtraction after a number.
- **Zero values:** Parsing `0` still completes a number and adds zero with the current sign. It does not interfere with later operators.
- **Integer range:** The reference guarantees every running calculation fits signed 32-bit range. Python integers would remain safe even beyond it.
- **Invalid syntax:** The implementation relies on the validity guarantee. It does not diagnose unmatched parentheses, unsupported characters, unary plus, or malformed operator sequences.

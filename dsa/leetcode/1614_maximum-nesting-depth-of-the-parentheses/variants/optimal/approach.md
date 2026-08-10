## General

**Depth is the number of currently open parentheses**

While scanning a valid parentheses string from left to right, each opening parenthesis begins one additional nested region, and each closing parenthesis ends the most recently opened region.

The current nesting depth is therefore:

$$
\text{open parentheses seen}
-\text{closing parentheses seen}.
$$

The source stores this current value in `d` and the largest value ever reached in `ans`.

**Processing an opening parenthesis**

When `c == '('`, the source increments `d` because the scan has entered one deeper level.

It immediately updates:

`ans = max(ans, d)`.

The update must occur after incrementing. At the instant an opening parenthesis is read, the new region is active and may establish a new maximum.

For a prefix `"((("`, the depth values after the openings are one, two, and three, so `ans` becomes three.

**Processing a closing parenthesis**

When `c == ')'`, the source decrements `d`. Leaving a region cannot increase maximum nesting depth, so no `ans` update is needed in this branch.

The input is guaranteed to be a valid parentheses string. Consequently, `d` never becomes negative and returns to zero after the complete scan.

**Ignoring all other characters**

Digits and arithmetic operators do not start or end parentheses regions. Neither conditional matches them, so they leave both `d` and `ans` unchanged.

This means the method works on the parentheses structure embedded in the expression without parsing or evaluating the arithmetic.

**A trace**

For `"(1+(2*3)+((8)/4))+1"`:

- the first opening sets depth one;
- the opening around `2*3` temporarily reaches depth two, then closes;
- the two openings before `8` take depth from one to two to three;
- later closings reduce it.

The largest observed depth is three.

For `"()(())"`, the first pair reaches one and returns to zero. The second part reaches one, then two, then unwinds. The maximum is two.

For an expression with no parentheses, `d` and `ans` remain zero, so zero is returned.

**Why a counter is enough**

A stack is useful when different bracket types must be matched or validity must be checked. Here, there is only one parenthesis type and validity is guaranteed. The identity of individual openings is irrelevant; only how many remain unmatched at the current prefix matters.

One integer counter stores exactly that number, reducing auxiliary space from linear to constant.

**Why the maximum counter value is the answer**

At every position, `d` equals the number of opening parentheses whose matching closings have not yet appeared. Those are precisely the nested parentheses containing the scan position immediately after processing the character.

Every nested region contributes one to this active count, so the deepest point in the string produces the maximum `d`. Conversely, any `d` value corresponds to that many simultaneously active, properly nested pairs. Thus `max d` over all prefixes is exactly the definition’s nesting depth.

The source records every possible increase at opening characters, which are the only places depth can rise. Therefore, `ans` cannot miss the maximum.

**Why checking only after an opening is complete**

Between two opening parentheses, the depth either stays unchanged on an ordinary character or decreases on a closing parenthesis. Neither event can create a value larger than the maximum already observed. Every new global maximum must therefore occur immediately after `d += 1`. Updating `ans` only in that branch is not merely an optimization; it checks precisely every moment at which a larger nesting depth can first appear.

**Validity is assumed, not checked**

The source does not reject a premature closing parenthesis or verify final `d == 0`. Such checks are unnecessary under the contract. On malformed input, it might return a number despite negative intermediate depth, so the implementation should not be presented as a general parentheses validator.

## Complexity detail

Let $N$ be the string length.

The loop visits each character exactly once and performs constant work, so time complexity is $O(N)$.

Only two integer variables and the current character reference are used. Auxiliary space is $O(1)$. No stack, parsed expression, or copy proportional to input length is created.

## Alternatives and edge cases

- **Explicit stack:** Push each opening and pop each closing, tracking maximum stack size. It is correct but uses $O(N)$ space when one counter suffices.
- **Recursive expression parser:** It could derive nesting through call depth but solves much more than the problem asks and may use linear stack space.
- **Count total parentheses only:** Total pairs do not reveal nesting; `()()()` has three pairs but depth one.
- **Update before incrementing:** This would lag one level and undercount. The source increments `d` before comparing with `ans`.
- **Update after closing:** It is harmless but unnecessary because closing can only decrease depth.
- **No parentheses:** The answer remains zero.
- **One pair:** Depth rises to one and returns to zero.
- **Sequential pairs:** Each reaches depth one; the count resets between them.
- **Fully nested pairs:** Each consecutive opening raises the maximum by one.
- **Digits and operators:** They are ignored because they do not affect active parentheses.
- **Valid-string guarantee:** It ensures depth never becomes negative and ends at zero.
- **Malformed input:** The source does not validate it; that behavior lies outside the contract.
- **Maximum length:** A linear scan and constant state easily handle the bound.

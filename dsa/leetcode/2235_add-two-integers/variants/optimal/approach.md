## General

**The requested operation is exactly integer addition**

The function receives two integers and must return their arithmetic sum. Python already defines `+` for integers with precisely these semantics, so the exact solution is

`return num1 + num2`.

There is no transformation, search, iteration, or data structure required. Adding extra machinery would not reveal a hidden constraint because the problem explicitly permits ordinary integer addition and asks for the direct result.

**Why the expression returns the required value**

Integer addition combines signed quantities. For positive inputs, it moves upward by both magnitudes. For two negative inputs, it combines their negative magnitudes. For opposite signs, it subtracts the smaller absolute magnitude from the larger and keeps the sign of the larger magnitude.

Python evaluates `num1 + num2` first and returns that resulting integer. The method has no later statement that could alter it.

For `num1 = 12` and `num2 = 5`, the expression evaluates to seventeen. For `num1 = -10` and `num2 = 4`, adding four moves four units toward zero from negative ten, producing negative six.

**Negative signs belong to the values**

A negative input is still one integer, not a special string or separate operation. Python's addition operator handles its sign automatically. No manual branching is necessary for combinations such as positive plus negative or negative plus negative.

For example:

- `7 + (-3) = 4`;
- `-7 + 3 = -4`;
- `-7 + (-3) = -10`.

These all follow the same single expression.

**Zero is the additive identity**

If either input is zero, the result is the other input because `x + 0 = x`. The implementation naturally follows this property. If both are zero, it returns zero.

**Order does not matter**

Integer addition is commutative:

$$
\texttt{num1} + \texttt{num2}
= \texttt{num2} + \texttt{num1}.
$$

The method uses the parameter order as written, but swapping the two arguments would not change the answer. This does not require any normalization before calculation.

**No overflow concern in the exact environment**

The constraints place each input between negative one hundred and one hundred, so the result lies between negative two hundred and two hundred. That range fits easily in every ordinary integer type.

Python integers also expand beyond fixed machine width, so even wider hypothetical inputs would not overflow. In fixed-width languages, the stated bounds still make standard integer addition safe.

**Why direct addition is optimal**

At least one arithmetic operation is conceptually needed to combine two independent input values. The built-in addition performs that work directly. Loops that add one repeatedly, bitwise carry simulations, string conversions, or external libraries all add complexity without improving time or space for this contract.

The solution is beginner-friendly precisely because its code mirrors the mathematical request with no indirection. The method name `sum` does not conflict with the operator; it is simply the LeetCode method that receives the two operands.

**Input values remain unchanged**

Integers are immutable in Python. Evaluating the expression creates the result value without modifying `num1` or `num2`. There is no observable state besides the returned sum.

**The return type follows automatically**

Both operands are annotated as `int`, and adding two Python integers produces another integer. There is no floating-point conversion, rounding, text formatting, or truncation step. The returned object therefore matches the declared `int` result type for every permitted input.

The expression is evaluated exactly once. This matters conceptually because the answer is a value, not a sequence of intermediate totals that the caller must inspect. The method completes the entire contract at the return statement.

## Complexity detail

Under the problem's fixed bounded integers, one addition takes `O(1)` time. Returning the result also takes `O(1)` time.

The method allocates no collection, recursion stack, or input-dependent workspace. It uses `O(1)` auxiliary space, and the returned integer is constant-sized under the constraints.

In a theoretical arbitrary-precision model, adding integers with `b` bits takes `O(b)` time and stores `O(b)` result bits. The problem's values are bounded, so `b` is constant and the declared bounds remain `O(1)`.

## Alternatives and edge cases

- **Repeated increment or decrement:** Move from `num1` one unit at a time according to `num2`. This is slower, more error-prone for negative values, and unnecessary when addition is permitted.
- **Bitwise carry simulation:** XOR and shifted AND can implement addition without `+`, but the problem does not prohibit `+`. Such code obscures the simple contract, especially for Python's signed integers.
- **Convert to strings:** Decimal digit addition would require sign and carry handling and extra memory while producing the same value.
- **One operand zero:** The other operand is returned mathematically through the same expression.
- **Both operands zero:** The result is zero.
- **Two positive operands:** Their magnitudes combine and the result is positive.
- **Two negative operands:** Their absolute magnitudes combine and the result remains negative.
- **Opposite signs with equal magnitude:** They cancel to zero.
- **Opposite signs with unequal magnitude:** The result has the sign of the larger absolute value.
- **Boundary values:** `100 + 100 = 200` and `-100 + -100 = -200` are both safely represented.
- **Parameter order:** Commutativity means exchanging `num1` and `num2` changes nothing.
- **Return type:** Integer operands remain in integer arithmetic, so the method never produces a string or floating-point approximation.
- **Exactness:** Every value in the constraint range is represented exactly; no rounding or precision loss occurs.
- **No input mutation:** Python integers are immutable, and the function has no side effects.

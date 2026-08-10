## General

**Keep one mutable running result**

The calculator represents a sequence of operations, so it needs state that survives from one method call to the next. The constructor stores the initial number in `this.result`. Every arithmetic method reads that current value, applies one operation, and writes the new value back to the same property.

There is no expression tree and no delayed evaluation. A chain is evaluated from left to right as ordinary JavaScript method calls, and each method immediately updates the shared calculator instance.

**Why returning this enables chaining**

Consider:

`new Calculator(10).add(5).subtract(7).getResult()`.

The constructor creates one object with result ten. Calling `add(5)` changes its result to fifteen. Crucially, `add` returns `this`, which is the same calculator object. JavaScript can therefore look up `subtract` on that returned object and continue the chain.

`subtract(7)` changes the same result to eight and again returns the instance. Finally, `getResult()` returns the number eight rather than the calculator because the chain is finished and the caller wants the answer.

If an arithmetic method returned the numeric result instead of `this`, the next method lookup would be attempted on a number and the fluent chain would break.

**Addition and subtraction**

`add(value)` uses `this.result += value`. Under the contract, `value` and the stored result are numbers, so this is numeric addition rather than string concatenation.

`subtract(value)` similarly uses `this.result -= value`. Both methods then return `this`.

The state after each call becomes the input to the next call. Operations are not rearranged because arithmetic expressions such as subtraction are order-sensitive.

**Multiplication and exponentiation**

`multiply(value)` applies `*=` to the current result.

`power(value)` uses `**=`, replacing the current result by its value raised to the supplied exponent. The second example starts with two, multiplies by five to obtain ten, then squares that current ten to obtain one hundred. It does not calculate $2\cdot 5^2$ because every operation is applied immediately in chain order.

JavaScript number arithmetic follows IEEE-754 floating-point semantics. The problem accepts a tolerance for non-exact floating results, so the class does not implement arbitrary-precision decimal arithmetic.

**Division needs an explicit guard**

JavaScript normally evaluates division by zero to `Infinity`, `-Infinity`, or `NaN` rather than throwing automatically. The problem requires a specific error, so `divide` first checks:

`if (value === 0)`.

If true, it throws `new Error("Division by zero is not allowed")`. The mutation `this.result /= value` occurs only after the check, so a failing division leaves the stored result unchanged.

JavaScript considers negative zero strictly equal to zero, so `-0` is also rejected, which is mathematically appropriate.

Throwing stops the current chain unless the caller catches the error. The judge can inspect the error message required by the contract.

**getResult is intentionally different**

All transformation methods return the calculator to support more transformations. `getResult` performs no mutation and returns `this.result`. It is the terminal observation operation.

Calling `getResult` does not freeze or destroy the calculator; a caller with a separate reference could invoke more arithmetic methods later. It simply exposes the current number.

**Object identity throughout a chain**

No arithmetic method creates another `Calculator`. This matters beyond saving allocations: all external references to the instance observe the same updated state. The fluent syntax is compact, but semantically it is a sequence of mutations on one object.

For example, if `calc` refers to a calculator at ten, then `calc.add(2) === calc` is true. Its result is now twelve.

**Why the design satisfies every operation**

The constructor establishes the required initial state. Each arithmetic method implements exactly its named operation on that state and returns the same object, allowing any legal sequence to continue. Division checks its forbidden denominator before mutation. `getResult` returns the state after the complete ordered sequence. By induction over the method calls, after each call `this.result` equals the mathematical result of the chain prefix, so the final returned value is correct.

**Sequence-level view**

The input harness may describe up to many thousands of actions. The class does not need to see that action list itself. The harness calls methods in order, and the object retains only the one running number. This is why storage does not grow with chain length.

## Complexity detail

Each constructor, getter, addition, subtraction, multiplication, and division call performs a constant number of JavaScript number operations, so it takes $O(1)$ time. Exponentiation is treated as a primitive JavaScript number operation under the problem's numeric model and is also summarized as $O(1)$.

For a chain of $q$ method calls, total wrapper work is $O(q)$, which is the manifest's sequence-level bound. The instance stores one `result` property regardless of $q$, so auxiliary space is $O(1)$.

No history of operations is retained. A thrown division error allocates one `Error` object, still constant additional space for that call.

## Alternatives and edge cases

- **Return numbers from arithmetic methods:** Performs the calculation but breaks method chaining because the next calculator method is no longer available.
- **Create a new Calculator per operation:** Can provide immutable chaining, but allocates $O(q)$ objects over a chain instead of mutating one instance.
- **Store an operation list and evaluate later:** Adds unnecessary memory and postpones errors such as division by zero.
- **Division by zero:** Throws before changing `result`.
- **Negative zero divisor:** `-0 === 0`, so it is rejected too.
- **Floating-point values:** Results follow JavaScript number semantics and may contain small representation error covered by the accepted tolerance.
- **Negative exponent:** JavaScript exponentiation produces a reciprocal when mathematically defined.
- **Zero exponent:** A finite nonzero current result becomes one; JavaScript's precise edge semantics govern special values.
- **Repeated getResult:** Merely reads the state and returns the same number until another operation mutates it.
- **Aliased instance:** Every reference observes updates because methods return and mutate the same object.

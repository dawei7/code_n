## General

**The definition gives the algorithm directly.** A positive integer is a Harshad number exactly when it is divisible by the sum of its decimal digits. The required output is that digit sum when divisibility holds and -1 otherwise. The source therefore needs two phases: compute the digit sum, then perform one remainder test.

**Preserve the original value.** The method begins with `s, y = 0, x`. Variable `x` remains unchanged because it is needed for the final divisibility test. Variable `y` is a working copy that can be repeatedly shortened while extracting digits. Without the copy, the loop would reduce the only version of the input to zero and lose the dividend.

**Extract the last decimal digit.** For a positive integer `y`:

`y % 10`

is its least significant decimal digit. For example, `184 % 10` is 4. The source adds this digit to `s`.

It then executes:

`y //= 10`.

Integer division by 10 discards the least significant decimal digit. Thus 184 becomes 18, then 1, then 0. Every loop iteration processes one digit and permanently removes exactly that digit from the working copy.

**A useful loop invariant.** Before each iteration, `s` equals the sum of the digits already removed from the original number, while `y` consists of the digits not yet processed. Initially, no digits have been removed, so `s=0` and `y=x` satisfy the statement.

During an iteration, `y % 10` is exactly the next unprocessed digit. Adding it moves that digit's value into `s`, and floor-dividing by 10 removes it from `y`. The invariant is preserved. When `y` becomes zero, no digits remain, so `s` is the complete decimal digit sum of `x`.

**Test the Harshad condition.** The final expression is:

`s if x % s == 0 else -1`.

A zero remainder means `s` divides `x` exactly, which is the definition of a Harshad number. In that case, the problem asks for the digit sum itself, not a Boolean and not the quotient, so the source returns `s`. A nonzero remainder returns -1.

**Trace for `x = 18`.** The working copy begins at 18. The first iteration adds 8 and changes `y` to 1. The second adds 1, producing `s=9`, and changes `y` to zero. Since `18 % 9 == 0`, the result is 9.

For `x = 23`, the extracted digits sum to five. `23 % 5` is three, so 23 is not divisible by its digit sum and the source returns -1.

**Why digit order is irrelevant.** The loop reads digits from right to left, while people commonly read numbers from left to right. Addition is commutative, so the order in which digits enter the sum has no effect. Reading from the least significant side is simply what remainder and integer division make convenient.

**Why no string conversion is needed.** Converting `x` to text and converting every character back to an integer would also work. Arithmetic extraction avoids allocating a string and keeps the reasoning directly in the number system. For the small constraint either method is fast, but the checked-in solution is numeric.

**The positive-input guarantee prevents division by zero.** The contract has `x >= 1`. Every positive integer contains at least one decimal digit, and its digit sum is at least one. Therefore, `x % s` is always defined. If zero or negative inputs were allowed, the implementation would need a separately stated policy; it is correct not to add one for this contract.

**Why the result cannot be another positive value.** There is only one digit sum for a fixed number. The loop computes it exactly, and divisibility is a deterministic remainder test. Therefore, returning either that exact sum or -1 covers all possible outputs.

**A one-digit observation.** Every positive one-digit number is a Harshad number because its digit sum equals the number itself. For `x=7`, the loop obtains `s=7` and `7 % 7 == 0`. The general code naturally handles this case without a special branch.

**Zeros inside the number.** A digit zero contributes nothing to `s` but still takes an iteration. For `x=101`, the processed digits are 1, 0, and 1, giving sum two. The fact that floor division passes through a trailing or internal zero does not skip any nonzero digit.

## Complexity detail

Let $d$ be the number of decimal digits of `x`. Each loop iteration removes one digit, so there are exactly $d$ iterations. Since:

$$
d=\lfloor\log_{10}x\rfloor+1
$$

for positive `x`, time complexity is $O(\log x)$. Under the concrete constraint `x <= 100`, there are at most three iterations, but $O(\log x)$ is the meaningful generalized bound.

The source stores only `s` and `y` in addition to the input. It allocates no collection or recursion stack, so auxiliary space is $O(1)$.

Modulo and integer division are treated as constant-time operations for values in the stated range. Python supports arbitrary-size integers, but that broader bit-complexity consideration is unnecessary here.

## Alternatives and edge cases

- **String conversion:** `sum(map(int, str(x)))` is concise and also $O(\log x)$ time, but allocates a decimal string and temporary iteration state.
- **Recursive digit sum:** It follows the same remainder/division recurrence but adds $O(\log x)$ call-stack space.
- **Lookup table:** The tiny `x <= 100` domain could be precomputed, but that obscures the definition and is unnecessary.
- **One-digit input:** Every value from one through nine is divisible by its own single digit.
- **`x = 10`:** Digit sum is one, so the result is one.
- **`x = 100`:** Digit sum is one, and 100 is divisible by one.
- **Internal zero digits:** They add zero but are still correctly removed one position at a time.
- **Repeated digits:** Each occurrence is extracted and added independently.
- **Positive guarantee:** It ensures `s > 0` and prevents a remainder-by-zero error.
- **Original preservation:** `y` is consumed by the loop while `x` remains available for the final test.
- **Right-to-left processing:** Addition order does not affect the final digit sum.
- **Divisibility equality:** A remainder of exactly zero is required; approximate division has no role.
- **Return contract:** A Harshad input returns the digit sum, not `True`, `x`, or the quotient.
- **No floating point:** Integer remainder and division avoid rounding entirely.
- **No mutation outside the method:** Integers are immutable, and only local bindings change.

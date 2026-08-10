## General

**What the generator must yield.** For a positive input `n`, successive calls to the returned generator should produce $1!, 2!, \ldots, n!$. For `n = 0`, it should produce the single conventional value $0! = 1$. A generator is important here: values are delivered lazily through `next()` rather than collected and returned in an array.

**Keep the product accumulated so far.** The variable `product` begins at one, the multiplicative identity. The loop variable `value` begins at one and rises by one on each iteration. Before yielding during iteration $v$, the method executes `product *= value`.

At the start of iteration $v$, `product` equals $(v-1)!$. Multiplying by $v$ changes it to $v!$, which is then yielded. This is the loop invariant that explains both correctness and efficiency: each factorial reuses the previous factorial instead of recomputing the full product from one.

For `n = 5`, the retained product evolves through one, two, six, twenty-four, and one hundred twenty. The generator pauses immediately after each `yield`. When the caller requests the next value, execution resumes after that yield, the `for` loop advances `value`, and the next multiplication occurs.

**Use one loop for both zero and positive inputs.** The upper bound is `Math.max(n, 1)`. When `n` is positive, this is simply `n`, so the inclusive loop yields every factorial through $n!$. When `n = 0`, the maximum is one. The loop performs one iteration with `value = 1`, computes `1 * 1`, and yields one. That value is simultaneously $1!$ and the required numerical value of $0!$; the sequence contract for zero asks only for the value one, so no special branch is necessary.

**Why the loop stops at the correct point.** JavaScript's `for` condition is `value <= Math.max(n, 1)`. After yielding the final required product, resumption increments `value`. The condition then becomes false, the generator function returns implicitly, and later `next()` calls report `done: true`. There is no extra factorial.

**Laziness changes when work happens.** Calling `factorial(n)` does not execute the body through the first yield. It creates a generator object that remembers how to execute the function. Each successful `next()` performs only the work needed to advance to the next `yield`. A caller that consumes only the first three values of `factorial(18)` performs three multiplications, not eighteen.

The local variables `product` and `value` are preserved in the suspended generator frame. This retained state is what makes the next factorial available in constant incremental work. Independent calls to `factorial` create independent frames, so consuming one generator does not affect another.

**Why JavaScript Number is sufficient here.** JavaScript uses binary floating-point `Number` values for these multiplications. Integers are represented exactly only through `Number.MAX_SAFE_INTEGER`. The constraint stops at `n = 18`, and $18! = 6{,}402{,}373{,}705{,}728{,}000$, which is below $9{,}007{,}199{,}254{,}740{,}991$, the largest safe integer. Therefore every factorial yielded by the allowed inputs is exact. Extending the input to nineteen would make `Number` unsafe for exact integer semantics, so a broader production version would use `BigInt`.
Initially, before the first multiplication, `product = 1 = 0!`. Assume that at the start of the iteration whose loop value is $v$, the product is $(v-1)!$. Multiplication by $v$ produces $v!$, and the generator yields exactly that value. This proves the invariant for the next iteration. The loop covers precisely $v=1$ through $v=n$ for positive $n$, and the adjusted single iteration yields the required one for zero. Thus every yielded value and the number of yields are correct.

## Complexity detail

For one call to `next()` that reaches a yield, the generator performs one multiplication, one loop comparison, and constant state updates. Under the bounded Number representation, this is $O(1)$ time per emitted value. This is the perspective captured by the manifest's constant-time claim.

If the caller consumes the complete generator, there are `Math.max(n, 1)` yielded values and therefore $O(n)$ total time for positive $n$, or constant time for zero. It is important to distinguish total enumeration cost from incremental cost; saying only $O(1)$ for the entire generator would be misleading.

The suspended frame retains a constant number of numeric variables and loop state, so auxiliary space is $O(1)$. The generator does not accumulate past results. If the caller spreads it into an array or otherwise stores every value, that caller-created collection uses $O(n)$ space, but it is not allocated by the generator implementation itself.

With arbitrary-precision factorials, multiplication cost would grow with the number of digits, and a more detailed bit-complexity analysis would be needed. The problem's $n \le 18$ bound and JavaScript Number arithmetic justify treating each multiplication as constant time.

## Alternatives and edge cases

- **Recompute every factorial independently:** For each $i$, multiply one through $i$. This performs $1+2+\cdots+n=O(n^2)$ multiplications and throws away useful previous work.
- **Return an array:** An eager loop can fill and return all factorials in $O(n)$ time, but it always performs all work and stores $O(n)$ values even if the caller needs only a prefix.
- **Recursive generator:** Recursion can produce the sequence, but it adds call-stack state and is less direct than retaining one running product.
- **Use `BigInt`:** This is required if the supported range extends beyond safe Number factorials. Every operand and expected output would then need consistent BigInt semantics.
- **Input zero:** `Math.max(0, 1)` causes exactly one yield of one, satisfying $0! = 1$.
- **Input one:** The loop also yields exactly one value, one. Although zero and one produce equal sequences of values, both contracts are correct.
- **Maximum input eighteen:** All produced factorials remain exact safe integers, including the final $18!$.
- **Partial consumption:** If the caller stops requesting values, no later multiplications occur. This is the principal benefit of the generator form.
- **Repeated `next()` after completion:** The generator remains completed and returns no new values.
- **Independent iterators:** Two calls to `factorial(n)` do not share `product`; each generator maintains its own progress.
- **Invalid negative input outside the contract:** `Math.max(n, 1)` would still yield one, which is not a defined negative factorial sequence. The constraints are what make the compact bound valid.
- **Non-integer input outside the contract:** The loop would yield factorial-like prefix products through the last integer not exceeding the bound, not a gamma-function value. Only integer `n` is supported.

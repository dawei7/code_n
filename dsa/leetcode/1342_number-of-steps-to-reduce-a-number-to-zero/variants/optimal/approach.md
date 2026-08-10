## General

The operation is completely determined by the current number: an odd value must lose one, and an even value must be divided by two. There is no decision to optimize. The checked-in solution simulates this unique sequence and counts how many operations occur before the value reaches zero.

**Use the least significant bit to test parity**

In binary, an integer is odd exactly when its final bit is one. The expression `num & 1` keeps only that least significant bit:

- A nonzero result means `num` is odd.
- A zero result means `num` is even.

For an odd value, `num -= 1` performs the required subtraction. This changes its last binary bit from one to zero, making the result even unless the original value was one.

For an even value, `num >>= 1` shifts every bit one position to the right. For a nonnegative integer, this is the same integer result as dividing by two. The discarded last bit is zero because this branch runs only for even values.

After either operation, `ans += 1` records the step. The loop condition `while num` is true for every positive current value and false exactly at zero, so the function returns immediately after counting the operation that first produces zero.

For `num = 14`, the binary value is `1110`. The transitions are fourteen to seven, seven to six, six to three, three to two, two to one, and one to zero. The code applies three shifts and three subtractions, returning six.

**Why the loop always terminates and counts exactly**

Every iteration strictly decreases a positive `num`. Subtracting one decreases it directly, and shifting a positive even value right divides it by two. The sequence can never become negative and cannot repeat a previous value. It must eventually reach zero.

At the start of every loop iteration, `ans` equals the number of required operations already simulated, and `num` equals the value produced by those operations. The branch performs exactly the next operation dictated by the statement, then increments `ans` once. This invariant remains true until `num` becomes zero. At termination, `ans` is therefore exactly the number of steps in the only valid reduction sequence.

**View the same count through binary digits**

The simulation also explains the logarithmic bound. For a positive input, every one bit eventually needs one subtraction when it becomes the least significant bit. Every bit position except the most significant one eventually disappears through one right shift. Therefore,

$$
\text{steps} = \operatorname{popcount}(\texttt{num}) + \operatorname{bitLength}(\texttt{num}) - 1.
$$

For fourteen, the representation `1110` has three one bits and length four, giving `3 + 4 - 1 = 6`. The loop obtains the same number without converting to a string or explicitly counting all bits in advance.

The zero input is handled naturally. `while num` is false immediately, so the initial `ans = 0` is returned. No special branch is needed.

## Complexity detail

Let $x$ be the initial value of `num`.

For a positive value, a subtraction from an odd number either reaches zero or makes the value even, so it is followed by a halving step. The number has $\lfloor\log_2 x\rfloor + 1$ binary digits. There are at most that many subtraction steps and one fewer right shifts. The total time is $O(\log x)$. For $x = 0$, the method takes $O(1)$ time.

The method stores only the current `num` and the counter `ans`. It creates no collection and uses no recursion, so auxiliary space is $O(1)$ under the standard fixed-width-integer model.

Python integers are arbitrary precision, and individual bit operations on extremely large integers technically depend on the number of machine words. The official input is bounded by one million, so the standard constant-cost arithmetic model is entirely appropriate here.

The parameter `num` is rebound locally as the simulation progresses. Python integers are immutable, so this does not alter any integer object held by the caller.

## Alternatives and edge cases

- **Modulo parity test:** Use `num % 2` instead of `num & 1` and integer division by two instead of a shift. It has the same logic and asymptotic bounds and may be more immediately readable to beginners.
- **Direct bit-count formula:** For positive input, return the population count plus bit length minus one. This can be concise with language built-ins but needs a separate zero case and hides the step-by-step process.
- **Binary string counting:** Count ones and total digits in `bin(num)`. It takes $O(\log x)$ extra space for the string, unlike the constant-state simulation.
- **Recursive simulation:** Recurse on `num - 1` or `num // 2` and add one. It mirrors the recurrence but consumes $O(\log x)$ call-stack space unnecessarily.
- **Zero input:** The loop does not execute and the answer is zero.
- **One input:** It is odd, one subtraction reaches zero, and the answer is one.
- **Power of two:** Repeated shifts reach one, followed by a final subtraction. A value `2^p` requires `p + 1` steps.
- **Odd value greater than one:** Subtracting one makes it even, guaranteeing that the next iteration can halve it.
- **Right shift semantics:** The equivalence to division by two relies on nonnegative input. The stated constraints guarantee that condition.
- **Deterministic operations:** There is no greedy choice. Each parity has exactly one permitted operation, so faithful simulation is automatically optimal.

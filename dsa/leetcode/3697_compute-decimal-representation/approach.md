## General

A base-10 component has exactly one nonzero decimal digit. For a digit $d\in\{1,\ldots,9\}$ in place $10^p$, its component is:

$$
d\cdot10^p.
$$

The ordinary decimal expansion already writes a positive integer as the sum of one such component for every nonzero digit. The exact source extracts those digits from right to left, constructs their place-value components, skips zero digits, and reverses the result into descending order.

**Extracting the least significant digit**

The loop maintains `p` as the place value of the digit currently being examined. It begins at one, the units place.

The statement:

`n, v = divmod(n, 10)`

performs quotient-and-remainder division by ten:

- `v` is the current least significant digit, from zero through nine;
- the new `n` is the remaining prefix after removing that digit.

For original number $537$:

- the first iteration yields quotient $53$ and digit $7$;
- the second yields quotient $5$ and digit $3$;
- the third yields quotient $0$ and digit $5$.

After each iteration:

`p *= 10`

moves from units to tens, then hundreds, and so on.

The parameter `n` is locally replaced by its shrinking quotient. Python integers are immutable, so this does not alter an integer held by the caller.

**Creating only nonzero components**

If `v` is nonzero, the source appends:

`p * v`

At that moment, `p` is exactly the decimal position from which `v` was extracted. The product has digit `v` in that position and zeros everywhere else, so it satisfies the base-10-component definition.

If `v == 0`, no component is appended. A zero component is not positive and would be unnecessary in a sum.

For $102$:

- units digit two produces component $2$;
- tens digit zero produces nothing;
- hundreds digit one produces component $100$.

The components sum to $102$.

**Why the components sum to the original number**

Let the decimal digits of the original integer be $d_0,d_1,\ldots,d_{D-1}$ from least significant to most significant. By positional notation:

$$
n=\sum_{p=0}^{D-1}d_p10^p.
$$

The loop appends exactly the nonzero terms of this sum. Terms with $d_p=0$ contribute nothing and may be omitted. Therefore, the returned components sum exactly to the input.

Every returned value is legal because each term uses one digit from one through nine multiplied by a nonnegative power of ten.

**Why one component per nonzero digit is minimal**

Let $h(n)$ be the number of nonzero digits in the decimal representation of $n$. The algorithm creates exactly $h(n)$ components.

To see why fewer cannot suffice, consider building a number from zero by adding base-10 components one at a time. Adding one component changes one starting decimal position. Without a carry, it can introduce at most one new nonzero digit. If a carry occurs, it may propagate through higher positions, but the propagation turns a run of nines into zeros before incrementing the first non-nine digit. It still increases the total number of nonzero positions by at most one; it may even decrease it.

Starting from zero nonzero digits, a sum of $t$ base-10 components can therefore have at most $t$ nonzero decimal digits. Since the target has $h(n)$ nonzero digits, every valid representation needs:

$$
t\ge h(n).
$$

The standard place-value decomposition uses exactly $h(n)$ components, meeting this lower bound. It has minimum possible cardinality.

This argument also rules out using carries to obtain a shorter representation. Carries can rearrange or eliminate nonzero digits, but one newly added single-place component cannot create more than one additional nonzero position overall.

**Producing descending order**

Digits are extracted from low place values to high place values, so `ans` is initially in ascending component order.

Any nonzero component at place $10^{p+1}$ is at least $10^{p+1}$, while any component at place $10^p$ is at most $9\cdot10^p$. Therefore, every nonzero higher-place component is strictly larger than every lower-place component.

The source calls:

`ans.reverse()`

once after extraction. This converts the low-to-high list into the required strictly descending order without sorting.

For $537$, the temporary list is `[7, 30, 500]` and the returned list is `[500, 30, 7]`.

**Loop termination**

Each `divmod` removes one decimal digit by replacing `n` with `n // 10`. Because the input is positive, repeated division eventually reaches zero. The loop executes once per decimal digit, including zero digits between nonzero ones.

The original upper bound $10^9$ is itself handled correctly: nine zero digits are skipped, the leading one produces component $10^9$, and the result contains that one component.

## Complexity detail

Let $D$ be the number of decimal digits:

$$
D=\lfloor\log_{10}n\rfloor+1.
$$

The loop runs exactly $D$ times. Each iteration performs constant arithmetic on the bounded input, and reversing at most $D$ components also takes $O(D)$ time. Total running time is $O(D)=O(\log n)$.

The answer contains one entry per nonzero digit and therefore at most $D$ entries. Including returned output, space usage is $O(D)=O(\log n)$.

Excluding the output list, the working state consists only of `n`, `p`, and `v`, so auxiliary workspace is $O(1)$.

## Alternatives and edge cases

- **Convert to a decimal string:** Scanning characters with their positions also takes $O(\log n)$ time and space. Repeated `divmod` keeps the logic numeric.
- **Sort the components:** Sorting is unnecessary because extraction order is already increasing by place value; one reversal is linear.
- **Append zero-place components:** Zero is not a positive base-10 component and adds nothing. Skipping zero digits is necessary for minimum cardinality.
- **One-digit input:** The first extracted digit forms the input itself, and reversing a one-element list changes nothing.
- **Internal zeros:** For $102$, the tens digit is skipped, producing `[100, 2]` rather than including zero.
- **Trailing zeros:** For $500$, units and tens are skipped and the result is simply `[500]`.
- **Largest allowed input:** $10^9$ is already one base-10 component, so the result has one element despite the ten-digit representation.
- **Carries in alternative sums:** Combining several smaller components can reproduce higher digits, but it cannot use fewer components than the number of target nonzero digits.
- **Descending requirement:** Reversing is required because `divmod` discovers the units component first.
- **Positive-input guarantee:** Zero would produce an empty list under the loop, but zero is outside the contract and is not a positive base-10 component.

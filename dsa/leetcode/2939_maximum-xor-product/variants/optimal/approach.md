## General

Let

$$
A=a\mathbin{\mathtt{\char94}}x,\qquad
B=b\mathbin{\mathtt{\char94}}x.
$$

Only the lowest $n$ bits of $x$ may vary because $0\le x<2^n$. Bits at positions $n$ and above of $A$ and $B$ are fixed to those of $a$ and $b$.

The source initializes

`ax = (a >> n) << n` and `bx = (b >> n) << n`,

which preserve exactly those fixed high bits and clear the low bits that will be decided.

It then processes variable positions from $n-1$ down to $0$, so each decision considers the most significant undecided bit first.

**When the bits of $a$ and $b$ are equal**

Suppose bit $i$ of both inputs is zero. Choosing `x_i = 1` makes bit $i$ of both XOR results one.

If both input bits are one, choosing `x_i = 0` also leaves bit $i$ equal to one in both results.

Thus whenever the two source bits match, there is a choice that sets the bit in both $A$ and $B$. This increases both nonnegative factors and can never reduce their product. The source directly applies

`ax |= 1 << i` and `bx |= 1 << i`.

It does not need to record the actual bit of $x$ because the answer asks only for the maximum product.

**When the source bits differ**

If one source bit is zero and the other is one, XOR with the same `x_i` keeps the result bits different: exactly one of $A$ and $B$ receives $2^i$.

The sum contributed by this position is fixed, regardless of which factor receives it. For a fixed total $A+B$, the product

$$
AB
$$

is maximized when the two factors are as close as possible. Therefore the bit should go to the currently smaller partial factor:

- if `ax > bx`, set the bit in `bx`;
- otherwise, set it in `ax`.

The source uses exactly this rule.

**Why balancing greedily from high bits is correct**

After all bits above $i$ have been fixed, their contribution determines the leading comparison between `ax` and `bx`. All still-lower bits together are worth less than $2^i$ in either number, so they cannot undo the significance of assigning the current $2^i$ bit.

At a differing position, the combined sum of the two eventual factors remains fixed whichever side receives the bit. Assigning it to the smaller partial factor minimizes their absolute difference at the highest position where the choice can affect that difference. Lower choices can only refine the balance.

Since

$$
AB=\frac{(A+B)^2-(A-B)^2}{4},
$$

with fixed sum, minimizing $|A-B|$ maximizes the product. The high-to-low greedy choice achieves the smallest possible difference lexicographically by bit significance.

**Why matching bits are always made one**

At a matching position, alternatives are both result bits zero or both one. Setting both one raises the total sum and raises each factor by the same positive amount. For nonnegative $A$ and $B$,

$$
(A+d)(B+d)-AB=d(A+B)+d^2>0
$$

for $d=2^i$. Therefore zeroing both can never be optimal.

**Modulo only after optimization**

The greedy comparisons must use the actual partial integers. Reducing `ax` or `bx` modulo $10^9+7$ during construction could reverse their order and lead to a wrong balancing decision.

The source first builds the true maximizing pair, multiplies it, and only then returns `ax * bx % mod`.

When $n=0$, no bit of $x$ may be set, so the loop is empty. The initialized values are exactly $a$ and $b$, and the method returns their product modulo the required modulus.

## Complexity detail

The loop examines exactly $n$ bit positions and performs constant work at each. Time complexity is $O(n)$; with $n\le50$, this is a very small fixed bound.

Only `ax`, `bx`, bit variables, and the modulus are stored. Auxiliary space is $O(1)$.

Python integers safely hold the unreduced product of values below $2^{50}$ before the final modulo.

## Alternatives and edge cases

- **Enumerate every $x$:** There are $2^n$ possibilities, which is infeasible for $n=50$.
- **Dynamic programming over bit states:** Possible but unnecessary because matching bits have a forced best choice and differing bits reduce to balancing.
- **Apply modulo during construction:** Incorrect; modular residues do not preserve magnitude or product ordering.
- **$a=b$ in variable bits:** Every low matching bit can be made one in both results, maximizing both simultaneously.
- **One factor initially larger in high bits:** Differing low bits are preferentially assigned to the smaller factor, though low bits may not fully close the fixed high-bit gap.
- **Tie between partial factors:** The source assigns the differing bit to `ax`. Assigning it to `bx` is symmetric and yields the same attainable optimum.
- **$n=0$:** Only $x=0$ is legal, and the initialization already gives the answer.
- **High bits:** They cannot be changed by legal $x$ and must be copied before low-bit decisions.
- **Actual $x$ not returned:** Each decision corresponds to some legal bit of $x$, but reconstructing it is unnecessary.

## General

**The apparent choices do not change the total cost**

At first, the problem looks like an optimization over many possible split trees. An integer `x` can be divided as `1+(x-1)`, `2+(x-2)`, and so on. After that split, either child larger than one can be split again, and the operations can be performed in many orders.

A dynamic program could try every first split and minimize

$$
a b+\text{cost}(a)+\text{cost}(b).
$$

However, a stronger fact makes that search unnecessary: every complete valid splitting process has exactly the same total cost. Since there is no cheaper or more expensive split tree, the minimum is that invariant total.

**Attach a potential to every current part**

For a positive integer `x`, define

$$
P(x)=\binom{x}{2}=\frac{x(x-1)}{2}.
$$

For the current multiset of parts, define the total potential as the sum of `P(x)` over all parts. Initially there is only the part `n`, so the potential is

$$
\binom n2.
$$

At the end there are `n` copies of one. Since

$$
\binom12=0,
$$

the final total potential is zero.

Now consider one permitted operation that replaces `x` by positive parts `a` and `b` with `a+b=x`. The potential before this local replacement is `\binom{x}{2}`. The two new parts contribute `\binom a2+\binom b2`. Their difference is

$$
\begin{aligned}
\binom{x}{2}-\binom a2-\binom b2
&=\frac{(a+b)(a+b-1)-a(a-1)-b(b-1)}{2}\\
&=\frac{2ab}{2}\\
&=ab.
\end{aligned}
$$

But `ab` is exactly the operation's stated cost. Therefore every split costs precisely the amount by which it decreases the potential.

**The costs telescope**

Imagine listing the potential after every operation:

$$
P_0,P_1,P_2,\ldots,P_m.
$$

For operation `j`, the previous identity says

$$
\text{cost}_j=P_{j-1}-P_j.
$$

Adding all operation costs causes every intermediate potential to cancel:

$$
\begin{aligned}
\sum_{j=1}^{m}\text{cost}_j
&=(P_0-P_1)+(P_1-P_2)+\cdots+(P_{m-1}-P_m)\\
&=P_0-P_m.
\end{aligned}
$$

The initial potential is `\binom n2` and the final potential is zero, so every complete process costs

$$
\binom n2=\frac{n(n-1)}2.
$$

This argument is independent of which part is split next, how balanced each split is, and what order independent branches are processed. It proves both a lower bound and attainability at once: every valid completion has that cost, and a completion always exists by repeatedly splitting off one.

**An equivalent pair-of-ones interpretation**

The same invariant has a combinatorial meaning. Think of the eventual `n` ones as distinguishable leaves of a binary split tree. When a node of size `x` is split into groups of sizes `a` and `b`, the cost `ab` counts the unordered pairs of final leaves with one leaf in the left group and one in the right group.

Every unordered pair of final ones is separated exactly once: at the first split where the two leaves go into different child groups, equivalently their lowest common ancestor in the split tree. Before that split they belong to the same part; afterward they remain in different descendant parts forever. Therefore all operation costs together count every pair of final ones once.

The number of unordered pairs among `n` objects is `\binom n2`. This recovers the same formula and makes it intuitive why changing the shape of the split tree cannot change the total.

**How the examples fit the invariant**

For `n=3`, the initial potential is

$$
\binom32=3.
$$

Splitting `3` into `1` and `2` costs two and changes the potential from three to `0+1=1`. Splitting the remaining two into two ones costs one and changes the potential from one to zero. The total is three.

For `n=4`, a balanced first split `2+2` costs four. Each two then splits as `1+1` for cost one, producing total six. An unbalanced route gives the same result: `4\to1+3` costs three, `3\to1+2` costs two, and `2\to1+1` costs one. The sum is again six, equal to

$$
\binom42=6.
$$

These are not merely two optimal examples. They illustrate that balanced and unbalanced trees share the invariant total.

**Why the direct return is sufficient**

The protected source returns

`n * (n - 1) // 2`.

The product of two consecutive integers is always even, so integer division by two is exact. There is no need to construct an actual sequence of splits because the function asks only for the minimum cost, not the operations themselves.

For `n=1`, no split is required. The formula gives `1\cdot0/2=0`, so the same line handles the smallest input correctly. For every `n>1`, repeatedly splitting `x` into `1` and `x-1` demonstrates that the terminal state of all ones is reachable, while the potential argument fixes the cost of that and every other valid route.

**Why “minimum” is still answered**

Showing that all complete processes cost `\binom n2` is stronger than producing one process with that cost. The set of attainable total costs contains exactly one value. Its minimum, maximum, and every other order statistic are the same value. Thus returning the invariant does not skip an optimization step; it proves that the optimization has no meaningful choice left.

## Complexity detail

The method performs one subtraction, one multiplication, and one exact integer division. Under the standard unit-cost arithmetic model used for the manifest, this is `O(1)` time and `O(1)` auxiliary space.

Python integers have arbitrary precision. If `n` were allowed to grow without a machine-word bound, multiplying two `O(\log n)`-bit integers would have a nonconstant bit-operation cost. Under the stated constraint `n\le500`, the result is at most

$$
\frac{500\cdot499}{2}=124750,
$$

so ordinary constant-sized arithmetic easily suffices. The manifest's `O(1)` time and `O(1)` space accurately describe the exact source in the intended model.

No recursion stack, dynamic-programming table, split tree, or list of current parts is built. The output is one integer, also constant space.

## Alternatives and edge cases

- **Dynamic programming over the first split:** The recurrence `dp[x]=\min_{1\le a<x}(a(x-a)+dp[a]+dp[x-a])` is correct but takes `O(n^2)` time if all split points are tried. Substituting `dp[t]=\binom t2` makes every candidate equal, revealing why the table is unnecessary.
- **Greedily split off one:** Repeatedly use `x=1+(x-1)`. Its costs are `n-1,n-2,\ldots,1`, whose sum is `n(n-1)/2`. This constructs a valid route but alone does not prove that another route cannot be cheaper; the potential identity supplies that proof.
- **Always split as evenly as possible:** Balanced splitting may look cheaper because each resulting part becomes small quickly, but the first balanced split has a larger product. Later savings exactly compensate, leaving the same invariant total.
- **Always minimize the immediate product:** The split `1+(x-1)` minimizes `ab` for one operation, but greedy local-cost reasoning is unnecessary and potentially misleading in other problems. Here all future costs telescope with the current one.
- **Explicit binary-tree pair counting:** Label the final ones and charge each unordered pair at the node where it separates. This is an equally strong derivation and may be more intuitive than algebra, though the source needs only the resulting formula.
- **Operation order:** Splitting the left child before the right child or vice versa changes no cost. Potential decreases depend only on each split, and all intermediate terms cancel.
- **`n=1`:** The initial state already consists of one one, so zero operations and zero cost are required. The triangular-number formula returns zero.
- **`n=2`:** The only split is `1+1` with cost one, matching `2\cdot1/2=1`.
- **Positive-part requirement:** The invariant assumes `a,b>0` and `a+b=x`. Allowing zero would add degenerate operations and could prevent progress, but such splits are excluded by the contract.
- **Completion requires all ones:** Stopping at larger parts leaves positive potential. The telescoping total reaches the full `\binom n2` only when every part is one and final potential is zero.
- **Number of operations:** Every split increases the number of parts by one. Starting with one part and ending with `n` parts requires exactly `n-1` operations, although their individual costs vary.
- **Overflow in fixed-width languages:** The multiplication should use a type capable of holding `n(n-1)` before division. The stated maximum is tiny, while Python handles it automatically.
- **No modulus:** Return the exact triangular number. Applying a modulus or floating-point division would change the required answer or risk precision loss.

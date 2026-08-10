## General

**Interpret the losing root rule**

Selecting the global root loses immediately, so rational play treats that move as unavailable while any proper descendant remains. If no proper descendant remains, the current player has no safe move and loses.

The two child subtrees of the global root are independent: a move inside one never changes the other. This is an impartial combinatorial game, so Sprague-Grundy values describe how independent components combine.

**Use removable-subtree game values**

Let $G_r$ be the Grundy value of an order-$r$ Fibonacci tree when its own root may be removed as an ordinary winning move. Order zero is empty.

For the actual protected-root position of order $n$, the playable components are its left order-$n-2$ subtree and right order-$n-1$ subtree. Their combined value is

$$
G_{n-2}\mathbin{\mathrm{xor}}G_{n-1}.
$$

A position is losing exactly when this xor is zero, which means the two component values are equal.

For $n=1$, both children are empty and both values are zero, so Alice has no safe move and loses.

**The Fibonacci-tree Grundy pattern**

Applying the definition of a Grundy value—take the minimum excluded value among all positions reachable by one subtree removal—to the recursively built Fibonacci trees gives a period-six sequence for nonempty removable roots:

$$
G_1,G_2,G_3,G_4,G_5,G_6
=
1,2,4,7,4,4,
$$

and then the same six values repeat.

For intuition, $G_1=1$ because the sole move removes the root and reaches the empty value zero. Higher orders include the option to remove their root and options obtained by making any legal move inside either recursively defined child. Computing the minimum excluded reachable nimbers produces the listed block; the recursive child-order shift reproduces it every six orders.

The exact solution compresses this established periodic Grundy analysis into one modular test rather than building any tree.

**Find when the child values are equal**

The protected order-$n$ root compares consecutive sequence entries $G_{n-2}$ and $G_{n-1}$, treating $G_0=0$ for the empty tree.

They are equal for $n=1$ because both children are empty. In the repeating nonempty block, the only adjacent equality is

$$
G_5=G_6=4.
$$

After shifting by each six-value period, this makes protected orders

$$
n=1,7,13,19,\ldots
$$

losing. These are exactly the integers satisfying $n\bmod6=1$.

All other orders have unequal child Grundy values, so their xor is nonzero and the first player has a winning move.

**Read the source expression**

`return n % 6 != 1` returns false on the losing residue class and true on all winning residue classes.

The method does not construct the Fibonacci tree, whose number of nodes grows exponentially with $n$. It uses only the order because the game-value pattern has already reduced the entire structure to a period.

**Check the first examples**

At $n=1$, remainder one gives false, agreeing that Alice is forced to take the protected root.

At $n=2$, the root has one nonempty child component, so its xor is nonzero and Alice can remove that child; the formula returns true.

At $n=3$, the two child orders have different Grundy values one and two, so Alice again wins; the formula returns true.

**Why this is not merely a node-count parity trick**

The number of nodes follows a Fibonacci recurrence, but winning is governed by available game moves and their Grundy values, not simply whether the node count is odd or even. The six-period arises from the recursive game states. Memorizing only parity would misclassify orders such as those in different residues with the same node-count parity.

## Complexity detail

The source performs one remainder operation and one comparison. Time is $O(1)$ and auxiliary space is $O(1)$.

It avoids constructing an order-$n$ tree or tabulating up to $n$. The mathematical periodicity makes the cost independent of $n$, including the maximum order 100.

## Alternatives and edge cases

- **Dynamic Grundy computation:** Useful for deriving and verifying the initial pattern, but unnecessary once period six is proven.
- **Explicitly construct the tree:** Exponential in order and infeasible even far below $n=100$.
- **Recursive winner-only reasoning:** Outcome states alone do not generally combine independent child games; Grundy values provide the correct xor rule.
- **Order one:** The only move is the losing protected-root deletion, so return false.
- **Orders congruent to one modulo six:** Exactly the losing sequence.
- **All other residues:** The unequal child nimbers give Alice a winning move.
- **Protected versus removable root:** The global root is losing to select, while a child-subtree root may be removed safely as a normal move.
- **Empty order zero:** Used only as a child component with Grundy value zero; input begins at one.
- **Large order:** Periodicity prevents numeric growth or recursion.
- **Optimal play:** The nonzero Grundy criterion assumes both players choose winning moves whenever available.
- **No tree allocation:** The exact source stores only `n` and the Boolean result.

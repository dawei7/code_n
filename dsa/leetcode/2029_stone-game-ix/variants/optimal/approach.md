## General
**Reduce every value modulo three**

Only the cumulative remainder matters. Count stones with residues $0$, $1$,
and $2$ as $c_0$, $c_1$, and $c_2$. A residue-zero stone does not change a
nonzero cumulative remainder, so it acts as a safe turn switch. Consequently,
only the parity of $c_0$ affects which player is forced to make the decisive
nonzero-residue move.

**Analyze the two zero-parity cases**

Without an unpaired residue-zero turn, Alice can force a loss for Bob exactly
when both nonzero residue classes are available. She starts with one class;
the rule that the next player must avoid completing remainder zero then forces
the safe choices to alternate between the two classes. If either class is
absent, Bob can instead survive until exhaustion.

When $c_0$ is odd, the extra safe turn reverses that parity. Alice now needs
one nonzero class to outnumber the other by more than two. That surplus
supplies the two same-residue stones needed at the beginning of a safe
sequence plus another stone after the alternating pairs are exhausted. With a
difference of at most two, Bob can match the sequence and obtain either the
forced loss or the exhaustion win.

These reduced cases give the complete criterion:

- if $c_0$ is even, Alice wins when $c_1 > 0$ and $c_2 > 0$;
- if $c_0$ is odd, Alice wins when $\lvert c_1 - c_2 \rvert > 2$.

The criterion considers both possible opening residues and every relevant
count; stones within one residue class are strategically interchangeable.

## Complexity detail
One pass counts the residues of all $N$ stones, taking $O(N)$ time. The three
counters occupy $O(1)$ space regardless of input size.

## Alternatives and edge cases
- **Minimax over individual stones:** Exploring move sequences repeats
  equivalent residue states and grows exponentially without memoization.
- **Memoization by residue counts:** This removes value identities but still
  has a state space proportional to $c_0c_1c_2$, far larger than the closed
  form.
- **Repeated front removal:** Counting residues by repeatedly deleting the
  first item of an array is correct but can take $O(N^2)$ time.
- A collection containing only residue-zero stones makes Alice lose on her
  first move.
- With even $c_0$, a missing residue-`1` or residue-`2` class prevents Alice
  from winning.
- For odd $c_0$, a nonzero-count difference of exactly two is still a Bob win.
- Exhausting the stones is not a neutral draw; it explicitly gives Bob the
  victory.

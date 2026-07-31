## General

**Different digit runs are independent**

A letter cannot use presses from two different keys. Every boundary between
unequal adjacent digits is therefore forced, while boundaries inside a maximal
run of one digit are choices. If one run has $a$ valid partitions and the next
has $b$, every choice for the first can be paired with every choice for the
second, so the whole string contributes $a\cdot b$ combinations.

**Count one run with a short recurrence**

For a run whose key supports at most $m$ presses per letter, let $D_i$ be the
number of ways to decode its first $i$ presses. Set $D_0=1$ for the empty
prefix. The last letter consumes $j$ presses for some
$1\le j\le\min(i,m)$, leaving any valid decoding of the preceding $i-j$
presses:

$$
D_i=\sum_{j=1}^{\min(i,m)}D_{i-j}.
$$

Use $m=4$ for `7` and `9`, and $m=3$ for every other permitted digit. Only the
previous three or four values are needed, so a fixed-size rolling window
evaluates the recurrence. Multiply the final value for each maximal run into
the answer and reduce modulo $10^9+7$ after every addition and multiplication.

**Why the product counts every message exactly once**

Within a run, the recurrence classifies decodings by the size of their last
letter group. Those classes are disjoint and cover every legal final group, so
each run partition is counted once. Boundaries between different digits are
mandatory, which means choosing one counted partition independently for every
run produces one complete message, and every possible message has exactly that
sequence of run partitions. Their product is therefore the exact total.

## Complexity detail

Let $n=\lvert\texttt{pressedKeys}\rvert$. The run scan and all recurrence
updates together process each character once, taking $O(n)$ time. The rolling
window holds at most four recurrence values, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Full prefix dynamic-programming array:** The same recurrence can store all $n+1$ prefix counts in $O(n)$ space, but earlier values beyond four positions are never reused.
- **Try every earlier split point:** A general partition dynamic program is correct but wastes $O(n^2)$ time checking splits that cannot form one keypad letter.
- **Recursive enumeration:** Explicitly generating all messages is exponential and infeasible for a long equal-digit run.
- **One press:** It represents exactly one letter and therefore has one decoding.
- **Keys `7` and `9`:** Their runs allow groups of four; treating every key as three-letter loses valid messages.
- **Changing digits:** A transition between two digits is a forced letter boundary.
- **Long runs:** Apply the modulus during recurrence updates rather than constructing the enormous exact count.
- **Several runs:** Multiply their counts; do not add them.

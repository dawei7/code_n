## General

**Represent position and direction explicitly**

The exact solution simulates one pass per second with two scalars:

- `ans` is the current person's one-based label;
- `k` is the direction, $+1$ toward person $n$ and $-1$ toward person $1$.

Both start at one: person one initially holds the pillow, and the first pass goes toward person two.

For each elapsed second, `ans += k` moves exactly one position. If the new position is either endpoint, `k *= -1` reverses the direction for the next second.

**Why reversal occurs after moving**

At an endpoint, the holder has just received the pillow. The pass that reached the endpoint used the old direction. Only the subsequent pass must go back inward.

For example, with $n=4$, positions evolve as:

$$
1\to2\to3\to4\to3\to2.
$$

When the update reaches $4$, direction changes from $+1$ to $-1$. The position remains $4$ at that instant; the next loop iteration moves it to $3$.

Reversing before movement whenever currently at an endpoint could also be made correct with a different loop structure, but mixing the conventions would cause an off-by-one pass.

**A loop invariant**

After exactly $t$ loop iterations, `ans` is the person holding the pillow after $t$ seconds, and `k` is the direction of the next legal pass.

The invariant holds before the loop at time zero: person one holds the pillow and the next direction is right. One iteration adds the direction, reaching the adjacent legal person after one second. If that person is an endpoint, the direction reverses; otherwise it remains. In either case, `k` is correct for the following pass.

By induction, the state after `time` iterations is the required answer.

**Trace the first example**

With $n=4$ and `time=5`:

- time zero: `ans=1`, `k=1`;
- after one second: `ans=2`;
- after two: `ans=3`;
- after three: `ans=4`, then `k` becomes $-1$;
- after four: `ans=3`;
- after five: `ans=2`.

The function returns two.

**The repeating pattern**

Traveling from person one to person $n$ takes $n-1$ seconds. Traveling back takes another $n-1$. Therefore the complete position sequence repeats every

$$
2(n-1)
$$

seconds.

The simulation does not explicitly reduce `time` by this period, but its state follows that periodic motion exactly. Understanding the period leads to the constant-time alternative described by the manifest and editorial.

**Exact implementation versus manifest**

The manifest labels the Optimal approach as direct mathematical folding with $O(1)$ time. The checked-in source, however, contains a `for` loop over `range(time)`. It is a straightforward simulation taking time proportional to the input `time`.

Under the given bound `time <= 1000`, this is easily fast enough, but an accurate explanation must not claim that this specific loop is constant time.

**Deriving the direct formula**

Let

`rounds = time // (n - 1)`

and

`rem = time % (n - 1)`.

Each complete endpoint-to-endpoint traversal reverses direction. If `rounds` is even, the remainder starts from person one and moves right, so the holder is `1 + rem`. If `rounds` is odd, it starts from person $n$ and moves left, so the holder is `n - rem`.

This formula produces the same state as the loop without simulating seconds. It is a genuine $O(1)$ alternative, not what the exact solution executes.

**Why positions never go out of bounds**

Initially `ans=1` and direction is inward. Direction reverses immediately upon arriving at either $1$ or $n$. Therefore, before every move from an endpoint, `k` points into the line. At interior positions either direction leads to another valid label.

This invariant means no bounds check is necessary inside the loop.

The complete simulation state is the pair `(ans, k)`, not the position alone. An interior person can be visited while the pillow moves right and again while it moves left; those visits have different next holders. Endpoint states are unambiguous because the code reverses immediately after arrival. After $2(n-1)$ moves, both the position and direction return to their initial values, proving the full-state period used by the mathematical shortcut.

## Complexity detail

The loop runs exactly `time` iterations, each with constant work. The exact implementation takes $O(\texttt{time})$ time and $O(1)$ auxiliary space.

This differs from the manifest's $O(1)$ time, which applies to the quotient-and-remainder formula. The function allocates no arrays or other input-sized structures.

## Alternatives and edge cases

- **Endpoint traversal formula:** Divide time by $n-1$, use traversal parity for direction, and compute the remaining offset in $O(1)$ time.
- **Full-period modulo:** Reduce time modulo $2(n-1)$ and reflect positions in the second half of the period.
- **Queue simulation:** Storing people or pillow passes is unnecessary; position and direction are sufficient state.
- **Exactly at person `n`:** Direction flips after arrival, but the returned holder remains $n$ if time ends there.
- **Exactly back at person one:** Direction flips to positive for a possible next second.
- **Two people:** The pillow alternates every second, and the same loop works without special cases.
- **One complete traversal:** At `time = n - 1`, person $n$ holds the pillow.
- **One complete period:** At `time = 2(n - 1)`, the pillow is back at person one.
- **Manifest distinction:** The source is a linear simulation; the mathematical $O(1)$ method is an alternative.
